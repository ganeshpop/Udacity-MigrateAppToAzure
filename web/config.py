import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:   
    DEBUG = True
    POSTGRES_URL="udacity-postgres-db-server.postgres.database.azure.com"  #TODO: Update value
    POSTGRES_USER="dbadmin@udacity-postgres-db-server" #TODO: Update value
    POSTGRES_PW="Password@123"   #TODO: Update value
    POSTGRES_DB="techconfdb"   #TODO: Update value
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://techconf-service-bus.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=B4ETq8I3SM+0I+c/fzY0FEu5eut/wAUpiwwmk6ojNug=' #TODO: Update value
    SERVICE_BUS_QUEUE_NAME ='notificationqueue'
    ADMIN_EMAIL_ADDRESS: 'info@techconf.com'
    SENDGRID_API_KEY = '' #Configuration not required, required SendGrid Account

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False