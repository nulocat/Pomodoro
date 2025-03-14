from flask import Flask, Blueprint
from . import views

def load_routes(instance: Flask | Blueprint):
    for url, func in views.ROUTES.items():
        instance.add_url_rule(url, view_func=func)
    return instance

def create_app(): # for use like a standalone app
    app = Flask(__name__)
    app = load_routes(app)
    return app

def create_blueprint(): # for use like a subapp
    bp = Blueprint('pomodoro', __name__, template_folder='templates')
    bp = load_routes(bp)
    return bp


