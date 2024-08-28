import os
from dotenv import load_dotenv, find_dotenv  # for using dotenv

load_dotenv(find_dotenv()) # loading up the .env file

class Config(object):
    DEBUG                   = True # auto reloading the app
    TESTING                 = False
    CSRF_ENABLED            = True
    apphost                 = os.getenv("HOST")  
    port                    = os.getenv("PORT")  
    __APP_NAME__            = os.getenv("APP_NAME")

    #<========== cookies HTTPS and other security ==========> 
    JWT_ALGORITHM           = "HS256"
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE   = True
    SESSION_COOKIE_SAMESITE = 'None'
    CSRF_COOKIE_SECURE      = True 
    SECURE_SSL_REDIRECT     = False
    #<========== cookies HTTPS and other security ==========> 
    

    #<================= mailing =================> 
    DEFAULT_FROM   = os.getenv('DEFAULT_FROM')
    MAIL_SERVER    = 'smtp.gmail.com'
    MAIL_PORT      = 587 # <=============> the better port for sending email
    MAIL_USE_TLS   = False
    MAIL_USE_SSL   = True
    MAIL_USERNAME  = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD  = os.getenv("MAIL_PASSWORD")
    #<================= mailing =================> 

    #<============== mysql database ==============> 
    db_ip          = os.getenv("DATA_BASE_HOST")
    db_name        = os.getenv("DATA_BASE")
    db_username    = os.getenv("USER_NAME")
    db_password    = os.getenv("PASSWORD")
    local_db_name  = os.getenv("LOCAL_DB_NAME")
    #<============== mysql database ==============> 

class ProductionConfig(Config):
    DEBUG          = False
    SECRET_KEY     = os.getenv("SECRET_KEY_PROD")
    
    def __init__(self):
        super().__init__()  # Call the initializer of the parent class

class DevelopmentConfig(Config):
    DEBUG          = True
    SECRET_KEY     = os.getenv("SECRET_KEY_DEV")

    # only in dev mode
    SECURE_HSTS_SECONDS             = 0 # set to zero in development mode,

    def __init__(self):
        super().__init__()  # Call the initializer of the parent class

