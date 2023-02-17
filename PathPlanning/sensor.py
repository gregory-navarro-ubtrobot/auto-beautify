import numpy as np

class LaserSensor:

    def __init__(self, Range, map, uncertainty):
        self.Range = Range
        self.speed = 4 # rounds per second
        self.sigma = np.array([uncertainty[0], uncertainty[1]])
        
