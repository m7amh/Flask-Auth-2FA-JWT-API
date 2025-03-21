from flask import Flask
from models import db
from routes import app

if __name__ == '__main__':
    app.run(debug=True)
