# coding: utf-8
# 参考
# https://qiita.com/meznat/items/19cfc3ee2e145d4e5baf
#モジュールのインポート
from tinydb import TinyDB, Query

#データベースの作成
db = TinyDB('sensor_log.json')


def insert(data):
    db.insert(data)

def select():
    return db.all()

def purge():
    db.purge()


if __name__ == '__main__':
    # insert({'apple':4, 'orange':2})
    # print select(1)
    purge()
