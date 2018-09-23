# -*- coding: utf-8 -*-
"""
参考サイト
http://d.hatena.ne.jp/nakamura001/20101212/1292163993
http://archives.seul.org/pygame/users/Sep-2005/msg00132.html
http://www.pygame.org/docs/ref/joystick.html#Joystick.get_numbuttons
joystick-pygame 日本語ドキュメント
http://westplain.sakuraweb.com/translate/pygame/Joystick.cgi
"""

import pygame
import time

pygame.init()

#Loop until the user clicks the close button.
#ユーザーが閉じるボタンをクリックするまでループします
done = False

# Initialize the joysticks
#ジョイスティックを初期化
pygame.joystick.init()

# -------- Main Program Loop -----------
#while done==False:
def joy():
    # EVENT PROCESSING STEP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    joystick_count = pygame.joystick.get_count()

    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        name = joystick.get_name()

        axes = joystick.get_numaxes()
        """
        for i in range( axes ):
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    print "Axis0 :", round(joystick.get_axis( 0), 1)
                    print "Axis1 :", round(joystick.get_axis( 1), 1)
                    print "Axis2 :", round(joystick.get_axis( 2), 1)
                    print "Axis3 :", round(joystick.get_axis( 3), 1)
                    print
        """

        joy_lx = my_map(round(joystick.get_axis(0), 2))
        joy_ly = my_map(round(joystick.get_axis(1), 2))
        joy_rx = my_map(round(joystick.get_axis(2), 2))
        joy_ry = my_map(round(joystick.get_axis(3), 2))

        hat_x = joystick.get_hat(0)[0]
        hat_y = joystick.get_hat(0)[1]

        btn1 = joystick.get_button(0)
        btn2 = joystick.get_button(1)
        btn3 = joystick.get_button(2)
        btn4 = joystick.get_button(3)
        btn5 = joystick.get_button(4)
        btn6 = joystick.get_button(5)
        btn7 = joystick.get_button(6)
        btn8 = joystick.get_button(7)
        btn9 = joystick.get_button(8)
        btn10 = joystick.get_button(9)
        btn11= joystick.get_button(10)
        btn12 = joystick.get_button(11)

        # my_dict = {"axis0":axis0, "axis1":axis1, "axis2":axis2, "axis3":axis3, "hatx":hatx, "haty":haty, \
        # "btn1":btn1, "btn2":btn2, "btn3":btn3, "btn4":btn4, "btn5":btn5, "btn6":btn6, "btn7":btn7, \
        # "btn8":btn8, "btn9":btn9, "btn10":btn10, "btn11":btn11, "btn12":btn12, }

        my_dict = {"joy_lx":joy_lx, "joy_ly":joy_ly, "joy_rx":joy_rx, "joy_ry":joy_ry, "hat_x":hat_x, "hat_y":hat_y, \
        "btn1":btn1, "btn2":btn2, "btn3":btn3, "btn4":btn4, "btn5":btn5, "btn6":btn6, "btn7":btn7, \
        "btn8":btn8, "btn9":btn9, "btn10":btn10, "btn11":btn11, "btn12":btn12, }

        return my_dict



#値変換関数(入力0-100, 出力50-0)
def my_map(val):
    in_min = -1
    in_max = 1
    out_min = -100
    out_max = 100
    return int((val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
