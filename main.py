"""
Trans Rights are Human Rights

This code gets flashed onto the Raspberry pi Pico, and is responsible for showing images on an
attached led matrix panel (Currently this is a 16x7 Unicorn HAT)
"""
# SYSTEM IMPORTS
import picounicorn
import time

# STANDARD LIBRARY IMPORTS

# LOCAL APPLICATION IMPORTS


picounicorn.init()

w = picounicorn.get_width()
h = picounicorn.get_height()

FRAME_RATE = 12
FRAME_RATE_IN_MS: float = 1.0/FRAME_RATE
GAMMA_INV = 2.2


# IMAGES AS ARRAYS [ w[ h( rgb ) ] ]
eye_static = [[(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255)]]
eye_backward = [[(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255)]]
eye_forward = [[(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255)]]
eye_blink = [[(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255)]]
eye_angry = [[(0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (229, 25, 102, 255), (0, 0, 0, 255), (229, 25, 102, 255), (229, 25, 102, 255), (0, 0, 0, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255)]]

mouth_closed = [[(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255)]]
mouth_open = [[(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (234, 67, 48, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (234, 67, 48, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255)]]
mouth_open_wide = [[(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (234, 67, 48, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (234, 67, 48, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (234, 67, 48, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (234, 67, 48, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (234, 67, 48, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (234, 67, 48, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (234, 67, 48, 255), (0, 0, 0, 255)], [(0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255)]]


# ANIM TIMINGS, TIMES IN FRAMES PER SECOND, RELATIVE TO FRAME_RATE
# CURRENTLY, A TIME OF 12 MEANS 1 SECOND
anim_timings = [
    [eye_static, 12],
    [eye_forward, 12],
    [eye_static, 12],
    [eye_backward, 12],
    [eye_blink, 6],
    [eye_static, 24],
    [eye_angry, 24],
]


def show_array(frame):
    for x in range(w):
        for y in range(h):
            r, g, b, _ = frame[y][x]
            picounicorn.set_pixel(x, y, r, g, b)


def run_animation(anim_set: list):
    for frame, wait_time in anim_set:
        show_array(frame=frame)
        time.sleep(wait_time*FRAME_RATE_IN_MS)


def show_image(shape=""):
    if shape == "closed":
        show_array(frame=mouth_closed)
    elif shape == "open":
        show_array(frame=mouth_open)
    elif shape == "open_wide":
        show_array(frame=mouth_open_wide)
    elif shape == "eye_forward":
        show_array(frame=eye_forward)
    elif shape == "eye_static":
        show_array(frame=eye_static)
    elif shape == "eye_backward":
        show_array(frame=eye_backward)
    elif shape == "eye_blink":
        show_array(frame=eye_blink)
