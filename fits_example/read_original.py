
import sys

import pyfits

from fits_example.common import dump, dump_fname


if __name__ == '__main__':

    in_fname = sys.argv[1]
    origin_header = pyfits.open(in_fname)[0].header
    images = pyfits.getdata(in_fname)[int(sys.argv[2]):int(sys.argv[3]), :, :] #h5in.root.images
    image_count, height, width = images.shape

    dump(4, origin_header)
    dump(5, (width, height))

    image_fnames = sys.argv[6].split("__JOINME__")
    for i, (fname, im) in enumerate(zip(image_fnames, images)):
        print("%d, %s" % (i, fname))
        dump_fname(fname, (i, im))