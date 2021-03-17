from flask import Blueprint

bp = Blueprint("flaskdemo", __name__, 
                template_folder='templates',
                static_folder='static',
                url_prefix='/demo'
)

from flaskdemo import demoapp