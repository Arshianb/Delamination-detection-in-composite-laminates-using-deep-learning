# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-22.27.30 176069
# Run by arshi on Fri Aug 12 18:13:52 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=173.510986328125, 
    height=114.429679870605)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
openMdb(
    pathName='C:/Users/arshi/OneDrive/Desktop/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/Base vibration model/main-model.cae')
#: The model database "C:\Users\arshi\OneDrive\Desktop\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\main-model.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Delamination-Case-1'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Delamination-Case-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
