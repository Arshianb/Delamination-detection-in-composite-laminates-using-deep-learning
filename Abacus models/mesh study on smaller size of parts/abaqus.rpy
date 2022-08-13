# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-22.27.30 176069
# Run by arshi on Sat Aug 13 01:19:44 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=87.1332321166992, 
    height=102.304679870605)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
openMdb(
    pathName='C:/Users/arshi/OneDrive/Desktop/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/mesh study on smaller size of parts/main-model.cae')
#: The model database "C:\Users\arshi\OneDrive\Desktop\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\mesh study on smaller size of parts\main-model.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['mesh-Size-1'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
openMdb(
    pathName='C:/Users/arshi/OneDrive/Desktop/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/Base Vibration for smaller parts/main-model.cae')
#: The model database "C:\Users\arshi\OneDrive\Desktop\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base Vibration for smaller parts\main-model.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Delamination-Case-1'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Delamination-Case-2'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Delamination-Case-2'].parts['Beam1']
s = p.features['Shell planar-1'].sketch
mdb.models['Delamination-Case-2'].ConstrainedSketch(name='__edit__', 
    objectToCopy=s)
s1 = mdb.models['Delamination-Case-2'].sketches['__edit__']
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s1, 
    upToFeature=p.features['Shell planar-1'], filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.753166, 
    farPlane=0.9114, width=0.47829, height=0.217938, cameraPosition=(0.0779374, 
    0.156265, 0.832283), cameraTarget=(0.0779374, 0.156265, 0))
s1.unsetPrimaryObject()
del mdb.models['Delamination-Case-2'].sketches['__edit__']
