# mainfolder = "/home/rufus/Descargas"

import os 

# estas lineas de abajo se comentan cuando el ambiente es produccion en el mismo heroku, porque heroku automaticamente reconoce las variables de entorno.
from dotenv import load_dotenv
load_dotenv()


SECRET_KEY = os.environ.get('SECRET_KEY')
ENVIROMENT = os.environ.get('FLASK_ENV')
IMAGE_PATH = os.environ.get('IMAGE_PATH')
MEDIA_DIR = '/home/rufus/Descargas'


if ENVIROMENT == 'production-heroku':
    DATABASE_URL= os.environ.get('DATABASE_URL')  
elif ENVIROMENT == 'development-fulllocal':
    DATABASE_URL= os.environ.get('DATABASE_URL_DEV')
else:        
    DATABASE_URL = os.environ.get('DATABASE_URL_DEVREMOTE')  #en esta opcion se entra cuando el tipo de enviroment es development-bdremote