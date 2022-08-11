# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-22.27.30 176069
# Run by 795593 on Thu Aug 11 12:29:21 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=291.390625, 
    height=197.092590332031)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
openMdb(
    pathName='C:/Users/795593/OneDrive/Desktop/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/Base vibration model/main-model.cae')
#: The model database "C:\Users\795593\OneDrive\Desktop\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\main-model.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Delamination-Case-1'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Delamination-Case-1'].rootAssembly
a.regenerate()
a = mdb.models['Delamination-Case-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
del mdb.jobs['Job-1']
cliCommand("""import time""")
cliCommand("""from initial import initial""")
cliCommand("""initial()""")
cliCommand("""from delamination_hole_onBeam1 import move_delamination_onBeam1""")
cliCommand("""from move_Beam1andBeam2 import moveBeam2""")
cliCommand("""from edit_partitionOfBeam1 import EditPartitionBEam1""")
cliCommand("""from edit_mesh import edit_mesh""")
cliCommand("""from submit_TheJob import Submit_the_job""")
cliCommand("""from copy_the_case_delamination1 import copy_the_caseDelamination1""")
cliCommand("""import os""")
cliCommand("""for i in range(1, 101):
    # copy_the_caseDelamination1(i)
    # move_delamination_onBeam1(i)
    # moveBeam2(i)
    # EditPartitionBEam1(i)
    # edit_mesh(i)
    # time.sleep(0.5)
    Submit_the_job(i)
    while os.path.exists('C:\\\\Users\\\\795593\\\\OneDrive\\\\Desktop\\\\Delamination-detection-in-composite-laminates-using-deep-learning\\Abacus models\\\\Base vibration model/Job-{}.023'.format(i)) == False:
        time.sleep(0.1)
    while os.path.exists('C:\\\\Users\\\\795593\\\\OneDrive\\\\Desktop\\\\Delamination-detection-in-composite-laminates-using-deep-learning\\Abacus models\\\\Base vibration model/Job-{}.023'.format(i)):
        time.sleep(0.1)
""")
