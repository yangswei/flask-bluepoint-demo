from flask import Flask
from flaskdemo.bluepoint import bp as demobp
from db import db
from rds import redis_client, redis_client2,  redis_client3
from flaskdemo.tasks import autotask
from flask_apscheduler import APScheduler

app = Flask(__name__)

'''
上线使用ProductConfig,测试使用DevConfig
from config import ProductConfig
app.config.from_object(ProductConfig)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['pool_pre_ping'] = True
'''

from config import DevConfig
app.config.from_object(DevConfig)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['pool_pre_ping'] = True

scheduler = APScheduler()
app.register_blueprint(demobp)

with app.app_context():
    db.init_app(app)
    #redis_client.init_app(app)
    #redis_client2.init_app(app)
    #redis_client3.init_app(app)
    scheduler.init_app(app)
    scheduler.add_job(func=autotask,trigger='interval',id='autotask1',args=[app], seconds=660)
    scheduler.start()
    db.create_all()