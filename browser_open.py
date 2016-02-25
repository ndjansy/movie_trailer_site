import time
import webbrowser

def take_break(): 
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=-qlJiGGvPUI")

count = 0

while count < 4:
    take_break()
    count -= 1
    break
