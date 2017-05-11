#!/usr/bin/env python

"""
chen.wu@icrar.org

How to run:

   mpirun -np <NUM> ./pseudo-whitening <INPUT-CUBE.fits> <OUTPUT-CUBE.fits>

"""

from __future__ import division

import sys
import pyfits
import numpy as np
from numpy.fft import fft2, ifft2

#=============================================================================
# Main
in_fname = sys.argv[-2]
out_fname = sys.argv[-1]

#in_fname = 'L1448_13CO.fits.gz'
left = 145
right = 245
rem = (right - left) % comm.size
if (rem != 0):
    right += comm.size - rem

images = pyfits.getdata(in_fname)[left:right, :, :] #h5in.root.images
image_count, height, width = images.shape
image_count = min(image_count, 200)

# Prepare convolution kernel in frequency space
kernel_ = np.ones((height, width))

# rank 0 needs buffer space to gather data
if comm.rank == 0:
    gbuf = np.empty( (comm.size, height, width) )
    origin_header = pyfits.open(in_fname)[0].header
    new_images = np.zeros((image_count, height, width))
else:
    gbuf = None

for i_base in range(0, image_count, comm.size):
    i = i_base + comm.rank
    #
    if i < image_count:
        img  = np.nan_to_num(images[i])            # load image from FITS file
        img_ = fft2(img)            # 2D FFT
        whi_ = img_ * kernel_       # multiply with kernel in freq.-space
        #whi_  = img_
        whi  = np.abs(ifft2(whi_))#.astype(np.float)  # inverse FFT back into image space

    # rank 0 gathers transformed images
    comm.Gather(
        whi,   # send buffer
        gbuf,  # receive buffer
        root=0               # rank 0 is root the root-porcess
    )

    # rank 0 has to write into the FITS file
    if comm.rank == 0:
        # Sequentially append each of the images
        for r in range(comm.size):
            new_images[i + r, :, :] = gbuf[r]

if comm.rank == 0:
    hdu = pyfits.PrimaryHDU(new_images)
    hdu.header = origin_header
    hdu.writeto(out_fname)

comm.Barrier()
