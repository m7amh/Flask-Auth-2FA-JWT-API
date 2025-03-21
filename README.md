# 🚀 Flask Secure API with 2FA & JWT Authentication

## 🔥 About the Project
A cutting-edge Flask-based REST API designed with **military-grade security** 🛡️, integrating:
- **User Authentication** with **hashed passwords** 🔐
- **Two-Factor Authentication (2FA)** using **Google Authenticator** 🏆
- **JWT-based Authorization** for **secure API access** 🔑
- **Protected CRUD Operations** on a MySQL database 📦

This API is engineered for **hackers, developers, and security enthusiasts** who demand **top-tier protection** in their applications. Whether you're a **penetration tester, startup founder, or cybersecurity researcher**, this repo is a **must-have**. 🚀

---

## 🔑 Features & Security Enhancements
✅ **Flask-SQLAlchemy** for database management 🗄️  
✅ **PBKDF2 Password Hashing** for unbreakable security 🔐  
✅ **Google Authenticator for 2FA** – No more weak logins! 🏆  
✅ **JWT Authentication** with secure token expiry & revocation 🔥  
✅ **Role-Based Access Control (RBAC) Ready** for enterprise security 🏢  
✅ **RESTful API Design** – Scalable & Future-proof ⚙️  
✅ **Postman-Ready Endpoints** for easy testing 🛠️  
✅ **100% Open-Source** – Fork it, break it, improve it! 🖥️  

---

## 🛠 Installation & Setup
### **Step 1: Clone the Repository**
```bash
 git clone https://github.com/YOUR_GITHUB_USERNAME/Flask-Secure-Auth.git
 cd Flask-Secure-Auth
```

### **Step 2: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 3: Configure Database in `config.py`**
Modify the database connection string with your **MySQL credentials**:
```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:yourpassword@localhost/yourdatabase'
```

### **Step 4: Initialize the Database**
```bash
python db_init.py
```

### **Step 5: Start the API Server**
```bash
python app.py
```

---

## 🔥 API Endpoints

### 🔹 **1️⃣ Register a New User**
**Endpoint:** `/register`  
**Method:** `POST`
```json
{
   "username": "testuser",
   "password": "testpass"
}
```

### 🔹 **2️⃣ Get 2FA QR Code**
**Endpoint:** `/qr_code/<username>`  
**Method:** `GET`

### 🔹 **3️⃣ User Login with 2FA**
**Endpoint:** `/login`  
**Method:** `POST`
```json
{
   "username": "testuser",
   "password": "testpass",
   "2fa_code": "123456"
}
```

### 🔹 **4️⃣ JWT-Secured CRUD Operations**
**Endpoints:**
- `POST /products` – Add a new product 📦
- `GET /products` – Get all products 📜
- `PUT /products/<id>` – Update product 🛠
- `DELETE /products/<id>` – Delete product ❌

**Headers (for secured endpoints):**
```json
{
  "Authorization": "Bearer YOUR_JWT_TOKEN"
}
```

---

## 🔥 Future Enhancements
🚀 **Multi-Role Authentication (Admin/User)**  
🚀 **OAuth2 & Social Logins (Google, GitHub, Discord)**  
🚀 **Rate-Limiting & DDoS Protection**  
🚀 **Cloud Deployment (AWS, GCP, Azure)**  

---

## 🏆 Want to Contribute?
🔥 **Fork the repo** & submit a **pull request**! Let’s build the most **secure Flask API** together! 💪

---

## 📢 Need Help? Reach Out!
💬 **Issues & Bugs?** Open an [Issue](https://www.linkedin.com/in/mohamed--abdelrahman--awad/)  
📧 **Business Inquiries?** Drop me a mail at **mohamed2291971@gmail.com**  
🔥 **Follow for more security projects!** [GitHub Profile](https://github.com/m7amh)

