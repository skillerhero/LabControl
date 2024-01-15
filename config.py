class Config:
    DEBUG=True
    TESTING=True

    #configuracion de Base de datos
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://root@127.0.0.1/analisis"

class ProductionConfig(Config):
    DEBUG=False

class DevelopmentConfig(Config):
    DEBUG=True
    SECRET_KEY='dev'
    TESTING=True