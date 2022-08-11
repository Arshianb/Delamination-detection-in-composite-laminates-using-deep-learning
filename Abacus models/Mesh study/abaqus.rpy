# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-22.27.30 176069
# Run by 795593 on Thu Aug 11 10:20:13 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=291.390625, 
    height=116.805549621582)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
openMdb(
    pathName='C:/Users/795593/OneDrive/Desktop/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/Mesh study/Modal Analysis.cae')
#: The model database "C:\Users\795593\OneDrive\Desktop\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Mesh study\Modal Analysis.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Delamination-Case-1'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
#--- Recover file: 'Modal Analysis.rec' ---
# -*- coding: mbcs -*- 
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
del mdb.jobs['Job-11']
del mdb.jobs['Job-12']
del mdb.jobs['Job-13']
del mdb.jobs['Job-14']
del mdb.jobs['Job-15']
del mdb.jobs['Job-16']
del mdb.jobs['Job-17']
del mdb.jobs['Job-18']
del mdb.jobs['Job-19']
del mdb.jobs['Job-20']
del mdb.jobs['Job-21']
del mdb.jobs['Job-22']
del mdb.jobs['Job-23']
del mdb.jobs['Job-24']
del mdb.jobs['Job-25']
del mdb.jobs['Job-26']
del mdb.jobs['Job-27']
del mdb.jobs['Job-28']
del mdb.jobs['Job-29']
del mdb.jobs['Job-30']
del mdb.jobs['Job-31']
del mdb.jobs['Job-32']
del mdb.jobs['Job-33']
del mdb.jobs['Job-34']
del mdb.jobs['Job-35']
del mdb.jobs['Job-36']
del mdb.jobs['Job-37']
del mdb.jobs['Job-38']
del mdb.jobs['Job-39']
del mdb.jobs['Job-40']
del mdb.jobs['Job-41']
del mdb.jobs['Job-42']
del mdb.jobs['Job-43']
del mdb.jobs['Job-44']
del mdb.jobs['Job-45']
#--- End of Recover file ------
p = mdb.models['Delamination-forModalAnalysis-Case-6'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Delamination-forModalAnalysis-Case-3'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.29971, 
    farPlane=1.5966, width=1.67422, height=0.58091, viewOffsetX=0.0796825, 
    viewOffsetY=0.00583503)
p = mdb.models['Delamination-forModalAnalysis-Case-4'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.28965, 
    farPlane=1.60666, width=1.76729, height=0.613201, viewOffsetX=0.150093, 
    viewOffsetY=-0.0383205)
a = mdb.models['Delamination-forModalAnalysis-Case-4'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.43149, 
    farPlane=1.46482, width=0.162566, height=0.088731, viewOffsetX=-0.189261, 
    viewOffsetY=0.211659)
a = mdb.models['Delamination-forModalAnalysis-Case-10'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.35463, 
    farPlane=1.54168, width=0.921531, height=0.502986, viewOffsetX=-0.0222823, 
    viewOffsetY=-0.00300942)
a = mdb.models['Delamination-forModalAnalysis-Case-2'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
p = mdb.models['Delamination-forModalAnalysis-Case-2'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.35018, 
    farPlane=1.54613, width=0.976928, height=0.533222, viewOffsetX=0.0549903, 
    viewOffsetY=0.0102866)
p = mdb.models['Delamination-forModalAnalysis-Case-10'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.33734, 
    farPlane=1.55897, width=1.23937, height=0.67647, viewOffsetX=0.109754, 
    viewOffsetY=0.0178461)
a = mdb.models['Delamination-forModalAnalysis-Case-10'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(width=0.909574, height=0.49646, 
    viewOffsetX=-0.00132211, viewOffsetY=0.00445504)
a = mdb.models['Delamination-forModalAnalysis-Case-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Delamination-forModalAnalysis-Case-6'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
p = mdb.models['Delamination-forModalAnalysis-Case-6'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.34972, 
    farPlane=1.54659, width=1.10525, height=0.60326, viewOffsetX=0.0437757, 
    viewOffsetY=-0.0427299)
p = mdb.models['Delamination-forModalAnalysis-Case-5'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.34972, 
    farPlane=1.54659, width=1.10525, height=0.60326, viewOffsetX=0.0635819, 
    viewOffsetY=-0.0360065)
p = mdb.models['Delamination-forModalAnalysis-Case-4'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.35069, 
    farPlane=1.54562, width=1.03968, height=0.567473, viewOffsetX=0.0366251, 
    viewOffsetY=-0.0304429)
p = mdb.models['Delamination-forModalAnalysis-Case-5'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Delamination-forModalAnalysis-Case-4'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Delamination-forModalAnalysis-Case-4'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Delamination-forModalAnalysis-Case-5'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
p = mdb.models['Delamination-forModalAnalysis-Case-5'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.34972, 
    farPlane=1.54659, width=1.10525, height=0.60326, viewOffsetX=0.0348433, 
    viewOffsetY=-0.0417252)
mdb.save()
#: The model database has been saved to "C:\Users\795593\OneDrive\Desktop\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Mesh study\Modal Analysis.cae".
mdb.saveAs(
    pathName='C:/Users/795593/OneDrive/Desktop/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/Base vibration model/main-model.cae')
#: The model database has been saved to "C:\Users\795593\OneDrive\Desktop\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\main-model.cae".
p1 = mdb.models['Delamination-forModalAnalysis-Case-1'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Delamination-forModalAnalysis-Case-6'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.34351, 
    farPlane=1.5528, width=1.17039, height=0.638815, viewOffsetX=0.067836, 
    viewOffsetY=-0.0489699)
p = mdb.models['Delamination-forModalAnalysis-Case-5'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.34972, 
    farPlane=1.54659, width=1.10525, height=0.60326, viewOffsetX=0.04753, 
    viewOffsetY=-0.0348586)
p = mdb.models['Delamination-forModalAnalysis-Case-4'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Delamination-forModalAnalysis-Case-4'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.40738, 
    farPlane=1.48893, width=0.402614, height=0.219753, viewOffsetX=-0.134215, 
    viewOffsetY=0.143488)
a = mdb.models['Delamination-forModalAnalysis-Case-5'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Delamination-forModalAnalysis-Case-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
del mdb.models['Delamination-forModalAnalysis-Case-1']
del mdb.models['Delamination-forModalAnalysis-Case-2']
del mdb.models['Delamination-forModalAnalysis-Case-3']
del mdb.models['Delamination-forModalAnalysis-Case-4']
a = mdb.models['Delamination-Case-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
del mdb.models['Delamination-Case-1']
a = mdb.models['Delamination-forModalAnalysis-Case-5'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Delamination-forModalAnalysis-Case-6'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
del mdb.models['Delamination-forModalAnalysis-Case-6']
del mdb.models['Delamination-forModalAnalysis-Case-7']
del mdb.models['Delamination-forModalAnalysis-Case-8']
del mdb.models['Delamination-forModalAnalysis-Case-9']
del mdb.models['Delamination-forModalAnalysis-Case-10']
a = mdb.models['Delamination-forModalAnalysis-Case-5'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.models.changeKey(fromName='Delamination-forModalAnalysis-Case-5', 
    toName='Delamination-Case-1')
a = mdb.models['Delamination-Case-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Delamination-Case-1'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.35069, 
    farPlane=1.54562, width=1.04242, height=0.567472, viewOffsetX=0.0358872, 
    viewOffsetY=-0.0264336)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Delamination-Case-1'].parts['Beam2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Delamination-Case-1'].parts['Beam3']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Delamination-Case-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
    interactions=OFF, constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.36174, 
    farPlane=1.53457, width=0.818536, height=0.44677, viewOffsetX=-0.0270818, 
    viewOffsetY=0.0254701)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, 
    optimizationTasks=ON, geometricRestrictions=ON, stopConditions=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON, optimizationTasks=OFF, 
    geometricRestrictions=OFF, stopConditions=OFF)
del mdb.models['Delamination-Case-1'].steps['Step-1']
mdb.models['Delamination-Case-1'].ImplicitDynamicsStep(name='Step-1', 
    previous='Initial', timePeriod=0.01, maxNumInc=1000000, 
    timeIncrementationMethod=FIXED, initialInc=5e-06, nohaf=OFF, noStop=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
a = mdb.models['Delamination-Case-1'].rootAssembly
region = a.instances['Beam1-1'].sets['Set-2']
mdb.models['Delamination-Case-1'].ConcentratedForce(name='Load-1', 
    createStepName='Step-1', region=region, cf3=0.0001, amplitude='sin (w t)', 
    distributionType=UNIFORM, field='', localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Delamination-Case-1'].parts['Beam3']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Delamination-Case-1'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Delamination-Case-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
regionDef=mdb.models['Delamination-Case-1'].rootAssembly.allInstances['Beam1-1'].sets['Set-3']
mdb.models['Delamination-Case-1'].historyOutputRequests['H-Output-1'].setValues(
    variables=('A1', ), region=regionDef, sectionPoints=DEFAULT, rebar=EXCLUDE)
mdb.models['Delamination-Case-1'].fieldOutputRequests['F-Output-1'].setValues(
    variables=('U', ))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
del mdb.jobs['Job-1']
del mdb.jobs['Job-2']
del mdb.jobs['Job-3']
del mdb.jobs['Job-4']
del mdb.jobs['Job-5']
del mdb.jobs['Job-6']
del mdb.jobs['Job-7']
del mdb.jobs['Job-8']
del mdb.jobs['Job-9']
del mdb.jobs['Job-10']
mdb.save()
#: The model database has been saved to "C:\Users\795593\OneDrive\Desktop\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\main-model.cae".

---------- RUNTIME EXCEPTION HAS OCCURRED ----------
*** ERROR: ABAQUS/ABQcaeK rank 0 received the ABORT signal
