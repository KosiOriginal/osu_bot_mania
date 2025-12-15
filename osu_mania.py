import win32gui
import os
import time

OSU_SONGS_PATH = r"C:\Users\Kosi\AppData\Local\osu!\Songs"

def find_osu_windows():
    osu_titles = []

    def callback(hwnd, extra):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if "osu!" in title.lower():
                osu_titles.append(title)
        return True

    win32gui.EnumWindows(callback, None)
    return osu_titles

def search_songs_folder(window_title):
    window_lower = window_title.lower()
    for folder_name in os.listdir(OSU_SONGS_PATH):
        folder_path = os.path.join(OSU_SONGS_PATH, folder_name)
        if os.path.isdir(folder_path):
            for file_name in os.listdir(folder_path):
                if window_lower in file_name.lower():
                    return os.path.join(folder_path, file_name)
    return None

while True:
    titles = find_osu_windows()
    if titles:
        for t in titles:
            print(f"osu window detected: {t}")
            found_file = search_songs_folder(t)
            if found_file:
                print("YES")
                print(f"Found file path: {found_file}")
            else:
                print("NO")
    else:
        print("osu is not running")
    
    time.sleep(1)
import win32gui
import os
import time

OSU_SONGS_PATH = r"C:\Users\Kosi\AppData\Local\osu!\Songs"

def find_osu_windows():
    osu_titles = []

    def callback(hwnd, extra):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if "osu!" in title.lower():
                osu_titles.append(title)
        return True

    win32gui.EnumWindows(callback, None)
    return osu_titles

def search_songs_folder(window_title):
    window_lower = window_title.lower()
    for folder_name in os.listdir(OSU_SONGS_PATH):
        folder_path = os.path.join(OSU_SONGS_PATH, folder_name)
        if os.path.isdir(folder_path):
            for file_name in os.listdir(folder_path):
                if window_lower in file_name.lower():
                    return os.path.join(folder_path, file_name)
    return None

while True:
    titles = find_osu_windows()
    if titles:
        for t in titles:
            print(f"osu window detected: {t}")
            found_file = search_songs_folder(t)
            if found_file:
                print("YES")
                print(f"Found file path: {found_file}")
            else:
                print("NO")
    else:
        print("osu is not running")
    
    time.sleep(1)
