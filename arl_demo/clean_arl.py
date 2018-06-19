
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
        dlg_string=os.environ['DLG_UID']
        dlg_string=dlg_string[(dlg_string.rindex('_')+1):len(dlg_string)]
        dlg_uid=dlg_string.split('/')
	Freq_Iteration= dlg_uid[1]  # derived from ID
	Facet_Iteration=dlg_uid[2]  # derived from ID
	vt = load(1)
	phasecentre_array=[[+15,-45],[+15.2,-45],[+15,-44],[+14.8,-45],[+15,-46]]

	phasecentre = SkyCoord(ra=phasecentre_array[Facet_Iteration][0] * u.deg,
                       dec=phasecentre_array[Facet_Iteration][1] * u.deg, frame='icrs', equinox='J2000')

	model = create_image_from_visibility(vt, phasecentre=phasecentre, cellsize=0.001, npixel=256)
	dirty, sumwt = invert_function(vt, model)
	psf, sumwt = invert_function(vt, model, dopsf=True)

	#show_image(dirty)
	print("Max, min in dirty image = %.6f, %.6f, sumwt = %f" % (dirty.data.max(), dirty.data.min(), sumwt))

	print("Max, min in PSF         = %.6f, %.6f, sumwt = %f" % (psf.data.max(), psf.data.min(), sumwt))

	export_image_to_fits(dirty, '%s/imaging_dirty_%02d_%02d.fits'%(results_dir,Freq_Iteration,Facet_Iteration))
	export_image_to_fits(psf, '%s/imaging_psf_%02d_%02d.fits'%(results_dir,Freq_Iteration,Facet_Iteration))

	# Deconvolve using clean

	comp, residual = deconvolve_cube(dirty, psf, niter=1000, threshold=0.001, fracthresh=0.01, window_shape='quarter',
                                 gain=0.7, scales=[0, 3, 10, 30])

	restored = restore_cube(comp, psf, residual)

	export_image_to_fits(restored, '%s/imaging_clean%02d_%02d.fits'%(results_dir,Freq_Iteration,Facet_Iteration))
        dump(2,restored)


if __name__ == '__main__':
	main()
