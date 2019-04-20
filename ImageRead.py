from PIL import Image
from threading import Thread
import numpy as np
import pytesseract as pt
import pyautogui as pa
import matplotlib.pyplot as plt
import pyperclip
import time

class LineReader (Thread):
    def __init__(self):
        Thread.__init__(self)
        self._return = None
    def run(self):
        im = pa.screenshot(region = (430, 610, 1570, 70))
        imar = np.array(im)
        image_string = pt.image_to_string(imar)
        words = image_string.split()
        self._return = words
    def join(self):
        Thread.join(self)
        return self._return

lineReaders = []

for i in range(1000):
    t = LineReader()
    lineReaders.append(t)


time.sleep(4)
im1 = pa.screenshot(region = (430, 530, 1570, 70))
imar1 = np.array(im1)
im2 = pa.screenshot(region = (430, 610, 1570, 70))
imar2 = np.array(im2)

image_string2 = pt.image_to_string(imar2)
words2 = image_string2.split()

image_string1 = pt.image_to_string(imar1)
words1 = image_string1.split()

pa.moveTo(700, 370, 0.2)
start_time = time.time()
pa.click(700, 370)
for word in words1:
#    pyperclip.copy(word)
#    pa.hotkey('command', 'v')
#    pa.press('space')
    pa.typewrite(word + ' ')

i = 0

while (time.time() - start_time < 60):

    lineReaders[i].start()

    for word in words2:
#        pyperclip.copy(word)
#        pa.hotkey('command', 'v')
#        pa.press('space')
        pa.typewrite(word + ' ')

    words = lineReaders[i].join()

    words2 = words
    i += 1
