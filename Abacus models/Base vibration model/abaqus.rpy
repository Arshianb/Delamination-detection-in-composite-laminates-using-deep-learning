# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-22.27.30 176069
# Run by arshi on Wed Aug  3 18:57:19 2022
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
mdb.saveAs(
    pathName='D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/Base vibration model/model num 1')
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
