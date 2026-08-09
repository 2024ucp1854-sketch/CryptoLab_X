from datetime import datetime
import os

def log_action(action):
    os.makedirs("outputs", exist_ok=True)

    with open("outputs/log.txt", "a") as log_file:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{current_time} -> {action}\n")