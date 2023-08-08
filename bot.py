from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from pynput.keyboard import Key
import pyautogui
import time
from random import *
import datetime
import psutil
import threading

vaccation_time = 0
vaccation = False

# -- Move Fun --
def auto_move():
    global vaccation
    current_time = datetime.datetime.now()
    hour = current_time.hour
    am_time = randint(10,60)
    timecount = 0
    pyautogui.keyDown('alt')
    for x in range(randint(1,5)):
        pyautogui.press('tab')
    pyautogui.keyUp('alt')
    while (timecount <= am_time):
        if (vaccation == False):
            return 
        timecount += 1
        # time.sleep(1)
        rnd = randint(0,999)
        if hour >= 17 or hour <= 10: 
            if (rnd <= 100):
                pyautogui.keyDown('ctrl')
                pyautogui.press('ctrl')
                pyautogui.keyUp('ctrl')
            elif (rnd <= 300):
                pyautogui.keyDown('up')
                pyautogui.press('up')
                pyautogui.keyUp('up')
            elif (rnd <= 500):
                pyautogui.keyDown('left')
                pyautogui.press('left')
                pyautogui.keyUp('left')
            elif (rnd <= 700):
                pyautogui.keyDown('right')
                pyautogui.press('right')
                pyautogui.keyUp('right')
            elif (rnd <= 900):
                pyautogui.keyDown('down')
                pyautogui.press('down')
                pyautogui.keyUp('down')
            else:
                continue
# Mouse event callback function
def on_mouse_move(x, y):
    global vaccation_time
    vaccation_time = 0

# Keyboard event callback function
def on_key_press(key):
    global vaccation_time, vaccation
    if (key== Key.space):
        vaccation = False 
        # print(vaccation)
        vaccation_time = 0 
    try:
        # print(key)
        vaccation_time = 0
    except AttributeError:
        print(f'Special key {key} pressed')

# confirm vaccation
def vaccation_time_count():
    global vaccation_time, vaccation
    vaccation_time += 1
    # print(vaccation_time)
    if (vaccation_time >= 118):
        vaccation = True
    if (vaccation):
        am_thread = threading.Thread(target = auto_move)
        #kill_process_by_name("AnyDesk.exe")
        am_thread.start()
        am_thread.join()

# -- kill anydesk ---
def kill_process_by_name(process_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            try:
                proc.kill()
            except psutil.AccessDenied:
                continue


# Create listener for mouse events
mouse_listener = MouseListener(on_move=on_mouse_move)

# Create listener for keyboard events
keyboard_listener = KeyboardListener(on_press=on_key_press)

# Start listening for mouse and keyboard events
mouse_listener.start()
keyboard_listener.start()

# auto_move thread

while (1):
    time.sleep(1)
    thread1 = threading.Thread(target = vaccation_time_count)
    thread1.start()
    thread1.join()

mouse_listener.join()
keyboard_listener.join()