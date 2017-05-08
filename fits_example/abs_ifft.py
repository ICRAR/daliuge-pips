'''
Created on 3May,2017

@author: rtobar
'''

import numpy as np
from numpy.fft import ifft2


from fits_example.common import load, dump

if __name__ == '__main__':
    i, whi = load(1)
    whi = np.abs(ifft2(whi))
    dump(2, (i, whi))