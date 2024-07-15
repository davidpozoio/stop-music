import re

pattern = r"Device ([\w+:]+)"

devices = []

with open("devices", "r") as file:
    devices = re.findall(pattern, file.read())    

print(devices)