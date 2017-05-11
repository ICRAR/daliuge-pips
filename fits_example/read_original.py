
import sys

import pyfits

from fits_example.common import dump, dump_fname


if __name__ == '__main__':
    in_fname = sys.argv[1]
    left = int(sys.argv[2])
    right = int(sys.argv[3])
    origin_header = pyfits.open(in_fname)[0].header
    images = pyfits.getdata(in_fname)[left:right, :, :]
    image_count, height, width = images.shape

    image_count = right - left
    dump(4, origin_header)
    dump(5, images.shape)

    for i in range(image_count):
        # we persist the identifier for future Application Drops
        dump(6 + i, (i, images[i]))
