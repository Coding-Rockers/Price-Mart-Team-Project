# Create dummy secrey key so we can use sessions
SECRET_KEY = 'jiuytfgbhjkoi87yhnbgf'

# Create in-memory database
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root2:root@localhost/inventory_db'
SQLALCHEMY_ECHO = True

FLASK_ADMIN_SWATCH = 'flatly'
