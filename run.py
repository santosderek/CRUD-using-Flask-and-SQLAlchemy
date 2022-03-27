from distutils.log import debug
from app import create_application_factory
from app.settings import HTTP_PORT, HTTP_DOMAIN, HTTP_SCHEME, FLASK_DEBUG
from app.sql import create_database


application = create_application_factory()


def run(*args, **kwargs):
    application.run(*args, port=HTTP_PORT, host=HTTP_DOMAIN, debug=FLASK_DEBUG, **kwargs)

if __name__ == '__main__':
    run()