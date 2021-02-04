import pyautogui
import time


def paste():
    """Will paste"""
    from sys import platform
    if platform == "darwin":
        hot_key(['command', 'v'])
    else:
        hot_key(['ctrl', 'v'])


def copy():
    """Will copy"""
    from sys import platform
    if platform == "darwin":
        hot_key(['command', 'c'])
    else:
        hot_key(['ctrl', 'c'])


def key_down(key):
    """Will hold on a key down """
    pyautogui.keyDown(key)


def key_up(key):
    """Will release a down key """
    pyautogui.keyUp(key)


def select_all():
    """Will select all."""
    from sys import platform
    if platform == "darwin":
        hot_key(['command', 'a'])
    else:
        hot_key(['ctrl', 'a'])


def hot_key(btn_list):
    pyautogui.keyDown(btn_list[0])

    time.sleep(1)
    for i in range(1, len(btn_list)):
        key_down(btn_list[i])

    time.sleep(1)
    for i in range(1, len(btn_list)):
        key_up(btn_list[i])

    time.sleep(1)
    key_up(btn_list[0])


def press(keys, presses=1, interval=0.0):
    """Performs a keyboard key press down, followed by a release."""
    pyautogui.press(keys, presses, interval)
