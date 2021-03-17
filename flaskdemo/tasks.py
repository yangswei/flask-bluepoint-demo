from models import Table1
from db import db
from .util import Classdemo
from datetime import datetime, timedelta
from rds import redis_client
from .cache import cache


def autotask(app):
    '''
    这里写定时任务的内容
    try:
        with app.app_context():
            #操作数据库需要使用app.app_context
            item = db.session.query(Table1).all()
    except Exception as e:
        raise e
    #Redis可以直接调用, cache同理
    xx = redis_client.keys()
    yy = cache.keys()
    #这里可以引入util模块，但是操作时同样需要app上下文
    Name = '111'
    with app.app_context():
        sl = Classdemo(Name)
        sl.funcdemo()
    '''
    print('This is auto task print')
    return 'ok'