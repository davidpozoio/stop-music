import re
import os
import threading
import subprocess

pattern = r"Device ([\w+:]+)"

devices = []

with open("devices", "r") as file:
    devices = re.findall(pattern, file.read())    


def l2flood(device):
    process = subprocess.Popen(["sudo", "./l2flood/l2flood", f"{device}"])
    try:
        print('Running in process', process.pid)
        process.wait(timeout=10)
    except subprocess.TimeoutExpired:
        print('Timed out - killing', process.pid)
        process.kill()
    print("Done")

for device in devices:
    l2flood(device=device)
