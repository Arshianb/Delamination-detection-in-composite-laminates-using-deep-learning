# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-22.27.30 176069
# Run by arshi on Fri Jul 29 12:57:40 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=217.581253051758, 
    height=127.565101623535)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
openMdb(
    pathName='D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/composite modal analysis.cae')
#: The model database "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\modal analysis\composite modal analysis.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
