import os

class Config:
    SECRET_KEY = '9bf6b0c566c53d42f92993fc061885d1a54f22d558e37c1e7754309067d64e51'  # استخدم مفتاحًا سريًا أقوى
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/mohamedataintegrity'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
