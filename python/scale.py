# Using the 'resolution' from the umap file, estimate what the maximum size of an instance of 'noise' might be.
# Then search each element of the array to see if it is the center of such a noise instance.
def  clean_noise(two_d_array, target_type, replacement_type, threshold, percent_positivity):
  updated_array = two_d_array.copy()
  imax = len(two_d_array)
  jmax = len(two_d_array[0])

  i = 0

  while i < imax:
    j = 0
    while j < jmax:
      if updated_array[i][j] == target_type and is_noise(updated_array, i, j, threshold, percent_positivity):
        updated_array[i][j] = replacement_type
      j += 1
    i += 1

  return updated_array



# determines if element might be noise be checking how many times element appears in subset of image
# i and j denote center of subset and element we are judging
# threshold is the number of 'layers' we should include around the center, 0 will only examine the center
# percent_positivity is the ratio stating how many positives we need to say if this element is not noise
def is_noise(two_d_array, i, j, threshold, percent_positivity):
  center_element = two_d_array[i][j]
  subset = get_subset(two_d_array, i, j, threshold)
  # find number of occurences of center element in hte subsetf
  positives = two_d_array.count(center_element)
  percent_positive = positives / len(subset)
  if (percent_positive >= percent_positivity):
    return False
  else: 
    return True


def get_subset(two_d_array, i, j, threshold):
  subset = []
  current_operand = 0
  while current_operand <= threshold:
    print(current_operand)
    for element in get_layer(i, j, current_operand):
      print(element)
      subset.append(two_d_array[element[0]][element[1]])
    current_operand += 1
  return subset

def get_layer(i, j, operand):
  layer = []
  # edge case: operand is 0
  if operand == 0: 
    if valid_coord([i,j]):
      return [[i,j]]
    else:
      return []
  # calculate the 'least' coordinate location of this layer, in a four setp process collect all neighbor coordinates
  least_coord = [i-operand, j-operand]
  icurrent = least_coord[0]
  jcurrent = least_coord[1]  
  
  # iterate over top of layer by iterating j upward
  while jcurrent < j + operand:
    print("first loop: ",icurrent, jcurrent)
    if valid_coord([icurrent, jcurrent]):
      layer.append([icurrent, jcurrent])
    jcurrent += 1
  
  # iterate 'downwards' over 'right' side of the layer
  while icurrent < i + operand:
    print("second loop: ",icurrent, jcurrent)
    if valid_coord([icurrent, jcurrent]):
      layer.append([icurrent, jcurrent])
    icurrent += 1
  
  # iterate 'leftwards' over 'bottom' side of the layer
  while jcurrent > j - operand:
    print("third loop: ",icurrent, jcurrent)
    if valid_coord([icurrent, jcurrent]):
      layer.append([icurrent, jcurrent])
    jcurrent -= 1
  
  # iterate 'upwards' over 'left' side of the layer
  while icurrent > least_coord[0]:
    print("fourth loop: ",icurrent, jcurrent)
    if valid_coord([icurrent, jcurrent]):
      layer.append([icurrent, jcurrent])
    icurrent -= 1
  return layer
  



def valid_coord(coord): 
  for element in coord:
    if not isinstance(element, int):
      return False
    if element < 0:
      return False
  return True


# x = get_layer(0,0,0)
# y = get_layer(0,0,1)
# z = get_layer(0,0,3)

# print(x)
# print(y)
# print(z)

# test_2d_array = [[1,2,3], [4,5,6,],[7,8,9]]

# print(get_subset(test_2d_array, 0, 0, 2))

# test 1: with our color matrix from assets, try replacing noise-y black elements with white elements
# keep both onhand and do a side by side comparison with pyplot
def get_color_matrix(mapdata):
    ground = 0
    wall = 1
    undefined = 1
    height = len(mapdata)
    width = len(mapdata[0])
    color_matrix = []
    for row in reversed(range(height)):
        temprow = []
        for col in range(width):
            obfuscatedInt = mapdata[row][col]
            for i in range(16):
                tmp = (obfuscatedInt & (0x03 << (i * 2))) >> (i * 2)
                if (tmp == 0):
                    temprow.append(wall)
                elif (tmp == 1):
                    temprow.append(ground)
                else:
                    temprow.append(undefined)
        color_matrix.append(temprow)
    return color_matrix

import matplotlib.pyplot as plt
import json
  
# Opening JSON file
f = open('/Users/administrator/Documents/GitHub/parse-.umap/assets/map.umap')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
# print(data.keys())
mapdata = data["mapdata"]
color_matrix = get_color_matrix(mapdata)
updated_color_matrix = clean_noise(color_matrix, 0, 2, 1, 0.5)

print("starting plot")
# updated_color_matrix = plt.imclose(color_matrix)
plt.figure(figsize=(8,8))
plt.subplot(121)

plt.imshow(color_matrix) #, cmap="Greys")
plt.axis('off')
plt.title('unprocessed')

plt.subplot(122)

plt.imshow(updated_color_matrix) #, cmap="Greys")
plt.axis('off')
plt.title('processed with clean_noise()')

plt.show()