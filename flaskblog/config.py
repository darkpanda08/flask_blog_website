import os


class Config:
	SECRET_KEY = '2d4fc582abd6ceeb0c8045f58f06c882'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	MAIL_SERVER = os.environ.get('MAIL_SERVER')
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('MAIL_USER')
	MAIL_PASSWORD = os.environ.get('MAIL_PASS')