import curses
import os
import audio

def main(win):
    win.nodelay(True)
    key=""
    win.clear()                
    win.addstr("Detected key:")
    while 1:          
        try:                 
           key = win.getkey()         
           win.clear()                
           win.addstr("Detected key:")
           win.addstr(str(key)) 
           if key == "r":
               audio.record()
           if key == os.linesep:
              break           
        except Exception as e:
           # No input   
           pass         

curses.wrapper(main)