from flask import Flask
from .views.root import GLOBAL_BLUEPRINT
from .settings import SECRET_VALUE

def create_application_factory() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(GLOBAL_BLUEPRINT)
    setattr(app, 'SECRET_VALUE', SECRET_VALUE)
    return app
