from flask import Blueprint, current_app, render_template, request

GLOBAL_BLUEPRINT = Blueprint('global', __name__, template_folder='templates')


@GLOBAL_BLUEPRINT.route('/', methods=['GET'])
def index():
    return render_template('landing_page/landing.html', SECRET_VALUE=current_app.SECRET_VALUE)