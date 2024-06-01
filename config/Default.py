#!/usr/bin/env python3
# by dongchao <cookie@maxcale.cn>


from urllib.parse import quote_plus as urlquote


class Default:

    APP_NAME = ''
    APP_AUTHOR = ''
    SECRET_KEY = '2e6089552d52dc6d703054f6eddfcd5c'

    APP_LOG_PATH = 'E:/python3/flask_api/logs'

    ES_HOST = 'http://192.168.0.138:9200'
    ES_USERNAME = 'elastic'
    ES_PASSWORD = 'Tms98!@#Md6'

    # 数据库连接参数
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://wisepkg:{}@192.168.0.138/wisepkg?charset=utf8".format(urlquote("W9gTsl{#"))
    # 设置sqlalchemy自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 设置每次请求结束后会自动提交数据库中的改动
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 查询时显示原始SQL语句
    SQLALCHEMY_ECHO  = False

    # client param error.
    CLIENT_REQUEST_PARAM_ERR_MESSAGE = 'The request parameter is empty.'
    CLIENT_REQUEST_PARAM_ERR_CODE = '40001'

    # server response success.
    SERVER_RESPONSE_SUCCESS_MESSAGE = 'The server processed successfully.'
    SERVER_RESPONSE_SUCCESS_CODE = '20000'
