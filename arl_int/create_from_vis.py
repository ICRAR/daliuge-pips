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
import logging

from arl.fourier_transforms.ftprocessor import create_image_from_visibility, \
invert_2d
from arl.image.operations import show_image
from .common import params, load, dump

def main():

    vt = load(1)

    #TODO move cellsize and npixel to Drop parameters
    model = create_image_from_visibility(vt, cellsize=0.001, npixel=256)
    dirty, sumwt = invert_2d(vt, model)
    psf, sumwt = invert_2d(vt, model, dopsf=True)
    fig = show_image(dirty)
    png = '%s_dirty_img.png' % sys.argv[4]
    fig.savefig(png)
    dump(2, psf)
    dump(3, dirty)

if __name__ == '__main__':
    main()
