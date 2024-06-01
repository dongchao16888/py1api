#!/usr/bin/env python3
# by dongchao <cookie@maxcale.cn>


from flask import Flask, request, g
from config import GetConfig
from flask_elasticsearch import Elasticsearch
from error.APIException import APIException, HTTPException
from error.AppException import AuthFailed, ServerError, RuntimeException
import traceback
from libs.log_handler import getLogHandler
import datetime
from libs.functions import generate_id


app = Flask(__name__)
app.config.from_object(GetConfig.run())
app.debug = app.config['DEBUG']


from .hello import hello_blueprint
from .room_record import room_blueprint

app.register_blueprint(hello_blueprint, url_prefix='/api')
app.register_blueprint(room_blueprint, url_prefix='/api')


# 配置日志记
app.logger.addHandler(getLogHandler(app.config['APP_LOG_PATH']))

es = Elasticsearch(
    hosts=[app.config['ES_HOST']],
    basic_auth=(app.config['ES_USERNAME'], app.config['ES_PASSWORD']),
    verify_certs=False,
)


@app.before_request
def before_request():
    g.request_id = generate_id()
    if request.headers.get('X-Token') is None:
        if not any(fd in request.full_path for fd in ('login', 'logout')):
            return AuthFailed()

    app.logger.info('[{}] - {} - Recevied Request>>>'.format(g.request_id, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))


@app.after_request
def after_request(response):
    app.logger.info('[{}] - {} - Send Request>>>'.format(g.request_id, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    return response


@app.errorhandler(Exception)
def framework_error(e):
    app.logger.error('{}'.format(traceback.format_exc())) # 对错误进行日志记录
    if isinstance(e, APIException):
        return e
    elif isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(code=code, msg=msg, error_code=error_code)
    elif isinstance(e, RuntimeException):
        code = 500
        msg = str(e)
        error_code = 50001
        return APIException(code=code, msg=msg, error_code=error_code)
    else:
        if not app.config['DEBUG']:
            return ServerError()
        else:
            return e

