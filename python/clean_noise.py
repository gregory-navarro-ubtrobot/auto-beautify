import copy

# Using the 'resolution' from the umap file, estimate what the maximum size of an instance of 'noise' might be.
# Then search each element of the array to see if it is the center of such a noise instance.
def  clean_color_matrix(two_d_array, target_type, replacement_type, threshold, percent_positivity):
  updated_array = copy.deepcopy(two_d_array)
  imax = len(two_d_array)
  jmax = len(two_d_array[0])

  i = 0
  mutations = 0 # TODO this is for testing, remove later
  while i < imax:
    j = 0
    while j < jmax:
      if updated_array[i][j] == target_type and is_noise(updated_array, i, j, threshold, percent_positivity):
        updated_array[i][j] = replacement_type
        mutations += 1  # TODO this is for testing, remove later
      j += 1
    i += 1
  print("threshold: {} -- percent positivity: {} -- mutations performed: {}".format(threshold, percent_positivity, mutations))  # TODO this is for testing, remove later
  return updated_array



# determines if element might be noise be checking how many times element appears in subset of image
# i and j denote center of subset and element we are judging
# threshold is the number of 'layers' we should include around the center, 0 will only examine the center
# percent_positivity is the ratio stating how many positives we need to say if this element is not noise
def is_noise(two_d_array, i, j, threshold, percent_positivity):
  center_element = two_d_array[i][j]
  subset = get_subset(two_d_array, i, j, threshold)
  # find number of occurences of center element in hte subsetf
  positives = subset.count(center_element)
  percent_positive = positives / len(subset)
  if (percent_positive >= percent_positivity):
    return False
  else: 
    return True


def get_subset(two_d_array, i, j, threshold):
  subset = []
  current_operand = 0
  while current_operand <= threshold:
    # print(current_operand)
    for element in get_layer(i, j, current_operand):
      # print(element)
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
    # print("first loop: ",icurrent, jcurrent)
    if valid_coord([icurrent, jcurrent]):
      layer.append([icurrent, jcurrent])
    jcurrent += 1
  
  # iterate 'downwards' over 'right' side of the layer
  while icurrent < i + operand:
    # print("second loop: ",icurrent, jcurrent)
    if valid_coord([icurrent, jcurrent]):
      layer.append([icurrent, jcurrent])
    icurrent += 1
  
  # iterate 'leftwards' over 'bottom' side of the layer
  while jcurrent > j - operand:
    # print("third loop: ",icurrent, jcurrent)
    if valid_coord([icurrent, jcurrent]):
      layer.append([icurrent, jcurrent])
    jcurrent -= 1
  
  # iterate 'upwards' over 'left' side of the layer
  while icurrent > least_coord[0]:
    # print("fourth loop: ",icurrent, jcurrent)
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


