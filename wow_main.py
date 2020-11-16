import pydirectinput
import time
import keyboard
import cooldown

def anti_afk():
    while True:
        # print(pydirectinput.position())
        print("starting loop")
        if keyboard.is_pressed('f12'):
            break

        pydirectinput.leftClick(1167, 1059)
        time.sleep(1)
        pydirectinput.leftClick(958, 597)
        print("waiting to log out")
        time.sleep(30)

        print("logging back in")
        pydirectinput.leftClick(959, 990)
        time.sleep(600)

if __name__ == "__main__":

    # keyboard.add_hotkey('f23', call_input, args=['shadow_stomp'])
    keyboard.add_hotkey('f24', anti_afk)

    keyboard.wait()