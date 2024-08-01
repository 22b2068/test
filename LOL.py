import subprocess
import time

def open_notepads(count):
    for _ in range(count):
        subprocess.Popen(['notepad.exe'])
        # Adding a short delay to avoid overwhelming the system
        time.sleep(0.1)

if __name__ == "__main__":
    num_notepads = 10
    open_notepads(num_notepads)
