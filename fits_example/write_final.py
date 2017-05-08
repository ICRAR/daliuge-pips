'''
Created on 3May,2017

@author: rtobar
'''


import sys

import pyfits

from fits_example.common import load, load_fname


if __name__ == '__main__':

    images = {}
    out_fname = load(1)
    origin_header = load(2)
    im_fnames = sys.argv[3].split("__JOINME__")
    for fname in im_fnames:
        idx, image = load_fname(fname)
        images[idx] = image

    images = images.values()
    hdu = pyfits.PrimaryHDU(images)
    hdu.header = origin_header
    hdu.writeto(out_fname)