#!/usr/bin/env python3
# by dongchao <cookie@maxcale.cn>


from flask import request, jsonify, g
from . import room_blueprint
from app import app
import json, datetime
from libs.mysqldb import Mysql


@room_blueprint.route('/query', methods=['POST'])
def room_query():
    app.logger.info("{} - {} - room_query - 接受到请求，开始处理>>>".format(g.request_id, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    try:
        post_json = json.loads(request.get_data(as_text=True))
    except Exception as e :
        app.logger.error(e)
        post_json = None
    finally:
        pass

    if post_json is None or post_json == '':
        return jsonify({'error_code': app.config['CLIENT_REQUEST_PARAM_ERR_CODE'], 'message': app.config['CLIENT_REQUEST_PARAM_ERR_MESSAGE'], 'data': None})

    # name = post_json.get('name')
    # sql = "select  * from china_open_room_id where Name='{}' limit 1".format(name)
    app.logger.info("{} - {} - room_query - 开始查询>>>".format(g.request_id, datetime.datetime.now().strftime(
        '%Y-%m-%d %H:%M:%S')))
    sql = "select * from china_open_room_id limit 100000"
    qy = Mysql().query_all(sql)
    app.logger.info("{} - {} - room_query - 处理完毕，开始返回。>>>".format(g.request_id, datetime.datetime.now().strftime(
        '%Y-%m-%d %H:%M:%S')))
    return jsonify({'error_code': app.config['SERVER_RESPONSE_SUCCESS_CODE'], 'message': app.config['SERVER_RESPONSE_SUCCESS_MESSAGE'], 'data': qy})
