import pyscreenshot as ImageGrab
import cv2
import numpy as np
import d3dshot

cooldown_coordinates = [
    (588, 468, 632, 511),
    (638, 468, 682, 511),
    (588, 518, 632, 561),
    (638, 518, 682, 561),
    (588, 568, 632, 611),
    (638, 568, 682, 611),
    (588, 618, 632, 661),
    (638, 618, 682, 661),
    (588, 668, 632, 711),
    (638, 668, 682, 711),
]

quickslot_coordinates = [
    (739, 1033, 783, 1076),
    (789, 1033, 833, 1076),
    (839, 1033, 883, 1076),
    (889, 1033, 933, 1076),
    (939, 1033, 983, 1076),
    (989, 1033, 1033, 1076),
    (1039, 1033, 1083, 1076),
    (1089, 1033, 1133, 1076),
    (1139, 1033, 1183, 1076),
]

abilities = {
    'fatal_blow': {
        'file': 'fatal_blow.png',
        'coords': cooldown_coordinates[7] 
    },
    'ankle_cutter': {
        'file': 'ankle_cutter.png',
        'coords': cooldown_coordinates[2]
    },
    'malice': {
        'file': 'malice.png',
        'coords': cooldown_coordinates[0]
    },
    'evasive_malice': {
        'file': 'evasive_malice.png',
        'coords': cooldown_coordinates[1]
    },
    'shuriken_flight': {
        'file': 'shuriken_flight.png',
        'coords': quickslot_coordinates[2]
    },
    'beheading_the_dead': {
        'file': 'beheading.png',
        'coords': quickslot_coordinates[6]
    },
    'bladespin': {
        'file': 'bladespin.png',
        'coords': quickslot_coordinates[0]
    },
    'moonlight': {
        'file': 'moonlight.png',
        'coords': quickslot_coordinates[7]
    },
    'fox_claw': {
        'file': 'fox_claw.png',
        'coords': quickslot_coordinates[8]
    },
    'crescent_slash': {
        'file': 'crescent_slash.png',
        'coords': cooldown_coordinates[3]
    }
}

def on_cooldown(ability) -> bool:
    template = cv2.imread(f"images/{abilities[ability]['file']}", 0)
    image = ImageGrab.grab(bbox=abilities[ability]['coords'], childprocess=False)
    image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(image, template, 1)
    score, _, _, _ = cv2.minMaxLoc(res)
    # print(score)

    if score < 0.6:
        return True

def test_coords():
    # If you want fullscreen, use d3dshot
    # image = d3dshot.create()
    # image.screenshot_to_disk(file_name='fullscreen.png')

    for i, box in enumerate(cooldown_coordinates):
        image = ImageGrab.grab(bbox=box, childprocess=False)
        image.save(f'{i}.png')

    for i, box in enumerate(quickslot_coordinates):
        image = ImageGrab.grab(bbox=box, childprocess=False)
        image.save(f'{i}_quickslot.png')



# 1, 3, 5 are good