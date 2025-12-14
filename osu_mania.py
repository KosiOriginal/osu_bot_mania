import win32gui
import pyautogui
import time

def find_osu_windows():
    osu_titles = []

    def callback(hwnd, extra):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if "osu!" in title.lower():  # match substring
                osu_titles.append(title)
        return True

    win32gui.EnumWindows(callback, None)
    return osu_titles

while True:
    titles = find_osu_windows()
    if titles:
        for t in titles:
            print(f"osu window detected: {t}")
            # Example: move mouse to center
            screen_width, screen_height = pyautogui.size()
            pyautogui.moveTo(screen_width // 2, screen_height // 2)
    else:
        print("osu is not running")
    
    time.sleep(1)
