print("starting test_clean_noise.py")

from clean_noise import *
from color_matrix import *
import json
import datetime
import matplotlib.pyplot as plt
import os

# TESTING 
# target_type will be WALL
# replacement_type will be GROUND
# threshold should be tested with values from 1 to 10
# percent_positivity should be tested from 0 to 1 in increments of 0.2
# all tests should record how different the results are from the unprocessed color matrix
# those should be recorded to test_results/test_results.txt
# additionally an image should be saved for each test under test_results/images/ with a number that corresponds to entry in test_results.txt

# obtain basic color_matrix
umapFile =  open('/Users/administrator/Documents/GitHub/Auto-Beautify/simple-webpage/assets/map.umap')
data = json.load(umapFile)
mapdata = data["mapdata"]
basic_color_matrix = get_color_matrix(mapdata)

WALL = 0
GROUND = 1
# TODO: no definite value for UNDEFINED in this implementation
#       this can be corrected in color_matrix.py
TARGET_TYPE = WALL
REPLACEMENT_TYPE = GROUND

THRESHOLD = 1
threshold_values = []
percent_positivity_values = [0.2, 0.4, 0.5, 0.55, 0.6]
color_matrix_outputs = [] # container for processed color_matrices

test_number = 1


for percent_positivity in percent_positivity_values:
    result_matrix = clean_color_matrix(basic_color_matrix, TARGET_TYPE, REPLACEMENT_TYPE, THRESHOLD, percent_positivity)
    color_matrix_outputs.append(result_matrix)


# Serializing json
json_object = json.dumps(color_matrix_outputs)
 
# Writing to sample.json
with open("color-matrices.json", "w") as outfile:
    outfile.write(json_object)

print("ending test_clean_noise.py")