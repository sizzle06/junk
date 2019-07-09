from time import sleep
import pyautogui as pa

if __name__ == '__main__':
    for i in range(2000):
        sleep(10)
        pa.click(x=183, y=1180, clicks=2)
        sleep(3)
        pa.hotkey("command", "shift", "l")
        sleep(15)
