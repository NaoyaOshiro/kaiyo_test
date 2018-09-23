#!/bin/env python
# coding: utf-8
import json
from bottle import route, run, request, HTTPResponse, template, static_file
import atexit
import time
import sys
sys.path.append("/kaiyo/my_mod2")
from my_get_serial import get_data, send_data, log
from my_motor import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, br_xr, go_back_each, up_down_each, spinturn_each, spinturn_meca
from my_balance import yaw, go_yaw, diving
from my_rc import t10j
from my_check import operation_check
from my_main import test, my_main

# ----------------------------------------------------------------------------


@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')


@route('/')
def root():
    return template("index")


def my_map(val):
    in_min = 0
    in_max = 360
    out_min = 0
    out_max = 200
    val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    val = 200 - val
    # 少数切り捨ての為intに変換
    return int(val)



# curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"num":"0", "onoff":true}' http://192.168.1.88:8080/setLed
@route('/setLed', method='POST')
def setLedEntry():
    var = request.json
    fnc(var)



def fnc(val):
    print
    print val
    # yaw(0, my_map(val["yaw"]))
    # go_back(50)
    print my_map(val["yaw"])
    # print "slider1", val["slider1"]
    # print "slider2", val["slider2"]
    # print "slider3", val["slider3"]
    if int(val["slider1"]) == 0:
        go_back(int(val["slider1"]))
    else:
        spinturn(int(val["slider2"]))

    up_down(int(val["slider3"]))
    # up_down(60)
    return 0




def set_kaiyo():
    stop()
    # センサー初期化
    send_data("reboot")
    # time.sleep(1)
    # send_data("yaw_zero off")

    # textにlogを残すか？
    # log()

    # 動作チェックするか？
    # operation_check()
























def main():
    print("Initialize port")
    print('Server Start')
    run(host='172.20.10.2', port=8080, debug=True, eloader=True)
    # run(host='172.20.10.6', port=8080)


def atExit():
    stop()
    print("atExit")

# atexit.register(atExit)
# main()
if __name__ == '__main__':
    set_kaiyo()
    atexit.register(atExit)
    main()
