# -*- coding: UTF-8 -*-
###################################
'''
Flask 项目中,外置脚本如何操作项目中的数据库
'''

import sys
from _init_ import app
from models import Table1
from db import db

def OperateDb(Idcount):
    '''
    操作数据库函数
    '''
    try:
      item = db.session.query(Table1).order_by(Table1.Id.desc()).first()
    except Exception as e:
      raise e

if __name__ == "__main__":
    argLen = len(sys.argv)
    #脚本是否接收参数，对参数进行解析
    #引入上下文，对数据库进行操作
    Idcount = 1
    with app.app_context():
      OperateDb(Idcount)