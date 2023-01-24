import subprocess
import time

while True:
    subprocess.Popen(["C:\\Program Files (x86)\\Grinding Gear Games\\Path of Exile\\PathOfExile"])
    time.sleep(600)
    subprocess.run(["taskkill", "/IM", "PathOfExile", "/F"])
    time.sleep(1200)
