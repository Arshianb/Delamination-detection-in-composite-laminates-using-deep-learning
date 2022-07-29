# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-22.27.30 176069
# Run by 795593 on Fri Jul 29 17:54:37 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=340.0, 
    height=211.055541992188)
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
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
openMdb(
    pathName='D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/composite modal analysis.cae')
#: The model database "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\modal analysis\3d shell planner\composite modal analysis.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['No delamination'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.368468, 
    farPlane=0.435522, width=0.421094, height=0.217843, 
    viewOffsetX=0.000188941, viewOffsetY=-0.00349617)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
#: 
#: Point 1: 0., 200.E-03, 0.  Point 2: 20.E-03, 200.E-03, 0.
#:    Distance: 20.E-03  Components: 20.E-03, 0., 0.
a = mdb.models['No delamination'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
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
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=6)
a = mdb.models['No delamination'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['No delamination'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
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
compositeLayup = mdb.models['No delamination'].parts['Part-1'].compositeLayups['CompositeLayup-1']
compositeLayup.orientation.setValues(additionalRotationType=ROTATION_NONE, 
    angle=0.0)
compositeLayup.deletePlies()
compositeLayup.suppress()
compositeLayup.CompositePly(suppressed=False, plyName='Ply-1', region=region1, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-2', region=region2, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-3', region=region3, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-4', region=region4, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-5', region=region5, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-6', region=region6, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-7', region=region7, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-8', region=region8, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.resume()
a = mdb.models['No delamination'].rootAssembly
a.regenerate()
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
a = mdb.models['No delamination'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
a = mdb.models['No delamination'].rootAssembly
e1 = a.instances['Part-1-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#4 ]', ), )
region = regionToolset.Region(edges=edges1)
mdb.models['No delamination'].EncastreBC(name='BC-2', createStepName='Initial', 
    region=region, localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
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
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
a = mdb.models['No delamination'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
del mdb.models['No delamination'].boundaryConditions['BC-2']
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
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
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['No delamination'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['No delamination'].parts['Part-1']
s = p.features['Shell planar-1'].sketch
mdb.models['No delamination'].ConstrainedSketch(name='__edit__', 
    objectToCopy=s)
s1 = mdb.models['No delamination'].sketches['__edit__']
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s1, 
    upToFeature=p.features['Shell planar-1'], filter=COPLANAR_EDGES)
s1.unsetPrimaryObject()
del mdb.models['No delamination'].sketches['__edit__']
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
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
compositeLayup = mdb.models['No delamination'].parts['Part-1'].compositeLayups['CompositeLayup-1']
compositeLayup.orientation.setValues(additionalRotationType=ROTATION_NONE, 
    angle=0.0)
compositeLayup.deletePlies()
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
a1 = mdb.models['No delamination'].rootAssembly
a1.regenerate()
a = mdb.models['No delamination'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
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
p = mdb.models['No delamination'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.Viewport(name='Viewport: 2', origin=(200.68, -22.8241), width=200.68, 
    height=233.88)
session.viewports['Viewport: 1'].restore()
session.viewports['Viewport: 1'].setValues(origin=(0, -22.8241), width=200.68, 
    height=233.88)
p = mdb.models['No delamination'].parts['Part-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(faces=faces)
detp = section.MdbPlyStackPlot(part=p, region=region)
session.viewports['Viewport: 2'].setValues(displayedObject=detp)
session.viewports['Viewport: 2'].viewportAnnotationOptions.setValues(
triadColor='Yellow', triadLabels=NUMBERS)
session.viewports['Viewport: 2'].view.setViewpoint(viewVector=(1, -1, 1), 
    cameraUpVector=(0, 0, 1))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.361922, 
    farPlane=0.442068, width=0.196847, height=0.224366, viewOffsetX=0.0017617, 
    viewOffsetY=-0.00598517)
del session.viewports['Viewport: 2']
session.viewports['Viewport: 1'].maximize()
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['No delamination'].materials['Material-1'].elastic.setValues(table=(
    (44700000000000.0, 13200000000000.0, 0.3, 5000000000000.0, 5000000000000.0, 
    5000000000000.0), ))
a1 = mdb.models['No delamination'].rootAssembly
a1.regenerate()
a = mdb.models['No delamination'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
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
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
p = mdb.models['No delamination'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['No delamination'].materials['Material-1'].elastic.setValues(table=(
    (44700000.0, 13200000.0, 0.3, 5000000.0, 5000000.0, 5000000.0), ))
a = mdb.models['No delamination'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
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
p = mdb.models['No delamination'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['No delamination'].materials['Material-1'].elastic.setValues(table=(
    (44700000000.0, 13200000000.0, 0.3, 5000000000.0, 5000000000.0, 
    5000000000.0), ))
a = mdb.models['No delamination'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
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
p = mdb.models['No delamination'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(width=0.433814, 
    height=0.252792, viewOffsetX=0.00165047, viewOffsetY=-0.00923826)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
a = mdb.models['No delamination'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['No delamination'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['No delamination'].materials['Material-1'].elastic.setValues(table=(
    (13200000000.0, 44700000000.0, 0.3, 5000000000.0, 5000000000.0, 
    5000000000.0), ))
a = mdb.models['No delamination'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
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
p = mdb.models['No delamination'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['No delamination'].materials['Material-1'].elastic.setValues(table=(
    (44700000000.0, 13200000000.0, 0.3, 5000000000.0, 5000000000.0, 
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
compositeLayup = mdb.models['No delamination'].parts['Part-1'].compositeLayups['CompositeLayup-1']
compositeLayup.orientation.setValues(additionalRotationType=ROTATION_NONE, 
    angle=0.0)
compositeLayup.deletePlies()
compositeLayup.suppress()
compositeLayup.CompositePly(suppressed=False, plyName='Ply-1', region=region1, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-2', region=region2, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-3', region=region3, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-4', region=region4, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-5', region=region5, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-6', region=region6, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-7', region=region7, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-8', region=region8, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.resume()
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.317353, 
    farPlane=0.497914, width=0.359168, height=0.209294, cameraPosition=(
    0.354996, -0.0749739, 0.128633), cameraUpVector=(0.261795, 0.846234, 
    0.464059), cameraTarget=(0.0134747, 0.0979661, 0.00593546), 
    viewOffsetX=0.00136648, viewOffsetY=-0.00764865)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.331448, 
    farPlane=0.483818, width=0.275303, height=0.160424, viewOffsetX=0.011, 
    viewOffsetY=-0.0139671)
a1 = mdb.models['No delamination'].rootAssembly
a1.regenerate()
a = mdb.models['No delamination'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
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
a = mdb.models['No delamination'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['No delamination'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['No delamination'].parts['Part-1']
p.deleteMesh()
p = mdb.models['No delamination'].parts['Part-1']
p.seedPart(size=0.002, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['No delamination'].parts['Part-1']
p.generateMesh()
a1 = mdb.models['No delamination'].rootAssembly
a1.regenerate()
a = mdb.models['No delamination'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, 
    optimizationTasks=ON, geometricRestrictions=ON, stopConditions=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
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
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON, mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
p = mdb.models['No delamination'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
mdb.Model(name='x_a on L eq to zero point fifteen', 
    modelType=STANDARD_EXPLICIT)
#: The model "x_a on L eq to zero point fifteen" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
s = mdb.models['x_a on L eq to zero point fifteen'].ConstrainedSketch(
    name='__profile__', sheetSize=1.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.rectangle(point1=(0.0, 0.0), point2=(0.02, 0.2))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.842896, 
    farPlane=1.04272, width=0.989371, height=0.576525, cameraPosition=(
    0.00144172, 0.0506382, 0.942809), cameraTarget=(0.00144172, 0.0506382, 0))
s.undo()
s.rectangle(point1=(0.0, 0.0), point2=(0.02, 0.01))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.895258, 
    farPlane=0.99036, width=0.470862, height=0.27438, cameraPosition=(
    0.0188572, 0.0228807, 0.942809), cameraTarget=(0.0188572, 0.0228807, 0))
p = mdb.models['x_a on L eq to zero point fifteen'].Part(name='Beam1', 
    dimensionality=THREE_D, type=DEFORMABLE_BODY)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
p.BaseShell(sketch=s)
s.unsetPrimaryObject()
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['x_a on L eq to zero point fifteen'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0418345, 
    farPlane=0.0476082, width=0.0322267, height=0.0187791, 
    viewOffsetX=0.00226656, viewOffsetY=0.00105044)
s1 = mdb.models['x_a on L eq to zero point fifteen'].ConstrainedSketch(
    name='__profile__', sheetSize=1.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.rectangle(point1=(0.0, 0.0), point2=(0.02, 0.04))
p = mdb.models['x_a on L eq to zero point fifteen'].Part(name='Beam2', 
    dimensionality=THREE_D, type=DEFORMABLE_BODY)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam2']
p.BaseShell(sketch=s1)
s1.unsetPrimaryObject()
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['x_a on L eq to zero point fifteen'].sketches['__profile__']
s = mdb.models['x_a on L eq to zero point fifteen'].ConstrainedSketch(
    name='__profile__', sheetSize=1.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.rectangle(point1=(0.0, 0.0), point2=(0.02, 0.04))
p = mdb.models['x_a on L eq to zero point fifteen'].Part(name='Beam3', 
    dimensionality=THREE_D, type=DEFORMABLE_BODY)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam3']
p.BaseShell(sketch=s)
s.unsetPrimaryObject()
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam3']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['x_a on L eq to zero point fifteen'].sketches['__profile__']
s1 = mdb.models['x_a on L eq to zero point fifteen'].ConstrainedSketch(
    name='__profile__', sheetSize=1.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.rectangle(point1=(0.0, 0.0), point2=(0.02, 0.15))
p = mdb.models['x_a on L eq to zero point fifteen'].Part(name='Beam4', 
    dimensionality=THREE_D, type=DEFORMABLE_BODY)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam4']
p.BaseShell(sketch=s1)
s1.unsetPrimaryObject()
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['x_a on L eq to zero point fifteen'].sketches['__profile__']
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam3']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam3']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['x_a on L eq to zero point fifteen'].Material(name='Material-1')
mdb.models['x_a on L eq to zero point fifteen'].materials['Material-1'].Density(
    table=((1942.5, ), ))
mdb.models['x_a on L eq to zero point fifteen'].materials['Material-1'].Elastic(
    type=LAMINA, table=((44700000000.0, 13200000000.0, 0.3, 5000000000.0, 
    5000000000.0, 5000000000.0), ))
layupOrientation = None
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam4']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region1 = regionToolset.Region(faces=faces)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam4']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region2 = regionToolset.Region(faces=faces)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam4']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region3 = regionToolset.Region(faces=faces)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam4']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region4 = regionToolset.Region(faces=faces)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam4']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region5 = regionToolset.Region(faces=faces)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam4']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region6 = regionToolset.Region(faces=faces)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam4']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region7 = regionToolset.Region(faces=faces)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam4']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region8 = regionToolset.Region(faces=faces)
compositeLayup = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam4'].CompositeLayup(
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
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-2', region=region2, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-3', region=region3, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-4', region=region4, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-5', region=region5, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-6', region=region6, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-7', region=region7, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-8', region=region8, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.resume()
a = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a1 = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
a1.DatumCsysByDefault(CARTESIAN)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
a1.Instance(name='Beam1-1', part=p, dependent=ON)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam3']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
layupOrientation = None
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam3']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region1 = regionToolset.Region(faces=faces)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam3']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region2 = regionToolset.Region(faces=faces)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam3']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region3 = regionToolset.Region(faces=faces)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam3']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region4 = regionToolset.Region(faces=faces)
compositeLayup = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam3'].CompositeLayup(
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
    material='Material-1', thicknessType=SPECIFY_THICKNESS, 
    thickness=0.00014999, orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
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
compositeLayup.resume()
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam3']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
layupOrientation = None
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam3']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region1 = regionToolset.Region(faces=faces)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam3']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region2 = regionToolset.Region(faces=faces)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam3']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region3 = regionToolset.Region(faces=faces)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam3']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region4 = regionToolset.Region(faces=faces)
compositeLayup = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam3'].compositeLayups['CompositeLayup-1']
compositeLayup.orientation.setValues(additionalRotationType=ROTATION_NONE, 
    angle=0.0)
compositeLayup.deletePlies()
compositeLayup.suppress()
compositeLayup.CompositePly(suppressed=False, plyName='Ply-1', region=region1, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-2', region=region2, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-3', region=region3, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-4', region=region4, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, 
    thickness=0.00014999, orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.resume()
session.Viewport(name='Viewport: 2', origin=(200.68, -22.8241), width=200.68, 
    height=233.88)
session.viewports['Viewport: 1'].restore()
session.viewports['Viewport: 1'].setValues(origin=(0, -22.8241), width=200.68, 
    height=233.88)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam3']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(faces=faces)
detp = section.MdbPlyStackPlot(part=p, region=region)
session.viewports['Viewport: 2'].setValues(displayedObject=detp)
session.viewports['Viewport: 2'].viewportAnnotationOptions.setValues(
triadColor='Yellow', triadLabels=NUMBERS)
session.viewports['Viewport: 2'].view.setViewpoint(viewVector=(1, -1, 1), 
    cameraUpVector=(0, 0, 1))
session.viewports['Viewport: 2'].view.setValues(nearPlane=2.50898, 
    farPlane=5.02914, width=1.68712, height=1.92297, viewOffsetX=0.0329945, 
    viewOffsetY=-0.0929441)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del session.viewports['Viewport: 2']
session.viewports['Viewport: 1'].maximize()
layupOrientation = None
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam2']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region1 = regionToolset.Region(faces=faces)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam2']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region2 = regionToolset.Region(faces=faces)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam2']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region3 = regionToolset.Region(faces=faces)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam2']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region4 = regionToolset.Region(faces=faces)
compositeLayup = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam2'].CompositeLayup(
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
    material='Material-1', thicknessType=SPECIFY_THICKNESS, 
    thickness=0.00014999, orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
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
compositeLayup.resume()
#: The selected region of part "Beam2" has the following material orientations:
#: ---------------------------------------------------------
#: Global orientation:                 '1 face'
#: 
#: Orientations shown for composite layup regions are the layup orientations only.
#: The individual ply orientations are not accounted for here.
#: Use the composite layup editor to see the ply orientations.
#: Warning: 
#: Some regions have been assigned global material orientation.
#: These directions depend on the final positioning of the instance
#: and hence cannot be displayed.
session.Viewport(name='Viewport: 2', origin=(200.68, -22.8241), width=200.68, 
    height=233.88)
session.viewports['Viewport: 1'].restore()
session.viewports['Viewport: 1'].setValues(origin=(0, -22.8241), width=200.68, 
    height=233.88)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam2']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(faces=faces)
detp = section.MdbPlyStackPlot(part=p, region=region)
session.viewports['Viewport: 2'].setValues(displayedObject=detp)
session.viewports['Viewport: 2'].viewportAnnotationOptions.setValues(
triadColor='Yellow', triadLabels=NUMBERS)
session.viewports['Viewport: 2'].view.setViewpoint(viewVector=(1, -1, 1), 
    cameraUpVector=(0, 0, 1))
layupOrientation = None
compositeLayup = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam2'].compositeLayups['CompositeLayup-1']
compositeLayup.orientation.setValues(additionalRotationType=ROTATION_NONE, 
    angle=0.0)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del session.viewports['Viewport: 2']
session.viewports['Viewport: 1'].maximize()
#: Warning: Cannot continue yet--complete the step or cancel the procedure.
#: Warning: Cannot continue yet--complete the step or cancel the procedure.
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0418345, 
    farPlane=0.0476082, width=0.0322267, height=0.0187791, 
    viewOffsetX=0.00290223, viewOffsetY=0.0011895)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0424367, 
    farPlane=0.047006, width=0.0255232, height=0.0148728, 
    viewOffsetX=0.0012203, viewOffsetY=0.000937832)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
layupOrientation = None
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region1 = regionToolset.Region(faces=faces)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region2 = regionToolset.Region(faces=faces)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region3 = regionToolset.Region(faces=faces)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region4 = regionToolset.Region(faces=faces)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region5 = regionToolset.Region(faces=faces)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region6 = regionToolset.Region(faces=faces)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region7 = regionToolset.Region(faces=faces)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region8 = regionToolset.Region(faces=faces)
compositeLayup = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1'].CompositeLayup(
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
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-2', region=region2, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-3', region=region3, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-4', region=region4, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-5', region=region5, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-6', region=region6, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-7', region=region7, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-8', region=region8, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=0.00015, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.resume()
a1 = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
a1.regenerate()
a = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a1 = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
a1.Instance(name='Beam1-2', part=p, dependent=ON)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam2']
a1.Instance(name='Beam2-1', part=p, dependent=ON)
a1 = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
a1.translate(instanceList=('Beam2-1', ), vector=(0.0, 0.01, 0.00045))
#: The instance Beam2-1 was translated by 0., 10.E-03, 450.E-06 with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0783132, 
    farPlane=0.0990343, width=0.0631074, height=0.0367739, cameraPosition=(
    0.0161225, 0.0297064, 0.0887016), cameraUpVector=(-0.573543, 0.817647, 
    -0.0500119), cameraTarget=(0.00998456, 0.0199755, 1.86916e-06))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0709792, 
    farPlane=0.107678, width=0.0571974, height=0.03333, cameraPosition=(
    0.096381, 0.0109222, 0.0187733), cameraUpVector=(-0.0969769, 0.619279, 
    0.779159), cameraTarget=(0.00928855, 0.0201384, 0.0006083))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.072115, 
    farPlane=0.106542, width=0.0482675, height=0.0281264, 
    viewOffsetX=-0.000114025, viewOffsetY=-1.30694e-06)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0714647, 
    farPlane=0.107349, width=0.0478322, height=0.0278727, cameraPosition=(
    0.0978299, 0.00779099, 0.00298442), cameraUpVector=(0.0554898, 0.555485, 
    0.829673), cameraTarget=(0.00927608, 0.0201482, 0.000633528), 
    viewOffsetX=-0.000112996, viewOffsetY=-1.29515e-06)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    renderBeamProfiles=ON, renderShellThickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0731974, 
    farPlane=0.105625, width=0.0317702, height=0.0185131, 
    viewOffsetX=-0.00392687, viewOffsetY=-0.00438001)
a = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
del a.features['Beam1-2']
a = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
del a.features['Beam2-1']
a1 = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam2']
a1.Instance(name='Beam2-1', part=p, dependent=ON)
a1 = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
a1.translate(instanceList=('Beam2-1', ), vector=(0.0, 0.01, 0.0003))
#: The instance Beam2-1 was translated by 0., 10.E-03, 300.E-06 with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0786331, 
    farPlane=0.10672, width=0.00753327, height=0.00439268, 
    viewOffsetX=-0.0064498, viewOffsetY=-0.00420484)
a1 = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam3']
a1.Instance(name='Beam3-1', part=p, dependent=ON)
a1 = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
a1.translate(instanceList=('Beam3-1', ), vector=(0.0, 0.01, -0.0003))
#: The instance Beam3-1 was translated by 0., 10.E-03, -300.E-06 with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.095833, 
    farPlane=0.123347, width=0.00433046, height=0.00252511, 
    viewOffsetX=-0.0105467, viewOffsetY=-0.00703556)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0958085, 
    farPlane=0.123372, width=0.00432936, height=0.00252447, cameraPosition=(
    0.117987, 0.0077264, 0.0110301), cameraUpVector=(-0.0296664, -0.0224866, 
    0.999307), cameraTarget=(0.00948601, 0.0228671, 0.00814968), 
    viewOffsetX=-0.010544, viewOffsetY=-0.00703376)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0965046, 
    farPlane=0.120839, width=0.00436081, height=0.00254281, cameraPosition=(
    0.118557, 0.0144556, -0.00111157), cameraUpVector=(0.084156, -0.106854, 
    0.990707), cameraTarget=(0.00970755, 0.0222076, 0.00897077), 
    viewOffsetX=-0.0106206, viewOffsetY=-0.00708486)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.096375, 
    farPlane=0.120968, width=0.00535138, height=0.00312042, 
    viewOffsetX=-0.0109606, viewOffsetY=-0.0069172)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0960781, 
    farPlane=0.122195, width=0.0053349, height=0.0031108, cameraPosition=(
    0.118609, 0.011328, 0.00173807), cameraUpVector=(0.0549213, -0.0544281, 
    0.997006), cameraTarget=(0.00980747, 0.0226637, 0.00835033), 
    viewOffsetX=-0.0109268, viewOffsetY=-0.00689589)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0965703, 
    farPlane=0.121703, width=0.000171496, height=0.0001, 
    viewOffsetX=-0.0117179, viewOffsetY=-0.00699817)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.096583, 
    farPlane=0.121679, width=0.000171518, height=0.000100013, cameraPosition=(
    0.118626, 0.0113368, 7.93494e-05), cameraUpVector=(0.0700328, -0.0625763, 
    0.99558), cameraTarget=(0.00993567, 0.0225936, 0.0084325), 
    viewOffsetX=-0.0117195, viewOffsetY=-0.00699909)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0956017, 
    farPlane=0.122661, width=0.0111696, height=0.00651306, 
    viewOffsetX=-0.010479, viewOffsetY=-0.00690979)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0945008, 
    farPlane=0.1268, width=0.011041, height=0.00643807, cameraPosition=(
    0.117105, 8.21535e-05, 0.0143673), cameraUpVector=(-0.05559, 0.0468135, 
    0.997356), cameraTarget=(0.0102366, 0.0233083, 0.00732048), 
    viewOffsetX=-0.0103583, viewOffsetY=-0.00683022)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.087859, 
    farPlane=0.133441, width=0.0858774, height=0.0500755, 
    viewOffsetX=0.00778998, viewOffsetY=-0.00132811)
a1 = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam4']
a1.Instance(name='Beam4-1', part=p, dependent=ON)
a1 = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
a1.translate(instanceList=('Beam4-1', ), vector=(0.0, 0.05, 0.0))
#: The instance Beam4-1 was translated by 0., 50.E-03, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.280948, 
    farPlane=0.349018, width=0.0341467, height=0.0199111, 
    viewOffsetX=-0.0188934, viewOffsetY=4.99118e-05)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
a = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.270024, 
    farPlane=0.359942, width=0.156044, height=0.0909903, 
    viewOffsetX=-0.0407839, viewOffsetY=-0.00379454)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.262469, 
    farPlane=0.441455, width=0.151679, height=0.0884445, cameraPosition=(
    0.258218, -0.149006, 0.0233772), cameraUpVector=(-0.0117675, 0.108259, 
    0.994053), cameraTarget=(0.030626, 0.0594686, -0.00202144), 
    viewOffsetX=-0.0396428, viewOffsetY=-0.00368837)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.269298, 
    farPlane=0.434627, width=0.078793, height=0.0459446, 
    viewOffsetX=-0.0460039, viewOffsetY=-0.00417142)
a = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
e1 = a.instances['Beam1-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(edges=edges1)
mdb.models['x_a on L eq to zero point fifteen'].EncastreBC(name='BC-1', 
    createStepName='Initial', region=region, localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
mdb.models['x_a on L eq to zero point fifteen'].FrequencyStep(name='Step-1', 
    previous='Initial', numEigen=10)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#1 ]', ), )
p.setMeshControls(regions=pickedRegions, technique=SWEEP)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
p.seedPart(size=0.001, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
p.generateMesh()
p = mdb.models['No delamination'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
p.deleteMesh()
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
p.seedPart(size=0.002, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
p.generateMesh()
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam2']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#1 ]', ), )
p.setMeshControls(regions=pickedRegions, technique=SWEEP)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam2']
p.seedPart(size=0.002, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam2']
p.generateMesh()
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam3']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam3']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#1 ]', ), )
p.setMeshControls(regions=pickedRegions, technique=SWEEP)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam3']
p.seedPart(size=0.002, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam3']
p.generateMesh()
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam3']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam4']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#1 ]', ), )
p.setMeshControls(regions=pickedRegions, technique=SWEEP)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam4']
p.seedPart(size=0.002, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam4']
p.generateMesh()
a = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a1 = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
a1.regenerate()
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.263648, 
    farPlane=0.440277, width=0.134626, height=0.0787093, 
    viewOffsetX=-0.0013974, viewOffsetY=0.00716547)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, 
    interactions=ON, constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.267672, 
    farPlane=0.436253, width=0.106997, height=0.0623902, 
    viewOffsetX=-0.0105417, viewOffsetY=0.00435664)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam4']
s = p.edges
side1Edges = s.getSequenceFromMask(mask=('[#1 ]', ), )
p.Surface(side1Edges=side1Edges, name='left')
#: The surface 'left' has been created (1 edge).
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam3']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
#: Warning: Cannot continue yet--complete the step or cancel the procedure.
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam3']
s = p.edges
side1Edges = s.getSequenceFromMask(mask=('[#4 ]', ), )
p.Surface(side1Edges=side1Edges, name='right')
#: The surface 'right' has been created (1 edge).
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam3']
s = p.edges
side1Edges = s.getSequenceFromMask(mask=('[#1 ]', ), )
p.Surface(side1Edges=side1Edges, name='left')
#: The surface 'left' has been created (1 edge).
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam3']
s = p.faces
side1Faces = s.getSequenceFromMask(mask=('[#1 ]', ), )
p.Surface(side1Faces=side1Faces, name='top')
#: The surface 'top' has been created (1 face).
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam3']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam2']
s = p.edges
side1Edges = s.getSequenceFromMask(mask=('[#4 ]', ), )
p.Surface(side1Edges=side1Edges, name='right')
#: The surface 'right' has been created (1 edge).
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam2']
s = p.edges
side1Edges = s.getSequenceFromMask(mask=('[#1 ]', ), )
p.Surface(side1Edges=side1Edges, name='left')
#: The surface 'left' has been created (1 edge).
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam2']
s = p.faces
side2Faces = s.getSequenceFromMask(mask=('[#1 ]', ), )
p.Surface(side2Faces=side2Faces, name='bottom')
#: The surface 'bottom' has been created (1 face).
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
s = p.edges
side1Edges = s.getSequenceFromMask(mask=('[#4 ]', ), )
p.Surface(side1Edges=side1Edges, name='right')
#: The surface 'right' has been created (1 edge).
a1 = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
a1.regenerate()
a = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
region1=a.instances['Beam1-1'].surfaces['right']
a = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
region2=a.instances['Beam2-1'].surfaces['left']
mdb.models['x_a on L eq to zero point fifteen'].Tie(name='Beam1 to Beam2', 
    main=region1, secondary=region2, positionToleranceMethod=COMPUTED, 
    adjust=ON, tieRotations=ON, thickness=ON)
a = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
region1=a.instances['Beam1-1'].surfaces['right']
a = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
region2=a.instances['Beam3-1'].surfaces['left']
mdb.models['x_a on L eq to zero point fifteen'].Tie(name='Beam1 to Beam3', 
    main=region1, secondary=region2, positionToleranceMethod=COMPUTED, 
    adjust=ON, tieRotations=ON, thickness=ON)
a = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
region1=a.instances['Beam4-1'].surfaces['left']
a = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
region2=a.instances['Beam2-1'].surfaces['right']
mdb.models['x_a on L eq to zero point fifteen'].Tie(name='Beam4 to Beam2', 
    main=region1, secondary=region2, positionToleranceMethod=COMPUTED, 
    adjust=ON, tieRotations=ON, thickness=ON)
a = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
region1=a.instances['Beam4-1'].surfaces['left']
a = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
region2=a.instances['Beam3-1'].surfaces['right']
mdb.models['x_a on L eq to zero point fifteen'].Tie(name='Beam4 to Beam3', 
    main=region1, secondary=region2, positionToleranceMethod=COMPUTED, 
    adjust=ON, tieRotations=ON, thickness=ON)
mdb.models['x_a on L eq to zero point fifteen'].ContactProperty('IntProp-1')
mdb.models['x_a on L eq to zero point fifteen'].interactionProperties['IntProp-1'].TangentialBehavior(
    formulation=FRICTIONLESS)
#: The interaction property "IntProp-1" has been created.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
a = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
region1=a.instances['Beam2-1'].surfaces['bottom']
a = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
region2=a.instances['Beam3-1'].surfaces['top']
mdb.models['x_a on L eq to zero point fifteen'].SurfaceToSurfaceContactStd(
    name='Int-1', createStepName='Initial', main=region1, secondary=region2, 
    sliding=FINITE, thickness=ON, interactionProperty='IntProp-1', 
    adjustMethod=NONE, initialClearance=OMIT, datumAxis=None, 
    clearanceRegion=None)
#: The interaction "Int-1" has been created.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.262683, 
    farPlane=0.441242, width=0.162584, height=0.0948032, 
    viewOffsetX=-0.00348052, viewOffsetY=-0.00419745)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.25997, 
    farPlane=0.443955, width=0.171175, height=0.100078, 
    viewOffsetX=-0.00324912, viewOffsetY=-0.00441181)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.Job(name='Job-2', model='x_a on L eq to zero point fifteen', 
    description='', type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, 
    queue=None, memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Job Job-2: Analysis Input File Processor completed successfully.
#: Job Job-2: Abaqus/Standard completed successfully.
#: Job Job-2 completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-1.odb'])
o3 = session.openOdb(
    name='D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-2.odb')
#: Model: D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-2.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     4
#: Number of Meshes:             4
#: Number of Element Sets:       5
#: Number of Node Sets:          2
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
a = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
mdb.models['x_a on L eq to zero point fifteen'].constraints['Beam1 to Beam2'].setValues(
    positionToleranceMethod=SPECIFIED, positionTolerance=0.002)
mdb.models['x_a on L eq to zero point fifteen'].constraints['Beam1 to Beam3'].setValues(
    positionToleranceMethod=SPECIFIED, positionTolerance=0.002)
mdb.models['x_a on L eq to zero point fifteen'].constraints['Beam4 to Beam2'].setValues(
    positionToleranceMethod=SPECIFIED, positionTolerance=0.002)
mdb.models['x_a on L eq to zero point fifteen'].constraints['Beam4 to Beam3'].setValues(
    positionToleranceMethod=SPECIFIED, positionTolerance=0.002)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Job Job-2: Analysis Input File Processor completed successfully.
#: Job Job-2: Abaqus/Standard completed successfully.
#: Job Job-2 completed successfully. 
o3 = session.openOdb(
    name='D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-2.odb')
#: Model: D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-2.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     4
#: Number of Meshes:             4
#: Number of Element Sets:       5
#: Number of Node Sets:          2
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.343078, 
    farPlane=0.537876, width=0.31285, height=0.182424, viewOffsetX=0.00716245, 
    viewOffsetY=-0.00676351)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.37365, 
    farPlane=0.510954, width=0.340728, height=0.19868, cameraPosition=(
    0.400093, 0.22391, 0.157989), cameraUpVector=(-0.442623, 0.799096, 
    -0.406855), cameraTarget=(0.0127884, 0.108961, -0.00262135), 
    viewOffsetX=0.0078007, viewOffsetY=-0.00736621)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.370858, 
    farPlane=0.513745, width=0.338182, height=0.197195, cameraPosition=(
    0.400594, 0.213468, 0.164253), cameraUpVector=(-0.714662, 0.55811, 
    0.42163), cameraTarget=(0.0132898, 0.0985193, 0.00364276), 
    viewOffsetX=0.00774241, viewOffsetY=-0.00731116)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.378851, 
    farPlane=0.506234, width=0.345471, height=0.201445, cameraPosition=(
    0.404919, 0.178817, 0.173969), cameraUpVector=(-0.678815, 0.597332, 
    0.427088), cameraTarget=(0.0131453, 0.0979408, 0.00371742), 
    viewOffsetX=0.00790929, viewOffsetY=-0.00746874)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.384032, 
    farPlane=0.500885, width=0.350196, height=0.2042, cameraPosition=(0.362014, 
    0.147773, 0.254127), cameraUpVector=(-0.730699, 0.599693, 0.326264), 
    cameraTarget=(0.0101719, 0.0968801, 0.0038668), viewOffsetX=0.00801746, 
    viewOffsetY=-0.00757088)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5)
p = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
a = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.261685, 
    farPlane=0.44224, width=0.154534, height=0.0901094, 
    viewOffsetX=-0.00587849, viewOffsetY=0.00487005)
mdb.Model(name='x_a on L eq to zero point fifty', modelType=STANDARD_EXPLICIT)
#: The model "x_a on L eq to zero point fifty" has been created.
a = mdb.models['x_a on L eq to zero point fifty'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p1 = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
del mdb.models['x_a on L eq to zero point fifty']
p = mdb.models['No delamination'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p1 = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
mdb.Model(name='x_a on L eq to zero point fifty', 
    objectToCopy=mdb.models['x_a on L eq to zero point fifteen'])
#: The model "x_a on L eq to zero point fifty" has been created.
p = mdb.models['x_a on L eq to zero point fifty'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0424295, 
    farPlane=0.0470132, width=0.0255188, height=0.0149197, 
    viewOffsetX=0.00146749, viewOffsetY=-0.00067038)
a = mdb.models['x_a on L eq to zero point fifty'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.352019, 
    farPlane=0.515902, width=0.250337, height=0.14636, cameraPosition=(
    0.248975, 0.328998, 0.280822), cameraUpVector=(-0.966783, 0.198517, 
    0.161004), cameraTarget=(0.00622774, 0.107709, -0.0039365))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.385805, 
    farPlane=0.47079, width=0.274364, height=0.160407, cameraPosition=(
    0.317625, 0.0600538, 0.295409), cameraUpVector=(-0.689699, 0.641053, 
    0.336699), cameraTarget=(0.00610741, 0.10818, -0.00396207))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.383517, 
    farPlane=0.473078, width=0.272737, height=0.159456, cameraPosition=(
    0.317625, 0.0600538, 0.295409), cameraUpVector=(-0.810434, 0.404016, 
    0.424227), cameraTarget=(0.00610741, 0.10818, -0.00396207))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.385731, 
    farPlane=0.471407, width=0.274311, height=0.160376, cameraPosition=(0.3983, 
    0.0750833, 0.179806), cameraUpVector=(-0.644883, 0.375806, 0.665504), 
    cameraTarget=(0.00489748, 0.107955, -0.00222829))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.386979, 
    farPlane=0.470159, width=0.275199, height=0.160896, 
    viewOffsetX=-0.00590682, viewOffsetY=0.00534316)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.343425, 
    farPlane=0.510505, width=0.244225, height=0.142787, cameraPosition=(
    0.351463, -0.104672, 0.154432), cameraUpVector=(-0.399447, 0.56261, 
    0.723818), cameraTarget=(0.0067118, 0.109141, -0.00181653), 
    viewOffsetX=-0.005242, viewOffsetY=0.00474179)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.347583, 
    farPlane=0.506348, width=0.21841, height=0.127694, viewOffsetX=-0.00103404, 
    viewOffsetY=0.0051969)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['x_a on L eq to zero point fifty'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['x_a on L eq to zero point fifty'].parts['Beam1']
s = p.features['Shell planar-1'].sketch
mdb.models['x_a on L eq to zero point fifty'].ConstrainedSketch(
    name='__edit__', objectToCopy=s)
s2 = mdb.models['x_a on L eq to zero point fifty'].sketches['__edit__']
g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
s2.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s2, 
    upToFeature=p.features['Shell planar-1'], filter=COPLANAR_EDGES)
s2.unsetPrimaryObject()
del mdb.models['x_a on L eq to zero point fifty'].sketches['__edit__']
p = mdb.models['x_a on L eq to zero point fifty'].parts['Beam1']
s = p.features['Shell planar-1'].sketch
mdb.models['x_a on L eq to zero point fifty'].ConstrainedSketch(
    name='__edit__', objectToCopy=s)
s1 = mdb.models['x_a on L eq to zero point fifty'].sketches['__edit__']
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s1, 
    upToFeature=p.features['Shell planar-1'], filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0421664, 
    farPlane=0.0472763, width=0.0286141, height=0.016685, cameraPosition=(
    0.0119413, 0.00411862, 0.0447214), cameraTarget=(0.0119413, 0.00411862, 0))
s1.FixedConstraint(entity=v[0])
s1.ObliqueDimension(vertex1=v[0], vertex2=v[1], textPoint=(
    -0.00192986149340868, 0.00612043589353561), value=0.08)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0236926, 
    farPlane=0.0657501, width=0.235508, height=0.137326, cameraPosition=(
    0.0508467, 0.0460543, 0.0447214), cameraTarget=(0.0508467, 0.0460543, 0))
s1.unsetPrimaryObject()
p = mdb.models['x_a on L eq to zero point fifty'].parts['Beam1']
p.features['Shell planar-1'].setValues(sketch=s1)
del mdb.models['x_a on L eq to zero point fifty'].sketches['__edit__']
p = mdb.models['x_a on L eq to zero point fifty'].parts['Beam1']
p.regenerate()
#: Warning: Failed to attach mesh to part geometry.
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0327965, 
    farPlane=0.0566462, width=0.119953, height=0.0699451, 
    viewOffsetX=0.0082931, viewOffsetY=0.0226869)
p1 = mdb.models['x_a on L eq to zero point fifty'].parts['Beam4']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['x_a on L eq to zero point fifty'].parts['Beam4']
s = p.features['Shell planar-1'].sketch
mdb.models['x_a on L eq to zero point fifty'].ConstrainedSketch(
    name='__edit__', objectToCopy=s)
s2 = mdb.models['x_a on L eq to zero point fifty'].sketches['__edit__']
g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
s2.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s2, 
    upToFeature=p.features['Shell planar-1'], filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.278537, 
    farPlane=0.326773, width=0.238666, height=0.139167, cameraPosition=(
    0.00633676, 0.0585927, 0.302655), cameraTarget=(0.00633676, 0.0585927, 0))
s2.FixedConstraint(entity=v[0])
s2.ObliqueDimension(vertex1=v[0], vertex2=v[1], textPoint=(-0.0511958822607994, 
    0.067620150744915), value=0.08)
s2.unsetPrimaryObject()
p = mdb.models['x_a on L eq to zero point fifty'].parts['Beam4']
p.features['Shell planar-1'].setValues(sketch=s2)
del mdb.models['x_a on L eq to zero point fifty'].sketches['__edit__']
p = mdb.models['x_a on L eq to zero point fifty'].parts['Beam4']
p.regenerate()
#: Warning: Failed to attach mesh to part geometry.
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.287832, 
    farPlane=0.317477, width=0.147189, height=0.0858269, 
    viewOffsetX=0.00953631, viewOffsetY=-0.0314186)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
a1 = mdb.models['x_a on L eq to zero point fifty'].rootAssembly
a1.regenerate()
a = mdb.models['x_a on L eq to zero point fifty'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.344697, 
    farPlane=0.474805, width=0.278158, height=0.162195, viewOffsetX=0.0115466, 
    viewOffsetY=0.00427095)
a = mdb.models['x_a on L eq to zero point fifty'].rootAssembly
a.deleteFeatures(('Beam1-1', 'Beam2-1', 'Beam3-1', 'Beam4-1', ))
a1 = mdb.models['x_a on L eq to zero point fifty'].rootAssembly
p = mdb.models['x_a on L eq to zero point fifty'].parts['Beam1']
a1.Instance(name='Beam1-1', part=p, dependent=ON)
p = mdb.models['x_a on L eq to zero point fifty'].parts['Beam2']
a1.Instance(name='Beam2-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.243193, 
    farPlane=0.282947, width=0.191652, height=0.111753, 
    viewOffsetX=9.02647e-05, viewOffsetY=-0.0193679)
a1 = mdb.models['x_a on L eq to zero point fifty'].rootAssembly
a1.translate(instanceList=('Beam2-1', ), vector=(0.0, 0.08, 0.0003))
#: The instance Beam2-1 was translated by 0., 80.E-03, 300.E-06 with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.221463, 
    farPlane=0.295676, width=0.174527, height=0.101767, cameraPosition=(
    0.0237195, 0.125038, 0.250799), cameraUpVector=(-0.947868, 0.316985, 
    0.0326576), cameraTarget=(-0.0097896, 0.0506018, 0.000714339), 
    viewOffsetX=8.21992e-05, viewOffsetY=-0.0176373)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.232693, 
    farPlane=0.286472, width=0.183377, height=0.106928, cameraPosition=(
    0.261043, 0.0535768, 0.0703175), cameraUpVector=(-0.173387, 0.32281, 
    0.930447), cameraTarget=(0.00232894, 0.0519637, 0.0226663), 
    viewOffsetX=8.63675e-05, viewOffsetY=-0.0185317)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.235357, 
    farPlane=0.283809, width=0.155317, height=0.090566, viewOffsetX=0.0223113, 
    viewOffsetY=-0.0201211)
a1 = mdb.models['x_a on L eq to zero point fifty'].rootAssembly
p = mdb.models['x_a on L eq to zero point fifty'].parts['Beam3']
a1.Instance(name='Beam3-1', part=p, dependent=ON)
a1 = mdb.models['x_a on L eq to zero point fifty'].rootAssembly
a1.translate(instanceList=('Beam3-1', ), vector=(0.0, 0.08, -0.0003))
#: The instance Beam3-1 was translated by 0., 80.E-03, -300.E-06 with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.232494, 
    farPlane=0.256874, width=0.021033, height=0.0122644, viewOffsetX=0.0226623, 
    viewOffsetY=0.00760148)
a1 = mdb.models['x_a on L eq to zero point fifty'].rootAssembly
p = mdb.models['x_a on L eq to zero point fifty'].parts['Beam4']
a1.Instance(name='Beam4-1', part=p, dependent=ON)
a1 = mdb.models['x_a on L eq to zero point fifty'].rootAssembly
a1.translate(instanceList=('Beam4-1', ), vector=(0.0, 0.12, 0.0))
#: The instance Beam4-1 was translated by 0., 120.E-03, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.225812, 
    farPlane=0.263065, width=0.0901919, height=0.0525913, 
    viewOffsetX=0.0332611, viewOffsetY=0.00879762)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
    interactions=OFF, constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['x_a on L eq to zero point fifty'].parts['Beam4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['x_a on L eq to zero point fifty'].parts['Beam4']
p.generateMesh()
p = mdb.models['x_a on L eq to zero point fifty'].parts['Beam3']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['x_a on L eq to zero point fifty'].parts['Beam2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['x_a on L eq to zero point fifty'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['x_a on L eq to zero point fifty'].parts['Beam1']
p.generateMesh()
a1 = mdb.models['x_a on L eq to zero point fifty'].rootAssembly
a1.regenerate()
a = mdb.models['x_a on L eq to zero point fifty'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.Job(name='Job-3', model='x_a on L eq to zero point fifty', description='', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['Job-3'].submit(consistencyChecking=OFF)
#: The job input file "Job-3.inp" has been submitted for analysis.
#: Error in job Job-3: in keyword *BOUNDARY, file "Job-3.inp", line 2732: Unknown assembly node set _PICKEDSET14
#: Error in job Job-3: NODE SET ASSEMBLY__PICKEDSET14 HAS NOT BEEN DEFINED
#: Error in job Job-3: A BOUNDARY CONDITION HAS BEEN SPECIFIED ON NODE SET ASSEMBLY__PICKEDSET14 BUT THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Error in job Job-3: NODE SET ASSEMBLY__PICKEDSET14 HAS NOT BEEN DEFINED
#: Error in job Job-3: NODE SET ASSEMBLY__PICKEDSET14 HAS NOT BEEN DEFINED
#: Error in job Job-3: NODE SET ASSEMBLY__PICKEDSET14 HAS NOT BEEN DEFINED
#: Job Job-3: Analysis Input File Processor aborted due to errors.
#: Error in job Job-3: Analysis Input File Processor exited with an error - Please see the  Job-3.dat file for possible error messages if the file exists.
#: Job Job-3 aborted due to errors.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.209317, 
    farPlane=0.27956, width=0.245139, height=0.10897, viewOffsetX=0.00615689, 
    viewOffsetY=0.0104537)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.152717, 
    farPlane=0.384768, width=0.178853, height=0.0795045, cameraPosition=(
    0.113118, -0.149466, -0.0122147), cameraUpVector=(0.53615, 0.234294, 
    0.810956), cameraTarget=(-0.00300711, 0.0654039, 0.00248116), 
    viewOffsetX=0.00449205, viewOffsetY=0.00762696)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.167315, 
    farPlane=0.37017, width=0.0876607, height=0.0389674, 
    viewOffsetX=-0.00703718, viewOffsetY=-0.00187322)
a = mdb.models['x_a on L eq to zero point fifty'].rootAssembly
e1 = a.instances['Beam1-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(edges=edges1)
mdb.models['x_a on L eq to zero point fifty'].boundaryConditions['BC-1'].setValues(
    region=region)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['Job-3'].submit(consistencyChecking=OFF)
#: The job input file "Job-3.inp" has been submitted for analysis.
#: Job Job-3: Analysis Input File Processor completed successfully.
#: Job Job-3: Abaqus/Standard completed successfully.
#: Job Job-3 completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-2.odb'])
o3 = session.openOdb(
    name='D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-3.odb')
#: Model: D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-3.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     4
#: Number of Meshes:             4
#: Number of Element Sets:       5
#: Number of Node Sets:          2
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.333449, 
    farPlane=0.52452, width=0.292726, height=0.130124, viewOffsetX=3.44106e-05, 
    viewOffsetY=-0.00368877)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['x_a on L eq to zero point fifty'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.Model(name='x_a on L eq to zero point eighty five', 
    objectToCopy=mdb.models['x_a on L eq to zero point fifty'])
#: The model "x_a on L eq to zero point eighty five" has been created.
p = mdb.models['x_a on L eq to zero point eighty five'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
#: The contents of viewport "Viewport: 1" have been copied to the clipboard.
del mdb.models['x_a on L eq to zero point eighty five']
p = mdb.models['No delamination'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p1 = mdb.models['x_a on L eq to zero point fifteen'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
mdb.Model(name='x_a on L eq to zero point eighty five', 
    objectToCopy=mdb.models['x_a on L eq to zero point fifteen'])
#: The model "x_a on L eq to zero point eighty five" has been created.
p = mdb.models['x_a on L eq to zero point eighty five'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['x_a on L eq to zero point eighty five'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
a = mdb.models['x_a on L eq to zero point eighty five'].rootAssembly
e1 = a.instances['Beam4-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#4 ]', ), )
region = regionToolset.Region(edges=edges1)
mdb.models['x_a on L eq to zero point eighty five'].boundaryConditions['BC-1'].setValues(
    region=region)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='Job-4', model='x_a on L eq to zero point eighty five', 
    description='', type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, 
    queue=None, memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['Job-4'].submit(consistencyChecking=OFF)
#: The job input file "Job-4.inp" has been submitted for analysis.
#: Job Job-4: Analysis Input File Processor completed successfully.
#: Job Job-4: Abaqus/Standard completed successfully.
#: Job Job-4 completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-3.odb'])
o3 = session.openOdb(
    name='D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-4.odb')
#: Model: D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-4.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     4
#: Number of Meshes:             4
#: Number of Element Sets:       5
#: Number of Node Sets:          2
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.327963, 
    farPlane=0.545082, width=0.392299, height=0.174387, viewOffsetX=0.0158024, 
    viewOffsetY=0.00758336)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5)
a = mdb.models['x_a on L eq to zero point eighty five'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.models.changeKey(fromName='x_a on L eq to zero point eighty five', 
    toName='x_a on L eq to zero point eighty five CF')
a = mdb.models['x_a on L eq to zero point eighty five CF'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['No delamination'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.models.changeKey(fromName='No delamination', toName='No delamination CF')
a = mdb.models['No delamination CF'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['x_a on L eq to zero point fifteen'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.models.changeKey(fromName='x_a on L eq to zero point fifteen', 
    toName='x_a on L eq to zero point fifteen CF')
a = mdb.models['x_a on L eq to zero point fifteen CF'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['x_a on L eq to zero point fifty'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.models.changeKey(fromName='x_a on L eq to zero point fifty', 
    toName='x_a on L eq to zero point fifty CF')
a = mdb.models['x_a on L eq to zero point fifty CF'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['No delamination CF'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.Model(name='No delamination CC', 
    objectToCopy=mdb.models['No delamination CF'])
#: The model "No delamination CC" has been created.
a = mdb.models['No delamination CC'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
a = mdb.models['No delamination CC'].rootAssembly
e1 = a.instances['Part-1-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#4 ]', ), )
region = regionToolset.Region(edges=edges1)
mdb.models['No delamination CC'].EncastreBC(name='BC-2', 
    createStepName='Initial', region=region, localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='Job-5', model='No delamination CC', description='', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['Job-5'].submit(consistencyChecking=OFF)
#: The job input file "Job-5.inp" has been submitted for analysis.
#: Job Job-5: Analysis Input File Processor completed successfully.
#: Job Job-5: Abaqus/Standard completed successfully.
#: Job Job-5 completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-4.odb'])
o3 = session.openOdb(
    name='D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-5.odb')
#: Model: D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-5.odb
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
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
p = mdb.models['No delamination CC'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['No delamination CC'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
a = mdb.models['No delamination CC'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-5.odb'])
o3 = session.openOdb(
    name='D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-5.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
p = mdb.models['No delamination CC'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['No delamination CC'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
a = mdb.models['x_a on L eq to zero point fifteen CF'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.Model(name='x_a on L eq to zero point fifteen CC', 
    objectToCopy=mdb.models['x_a on L eq to zero point fifteen CF'])
#: The model "x_a on L eq to zero point fifteen CC" has been created.
a = mdb.models['x_a on L eq to zero point fifteen CC'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['x_a on L eq to zero point fifteen CC'].rootAssembly
e1 = a.instances['Beam4-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#4 ]', ), )
region = regionToolset.Region(edges=edges1)
mdb.models['x_a on L eq to zero point fifteen CC'].EncastreBC(name='BC-2', 
    createStepName='Initial', region=region, localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='Job-6', model='x_a on L eq to zero point fifteen CC', 
    description='', type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, 
    queue=None, memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['Job-6'].submit(consistencyChecking=OFF)
#: The job input file "Job-6.inp" has been submitted for analysis.
#: Job Job-6: Analysis Input File Processor completed successfully.
#: Job Job-6: Abaqus/Standard completed successfully.
#: Job Job-6 completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-5.odb'])
o3 = session.openOdb(
    name='D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-6.odb')
#: Model: D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-6.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     4
#: Number of Meshes:             4
#: Number of Element Sets:       5
#: Number of Node Sets:          2
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.326716, 
    farPlane=0.531252, width=0.36736, height=0.163301, viewOffsetX=0.00748781, 
    viewOffsetY=-0.0101717)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON, mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
p = mdb.models['x_a on L eq to zero point fifteen CC'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0420118, 
    farPlane=0.0474309, width=0.030235, height=0.0134402, 
    viewOffsetX=0.00119656, viewOffsetY=-0.00026595)
p1 = mdb.models['x_a on L eq to zero point fifty CF'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
mdb.Model(name='x_a on L eq to zero point fifty CC', 
    objectToCopy=mdb.models['x_a on L eq to zero point fifty CF'])
#: The model "x_a on L eq to zero point fifty CC" has been created.
p = mdb.models['x_a on L eq to zero point fifty CC'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['x_a on L eq to zero point fifty CC'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
a = mdb.models['x_a on L eq to zero point fifty CC'].rootAssembly
e1 = a.instances['Beam4-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#4 ]', ), )
region = regionToolset.Region(edges=edges1)
mdb.models['x_a on L eq to zero point fifty CC'].EncastreBC(name='BC-2', 
    createStepName='Initial', region=region, localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['Job-6'].submit(consistencyChecking=OFF)
#: The job input file "Job-6.inp" has been submitted for analysis.
mdb.jobs['Job-6'].kill()
#: Error in job Job-6: Process terminated by external request (SIGTERM or SIGINT received).
#: Job Job-6: Analysis Input File Processor was terminated prior to analysis completion.
a = mdb.models['x_a on L eq to zero point fifteen CF'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
#: Error in job Job-6: Analysis Input File Processor exited with an error - Please see the  Job-6.dat file for possible error messages if the file exists.
mdb.jobs['Job-6'].submit(consistencyChecking=OFF)
#: The job input file "Job-6.inp" has been submitted for analysis.
#: Job Job-6: Analysis Input File Processor completed successfully.
#: Job Job-6: Abaqus/Standard completed successfully.
#: Job Job-6 completed successfully. 
a = mdb.models['x_a on L eq to zero point fifty CC'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.Job(name='Job-7', model='x_a on L eq to zero point fifty CC', 
    description='', type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, 
    queue=None, memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['Job-7'].submit(consistencyChecking=OFF)
#: The job input file "Job-7.inp" has been submitted for analysis.
#: Job Job-7: Analysis Input File Processor completed successfully.
#: Job Job-7: Abaqus/Standard completed successfully.
#: Job Job-7 completed successfully. 
o3 = session.openOdb(
    name='D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-7.odb')
#: Model: D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-7.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     4
#: Number of Meshes:             4
#: Number of Element Sets:       5
#: Number of Node Sets:          2
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.359423, 
    farPlane=0.521813, width=0.117242, height=0.0521171, viewOffsetX=0.0124552, 
    viewOffsetY=-0.00778811)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.324517, 
    farPlane=0.544356, width=0.389766, height=0.173261, viewOffsetX=0.0413866, 
    viewOffsetY=0.00402443)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['x_a on L eq to zero point fifty CC'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['x_a on L eq to zero point fifty CC'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-7.odb'])
o3 = session.openOdb(
    name='D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-7.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['x_a on L eq to zero point fifty CC'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.34018, 
    farPlane=0.529262, width=0.305256, height=0.135694, viewOffsetX=0.00361159, 
    viewOffsetY=0.000800616)
mdb.Model(name='x_a on L eq to zero point thrity CC', 
    objectToCopy=mdb.models['x_a on L eq to zero point fifty CC'])
#: The model "x_a on L eq to zero point thrity CC" has been created.
a = mdb.models['x_a on L eq to zero point thrity CC'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['x_a on L eq to zero point thrity CC'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['x_a on L eq to zero point thrity CC'].parts['Beam1']
s = p.features['Shell planar-1'].sketch
mdb.models['x_a on L eq to zero point thrity CC'].ConstrainedSketch(
    name='__edit__', objectToCopy=s)
s1 = mdb.models['x_a on L eq to zero point thrity CC'].sketches['__edit__']
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s1, 
    upToFeature=p.features['Shell planar-1'], filter=COPLANAR_EDGES)
s1.delete(objectList=(d[0], ))
s1.ObliqueDimension(vertex1=v[0], vertex2=v[1], textPoint=(-0.0210051368921995, 
    0.0378746949136257), value=0.04)
s1.unsetPrimaryObject()
p = mdb.models['x_a on L eq to zero point thrity CC'].parts['Beam1']
p.features['Shell planar-1'].setValues(sketch=s1)
del mdb.models['x_a on L eq to zero point thrity CC'].sketches['__edit__']
p = mdb.models['x_a on L eq to zero point thrity CC'].parts['Beam1']
p.regenerate()
#: Warning: Failed to attach mesh to part geometry.
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.14865, 
    farPlane=0.181198, width=0.181191, height=0.080544, viewOffsetX=0.00196626, 
    viewOffsetY=-0.00341943)
p = mdb.models['x_a on L eq to zero point thrity CC'].parts['Beam2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['x_a on L eq to zero point thrity CC'].parts['Beam2']
s = p.features['Shell planar-1'].sketch
mdb.models['x_a on L eq to zero point thrity CC'].ConstrainedSketch(
    name='__edit__', objectToCopy=s)
s2 = mdb.models['x_a on L eq to zero point thrity CC'].sketches['__edit__']
g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
s2.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s2, 
    upToFeature=p.features['Shell planar-1'], filter=COPLANAR_EDGES)
s2.unsetPrimaryObject()
del mdb.models['x_a on L eq to zero point thrity CC'].sketches['__edit__']
p1 = mdb.models['x_a on L eq to zero point thrity CC'].parts['Beam4']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['x_a on L eq to zero point thrity CC'].parts['Beam4']
s = p.features['Shell planar-1'].sketch
mdb.models['x_a on L eq to zero point thrity CC'].ConstrainedSketch(
    name='__edit__', objectToCopy=s)
s1 = mdb.models['x_a on L eq to zero point thrity CC'].sketches['__edit__']
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s1, 
    upToFeature=p.features['Shell planar-1'], filter=COPLANAR_EDGES)
s1.delete(objectList=(d[0], ))
s1.ObliqueDimension(vertex1=v[0], vertex2=v[1], textPoint=(-0.0478768385946751, 
    0.0308346375823021), value=0.12)
s1.unsetPrimaryObject()
p = mdb.models['x_a on L eq to zero point thrity CC'].parts['Beam4']
p.features['Shell planar-1'].setValues(sketch=s1)
del mdb.models['x_a on L eq to zero point thrity CC'].sketches['__edit__']
p = mdb.models['x_a on L eq to zero point thrity CC'].parts['Beam4']
p.regenerate()
#: Warning: Failed to attach mesh to part geometry.
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.132858, 
    farPlane=0.196991, width=0.321162, height=0.142765, viewOffsetX=0.0251375, 
    viewOffsetY=0.024702)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
a1 = mdb.models['x_a on L eq to zero point thrity CC'].rootAssembly
a1.regenerate()
a = mdb.models['x_a on L eq to zero point thrity CC'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.309996, 
    farPlane=0.536353, width=0.420291, height=0.18683, viewOffsetX=0.0097521, 
    viewOffsetY=0.00410084)
a = mdb.models['x_a on L eq to zero point thrity CC'].rootAssembly
a.deleteFeatures(('Beam1-1', 'Beam2-1', 'Beam3-1', 'Beam4-1', ))
a1 = mdb.models['x_a on L eq to zero point thrity CC'].rootAssembly
p = mdb.models['x_a on L eq to zero point thrity CC'].parts['Beam1']
a1.Instance(name='Beam1-1', part=p, dependent=ON)
p = mdb.models['x_a on L eq to zero point thrity CC'].parts['Beam2']
a1.Instance(name='Beam2-1', part=p, dependent=ON)
a1 = mdb.models['x_a on L eq to zero point thrity CC'].rootAssembly
a1.translate(instanceList=('Beam2-1', ), vector=(0.0, 0.04, 0.0003))
#: The instance Beam2-1 was translated by 0., 40.E-03, 300.E-06 with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.450457, 
    farPlane=0.512882, width=0.304159, height=0.135206, viewOffsetX=0.0113974, 
    viewOffsetY=-0.0387639)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.452067, 
    farPlane=0.511272, width=0.305246, height=0.13569, cameraPosition=(
    -0.0194107, 0.0902224, 0.48167), cameraUpVector=(-0.847507, 0.530785, 0), 
    cameraTarget=(-0.0194107, 0.0902224, 0), viewOffsetX=0.0114381, 
    viewOffsetY=-0.0389025)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.425067, 
    farPlane=0.531685, width=0.287015, height=0.127586, cameraPosition=(
    0.460312, -0.101922, 0.0966881), cameraUpVector=(-0.00297651, 0.277762, 
    0.960645), cameraTarget=(0.0172808, 0.0792911, 0.0429191), 
    viewOffsetX=0.0107549, viewOffsetY=-0.036579)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.444686, 
    farPlane=0.512065, width=0.104876, height=0.0466201, 
    viewOffsetX=-0.0236459, viewOffsetY=-0.0483574)
a1 = mdb.models['x_a on L eq to zero point thrity CC'].rootAssembly
p = mdb.models['x_a on L eq to zero point thrity CC'].parts['Beam3']
a1.Instance(name='Beam3-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.13827, 
    farPlane=0.236662, width=0.091391, height=0.0406256, 
    viewOffsetX=0.000676416, viewOffsetY=0.00426551)
a1 = mdb.models['x_a on L eq to zero point thrity CC'].rootAssembly
a1.translate(instanceList=('Beam3-1', ), vector=(0.0, 0.04, -0.0003))
#: The instance Beam3-1 was translated by 0., 40.E-03, -300.E-06 with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.137082, 
    farPlane=0.204394, width=0.103805, height=0.0461439, 
    viewOffsetX=0.00463836, viewOffsetY=0.00852773)
a1 = mdb.models['x_a on L eq to zero point thrity CC'].rootAssembly
p = mdb.models['x_a on L eq to zero point thrity CC'].parts['Beam4']
a1.Instance(name='Beam4-1', part=p, dependent=ON)
a1 = mdb.models['x_a on L eq to zero point thrity CC'].rootAssembly
a1.translate(instanceList=('Beam4-1', ), vector=(0.0, 0.08, 0.0003))
#: The instance Beam4-1 was translated by 0., 80.E-03, 300.E-06 with respect to the assembly coordinate system
a = mdb.models['x_a on L eq to zero point thrity CC'].rootAssembly
del a.features['Beam4-1']
a1 = mdb.models['x_a on L eq to zero point thrity CC'].rootAssembly
p = mdb.models['x_a on L eq to zero point thrity CC'].parts['Beam4']
a1.Instance(name='Beam4-1', part=p, dependent=ON)
a1 = mdb.models['x_a on L eq to zero point thrity CC'].rootAssembly
a1.translate(instanceList=('Beam4-1', ), vector=(0.0, 0.08, 0.0))
#: The instance Beam4-1 was translated by 0., 80.E-03, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.358199, 
    farPlane=0.494383, width=0.236687, height=0.105213, viewOffsetX=0.0225583, 
    viewOffsetY=0.00880842)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.360661, 
    farPlane=0.491921, width=0.186063, height=0.0827099, 
    viewOffsetX=0.00965777, viewOffsetY=0.00258955)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.358199, 
    farPlane=0.494383, width=0.236687, height=0.105213, viewOffsetX=0.0122725, 
    viewOffsetY=0.000313698)
a = mdb.models['x_a on L eq to zero point thrity CC'].rootAssembly
e1 = a.instances['Beam4-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#4 ]', ), )
region = regionToolset.Region(edges=edges1)
mdb.models['x_a on L eq to zero point thrity CC'].boundaryConditions['BC-1'].setValues(
    region=region)
del mdb.models['x_a on L eq to zero point thrity CC'].boundaryConditions['BC-2']
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
a = mdb.models['x_a on L eq to zero point thrity CC'].rootAssembly
e1 = a.instances['Beam1-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(edges=edges1)
mdb.models['x_a on L eq to zero point thrity CC'].EncastreBC(name='BC-2', 
    createStepName='Initial', region=region, localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['x_a on L eq to zero point thrity CC'].parts['Beam4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['x_a on L eq to zero point thrity CC'].parts['Beam4']
p.generateMesh()
p = mdb.models['x_a on L eq to zero point thrity CC'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['x_a on L eq to zero point thrity CC'].parts['Beam1']
p.generateMesh()
p = mdb.models['x_a on L eq to zero point thrity CC'].parts['Beam2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['x_a on L eq to zero point thrity CC'].parts['Beam4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['x_a on L eq to zero point thrity CC'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a1 = mdb.models['x_a on L eq to zero point thrity CC'].rootAssembly
a1.regenerate()
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.Job(name='Job-8', model='x_a on L eq to zero point thrity CC', 
    description='', type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, 
    queue=None, memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['Job-8'].submit(consistencyChecking=OFF)
#: The job input file "Job-8.inp" has been submitted for analysis.
#: Job Job-8: Analysis Input File Processor completed successfully.
#: Job Job-8: Abaqus/Standard completed successfully.
#: Job Job-8 completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-7.odb'])
o3 = session.openOdb(
    name='D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-8.odb')
#: Model: D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d shell planner/Job-8.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     4
#: Number of Meshes:             4
#: Number of Element Sets:       5
#: Number of Node Sets:          2
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=7)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=10)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=9)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=10)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=8)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
a = mdb.models['x_a on L eq to zero point thrity CC'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['x_a on L eq to zero point thrity CC'].parts['Beam4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.209431, 
    farPlane=0.27719, width=0.375239, height=0.167246, viewOffsetX=0.036873, 
    viewOffsetY=-0.0102818)
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\modal analysis\3d shell planner\composite modal analysis.cae".
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\modal analysis\3d shell planner\composite modal analysis.cae".
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\modal analysis\3d shell planner\composite modal analysis.cae".
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\modal analysis\3d shell planner\composite modal analysis.cae".
