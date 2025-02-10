import os
from dotenv import load_dotenv

load_dotenv()

class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_DB = 'discoteca'

config = {
    'development': DevelopmentConfig
}