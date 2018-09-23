#coding: utf-8
import time
import sys
sys.path.append("/kaiyo/my_mod")
from my_get_serial import get_data, send_data
from my_motor import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, br_xr, go_back_each, up_down_each, spinturn_each, spinturn_meca
from my_balance import yaw, go_yaw
from my_rc import t10j

# -------------------------------------------------------------------


def operation_check():
    while True:
        my_time = 0.002
        print "Do you check the operation? [Y/n]",
        key_in = raw_input()

        if key_in == "y" or key_in == "Y":
            for i in range(100):
                go_back_each(i, 0, 0)
                print i
                time.sleep(my_time)
            for i in range(100):
                go_back_each(0, i, 0)
                print i
                time.sleep(my_time)
            for i in range(100):
                go_back_each(0, 0, i)
                print i
                time.sleep(my_time)



            stop()

            for i in range(100):
                up_down_each(0, i)
                print i
                time.sleep(my_time)
            for i in range(100):
                up_down_each(i, 0)
                print i
                time.sleep(my_time)



            stop()


            for i in range(0, -100, -1):
                up_down_each(i, 0)
                print i
                time.sleep(my_time)
            for i in range(0, -100, -1):
                up_down_each(0, i)
                print i
                time.sleep(my_time)


            stop()


            for i in range(0, -100, -1):
                go_back_each(0, 0, i)
                print i
                time.sleep(my_time)
            for i in range(0, -100, -1):
                go_back_each(0, i, 0)
                print i
                time.sleep(my_time)
            for i in range(0, -100, -1):
                go_back_each(i, 0, 0)
                print i
                time.sleep(my_time)

            stop()

            for i in range(0, -100, -1):
                go_back_each(i, i, i)
                up_down_each(i, i)
                print i
                time.sleep(my_time)

            stop()
            print "It worked normally!!"
            return 0

        elif key_in == "n" or key_in == "N":
            print "nnn"
            return 0



# for i in range(100):
#     # 前進_更新(-100 ~ 100)
#     go_back(i)
#
#     # 浮上_潜水(-100 ~ 100)
#     up_down(i)
#     print i
#     time.sleep(0.05)
# stop()
# time.sleep(2)

# -------------------------------------------------------------------
if __name__ == '__main__':
    operation_check()
