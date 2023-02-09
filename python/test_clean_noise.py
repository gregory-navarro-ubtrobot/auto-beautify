print("starting test_clean_noise.py")

from clean_noise import *
from color_matrix import *
import json
import datetime
import matplotlib.pyplot as plt

# test the methods used to by top level method clean_noise
# x = get_layer(0,0,0)
# y = get_layer(0,0,1)
# z = get_layer(0,0,3)

# print(x)
# print(y)
# print(z)

# test_2d_array = [[1,2,3], [4,5,6,],[7,8,9]]

# print(get_subset(test_2d_array, 0, 0, 2))


# TESTING 
# target_type will be WALL
# replacement_type will be GROUND
# threshold should be tested with values from 1 to 10
# percent_positivity should be tested from 0 to 1 in increments of 0.2
# all tests should record how different the results are from the unprocessed color matrix
# those should be recorded to test_results/test_results.txt
# additionally an image should be saved for each test under test_results/images/ with a number that corresponds to entry in test_results.txt

# obtain basic color_matrix
umapFile =  open('/home/administrator/Documents/research/Auto-Beautify/simple-webpage/assets/map.umap')
data = json.load(umapFile)
mapdata = data["mapdata"]
basic_color_matrix = get_color_matrix(mapdata)

# open file for writing logs
datetimestr = datetime.datetime.now() # .replace(" ", "-")
datetimestr = str(datetimestr).replace(" ", "_")
directory_name = 'test_results_{}'.format(datetimestr)
log_file = 'test_results.txt'
log_file_url = directory_name + "/" + log_file
test_out = open(log_file_url, 'r')

WALL = 0
GROUND = 1
# TODO: no definite value for UNDEFINED in this implementation
#       this can be corrected in color_matrix.py

TARGET_TYPE = WALL
REPLACEMENT_TYPE = GROUND

MAX_THRESHOLD_VALUE = 10
threshold_values = []
percent_positivity_values = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
color_matrix_outputs = [] # container for processed color_matrices

test_number = 1

for threshold in range(MAX_THRESHOLD_VALUE):
    threshold_values.append(threshold)
    for percent_positivity in percent_positivity_values:
        result_matrix = clean_color_matrix(basic_color_matrix, TARGET_TYPE, REPLACEMENT_TYPE, threshold, percent_positivity)
        color_matrix_outputs.append(result_matrix)
        # record details of test in log
        logEntry = "{} -- threshold: {} -- percent positivity: {} \n".format(test_number, threshold, percent_positivity) 
        test_out.write(logEntry)
        # TODO add method to count how many differences exist between the two arrays
        # plot figures, and save the figures to disk in /test_results_<datetime>/images/ 
        plt.figure(figsize=(8, 8))
        plt.subplot(121)
        plt.imshow(basic_color_matrix) 
        plt.axis('off')
        plt.title('unprocessed')
        plt.subplot(122)
        plt.imshow(result_matrix) 
        plt.axis('off')
        plt.title('threshold: {} -- percent positivity: {}'.format(threshold, percent_positivity))
        plt.savefig('{}/images/{}.png'.format(directory_name, test_number))


test_out.close()
print("ending test_clean_noise.py")