# import keyboard
import sys
import input
import window
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from pynput.keyboard import Key


def test(x, y, button, pressed):
    print("test")
    print(button)

def kill_listener(listener):
    listener.stop()

def on_press(key):
    print(key)

def main():
    window.display_bdo()

    # keyboard.add_hotkey('e', input.shadow_stomp, suppress=True, trigger_on_release=True)
    # mouse.on_button(input.pve, buttons='x')

    with MouseListener(on_click=test) as listener:
        with KeyboardListener(on_press=on_press) as listener:
            listener.join()
    # with Listener(on_click=test) as listener:
    #     listener.join()
    #     keyboard.add_hotkey('f10', kill_listener, args=(listener))
    #     keyboard.add_hotkey('f9', input.test)
    #     keyboard.add_hotkey('z', input.shadow_stomp, suppress=True)

    # try:
    #     while True:
    #         pass
    # except KeyboardInterrupt:
    #     sys.exit(0)


if __name__== "__main__":
    main()