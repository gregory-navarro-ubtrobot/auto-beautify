print("starting test_clean_noise.py")

from clean_noise import *
from color_matrix import *
import json
import datetime
import matplotlib.pyplot as plt
import os

# test the methods used to by top level method clean_noise
x = get_layer(0,0,1)
# y = get_layer(0,0,1)
# z = get_layer(0,0,3)

print(x)
# print(y)
# print(z)

# test_2d_array = [[1,2,3], [4,5,6,],[7,8,9]]

# print(get_subset(test_2d_array, 0, 0, 2))