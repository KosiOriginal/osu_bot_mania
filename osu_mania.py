import psutil
import pyautogui
import time

KEYWORD = "osu!"  # match any osu! process

def find_osu_process():
    for p in psutil.process_iter(['name', 'cmdline']):
        try:
            name = p.info.get('name') or ""
            cmdline = " ".join(p.info.get('cmdline') or [])
            if KEYWORD.lower() in name.lower() or KEYWORD.lower() in cmdline.lower():
                return p.pid, name  # return PID and full name
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return None, None

while True:
    pid, name = find_osu_process()
    if pid:
        print(f"osu is running! PID={pid}, Name={name}")

        # Example: move the mouse to the center of the screen
        screen_width, screen_height = pyautogui.size()
        pyautogui.moveTo(screen_width // 2, screen_height // 2)

        # Example: click (you can replace with osu! interaction logic)
        # pyautogui.click()

    else:
        print("osu process not running")
    
    time.sleep(1)
