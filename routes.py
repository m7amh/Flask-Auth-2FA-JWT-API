from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import pyotp, qrcode, io

from models import db, User, Product
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)

@app.route('/')
def home():
    return jsonify({'message': 'Flask API is running!'})

# تسجيل مستخدم جديد
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    secret = pyotp.random_base32()
    
    new_user = User(username=data['username'], password=hashed_password, twofa_secret=secret)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully!', '2fa_secret': secret})

# توليد QR Code للمصادقة الثنائية
@app.route('/qr_code/<username>', methods=['GET'])
def generate_qr(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    otp_uri = pyotp.totp.TOTP(user.twofa_secret).provisioning_uri(username, issuer_name="SecureApp")
    qr = qrcode.make(otp_uri)
    
    img_io = io.BytesIO()
    qr.save(img_io, 'PNG')
    img_io.seek(0)
    
    return img_io.getvalue(), 200, {'Content-Type': 'image/png'}

# تسجيل الدخول وإصدار JWT
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Invalid credentials'}), 401
    
    totp = pyotp.TOTP(user.twofa_secret)
    if not totp.verify(data['2fa_code']):
        return jsonify({'message': 'Invalid 2FA code'}), 401

    access_token = create_access_token(identity=user.username)
    return jsonify({'token': access_token})

# حماية الـ Endpoints باستخدام JWT
@app.route('/products', methods=['POST'])
@jwt_required()
def create_product():
    data = request.json
    new_product = Product(name=data['name'], description=data.get('description'), price=data.get('price'), quantity=data.get('quantity'))
    
    db.session.add(new_product)
    db.session.commit()
    
    return jsonify({'message': 'Product added successfully'})

@app.route('/products', methods=['GET'])
@jwt_required()
def get_products():
    products = Product.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'description': p.description, 'price': float(p.price), 'quantity': p.quantity} for p in products])

@app.route('/products/<int:id>', methods=['PUT'])
@jwt_required()
def update_product(id):
    data = request.json
    product = Product.query.get(id)
    
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    
    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.quantity = data.get('quantity', product.quantity)
    
    db.session.commit()
    return jsonify({'message': 'Product updated successfully'})

@app.route('/products/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_product(id):
    product = Product.query.get(id)
    
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'})
