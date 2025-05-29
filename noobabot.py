#-----------------------------------PIP---------------------------------------------
import keyboard
import pygetwindow as gw
import time
import random
#------------------------------WINDOW TO ROBLOX-------------------------------------
def focus_roblox():
    windows = gw.getWindowsWithTitle("Roblox")
    if windows:
        roblox_window = windows[0]
        roblox_window.activate()
    else:
        print("Run Roblox first silly :P")
#-----------------------------------INTRO-------------------------------------------
focus_roblox()
time.sleep(0.3)
keyboard.press("/")
keyboard.release("/")
keyboard.write(".NOOBABOT", delay=0.1)
keyboard.press("enter")
keyboard.release("enter")
#----------------------------------SHOW COMMANDS------------------------------------
print("NOOBABOT BETA")
print("Commands:")
print("- say")
print("- credits")
print("- exit")
print("- jump")
print("- move_forward")
print("- move_backwards")
print("- move_left")
print("- move_right")

#-------------------------------INSERT COMMAND LOOP---------------------------------
while True:
    
    iput = input("Insert Command: ")

#--------------------------------CODE FOR COMMANDS----------------------------------
    if iput == "say":
        ipsay = input("What should i say? Add a dot at the beggining(theres a bug)! ")
        focus_roblox()
        keyboard.press("/")
        keyboard.release("/")
        keyboard.write(ipsay, delay=0.1)
        keyboard.press("enter")
        keyboard.release("enter")
    elif iput == "credits":
        print("Code made by theamazingnoob :)")
    elif iput == "exit":
        print("Exiting...")
        break
    elif iput == "jump":
        focus_roblox()
        time.sleep(0.5)
        keyboard.press("space")
        time.sleep(0.1)
        keyboard.release("space")
    elif iput == "move_forward":
        try:
            movsec = float(input("How many seconds do i move?"))
            focus_roblox()
            time.sleep(0.1)
            keyboard.press("w")
            time.sleep(movsec)
            keyboard.release("w")
        except ValueError:
            print("Put a number, not a letter!")

    elif iput == "move_backwards":
        try:
            movsec = float(input("How many seconds do I move?"))
            focus_roblox()
            time.sleep(0.1)
            keyboard.press("s")
            time.sleep(movsec)
            keyboard.release("s")
        except ValueError:
            print("Put a number, not a letter!")

    elif iput == "move_left":
        try:
            movsec = float(input("How many seconds do I move?"))
            focus_roblox()
            time.sleep(0.1)
            keyboard.press("a")
            time.sleep(movsec)
            keyboard.release("a")
        except ValueError:
            print("Put a number, not a letter!")

    elif iput == "move_right":
        try:
            movsec = float(input("How many seconds do I move?"))
            focus_roblox()
            time.sleep(0.1)
            keyboard.press("d")
            time.sleep(movsec)
            keyboard.release("d")
        except ValueError:
            print("Put a number, not a letter!")
