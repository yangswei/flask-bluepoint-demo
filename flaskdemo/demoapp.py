from flask import Flask, request, render_template, redirect
from .bluepoint import bp

#from .util      import utilclass or function
#from .otherutil import utilclass or function
from rds import redis_client, redis_client2, redis_client3





@bp.route('/', methods=["POST"], strict_slashes=False)
def Indexf():
  '''
  默认视图，请求路径是   http://xxx/demo/ -> bluepoint.py中定义
  '''
  #Arg1 = request.args["arg1"]
  return '200'