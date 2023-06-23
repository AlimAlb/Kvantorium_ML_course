import colorama
import time
import os
from pynput import keyboard

white = colorama.Fore.WHITE
red = colorama.Fore.RED
back = colorama.Back.BLACK
blue = colorama.Fore.BLUE
bwhite = colorama.Back.WHITE
black = colorama.Fore.BLACK
colorama.init(autoreset=True)

def clear():
    if os.name == "posix": os.system('clear')
    elif os.name in ("nt", "dos", "ce"): os.system('CLS')

def func1():
    print("var 1 func")

def func2():
    print("var 2 func")

def func3():
    print("var 3 func")


def printVariants(variants, variant):
    for varId, var in enumerate(variants):
        if varId == variant:
            file = open('start.txt')
            start = file.read()
            print(back+bwhite+black+var["text"])
        else:
            print("", back+var["text"])    





def handler(key):
    global isChoosed
    global varid
    if key == keyboard.Key.up:
        varid-=1
    elif key == keyboard.Key.down:
        varid+=1
    elif key == keyboard.Key.enter:
        print(varid+1, "selected!")
        eval(variants[varid]["data"])
        listener.stop()
        return
        
    if varid == -1:
        varid = len(variants)-1
    if varid  == len(variants):
        varid = 0
    clear()
    printVariants(variants, varid)

    print(varid)
with keyboard.Listener(on_press=handler) as listener:
    clear()
    printVariants(variants, varid)
    listener.join()


