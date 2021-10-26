from ctypes import pythonapi
import pyautogui
import time


# 1
def cursor_position():
    print(pyautogui.position())


# 2
def cursor_position_time(time1, inter):
    i = 0
    while time1 >= i:
        print(pyautogui.position())
        i += 1
        time.sleep(inter)


# 3
def screen_size():
    print(pyautogui.size())


def move_to(x, y, duration):
    pyautogui.moveTo(x, y, duration)


def click_er(x, y, clicks, interval):
    pyautogui.click(x=x, y=y, clicks=clicks, interval=interval, button='left')
    #  >>> pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')


while True:

    #  input("Press Enter to continue...")

    print('------------------')
    print('choose option')
    print('1 - cursor position (no arguments)')
    print('2 - cursor position (how times will check, interval)')
    print('3 - screen size resolution')
    print('4 - move to screen point (x, y, duration)')
    print('5 - click (x, y, clicks, interval, button)')
    print('------------------')

    option_1 = int(input())

    if option_1 == 1:
        cursor_position()
        input("Press Enter to continue...")

    if option_1 == 2:
        print('how many times will check')
        option_2_1 = int(input())

        print('interval behind checks')
        option_2_2 = int(input())

        cursor_position_time(option_2_1, option_2_2)

        input("Press Enter to continue...")

    if option_1 == 3:
        screen_size()
        input("Press Enter to continue...")

    if option_1 == 4:
        print('x position')
        option_4_1 = int(input())

        print('y position')
        option_4_2 = int(input())

        print('duration in sec how long will go to the point')
        option_4_3 = int(input())

        move_to(option_4_1, option_4_2, option_4_3)

        input("Press Enter to continue...")

    if option_1 == 5:
        print('x position')
        option_5_1 = int(input())

        print('y position')
        option_5_2 = int(input())

        print('how many clicks will click')
        option_5_3 = int(input())

        print('interval')
        option_5_4 = int(input())

        print('left button or right button')
        option_5_5 = "left"

        click_er(option_5_1, option_5_2, option_5_3, option_5_4)

        input("Press Enter to continue...")
