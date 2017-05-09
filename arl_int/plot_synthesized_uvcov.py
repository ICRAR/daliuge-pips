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

from astropy import constants as const
from matplotlib import pyplot as plt

from .common import frequency, load


def main():

    vt = load(1)
    plt.plot(vt.data['uvw'][:,0], vt.data['uvw'][:,1], '.', color='b')
    plt.plot(-vt.data['uvw'][:,0], -vt.data['uvw'][:,1], '.', color='b')
    # for f in frequency:
    #     x = f / const.c
    #     plt.plot(x * vis.data['uvw'][:, 0], x * vis.data['uvw'][:, 1], '.', color='b')
    #     plt.plot(-x * vis.data['uvw'][:, 0], -x * vis.data['uvw'][:, 1], '.', color='r')
    plt.savefig(sys.argv[2])

if __name__ == '__main__':
    main()
