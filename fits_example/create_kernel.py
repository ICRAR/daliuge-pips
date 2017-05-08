'''
Created on 3May,2017

@author: rtobar
'''

import numpy as np

from fits_example.common import dump, load

if __name__ == '__main__':
    width, height = load(1)
    kernel = np.ones((height, width))
    dump(2, kernel)