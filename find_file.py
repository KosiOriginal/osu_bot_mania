import os
import win32api
import time
import win32gui
import pyautogui

found = False
difficulty = "Hard" # difuculty
name_song = "Transform" # imeto na songa




#finding first folder of file
#os.listdir("") - listing files & directory in directory
for filename in os.listdir(r"C:\Users\Kosi\AppData\Local\osu!\Songs"): # NIKI TOWA E MOQTA DIREKTORIQ . TOEST NQMA DA RABOTI ZA TEB, trqbwa da si slovish svoqta 
    if name_song in filename:
        found = True
        print(filename)
        break
if found:
    print("YES")
else:
    print("No")



#combination of files
first_path = r"C:\Users\Kosi\AppData\Local\osu!\Songs"
secound_path = os.path.join(first_path, filename)


#difficulty finding
for filename2 in os.listdir(secound_path):
    if difficulty in filename2:
        print(filename2)
        break

file_path = os.path.join(secound_path, filename2)
print(file_path)


#extracting file data
with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
    print(f.read())


# active windows on screen
while True:
    def enum_windows(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if title:  
                windows.append(title)

    all_windows = []
    win32gui.EnumWindows(enum_windows, all_windows)

    #searching osu in active windows
    for title in all_windows:
        if "osu" in title.lower():
            print("Found:", title)
            time.sleep(0.5)
