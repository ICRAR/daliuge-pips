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

from matplotlib import pyplot as plt
import numpy

from .common import load


def main():
    vis = load(1)
    if len(sys.argv) > 3:
        vis2 = load(2)
        fout = sys.argv[3]
    else:
        vis2 = None
        fout = sys.argv[2]

    uvdist = numpy.sqrt(vis.data['uvw'][:, 0] ** 2 + vis.data['uvw'][:, 1] ** 2)
    plt.clf()
    plt.plot(uvdist, numpy.abs(vis.data['vis']), '.')
    if vis2 is not None:
        plt.plot(uvdist, numpy.abs(vis.data['vis'] - vis2.data['vis']), '.', color='r')
    plt.xlabel('uvdist')
    plt.ylabel('Amp Visibility')
    plt.savefig('%s_amp_vis.png' % fout)

if __name__ == '__main__':
    main()
