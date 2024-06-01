#!/usr/bin/env python3
# by dongchao <cookie@maxcale.cn>


import pymysql
from app import app


class Mysql(object):
    def __init__(self):
        try:
            self.db = pymysql.connect(host="192.168.0.138", user="wisepkg", password="W9gTsl{#", database="wisepkg")
            # 游标对象
            self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
        except Exception as e:
            app.logger.error(e)
        finally:
            pass

    # 查询数据函数
    def query_all(self, sql):
        # 执行sql语句
        self.cursor.execute(sql)
        # 获取所有的记录
        results = self.cursor.fetchall()
        return results

    # 关闭
    def __del__(self):
        self.cursor.close()
        self.db.close()
