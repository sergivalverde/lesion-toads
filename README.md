# Lesion-Toads 

[Nypipe](http://www.mit.edu/~satra/nipype-nightly/index.html) interface for the Lesion-toads approach (Topology-preserving approach to the segmentation of brain images with multiple sclerosis lesions) proposed by [Shiee et al. 2010](http://www.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pubmed&retmode=ref&cmd=prlinks&id=19766196).

## Install 

- This interface is based on [Nypipe](http://www.mit.edu/~satra/nipype-nightly/index.html). Follow the instructions of the authors [webpage](http://www.mit.edu/~satra/nipype-nightly/users/install.html).

- Lesion-toads has to be installed following the provided [manual](http://www.iacl.ece.jhu.edu/~nshiee/research/LesionTOADS_manual.pdf), which is run from the [Mipav](http://mipav.cit.nih.gov/) environment. 

- Then, be sure that MIPAV and the corresponding libraries are in the path. Tipically, MIPAV is installed in the home folder.  

```
JAVALIB=/home/ThisUser/mipav/jre/Contents/Home/lib/ext/
# location of the MIPAV installation to use  
MIPAV=/home/ThisUser/mipav
# location of the plugin installation to use   
# please replace 'ThisUser' by your user name
PLUGINS=/home/ThisUser/mipav/plugins
```


## Running the code

So far, the implementation is simple. Just run the method using the provided function. Only the T1 and FLAIR images are available as options. The rest of parameters are run with default values.

```python
from lesion_toads import *
import os

# database dependent
IMAGE_FOLDER='/path/to/your/images'
dirs = os.listdir(IMAGE_FOLDER)

T1='t1name'
FLAIR='flairname'

for f in dirs:
    print('processing scan: '+f)
    current_t1 = os.path.join(IMAGE_FOLDER,f,T1)
    current_flair = os.path.join(IMAGE_FOLDER,f,FLAIR)
    lesion_toads(current_t1, current_flair)
``` 

New parameters can be tuned. Just run the `get_help()` function to obtain the number of possible parameter to tune.

```
Wraps command **java edu.jhu.ece.iacl.jist.cli.run edu.jhu.ece.iacl.plugins.classification.MedicAlgorithmLesionToads **

title: Lesion TOADS

category: Developer Tools

description: Algorithm for simulataneous brain structures and MS lesion segmentation of MS Brains. The brain segmentation is topologically consistent and the algorithm can use multiple MR sequences as input data.
N. Shiee, P.-L. Bazin, A.Z. Ozturk, P.A. Calabresi, D.S. Reich, D.L. Pham, "A Topology-Preserving Approach to the Segmentation of Brain Images with Multiple Sclerosis", NeuroImage, vol. 49, no. 2, pp. 1524-1535, 2010.

version: 1.9.R

contributor: Navid Shiee (navid.shiee@nih.gov) http://iacl.ece.jhu.edu/~nshiee/

Inputs::

	[Mandatory]

	[Optional]
	args: (a string)
		Additional parameters to the command
		flag: %s
	environ: (a dictionary with keys which are a value of type 'str' and
		 with values which are a value of type 'str', nipype default value:
		 {})
		Environment variables
	ignore_exception: (a boolean, nipype default value: False)
		Print an error message instead of throwing an exception in case the
		interface fails to run
	inAtlas: ('With Lesion' or 'No Lesion')
		Atlas to Use
		flag: --inAtlas %s
	inAtlas2: (an existing file name)
		Atlas File - With Lesions
		flag: --inAtlas2 %s
	inAtlas3: (an existing file name)
		Atlas File - No Lesion - T1 and FLAIR
		flag: --inAtlas3 %s
	inAtlas4: (an existing file name)
		Atlas File - No Lesion - T1 Only
		flag: --inAtlas4 %s
	inAtlas5: (a float)
		Controls the effect of the statistical atlas on the segmentation
		flag: --inAtlas5 %f
	inAtlas6: ('rigid' or 'multi_fully_affine')
		Atlas alignment
		flag: --inAtlas6 %s
	inConnectivity: ('(26,6)' or '(6,26)' or '(6,18)' or '(18,6)')
		Connectivity (foreground,background)
		flag: --inConnectivity %s
	inCorrect: ('true' or 'false')
		Correct MR field inhomogeneity.
		flag: --inCorrect %s
	inFLAIR: (an existing file name)
		FLAIR Image
		flag: --inFLAIR %s
	inInclude: ('true' or 'false')
		Include lesion in WM class in hard classification
		flag: --inInclude %s
	inMaximum: (an integer (int or long))
		Maximum distance from the interventricular WM boundary to downweight
		the lesion membership to avoid false postives
		flag: --inMaximum %d
	inMaximum2: (an integer (int or long))
		Maximum Ventircle Distance
		flag: --inMaximum2 %d
	inMaximum3: (an integer (int or long))
		Maximum InterVentricular Distance
		flag: --inMaximum3 %d
	inMaximum4: (a float)
		Maximum amount of relative change in the energy function considered
		as the convergence criteria
		flag: --inMaximum4 %f
	inMaximum5: (an integer (int or long))
		Maximum iterations
		flag: --inMaximum5 %d
	inOutput: ('hard segmentation' or 'hard segmentation+memberships' or
		 'cruise inputs' or 'dura removal inputs')
		Output images
		flag: --inOutput %s
	inOutput2: ('true' or 'false')
		Output the hard classification using maximum membership (not
		neceesarily topologically correct)
		flag: --inOutput2 %s
	inOutput3: ('true' or 'false')
		Output the estimated inhomogeneity field
		flag: --inOutput3 %s
	inSmooting: (a float)
		Controls the effect of neighberhood voxels on the membership
		flag: --inSmooting %f
	inT1_MPRAGE: (an existing file name)
		T1_MPRAGE Image
		flag: --inT1_MPRAGE %s
	inT1_SPGR: (an existing file name)
		T1_SPGR Image
		flag: --inT1_SPGR %s
	null: (a string)
		Execution Time
		flag: --null %s
	outCortical: (a boolean or a file name)
		Cortical GM Membership
		flag: --outCortical %s
	outFilled: (a boolean or a file name)
		Filled WM Membership
		flag: --outFilled %s
	outHard: (a boolean or a file name)
		Hard segmentation
		flag: --outHard %s
	outHard2: (a boolean or a file name)
		Hard segmentationfrom memberships
		flag: --outHard2 %s
	outInhomogeneity: (a boolean or a file name)
		Inhomogeneity Field
		flag: --outInhomogeneity %s
	outLesion: (a boolean or a file name)
		Lesion Segmentation
		flag: --outLesion %s
	outMembership: (a boolean or a file name)
		Membership Functions
		flag: --outMembership %s
	outSulcal: (a boolean or a file name)
		Sulcal CSF Membership
		flag: --outSulcal %s
	outWM: (a boolean or a file name)
		WM Mask
		flag: --outWM %s
	terminal_output: ('stream' or 'allatonce' or 'file' or 'none')
		Control terminal output: `stream` - displays to terminal immediately
		(default), `allatonce` - waits till command is finished to display
		output, `file` - writes output to file, `none` - output is ignored
	xDefaultMem: (an integer (int or long))
		Set default maximum heap size
		flag: -xDefaultMem %d
	xMaxProcess: (an integer (int or long), nipype default value: 1)
		Set default maximum number of processes.
		flag: -xMaxProcess %d
	xPrefExt: ('nrrd')
		Output File Type
		flag: --xPrefExt %s

Outputs::

	outCortical: (an existing file name)
		Cortical GM Membership
	outFilled: (an existing file name)
		Filled WM Membership
	outHard: (an existing file name)
		Hard segmentation
	outHard2: (an existing file name)
		Hard segmentationfrom memberships
	outInhomogeneity: (an existing file name)
		Inhomogeneity Field
	outLesion: (an existing file name)
		Lesion Segmentation
	outMembership: (an existing file name)
		Membership Functions
	outSulcal: (an existing file name)
		Sulcal CSF Membership
	outWM: (an existing file name)
		WM Mask

```

