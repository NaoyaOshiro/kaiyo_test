#coding: utf-8
import time
import sys
sys.path.append("/kaiyo/my_mod")
from my_get_serial import get_data, send_data
from my_motor import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, br_xr, go_back_each, up_down_each, spinturn_each, spinturn_meca

# yawの値が「右に-1~-180, 左に1~180」
def my_map( val ):
    if val <= 50:
        in_min = 0
        in_max = 50
        out_min = 0
        out_max = 100
        val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
        # 少数切り捨ての為intに変換
        return int(val)
    else:
        in_min = 100
        in_max = 50
        out_min = -0
        out_max = -100
        val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
        # 少数切り捨ての為intに変換
        return int(val)


def my_map_p( val ):
    if val >= 1:
        in_min = 1
        in_max = 100
        out_min = 1
        out_max = 100
        val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
        # 少数切り捨ての為intに変換
        return int(val)
    elif val <= -1:
        in_min = -1
        in_max = -100
        out_min = -1
        out_max = -100
        val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
        # 少数切り捨ての為intに変換
        return int(val)
    else:
        return 0


# 目標値
# gol_val = 0
# # 現在値
# now_val = 0
# # 偏差
# dev_val = 0
# # 操作量
# set_val = 0


# yawの値が「右に0~360」
def my_map_3( val ):
    if val >= 1:
        in_min = 1
        in_max = 100
        out_min = 1
        out_max = 100
        val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
        # 少数切り捨ての為intに変換
        return int(val)
    elif val <= -1:
        in_min = -100
        in_max = -1
        out_min = 101
        out_max = 200
        val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
        # 少数切り捨ての為intに変換
        return int(val)
    else:
        return 0



# 指定した角度に機体を持っていく関数
def yaw(val):
    while True:
        # up_down(60)
        diving(50)

        gol_val = val
        # yawを取得して変換(now_val = -100 ~ 100)
        now_val = my_map(get_data("yaw"))
        print "aaa", now_val
        # (now_val2 = 0 ~ 200)
        now_val2 = my_map_3(now_val)
        print "bbb", now_val2
        print "gol_val", gol_val
        print "now_val", now_val
        # 偏差を調べる
        # dev_val = gol_val - now_val
        dev_val = now_val2 - gol_val
        if dev_val >= 101:
            dev_val = -(200 - dev_val)

        spinturn(-dev_val)

        print "dev_val", -dev_val

        # 目標角度になったら終了
        if dev_val <= 2 and dev_val >= -2:
            print "balance OK !!!"
            stop_go_back()
            return 0

        print


# 指定した角度に機体を持っていく関数
def go_yaw(speed, angle, set_time):
    old_time = time.time()
    while True:
        diving(80)
        # up_down(-80)

        gol_val = angle
        # yawを取得して変換
        now_val = my_map(get_data("yaw"))
        print "gol_val", gol_val
        print "now_val", now_val
        # 偏差を調べる
        dev_val = gol_val - now_val
        if dev_val <= 100:
            print "dev_val",dev_val
        else:
            # 左側を向いていれば、この計算
            dev_val = -1*((100 - (-1*now_val)) + (100 - gol_val))
            print "dev_val2", dev_val

        r = speed
        l = speed

        if dev_val >= 0:
            # 右に動く（右を弱める）
            r = speed - dev_val
        else:
            # 左に動く（左を弱める）
            l = speed + dev_val

        go_back_each(l, r, 0)

        print l, r
        print

        ela_time = time.time() - old_time
        print ela_time

        if ela_time >= set_time:
            break

# 潜水
def diving(val):

    depth = get_data("depth")
    # 変換
    map_depth = my_map_depth(depth)
    print "depth", depth

    now_val = map_depth
    gol_val = val
    dev_val = gol_val - now_val


    print "now_val", now_val
    print "gol_val", gol_val
    print "dev_val", dev_val
    dev_val = my_map_depth2(dev_val)
    print "dev_val_map",dev_val
    print
    up_down(-dev_val)

# 潜水
def diving_while(val):
    while True:
        depth = get_data("depth")
        # 変換
        map_depth = my_map_depth(depth)
        print "depth", depth

        now_val = map_depth
        gol_val = val
        dev_val = gol_val - now_val


        print "now_val", now_val
        print "gol_val", gol_val
        print "dev_val", dev_val
        dev_val = my_map_depth2(dev_val)
        print "dev_val_map",dev_val
        print
        up_down(-dev_val)
        
        if dev_val <= 2 and dev_val >= -2:
            print "depth OK !!!"
            stop_up_down()
            return 0


def my_map_depth2(val):
    in_min = -50
    in_max = 50
    out_min = -100
    out_max = 100
    val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    if val >= 100: val = 100
    if val <= -100: val = -100
    # 少数切り捨ての為intに変換
    return int(val)


def my_map_depth(val):
    # in_min = -0.064
    in_min = -1.4
    in_max = 2.5

    if val <= in_min: val = in_min
    if val >= in_max: val = in_max

    in_min = in_min
    in_max = in_max
    out_min = 0
    out_max = 100
    val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    # 少数切り捨ての為intに変換
    return int(val)
