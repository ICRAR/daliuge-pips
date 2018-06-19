
# coding: utf-8

# # Imaging and deconvolution demonstration

# This script makes a fake data set and then deconvolves it. Finally the full and residual visibility are plotted.

# In[26]:


#get_ipython().run_line_magic('matplotlib', 'inline')

import os
import sys

sys.path.append(os.path.join('..', '..'))

from data_models.parameters import arl_path
results_dir = arl_path('test_results')

from common import load, dump, params

#from matplotlib import pylab

##pylab.rcParams['figure.figsize'] = (8.0, 8.0)
#pylab.rcParams['image.cmap'] = 'rainbow'

import numpy

from astropy.coordinates import SkyCoord
from astropy import units as u
from astropy.wcs.utils import pixel_to_skycoord

#from matplotlib import pyplot as plt

from libs.image.iterators import image_raster_iter

from processing_components.visibility.base import create_visibility
from processing_components.skycomponent.operations import create_skycomponent
from processing_components.image.operations import show_image, export_image_to_fits
from processing_components.image.deconvolution import deconvolve_cube, restore_cube
from processing_components.visibility.iterators import vis_timeslice_iter
from processing_components.util.testing_support import create_named_configuration, create_test_image
from processing_components.imaging.base import create_image_from_visibility
from processing_components.imaging.imaging_functions import invert_function, predict_function

from data_models.polarisation import PolarisationFrame

import logging

log = logging.getLogger()
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))

def main():
	lowcore = create_named_configuration('LOWBD2', rmax=400.0)
        # We create the visibility. 
	# This just makes the uvw, time, antenna1, antenna2, weight columns in a table

        dlg_string=os.environ['DLG_UID']
        dlg_string=dlg_string[(dlg_string.rindex('_')+1):len(dlg_string)]
        dlg_uid=dlg_string.split('/')
	Freq_Iteration= int(dlg_uid[1])  # derived from ID
	#Facet_Iteration=int(dlg_uid[2])  # derived from ID
	phasecentre_array=[[+15,-45],[+15.2,-45],[+15,-44],[+14.8,-45],[+15,-46]]

        t_range=0
        t_step=1.0
        # once a second between the time ranges in HA
	times = numpy.arange(-t_range,+t_range,tstep/3600.0) * (numpy.pi / 12.0)
	frequency = numpy.array([1e8+Freq_Iteration*1e6])
	channel_bandwidth = numpy.array([1e6])
	phasecentre = SkyCoord(ra=phasecentre_array[0][0] * u.deg,
                       dec=phasecentre_array[0][1] * u.deg, frame='icrs', equinox='J2000')
	vt = create_visibility(lowcore, times, frequency, channel_bandwidth=channel_bandwidth,
                       weight=1.0, phasecentre=phasecentre, polarisation_frame=PolarisationFrame('stokesI'))

	dump(1,vt)

if __name__ == '__main__':
	main()
