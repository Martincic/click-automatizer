from threading import Thread
from time import sleep
import win32api, win32con
import pyautogui
import keyboard
import os

def clickPositions(all_positions, repeat, timeout):

    #Activate safety killswitch
    thread = Thread(target = safetyKillswitch)
    thread.start()
    
    should_repeat = True
    iteration = 0

    while should_repeat:
        for position in all_positions:
            sleep(float(timeout))
            click(position.x, position.y)
        
        iteration += 1
        if iteration == int(repeat):
            should_repeat = False

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def safetyKillswitch():
    while True:
        keyboard.wait("esc")
        print("ESC key pressed! Emergency exit activated... ")
        os._exit(1)
