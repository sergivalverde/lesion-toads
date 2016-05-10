# ***********************************************************************************
# LESION TOADS SEGMENTATION (Using nipype batch pipelines)
# Simple interface for the automated tissue segmentation proposed by Shiee et al 2010
#
# http://www.sciencedirect.com/science/article/pii/S1053811909009823
#
# NOTE: The current implementation really lacks of input options so far :(
#
# sergi.valverde@udg.edu
# NIC-VICOROB
# ***********************************************************************************

from __future__ import print_function
import numpy as np
import os
from nipype.interfaces.mipav import developer
import  nibabel as nib


def lesion_toads(T1_image, FLAIR_image):
    ''' 
    LESION TOADS
    by default, using -inAtlas1 = 'With lesions'
                   -inOutput = 'cruise inputs'

    The output segmentation and lesion mask are stored in a new folder called
    "lesion-toads". After segmentation labels are transformed into CSF, GM and
    WM as follows:
    
    # BACKGROUND
    #0  way outside the brain
    #1  outside the brain

    # CSF
    #5  sulcal/cisternal CSF
    #6  ventricles

    # GM
    #14  cerebellar cortical gray matter
    #15  cerebral cortical gray matter
    #16  caudate
    #17  thalamus
    #18  putamen
    #22  brainstem
    
    # WM (lesions are added as WM)
    #24  cerebellar white matter
    #25  cerebral white matter
    #10  lesions
    
    '''
    
    # Atlas locations 
    atlas_lesions = "atlas/cruise-atlas-12obj-lesiontoads2012.txt"
    atlas_nolesions = "atlas/cruise-atlas-12obj-toads2012.txt"
    
    # output directory
    [image_folder, image_name] = os.path.split(T1_image)
    out_mask = image_name.split('.')[0]
    
    toads_directory = os.path.join(image_folder,'lesion-toads')
    if not os.path.exists(toads_directory):
        os.makedirs(toads_directory)


    # options
    lesion_toads = developer.MedicAlgorithmLesionToads()
    lesion_toads.inputs.inAtlas2 = atlas_lesions
    lesion_toads.inputs.inAtlas3 = atlas_nolesions
    lesion_toads.inputs.inAtlas4 = atlas_nolesions
    lesion_toads.inputs.inT1_MPRAGE = T1_image
    lesion_toads.inputs.inFLAIR = FLAIR_image
    lesion_toads.inputs.outHard = os.path.join(toads_directory, out_mask + '_alllabels.nii.gz')
    lesion_toads.inputs.outLesion = os.path.join(toads_directory, out_mask  + '_lesionseg.nii.gz')
    lesion_toads.run()

    # correct labels
    label_transf = {0:0, 1:0, 5:1, 6:1, 14:2, 15:2, 16:2, 17:2, 18:2, 22:2, 24:3, 25:3, 10:3}


    # apply label trasnformation to image
    im = nib.load(os.path.join(toads_directory, out_mask + '_alllabels.nii.gz'))
    toads_segmentation = im.get_data()

    labels = np.unique(toads_segmentation)
    for l in labels:
        toads_segmentation[toads_segmentation==l] = label_transf[l];
    
    # save the image back
    [imagepath, filename] = os.path.split(image_folder)
    im.get_data()[:] = toads_segmentation
    nib.save(im, os.path.join(toads_directory, out_mask + '_seg.nii.gz'))

    

        
def get_help():
    lesion_toads = developer.MedicAlgorithmLesionToads()
    print(lesion_toads.help())
    
    
    


    
