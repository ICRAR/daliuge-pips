#
#    ICRAR - International Centre for Radio Astronomy Research
#    (c) UWA - The University of Western Australia, 2016
#    Copyright by UWA (in the framework of the ICRAR)
#    All rights reserved
#
#    This library is free software; you can redistribute it and/or
#    modify it under the terms of the GNU Lesser General Public
#    License as published by the Free Software Foundation; either
#    version 2.1 of the License, or (at your option) any later version.
#
#    This library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with this library; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston,
#    MA 02111-1307  USA
#
import logging

import numpy

from arl.fourier_transforms.ftprocessor import weight_visibility, invert_2d

from .common import load, dump, params


logger = logging.getLogger(__name__)

def main():

    vis = load(1)
    dirty = load(2)
    psf = load(3)

    vis = weight_visibility(vis, dirty, params)

    psf = invert_2d(vis, psf, dopsf=True, params=params)
    psfmax = numpy.max(psf.data)
    psf.data=psf.data/psfmax
    #show_image(psf)
    logger.info("run_imaging: Max, min in PSF         = %.6f, %.6f" % (psf.data.max(), psf.data.min()))

    # Now use straightforward 2D transform to make dirty image and psf.
    dirty = invert_2d(vis, dirty, params=params)
    dirty.data=dirty.data/psfmax

    dump(4, vis)
    dump(5, dirty)
    dump(6, psf)

if __name__ == '__main__':
    main()