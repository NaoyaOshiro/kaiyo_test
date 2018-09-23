# -*- coding: utf-8 -*-
# sudo pip install pyserial
import serial
import ast
import time
from datetime import datetime

import sys
sys.path.append("/kaiyo/my_mod2")
# from my_tinydb import insert, select, purge

# 追加書き込みモードでオープン
# file = open('/kaiyo/log/'+str(datetime.now().strftime('%y%m%d_%H%M%S'))+'.txt', 'a')

# logsをテキストに残すか聞くプログラム
log = 0
def log():
    print "Do you want to logs? [Y/n]",
    key_in = raw_input()
    if key_in == "y" or key_in == "Y":
        print "It worked normally!!"
        log = 1
        file = open('/kaiyo/log/'+str(datetime.now().strftime('%y%m%d_%H%M%S'))+'.txt', 'a')

    elif key_in == "n" or key_in == "N":
        print "NO!!"
    else:
        log = 0


# ArduinoMEGAとpinで接続
ser = serial.Serial('/dev/ttyS0', 115200)
# ArduinoMEGAとUSBケーブル接続
# ser = serial.Serial('/dev/ttyACM0', 115200)


def get_data(val):
    while True:
        # Arduino から一行受信
        data = ser.readline()
        # 受信エラー確認
        try:
            # dictに変換
            data = ast.literal_eval(data)
            # print data
            # tinydbにinsert
            # insert(data)
            if log == 1:
                text_write(data)

            if data["state"] != "normal":
                print "state", data["state"] + "!!"
                return 0
            # すべてのデータがほしいとき
            # if val == "all": return data
            if val == "all":
                # yawの値を変換してから渡す
                # 0 ~ 180, 0 ~ -180
                # print "aaa", data["yaw"]
                data["yaw"] = my_map(data["yaw"])
                # print "bbb", data["yaw"]
                return data
            if val == "yaw": return my_map(data[val])
            if val == "state": return data["state"]
            return data[val]
        except SyntaxError:
            # 受信エラー
            print "Reception Error!!"

"""
def get_data(val):
    while True:
        # Arduino から一行受信
        data = ser.readline()
        # 受信エラー確認
        try:
            data = data[:-3]
            data = float(data)
            print data
            data = my_map(data)
            return data
        except SyntaxError:
            # 受信エラー
            print "Reception Error!!"
"""
# ArduinoMEGAにコマンド送信
def send_data(val):
    ser.write(val)


# TinyDBにlog書き込み
def text_write(data):
    data["datetime"] = str(datetime.now())
    file.writelines(str(data) + "\n")

"""
# yawの値変換
def my_map(val):
    in_min = 0
    in_max = 360
    out_min = 0
    out_max = 100
    val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    # 少数切り捨ての為intに変換
    return int(val)
"""

# yawの値が「右に-1~-180, 左に1~180」
def my_map(val):
    if val <= 0:
        in_min = -1
        in_max = -180
        out_min = 0
        out_max = 50
        val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
        # 少数切り捨ての為intに変換
        return int(val)
    else:
        in_min = 1
        in_max = 180
        out_min = 100
        out_max = 50
        val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
        # 少数切り捨ての為intに変換
        return int(val)


if __name__ == '__main__':
    send_data("reboot")
    while True:
        # print type(get_data("all"))
        print get_data("all")

# ser.close()
