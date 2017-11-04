#!/usr/bin/python
#coding:utf-8

from sense_hat import SenseHat
# import pygame.mixer
import subprocess
import time

WAIT = 3

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)

sense = SenseHat()
sense.set_rotation(180)
sense.clear()
time.sleep(0.5)

for x in range(0, 8):
   sense.set_pixel(x, 0, red)
   sense.set_pixel(x, 1, red)
for x in range(1, 7):
   sense.set_pixel(x, 2, red)
   sense.set_pixel(x, 3, red)
for x in range(2, 6):
   sense.set_pixel(x, 4, red)
   sense.set_pixel(x, 5, red)
for x in range(3, 5):
   sense.set_pixel(x, 6, red)
   sense.set_pixel(x, 7, red)

for y in range(8):
   time.sleep(WAIT)
   for x in range(0, 8):
      sense.set_pixel(x, y, black)
time.sleep(0.5)

for x in range(0, 8):
   sense.set_pixel(x, 0, green)
   sense.set_pixel(x, 1, green)
for x in range(1, 7):
   sense.set_pixel(x, 2, green)
   sense.set_pixel(x, 3, green)
for x in range(2, 6):
   sense.set_pixel(x, 4, green)
   sense.set_pixel(x, 5, green)
for x in range(3, 5):
   sense.set_pixel(x, 6, green)
   sense.set_pixel(x, 7, green)

subprocess.call("omxplayer signal.mp3", shell=True)

for i in range(5):
   for x in range(0, 8):
      sense.set_pixel(x, 0, green)
      sense.set_pixel(x, 1, green)
   for x in range(1, 7):
      sense.set_pixel(x, 2, green)
      sense.set_pixel(x, 3, green)
   for x in range(2, 6):
      sense.set_pixel(x, 4, green)
      sense.set_pixel(x, 5, green)
   for x in range(3, 5):
      sense.set_pixel(x, 6, green)
      sense.set_pixel(x, 7, green)
   time.sleep(0.3)
   for y in range(8):
      for x in range(0, 8):
         sense.set_pixel(x, y, black)
   time.sleep(0.3)

# vim:ts=3 sw=3 et:
