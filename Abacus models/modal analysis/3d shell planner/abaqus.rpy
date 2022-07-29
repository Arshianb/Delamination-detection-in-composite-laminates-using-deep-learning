# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-22.27.30 176069
# Run by arshi on Fri Jul 29 16:13:54 2022
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
openMdb(
    pathName='D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/composite modal analysis.cae')
#: The model database "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\modal analysis\3d shell planner\composite modal analysis.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['No delamination'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['No delamination'].Material(name='Material-1')
mdb.models['No delamination'].materials['Material-1'].Depvar()
mdb.models['No delamination'].materials['Material-1'].Density(table=((0.0, ), 
    ))
del mdb.models['No delamination'].materials['Material-1']
mdb.models['No delamination'].Material(name='Material-1')
mdb.models['No delamination'].materials['Material-1'].Density(table=((1942.5, 
    ), ))
mdb.models['No delamination'].materials['Material-1'].Elastic(type=LAMINA, 
    table=((44700000000.0, 13200000000.0, 0.3, 5000000000.0, 5000000000.0, 
    5000000000.0), ))
layupOrientation = None
p = mdb.models['No delamination'].parts['Part-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region1 = regionToolset.Region(faces=faces)
p = mdb.models['No delamination'].parts['Part-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region2 = regionToolset.Region(faces=faces)
p = mdb.models['No delamination'].parts['Part-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region3 = regionToolset.Region(faces=faces)
p = mdb.models['No delamination'].parts['Part-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region4 = regionToolset.Region(faces=faces)
p = mdb.models['No delamination'].parts['Part-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region5 = regionToolset.Region(faces=faces)
p = mdb.models['No delamination'].parts['Part-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region6 = regionToolset.Region(faces=faces)
p = mdb.models['No delamination'].parts['Part-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region7 = regionToolset.Region(faces=faces)
p = mdb.models['No delamination'].parts['Part-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region8 = regionToolset.Region(faces=faces)
compositeLayup = mdb.models['No delamination'].parts['Part-1'].CompositeLayup(
    name='CompositeLayup-1', description='', elementType=SHELL, 
    offsetType=MIDDLE_SURFACE, symmetric=False, 
    thicknessAssignment=FROM_SECTION)
compositeLayup.Section(preIntegrate=OFF, integrationRule=SIMPSON, 
    thicknessType=UNIFORM, poissonDefinition=DEFAULT, temperature=GRADIENT, 
    useDensity=OFF)
compositeLayup.ReferenceOrientation(orientationType=GLOBAL, localCsys=None, 
    fieldName='', additionalRotationType=ROTATION_NONE, angle=0.0, axis=AXIS_3)
compositeLayup.suppress()
compositeLayup.CompositePly(suppressed=False, plyName='Ply-1', region=region1, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-2', region=region2, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-3', region=region3, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-4', region=region4, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-5', region=region5, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-6', region=region6, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-7', region=region7, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-8', region=region8, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.resume()
a = mdb.models['No delamination'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['No delamination'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['No delamination'].parts['Part-1']
a.Instance(name='Part-1-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
a = mdb.models['No delamination'].rootAssembly
e1 = a.instances['Part-1-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(edges=edges1)
mdb.models['No delamination'].EncastreBC(name='BC-1', createStepName='Initial', 
    region=region, localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
mdb.models['No delamination'].FrequencyStep(name='Step-1', previous='Initial', 
    numEigen=10)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
mdb.Job(name='Job-1', model='No delamination', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Error in job Job-1: in keyword *BOUNDARY, file "Job-1.inp", line 32: Unknown assembly node set _PICKEDSET4
#: Error in job Job-1: THIS MODEL HAS EITHER INCORRECT OR NO ELEMENT DEFINITIONS.
#: Job Job-1: Analysis Input File Processor aborted due to errors.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
#: Error in job Job-1: Analysis Input File Processor exited with an error - Please see the  Job-1.dat file for possible error messages if the file exists.
#: Job Job-1 aborted due to errors.
p = mdb.models['No delamination'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['No delamination'].parts['Part-1']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#1 ]', ), )
p.setMeshControls(regions=pickedRegions, technique=SWEEP)
p = mdb.models['No delamination'].parts['Part-1']
p.seedPart(size=0.01, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['No delamination'].parts['Part-1']
p.generateMesh()
p = mdb.models['No delamination'].parts['Part-1']
p.deleteMesh()
p = mdb.models['No delamination'].parts['Part-1']
p.seedPart(size=0.005, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['No delamination'].parts['Part-1']
p.generateMesh()
elemType1 = mesh.ElemType(elemCode=S4R, elemLibrary=STANDARD, 
    secondOrderAccuracy=OFF, hourglassControl=DEFAULT)
elemType2 = mesh.ElemType(elemCode=S3, elemLibrary=STANDARD)
p = mdb.models['No delamination'].parts['Part-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
pickedRegions =(faces, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
a1 = mdb.models['No delamination'].rootAssembly
a1.regenerate()
a = mdb.models['No delamination'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Job Job-1: Analysis Input File Processor completed successfully.
#: Job Job-1: Abaqus/Standard completed successfully.
#: Job Job-1 completed successfully. 
o3 = session.openOdb(
    name='D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-1.odb')
#: Model: D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          1
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.461164, 
    farPlane=0.703255, width=0.370899, height=0.16301, viewOffsetX=-0.0156096, 
    viewOffsetY=0.00201439)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON, mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
p = mdb.models['No delamination'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['No delamination'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    renderBeamProfiles=ON, renderShellThickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.34204, 
    farPlane=0.461951, width=0.385114, height=0.17868, cameraPosition=(0.01, 
    0.1, 0.401995), cameraUpVector=(-0.925333, 0.379155, 0), cameraTarget=(
    0.01, 0.1, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.295264, 
    farPlane=0.508727, width=0.332447, height=0.154244, cameraPosition=(
    0.357826, -0.0898417, 0.0676555), cameraUpVector=(-0.086066, 0.190797, 
    0.977849), cameraTarget=(0.0100004, 0.0999998, -3.96743e-07))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.315342, 
    farPlane=0.488648, width=0.219993, height=0.102069, 
    viewOffsetX=-0.00818793, viewOffsetY=-0.00605935)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-1.odb'])
o3 = session.openOdb(
    name='D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-1.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['No delamination'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
layupOrientation = None
compositeLayup = mdb.models['No delamination'].parts['Part-1'].compositeLayups['CompositeLayup-1']
compositeLayup.orientation.setValues(additionalRotationType=ROTATION_NONE, 
    angle=0.0)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
a = mdb.models['No delamination'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-1.odb'])
o3 = session.openOdb(
    name='D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-1.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['No delamination'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-1.odb'])
o3 = session.openOdb(
    name='D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-1.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\modal analysis\3d shell planner\composite modal analysis.cae".
