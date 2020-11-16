import input
import window
import keyboard

def call_input(input_func, bind):
    print("hotkey pressed")
    if window.bdo_active():
        function = getattr(input, input_func)
        function(bind)

    return

if __name__ == "__main__":
    window.display_bdo()
    print("displaying bdo")

    # keyboard.add_hotkey('f23', call_input, args=['shadow_stomp'])
    keyboard.add_hotkey('f24', call_input, args=['pve', 'f24'])

    keyboard.wait()