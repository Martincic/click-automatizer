from time import sleep
import win32api, win32con
import pyautogui

def clickPositions(all_positions, repeat, timeout):
    
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

