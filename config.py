'''
FileName: config.py
'''


class DevConfig():
  ENV='production'
  DEBUG = False
  REDIS_URL = "redis://:xx@127.0.0.1/0"
  REDIS2_URL = "redis://:xx@127.0.0.1/1"
  REDIS3_URL = "redis://:xx@127.0.0.1/2"
  SQLALCHEMY_DATABASE_URI = "sqlite:///db/alertcloud.db"

class ProductConfig():
  ENV='production'
  DEBUG = False
  REDIS_URL = "redis://:xx@127.0.0.1/0"
  REDIS2_URL = "redis://:xx@127.0.0.1/1"
  REDIS3_URL = "redis://:xx@127.0.0.1/2"
  SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@127.0.0.1/xxxx"
