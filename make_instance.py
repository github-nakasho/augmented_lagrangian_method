#!/usr/bin/env python3

import numpy as np


def make_instance():
    num_city = 20
    x, y = np.random.uniform(0, 1, (2, num_city))
    xx, xx_t = np.meshgrid(x, x)
    yy, yy_t = np.meshgrid(y, y)
    distance = np.sqrt((xx-xx_t)**2+(yy-yy_t)**2)
    return num_city, distance
