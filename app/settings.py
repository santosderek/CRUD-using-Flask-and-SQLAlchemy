from os import getenv

from dotenv import load_dotenv

load_dotenv()

HTTP_PORT = int(getenv('HTTP_PORT', 80))
HTTP_DOMAIN = getenv('HTTP_DOMAIN', None)
HTTP_SCHEME = getenv('HTTP_SCHEME', None)
FLASK_DEBUG = getenv('FLASK_DEBUG', "False").lower() in ['1', 'true', True]
SECRET_VALUE = getenv('SECRET_VALUE', None)