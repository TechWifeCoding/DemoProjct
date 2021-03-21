# -*- coding:utf-8 -*-
__author__ = 'liuxiaotong'

import dataset


# data access object
from config import db as odb
from config.db import con_str


class UserInfoDao:
    #                     协议     账号  密码                ip   : 端口 / cls.db_name
    db=odb
    @classmethod
    def get_by_username(cls, username):
        res = cls.db.query('select * from user_info where username = :username;', {"username": username})
        res = [dict(item) for item in res]
        if res:
            return res[0]
        return None

    @classmethod
    def get_by_uid(cls, uid):
        res = cls.db.query('select * from user_info where uid = :uid;', {"uid": uid})
        res = [dict(item) for item in res]
        if res:
            return res[0]
        return None

    @classmethod
    def create_user(cls, username, password):
        # sql = 'insert into user_info (username, password) values (:username, :password)'
        params = {
            'username': username,
            'password': password,
        }
        table = cls.db['user_info']
        return table.insert(params)

if __name__ == '__main__':
    res = UserInfoDao.create_user(
        "chenxi3", "123123"
    )
    print(res)

