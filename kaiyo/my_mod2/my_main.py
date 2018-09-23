#coding: utf-8
import time
import sys
sys.path.append("/kaiyo/my_mod2")
from my_get_serial import get_data, send_data, log
from my_motor import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, br_xr, go_back_each, up_down_each, spinturn_each, spinturn_meca
from my_balance import yaw, go_yaw, diving
from my_rc import t10j
from my_check import operation_check






def test(set_time):
    stop()

    # Uターン地点まで行く
    print "go_yaw"
    go_yaw(30, 0, set_time)

    # Uターン
    print "yaw"
    yaw(100)

    # スタート地点まで行く
    print "go_yaw"
    go_yaw(30, 100, set_time)

    stop()

# -------------------------------------------------------------------
# if __name__ == '__main__':
def my_main(bottlle_val):
    # センサーデータ取得
    # data =  get_data("all")

    print bottlle_val
    return 0
    # print datarint
    # print data["depth"]

    # test(10)
    # break

    # 潜水
    # diving(80)

    # 指定した角度に向く(-100 ~ 0 ~ 100)
    # up_down(50)
    # yaw(0)


    # 指定した速度で指定した角度と時間の前進(0~100, -100 ~ 0 ~ 100)
    # (速度0 ~ 100, 角度-100 ~ 100, 時間s)

    # try:
    #     go_yaw(20, 0, 20)
    # except IOError:
    #     # 受信エラー
    #     stop()
    #     print "IOError!!!!!!!!!!"
    #     break
    #
    # break


    # go_back_each(-7, -7, 0)

    # go_back(100)
    # up_down(100)

    # 右旋回_左旋回(-100 ~ 100)
    # spinturn(10)

    # 右傾き_左傾き(-100 ~ 100)
    # roll(20)

    # t10j(data)

    # try:
    #     t10j(data)
    # except IOError:
    #     # 受信エラー
    #     stop()
    #     print "IOError!!!!!!!!!!"
    #     break
