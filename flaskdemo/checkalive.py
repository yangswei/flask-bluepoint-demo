from models import MachineidList
from db import db
from rds import redis_client

class Checkalive:
    def __init__(self, License):
        self.License = License
    def MakeEnterpriseCache(self):
        '''
        将整个数据库表缓存到cache
        '''
        try:
            item = db.session.query(MachineidList).all()
        except Exception as e:
            raise e
        #item是一个list类型
        pipe = redis_client.pipeline()
        for enterprise in item:
            enterprisename=enterprise.split('-')[0].strip()
            enterpriselicense=enterprise.split('-')[1].strip()
            pipe.set(enterpriselicense, enterprisename, ex=600)
        res = pipe.execute()
        return res
        
    def ReMakeCache(self):
        for k in redis_client.keys():
            redis_client.delete(k)
        self.MakeEnterpriseCache()
    
    def GetEnterpriseName(self):
        entrprisename=redis_client.get(self.License)
        if entrprisename is None:
            #如果缓存中是空，则去数据库做一次查询
            item = db.session.query(MachineidList).filter(MachineidList.License == self.License).first()
            if item is None:
                return None
            else:
                entrprisename=item.EnterPriseName
                enterpriselicense=item.License
                redis_client.set(enterpriselicense, entrprisename, ex=600)
                return entrprisename
        else:
            redis_client.set(self.License, entrprisename, ex=600)
            return entrprisename
    
    def CheckIfRuleUpdate(self):
        item = db.session.query(MachineidList).filter(MachineidList.License == self.License).first()
        IsRuleUpdate = item.IsRuleUpdate
        if IsRuleUpdate:
            return True
        else:
            return False
    