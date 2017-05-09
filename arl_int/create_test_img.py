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

import sys

from arl.util.testing_support import create_test_image
from arl.image.operations import show_image

from .common import frequency, cellsize, dump, load

def main():
    m31image = create_test_image(frequency=frequency, cellsize=cellsize)
    nchan, npol, ny, nx = m31image.data.shape
    vt = load(3)
    m31image.wcs.wcs.crval[0] = vt.phasecentre.ra.deg
    m31image.wcs.wcs.crval[1] = vt.phasecentre.dec.deg
    m31image.wcs.wcs.crpix[0] = float(nx // 2)
    m31image.wcs.wcs.crpix[1] = float(ny // 2)
    fig = show_image(m31image)
    fig.savefig('%s_created_img.png' % sys.argv[2])
    dump(1, m31image)

if __name__ == '__main__':
    main()
