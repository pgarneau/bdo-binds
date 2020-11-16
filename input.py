import pydirectinput
import time
import keyboard
import cooldown


current_bind = None

def execute(instructions):
    for i, instruction in enumerate(instructions):
        if i >= 1 and keyboard.is_pressed(current_bind):
            time.sleep(2)
            return
        
        instruction()

def wait_for(skill):
    while not cooldown.on_cooldown(skill):
        if keyboard.is_pressed(current_bind):
            break
        pass
        

def pve(bind):
    global current_bind
    current_bind = bind

    # cooldown.test_coords()
    instructions = [
        shadow_slash_greeting,
        fatal_blow,
        ankle_cutter,
        malice_stomp,
        shuriken_flight,
        evasive_malice_beheading,
        bladespin,
        fox_claw_moonlight,
        crescent_slash
    ]
    execute(instructions)


def fatal_blow():
    pydirectinput.mouseDown()
    pydirectinput.mouseDown(button='right')

    wait_for('fatal_blow')

    pydirectinput.mouseUp()
    pydirectinput.mouseUp(button='right')

def red_rain():
    pydirectinput.keyDown('s')
    pydirectinput.rightClick()
    pydirectinput.keyUp('s')

def dark_frenzy():
    pydirectinput.keyDown('s')
    pydirectinput.press('c')
    pydirectinput.keyUp('s')


def shadow_slash_greeting():
    pydirectinput.mouseDown(button='left')
    keyboard.send('d')
    time.sleep(0.08)
    keyboard.press('shift+w')
    time.sleep(0.25)
    keyboard.release('shift+w')


def malice_stomp():
    keyboard.press('q')

    wait_for('malice')

    keyboard.release('q')
    keyboard.press('s+e')
    time.sleep(0.3)
    keyboard.release('s+e')


def ankle_cutter():
    keyboard.press('shift')
    pydirectinput.mouseDown()

    wait_for('ankle_cutter')

    keyboard.release('shift')
    pydirectinput.mouseUp()
    pydirectinput.rightClick()


def shuriken_flight():
    keyboard.press('s+q')

    wait_for('shuriken_flight')

    keyboard.release('s+q')
    pydirectinput.mouseDown()
    time.sleep(0.5)
    pydirectinput.mouseUp()


def evasive_malice_beheading():
    keyboard.press('d+q')

    wait_for('evasive_malice')

    keyboard.release('d+q')
    pydirectinput.mouseDown(button='right')
    keyboard.press('shift+e')

    wait_for('beheading_the_dead')

    pydirectinput.mouseUp(button='right')
    keyboard.release('shift+e')

def bladespin():
    while not cooldown.on_cooldown('bladespin'):
        if keyboard.is_pressed(current_bind):
            break

        keyboard.send('1')
        time.sleep(0.15)

def fox_claw_moonlight():
    keyboard.press('shift')
    pydirectinput.mouseDown(button='right')

    wait_for('fox_claw')

    keyboard.release('shift')
    pydirectinput.mouseUp(button='right')
    pydirectinput.mouseDown()

    wait_for('moonlight')

    pydirectinput.mouseUp()


def crescent_slash():
    keyboard.press('s')
    pydirectinput.mouseDown()

    wait_for('crescent_slash')

    keyboard.release('s')
    pydirectinput.mouseUp()
    pydirectinput.mouseDown(button='right')
    time.sleep(0.4)
    pydirectinput.mouseUp(button='right')

