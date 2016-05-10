# ***********************************************************************************
# Run Lesion-toads in a batch of data
#
#
# sergi.valverde@udg.edu
# NIC-VICOROB
# ***********************************************************************************

from lesion_toads import *
import os

# database dependent
IMAGE_FOLDER='/home/s/w/ALFI/images/VH'
dirs = os.listdir(IMAGE_FOLDER)

T1='t1_n3.nii.gz'
FLAIR='rFLAIR.denoised.n3.nii.gz'

for f in dirs:
    print('processing scan: '+f)
    current_t1 = os.path.join(IMAGE_FOLDER,f,T1)
    current_flair = os.path.join(IMAGE_FOLDER,f,FLAIR)
    lesion_toads(current_t1, current_flair)
