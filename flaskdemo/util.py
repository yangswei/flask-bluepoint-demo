from flask import current_app
from models import Table1



class Classdemo:
    '''Classdemo'''
    def __init__(self, Name):
        self.Name = Name

    def funcdemo(self):
        '''
        Util 函数
        这里 可以通过current_app 获取配置文件配置
        '''
        Confi=current_app.config.get('DEBUG')
        return Confi
