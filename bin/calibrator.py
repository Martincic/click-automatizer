from threading import Thread
from time import sleep
import win32api
import pyautogui

TIME_TO_PRINT = 4
POSITIONING = True

all_positions = []
current_position = {}

def calibrateMousePositions(num):
    global POSITIONING, current_position

    #Start printing positions
    thread = Thread(target = printPositions)
    thread.start()
    
    for x in range(0, num):

        input() 
        all_positions.append(current_position)
        print("Your %d. position: %s" % (x+1, current_position))
    
    print("\nAll positions set!")
    POSITIONING = False
    return all_positions


def printPositions():
    global POSITIONING, current_position
    try:
        while POSITIONING:
            print(pyautogui.position())
            current_position = pyautogui.position()
            sleep(TIME_TO_PRINT)
    except KeyboardInterrupt:

        exit()


