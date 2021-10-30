"""
For listing down endpoints relevant to location feature
"""
from flask.blueprints import Blueprint
from flaskr import db

location_bp = Blueprint(url_prefix='/location', name='location', import_name=__name__)


@location_bp.route('/')
def index():
    return 'Yellow'
