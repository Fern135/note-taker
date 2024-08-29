import os
from dotenv import load_dotenv, find_dotenv  # for using dotenv

load_dotenv(find_dotenv()) # loading up the .env file

class Config(object):
    DEBUG                   = True # auto reloading the app
    TESTING                 = False
    # CSRF_ENABLED            = True #todo: figure out how to use this in js 
    apphost                 = os.getenv("HOST")  
    port                    = os.getenv("PORT")  
    __APP_NAME__            = os.getenv("APP_NAME")
    __APP_VER__             = "1.0.0"

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


class HttpResponseCodes(Config):
    response_codes = {
        "continue" : 100,
        "switching-protocols" : 101,
        "ok": 200,
        "created" : 201,
        "accepted" : 202,
        "Non-Auth-information" : 203,
        "no-content" : 204,
        "reset-content" : 205,
        "patial-content" : 206,
        "multiple-choices" : 300,
        "moved-permanently" : 301,
        "found" : 302,
        "see-other" : 303,
        "not-modified" : 304,
        "use-proxy" : 305,
        "temp-redirect" : 307,
        "perm-redirect" : 308,
        "bad-request" : 400,
        "unauthorized" : 401,
        "pay-required" : 402,
        "forbidden" : 403,
        "not-found" : 404,
        "method-not-allowed" : 405,
        "not-acceptable" : 406,
        "proxy-auth-req" : 407,
        "request-timeout" : 408,
        "conflict" : 409,
        "gone" : 410,
        "length-req" : 411,
        "precondition-failed" : 412,
        "payload-too-large" : 413,
        "URI-too-long" : 414,
        "unsupported-media-type" : 415,
        "range-not-satisfiable" : 416,
        "expectation-failed" : 417,
        "upgrade-required" : 426,
        "internal-server-error" : 500,
        "not-implemented" : 501,
        "bad-gateway" : 502,
        "service-unavailable" : 503,
        "gateway-timeout" : 504,
        "HTTP-version-not-supported" : 505,
    }

    def __init__(self):
        super().__init__()
