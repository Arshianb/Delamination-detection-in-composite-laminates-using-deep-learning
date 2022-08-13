# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-22.27.30 176069
# Run by arshi on Sat Aug 13 19:09:52 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=87.1332321166992, 
    height=95.7369766235352)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
openMdb(
    pathName='C:/Users/arshi/OneDrive/Desktop/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/Base Vibration for smaller parts/main-model.cae')
#: The model database "C:\Users\arshi\OneDrive\Desktop\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base Vibration for smaller parts\main-model.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Delamination-Case-1'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Delamination-Case-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
p1 = mdb.models['Delamination-Case-2'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
del mdb.models['Delamination-Case-2']
del mdb.models['Delamination-Case-3']
del mdb.models['Delamination-Case-4']
del mdb.models['Delamination-Case-5']
del mdb.models['Delamination-Case-6']
del mdb.models['Delamination-Case-7']
del mdb.models['Delamination-Case-8']
del mdb.models['Delamination-Case-9']
del mdb.models['Delamination-Case-10']
del mdb.models['Delamination-Case-11']
del mdb.models['Delamination-Case-12']
del mdb.models['Delamination-Case-13']
del mdb.models['Delamination-Case-14']
del mdb.models['Delamination-Case-15']
del mdb.models['Delamination-Case-16']
del mdb.models['Delamination-Case-17']
del mdb.models['Delamination-Case-18']
del mdb.models['Delamination-Case-19']
del mdb.models['Delamination-Case-20']
del mdb.models['Delamination-Case-21']
del mdb.models['Delamination-Case-22']
del mdb.models['Delamination-Case-23']
del mdb.models['Delamination-Case-24']
del mdb.models['Delamination-Case-25']
del mdb.models['Delamination-Case-26']
del mdb.models['Delamination-Case-27']
del mdb.models['Delamination-Case-28']
del mdb.models['Delamination-Case-29']
del mdb.models['Delamination-Case-30']
del mdb.models['Delamination-Case-31']
del mdb.models['Delamination-Case-32']
del mdb.models['Delamination-Case-33']
del mdb.models['Delamination-Case-34']
del mdb.models['Delamination-Case-35']
del mdb.models['Delamination-Case-36']
del mdb.models['Delamination-Case-37']
del mdb.models['Delamination-Case-38']
del mdb.models['Delamination-Case-39']
del mdb.models['Delamination-Case-40']
del mdb.models['Delamination-Case-41']
del mdb.models['Delamination-Case-42']
del mdb.models['Delamination-Case-43']
del mdb.models['Delamination-Case-44']
del mdb.models['Delamination-Case-45']
del mdb.models['Delamination-Case-46']
del mdb.models['Delamination-Case-47']
del mdb.models['Delamination-Case-48']
del mdb.models['Delamination-Case-49']
del mdb.models['Delamination-Case-50']
del mdb.models['Delamination-Case-51']
del mdb.models['Delamination-Case-52']
del mdb.models['Delamination-Case-53']
del mdb.models['Delamination-Case-54']
del mdb.models['Delamination-Case-55']
del mdb.models['Delamination-Case-56']
del mdb.models['Delamination-Case-57']
del mdb.models['Delamination-Case-58']
del mdb.models['Delamination-Case-59']
del mdb.models['Delamination-Case-60']
del mdb.models['Delamination-Case-61']
del mdb.models['Delamination-Case-62']
del mdb.models['Delamination-Case-63']
del mdb.models['Delamination-Case-64']
del mdb.models['Delamination-Case-65']
del mdb.models['Delamination-Case-66']
del mdb.models['Delamination-Case-67']
del mdb.models['Delamination-Case-68']
del mdb.models['Delamination-Case-69']
del mdb.models['Delamination-Case-70']
del mdb.models['Delamination-Case-71']
del mdb.models['Delamination-Case-72']
del mdb.models['Delamination-Case-73']
del mdb.models['Delamination-Case-74']
del mdb.models['Delamination-Case-75']
del mdb.models['Delamination-Case-76']
del mdb.models['Delamination-Case-77']
del mdb.models['Delamination-Case-78']
del mdb.models['Delamination-Case-79']
del mdb.models['Delamination-Case-80']
del mdb.models['Delamination-Case-81']
del mdb.models['Delamination-Case-82']
del mdb.models['Delamination-Case-83']
del mdb.models['Delamination-Case-84']
del mdb.models['Delamination-Case-85']
del mdb.models['Delamination-Case-86']
del mdb.models['Delamination-Case-87']
del mdb.models['Delamination-Case-88']
del mdb.models['Delamination-Case-89']
del mdb.models['Delamination-Case-90']
del mdb.models['Delamination-Case-91']
del mdb.models['Delamination-Case-92']
del mdb.models['Delamination-Case-93']
del mdb.models['Delamination-Case-94']
del mdb.models['Delamination-Case-95']
del mdb.models['Delamination-Case-96']
del mdb.models['Delamination-Case-97']
del mdb.models['Delamination-Case-98']
del mdb.models['Delamination-Case-99']
del mdb.models['Delamination-Case-100']
p = mdb.models['Delamination-Case-1'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Delamination-Case-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON, optimizationTasks=OFF, 
    geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
mdb.save()
#: The model database has been saved to "C:\Users\arshi\OneDrive\Desktop\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base Vibration for smaller parts\main-model.cae".
mdb.saveAs(
    pathName='C:/Users/arshi/OneDrive/Desktop/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/main-model.cae')
#: The model database has been saved to "C:\Users\arshi\OneDrive\Desktop\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\main-model.cae".
mdb.save()
#: The model database has been saved to "C:\Users\arshi\OneDrive\Desktop\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\main-model.cae".
