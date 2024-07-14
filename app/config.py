import os

class DevelomentConfig():   
    DEBUG = True
    
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'contraseña_mysql'
    MYSQL_DB = 'nombre_basedatos'
    
Config = {
    'develoment': DevelomentConfig
}