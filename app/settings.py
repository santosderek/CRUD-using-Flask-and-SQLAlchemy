from os import getenv

from dotenv import load_dotenv

load_dotenv()

HTTP_PORT = getenv('HTTP_PORT', None)
HTTP_DOMAIN = getenv('HTTP_DOMAIN', None)
HTTP_SCHEME = getenv('HTTP_SCHEME', None)
FLASK_DEBUG = getenv('FLASK_DEBUG', None)
SECRET_VALUE = getenv('SECRET_VALUE', None)