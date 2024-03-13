class Config:
    DEBUG=False
    TESTING=False

    # Configuración de la Base de datos
    DB_USER = 'admin'
    DB_PASSWORD = 'TN#z2bQX94&bd$n'
    DB_HOST = 'databaserafael.cj2mqqcw6wf0.us-east-2.rds.amazonaws.com'
    DB_NAME = 'analisis'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI=f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

class ProductionConfig(Config):
    DEBUG=False

class DevelopmentConfig(Config):
    DEBUG=True
    SECRET_KEY='dev'
    TESTING=True
