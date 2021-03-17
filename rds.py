from flask_redis import FlaskRedis
'''
redis 默认返回二进制数据，decode_responses参数对返回进行处理
'''

redis_client = FlaskRedis(decode_responses=True)
redis_client2 = FlaskRedis(decode_responses=True, config_prefix='REDIS2')
redis_client3 = FlaskRedis(decode_responses=True, config_prefix='REDIS3')