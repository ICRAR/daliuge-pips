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
import pickle
import sys

from astropy import units as u
from astropy.coordinates import SkyCoord  # @UnresolvedImport
import numpy

from arl.util.testing_support import create_named_configuration


def dump(n, obj):
    with open(sys.argv[n], "wb") as fout:
        pickle.dump(obj, fout)

def dump_text(n, o):
    with open(sys.argv[n], "wt") as fout:
        fout.write(o)

def load(n):
    with open(sys.argv[n], "rb") as fin:
        return pickle.load(fin)

cellsize = 2e-5
params = {'wstep': 100.0, 'npixel': 512, 'cellsize': cellsize, 'niter': 1000, 'scales':[0,10,30],
              'threshold': 0.001, 'fracthresh': 0.01, 'weighting':'uniform'}

vlaa = create_named_configuration('VLAA')
vlaa.data['xyz'] = vlaa.data['xyz']
times = numpy.arange(-numpy.pi / 2.0, +numpy.pi / 2.0, 0.05)
frequency = numpy.array([1e8])
phasecentre = SkyCoord(0.0 * u.rad, u.rad * numpy.pi / 4, frame='icrs', equinox=2000.0)