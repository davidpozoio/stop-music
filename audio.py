import subprocess

def record():
    process = subprocess.Popen(["arecord", "-vv", "-fdat", "audio.wav"])
    try:
        print('Running in process', process.pid)
        process.wait(timeout=4)
    except subprocess.TimeoutExpired:
        print('Timed out - killing', process.pid)
        process.kill()
    print("Done")