def get_color_matrix(mapdata):
    ground = "#fff"
    wall = "rgba(59, 59, 59, 0.5)"
    undefined = "#eee"
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