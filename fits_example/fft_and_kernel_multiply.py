'''
Created on 3May,2017

@author: rtobar
'''

import numpy as np
from numpy.fft import fft2


from fits_example.common import load, dump

if __name__ == '__main__':

    i, image = load(1)
    kernel = load(2)
    img  = np.nan_to_num(image)            # load image from HDF file
    img_ = fft2(img)            # 2D FFT
    whi = img_ * kernel       # multiply with kernel in freq.-space

    dump(3, (i,whi))