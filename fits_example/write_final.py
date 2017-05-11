'''
Created on 3May,2017

@author: rtobar, cwu
'''


import sys
import pyfits
import numpy as np

from fits_example.common import load, load_fname

if __name__ == '__main__':
    out_fname = sys.argv[1]
    origin_header = load(2)
    image_count, height, width = load(3)
    images = np.zeros((image_count, height, width))

    for i in range(image_count):
        # we restore the original identifier to insert the image plane
        j, image_plane = load(4 + i)
        images[j, :, :] = image_plane

    hdu = pyfits.PrimaryHDU(images)
    hdu.header = origin_header
    hdu.writeto(out_fname)
