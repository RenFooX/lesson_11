from flask import Blueprint

loader = Blueprint('loader', __name__, template_folder='templates', static_folder='static')
