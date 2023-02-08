print("starting basic_test.py")

# test 1: with our color matrix from assets, try replacing noise-y black elements with white elements
# keep both onhand and do a side by side comparison with pyplot
from color_matrix import get_color_matrix
from clean_noise import clean_noise
import matplotlib.pyplot as plt
import json
  
# Opening JSON file
f = open('/Users/administrator/Documents/GitHub/parse-.umap/assets/map.umap')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
# # print(data.keys())
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

print("ending basic_test.py")