import subprocess
import time
import psutil

def open_new_session():
    # Kill existing processes related to 'node' command
    for proc in psutil.process_iter():
        try:
            if 'node' in proc.name():
                proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    # Start new session
    subprocess.run(['node', 'bottok.js', '-t', 'Up Views', '-l', 'https://www.tiktok.com/@user/video/7338810538903866630'])

while True:
    open_new_session()
    time.sleep(640)  # 10 minutes and 40 seconds
