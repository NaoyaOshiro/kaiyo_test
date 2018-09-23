#coding: utf-8
import time
import sys
sys.path.append("/kaiyo/my_mod")
from my_get_serial import get_data, send_data, log
from my_motor import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, br_xr, go_back_each, up_down_each, spinturn_each, spinturn_meca
from my_balance import yaw, go_yaw, diving, diving_while
from my_rc import t10j
from my_check import operation_check


# -----------------------------------------------------------------------------

def mode_set():
    stop()
    # センサー初期化
    send_data("reboot")
    # time.sleep(1)
    # send_data("yaw_zero off")

    # textにlogを残すか？
    # log()

    # 動作チェックするか？
    # operation_check()

    # data =  get_data("all")
    # while data["mgs"] == 0:
    #     data =  get_data("all")
    #     print data["mgs"]
    #     print "Ready !!"

    # print "5"
    # time.sleep(1)
    # print "4"
    # time.sleep(1)
    print "3"
    time.sleep(1)
    print "2"
    time.sleep(1)
    print "1"
    time.sleep(1)
    print "Go !!"





def test(set_speed, set_time):
    stop()

    # 浮上
    print "up"
    # diving_while(20)
    up_down(80)
    time.sleep(3)
    yaw(0)

    # Uターン地点まで行く
    print "go_yaw"
    go_yaw(set_speed, 0, set_time)

    # 慣性で流れるのを停止
    stop()
    time.sleep(0.5)
    go_back(-50)
    time.sleep(1)
    stop()

    # 浮上
    print "up"
    # diving_while(20)
    up_down(100)
    time.sleep(2)

    # Uターン
    print "yaw"
    yaw(100)

    # スタート地点まで行く
    print "go_yaw"
    go_yaw(set_speed-2, 100, set_time)


    # 浮上
    print "up"
    # diving_while(20)
    up_down(80)
    time.sleep(3)


    # Uターン
    print "yaw"
    yaw(0)

    stop()

# -------------------------------------------------------------------
if __name__ == '__main__':
    try:
        mode_set()

        while True:
            # センサーデータ取得
            data =  get_data("all")
            # if data["mgs"] == 0: break
            # print data["mgs"]
            # print data["rot3"]
            # a = data["rot3"]
            # print data

            # if data["mgs"] == 1: break

            # print data["depth"]

            # test(set_speed, set_time)
            try:
                # test(30, 7)
                yaw(0)
                # diving_while(1)
            except IOError:
                # 受信エラー
                stop()
                print "IOError!!!!!!!!!!"
                break

            # break

            # test(30, 7)
            # break

            # 潜水
            # diving(50)

            # 指定した角度に向く(-100 ~ 0 ~ 100)
            # up_down(-100)
            # go_back(100)

            # yaw(20)


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
            # up_down(-30)

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



        stop()

    except KeyboardInterrupt as e:
        stop() #Ctrl + Cを押したときの処理
