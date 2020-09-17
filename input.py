import pydirectinput
import time
import keyboard



def pve():
    # Red rain + Dark Frenzy
    red_rain()
    time.sleep(1.25)
    dark_frenzy()
    time.sleep(2.3)

    # Shadow Slash
    shadow_slash()

    # Ghost Greeting
    ghost_greeting()

    # Fatal Blow
    fatal_blow()

    # Ankle Cutter
    ankle_cutter()
    time.sleep(0.6)

    # Malice
    malice()

    # Shadow Stomp
    shadow_stomp()

    # Shuriken Flight
    shuriken_flight()
    time.sleep(0.2)

    evasive_malice_alert_stance()

    beheading_the_dead()
    time.sleep(0.9)

    bladespin('1')
    time.sleep(0.15)

    fox_claw_moonlight()
    time.sleep(0.1)

    crescent_slash()


def test():
    keyboard.send('s+e')

def test2():
    keyboard.send(31)

def dash(direction: str):
    pydirectinput.keyDown('shift')
    pydirectinput.keyDown(direction)
    pydirectinput.keyUp('shift')
    pydirectinput.keyUp(direction)

def fatal_blow():
    pydirectinput.mouseDown(button='left')
    pydirectinput.mouseDown(button='right')
    time.sleep(0.3)
    pydirectinput.mouseUp(button='left')
    pydirectinput.mouseUp(button='right')

def red_rain():
    pydirectinput.keyDown('s')
    pydirectinput.rightClick()
    pydirectinput.keyUp('s')

def dark_frenzy():
    pydirectinput.keyDown('s')
    pydirectinput.press('c')
    pydirectinput.keyUp('s')

def shadow_slash():
    pydirectinput.keyDown('d')
    pydirectinput.leftClick()
    pydirectinput.keyUp('d')

def ghost_greeting():
    pydirectinput.keyDown('shift')
    pydirectinput.keyDown('w')
    pydirectinput.leftClick()
    pydirectinput.keyUp('shift')
    pydirectinput.keyUp('w')

def ankle_cutter():
    pydirectinput.keyDown('shift')
    pydirectinput.leftClick()
    pydirectinput.keyUp('shift')
    pydirectinput.mouseDown(button='right')
    time.sleep(0.1)
    pydirectinput.mouseUp(button='right')

def malice():
    pydirectinput.keyDown('q')
    pydirectinput.keyUp('q')

def shadow_stomp():
    pydirectinput.keyDown('s')
    pydirectinput.keyDown('e')
    pydirectinput.keyUp('s')
    pydirectinput.keyUp('e')

def shuriken_flight():
    pydirectinput.keyDown('s')
    pydirectinput.keyDown('q')
    pydirectinput.keyUp('s')
    pydirectinput.keyUp('q')
    time.sleep(0.25)
    pydirectinput.rightClick()

def evasive_malice_alert_stance():
    pydirectinput.keyDown('w')
    pydirectinput.keyDown('q')
    pydirectinput.keyUp('w')
    pydirectinput.keyUp('q')
    pydirectinput.mouseDown(button='right')
    time.sleep(0.1)
    pydirectinput.mouseUp(button='right')

def beheading_the_dead():
    pydirectinput.keyDown('shift')
    pydirectinput.keyDown('e')
    pydirectinput.keyUp('shift')
    pydirectinput.keyUp('e')

def bladespin(quickslot: str):
    pydirectinput.keyDown(quickslot)
    pydirectinput.keyUp(quickslot)
    pydirectinput.keyDown('space')
    time.sleep(0.2)
    pydirectinput.keyUp('space')

def fox_claw_moonlight():
    pydirectinput.keyDown('shift')
    pydirectinput.rightClick()
    pydirectinput.keyUp('shift')
    pydirectinput.mouseDown(button='left')
    time.sleep(0.8)
    pydirectinput.mouseUp(button='left')

def crescent_slash():
    pydirectinput.keyDown('s')
    pydirectinput.leftClick()
    pydirectinput.keyUp('s')
    pydirectinput.mouseDown(button='right')
    time.sleep(0.4)
    pydirectinput.mouseUp(button='right')