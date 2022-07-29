# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-22.27.30 176069
# Run by 795593 on Fri Jul 29 18:16:52 2022
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
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.rectangle(point1=(0.0, 0.0), point2=(0.02, 0.2))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.86512, 
    farPlane=1.0205, width=0.866548, height=0.448287, cameraPosition=(
    -0.0504842, 0.0768467, 0.942809), cameraTarget=(-0.0504842, 0.0768467, 0))
p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-1']
p.BaseSolidExtrude(sketch=s, depth=0.0012)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['Model-1'].Material(name='Material-1')
mdb.models['Model-1'].materials['Material-1'].Density(table=((1942.5, ), ))
mdb.models['Model-1'].materials['Material-1'].Elastic(type=LAMINA, table=((
    44700000000.0, 13200000000.0, 0.3, 5000000000.0, 5000000000.0, 
    5000000000.0), ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.351054, 
    farPlane=0.518389, width=0.2493, height=0.128969, viewOffsetX=-0.0037784, 
    viewOffsetY=0.00429085)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.363283, 
    farPlane=0.50616, width=0.0847023, height=0.0438187, 
    viewOffsetX=0.00626228, viewOffsetY=0.0509482)
p = mdb.models['Model-1'].parts['Part-1']
f, e, d1 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f[1], sketchUpEdge=e[5], 
    sketchPlaneSide=SIDE1, origin=(0.01, 0.2, 0.0006))
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=0.4, 
    gridSpacing=0.01, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['Part-1']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0394909, 
    farPlane=0.240653, width=0.0064811, height=0.00335284, cameraPosition=(
    0.0187561, 0.240072, 0.000569931), cameraTarget=(0.0187561, 0.2, 
    0.000569931))
s1.Spot(point=(0.01, 0.000509320962615311))
s1.CoincidentConstraint(entity1=v[4], entity2=g[4], addUndoState=False)
s1.Spot(point=(0.01, 0.000370742258988321))
s1.CoincidentConstraint(entity1=v[5], entity2=g[4], addUndoState=False)
s1.Spot(point=(0.01, 0.000143627025559545))
s1.CoincidentConstraint(entity1=v[6], entity2=g[4], addUndoState=False)
s1.Spot(point=(0.01, -0.000141229392588139))
s1.CoincidentConstraint(entity1=v[7], entity2=g[4], addUndoState=False)
s1.Spot(point=(0.01, -0.00029905527420342))
s1.CoincidentConstraint(entity1=v[8], entity2=g[4], addUndoState=False)
s1.Spot(point=(0.01, -0.000445332872308791))
s1.CoincidentConstraint(entity1=v[9], entity2=g[4], addUndoState=False)
s1.Spot(point=(0.01, -0.0006))
s1.CoincidentConstraint(entity1=v[10], entity2=g[2], addUndoState=False)
s1.undo()
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0395893, 
    farPlane=0.240555, width=0.00486769, height=0.00251818, cameraPosition=(
    0.019058, 0.240072, 0.000710603), cameraTarget=(0.019058, 0.2, 
    0.000710603))
s1.Spot(point=(0.01, -0.00052837296910584))
s1.CoincidentConstraint(entity1=v[10], entity2=g[4], addUndoState=False)
s1.Spot(point=(0.01, 0.000509320962615311))
s1.Spot(point=(0.01, 0.0006))
s1.CoincidentConstraint(entity1=v[12], entity2=g[4], addUndoState=False)
s1.undo()
s1.undo()
s1.undo()
s1.redo()
s1.redo()
s1.undo()
s1.VerticalDimension(vertex1=v[3], vertex2=v[4], textPoint=(0.0104279478639364, 
    0.000526892865914851), value=0.00015)
s1.ObliqueDimension(vertex1=v[4], vertex2=v[5], textPoint=(0.00935259439051151, 
    0.000304274989198893), value=0.00015)
s1.VerticalDimension(vertex1=v[5], vertex2=v[6], textPoint=(0.0102163085341454, 
    0.000177064823824912), value=0.00015)
s1.VerticalDimension(vertex1=v[6], vertex2=v[7], textPoint=(
    0.00957567222416401, -5.07672606036072e-06), value=0.00015)
s1.VerticalDimension(vertex1=v[7], vertex2=v[8], textPoint=(0.0103049685806036, 
    -0.000169871694501489), value=0.00015)
s1.VerticalDimension(vertex1=v[8], vertex2=v[9], textPoint=(
    0.00947271265089512, -0.000369360291492194), value=0.00015)
s1.VerticalDimension(vertex1=v[9], vertex2=v[10], textPoint=(0.010462267100811, 
    -0.000406945036351681), value=0.00015)
s1.Line(point1=(0.01, 0.0006), point2=(0.01, 0.00045))
s1.VerticalConstraint(entity=g[6], addUndoState=False)
s1.ParallelConstraint(entity1=g[4], entity2=g[6], addUndoState=False)
s1.Line(point1=(0.01, 0.00045), point2=(0.01, 0.0003))
s1.VerticalConstraint(entity=g[7], addUndoState=False)
s1.ParallelConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
s1.Line(point1=(0.01, 0.0003), point2=(0.01, 0.00015))
s1.VerticalConstraint(entity=g[8], addUndoState=False)
s1.ParallelConstraint(entity1=g[7], entity2=g[8], addUndoState=False)
s1.Line(point1=(0.01, 0.00015), point2=(0.01, 0.0))
s1.VerticalConstraint(entity=g[9], addUndoState=False)
s1.ParallelConstraint(entity1=g[8], entity2=g[9], addUndoState=False)
s1.Line(point1=(0.01, 0.0), point2=(0.01, -0.00015))
s1.VerticalConstraint(entity=g[10], addUndoState=False)
s1.ParallelConstraint(entity1=g[9], entity2=g[10], addUndoState=False)
s1.Line(point1=(0.01, -0.00015), point2=(0.01, -0.0003))
s1.VerticalConstraint(entity=g[11], addUndoState=False)
s1.ParallelConstraint(entity1=g[10], entity2=g[11], addUndoState=False)
s1.Line(point1=(0.01, -0.0003), point2=(0.01, -0.00045))
s1.VerticalConstraint(entity=g[12], addUndoState=False)
s1.ParallelConstraint(entity1=g[11], entity2=g[12], addUndoState=False)
s1.Line(point1=(0.01, -0.00045), point2=(0.01, -0.0006))
s1.VerticalConstraint(entity=g[13], addUndoState=False)
s1.ParallelConstraint(entity1=g[12], entity2=g[13], addUndoState=False)
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#2 ]', ), )
e1, d2 = p.edges, p.datums
p.PartitionFaceBySketch(sketchUpEdge=e1[5], faces=pickedFaces, sketch=s1)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.370653, 
    farPlane=0.498791, width=0.002388, height=0.00123537, 
    viewOffsetX=0.00686591, viewOffsetY=0.0678667)
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
e, v1, d1 = p.edges, p.vertices, p.datums
p.PartitionCellByPlanePointNormal(point=v1[5], normal=e[5], cells=pickedCells)
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#2 ]', ), )
e1, v2, d2 = p.edges, p.vertices, p.datums
p.PartitionCellByPlanePointNormal(point=v2[11], normal=e1[12], 
    cells=pickedCells)
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#4 ]', ), )
e, v1, d1 = p.edges, p.vertices, p.datums
p.PartitionCellByPlanePointNormal(point=v1[4], normal=e[4], cells=pickedCells)
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
e1, v2, d2 = p.edges, p.vertices, p.datums
p.PartitionCellByPlanePointNormal(point=v2[11], normal=e1[16], 
    cells=pickedCells)
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#2 ]', ), )
e, v1, d1 = p.edges, p.vertices, p.datums
p.PartitionCellByPlanePointNormal(point=v1[4], normal=e[4], cells=pickedCells)
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
e1, v2, d2 = p.edges, p.vertices, p.datums
p.PartitionCellByPlanePointNormal(point=v2[11], normal=e1[16], 
    cells=pickedCells)
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#2 ]', ), )
e, v1, d1 = p.edges, p.vertices, p.datums
p.PartitionCellByPlanePointNormal(point=v1[4], normal=e[4], cells=pickedCells)
#: 
#: Point 1: 20.E-03, 200.E-03, 1.05E-03  Point 2: 20.E-03, 200.E-03, 1.2E-03
#:    Distance: 150.E-06  Components: 0., 0., 150.E-06
#: 
#: Point 1: 20.E-03, 200.E-03, 150.E-06  Point 2: 20.E-03, 200.E-03, 0.
#:    Distance: 150.E-06  Components: 0., 0., -150.E-06
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.370521, 
    farPlane=0.498923, width=0.00386082, height=0.0019973, 
    viewOffsetX=0.00669223, viewOffsetY=0.0681675)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
layupOrientation = None
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#40 ]', ), )
region1 = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#20 ]', ), )
region2 = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#80 ]', ), )
region3 = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#8 ]', ), )
region4 = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#10 ]', ), )
region5 = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#2 ]', ), )
region6 = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#4 ]', ), )
region7 = regionToolset.Region(cells=cells)
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region8 = regionToolset.Region(cells=cells)
compositeLayup = mdb.models['Model-1'].parts['Part-1'].CompositeLayup(
    name='CompositeLayup-1', description='', elementType=CONTINUUM_SHELL, 
    symmetric=False)
compositeLayup.Section(preIntegrate=OFF, integrationRule=SIMPSON, 
    poissonDefinition=DEFAULT, thicknessModulus=None, temperature=GRADIENT, 
    useDensity=OFF)
compositeLayup.ReferenceOrientation(orientationType=GLOBAL, localCsys=None, 
    fieldName='', additionalRotationType=ROTATION_NONE, angle=0.0, axis=AXIS_3, 
    stackDirection=STACK_3)
compositeLayup.suppress()
compositeLayup.CompositePly(suppressed=False, plyName='Ply-1', region=region1, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=1.0, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-2', region=region2, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=1.0, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-3', region=region3, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=1.0, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-4', region=region4, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=1.0, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-5', region=region5, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=1.0, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-6', region=region6, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=1.0, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-7', region=region7, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=1.0, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-8', region=region8, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=1.0, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.resume()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON, optimizationTasks=OFF, 
    geometricRestrictions=OFF, stopConditions=OFF)
mdb.models['Model-1'].FrequencyStep(name='Step-1', previous='Initial', 
    numEigen=10)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['Part-1']
a.Instance(name='Part-1-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.331143, 
    farPlane=0.5383, width=0.498169, height=0.257715, viewOffsetX=-0.0676408, 
    viewOffsetY=0.00666793)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.416912, 
    farPlane=0.566659, width=0.627199, height=0.324466, cameraPosition=(
    -0.0450685, -0.0681942, 0.459873), cameraUpVector=(0.450592, 0.892689, 
    0.00855825), cameraTarget=(0.0153769, 0.0675389, 0.0513316), 
    viewOffsetX=-0.0851603, viewOffsetY=0.00839499)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.290782, 
    farPlane=0.596912, width=0.437451, height=0.226304, cameraPosition=(
    0.087194, -0.340005, -0.0175053), cameraUpVector=(0.3936, 0.45046, 
    0.801352), cameraTarget=(0.0288502, 0.0895933, -0.0495084), 
    viewOffsetX=-0.0593965, viewOffsetY=0.00585523)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.34097, 
    farPlane=0.546723, width=0.0297824, height=0.0154072, 
    viewOffsetX=-0.0423346, viewOffsetY=0.0281745)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.342104, 
    farPlane=0.545589, width=0.0171219, height=0.00885761, 
    viewOffsetX=-0.0428503, viewOffsetY=0.0274352)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['Part-1-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#10280a02 #42 ]', ), )
e1 = a.instances['Part-1-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#2 ]', ), )
region = regionToolset.Region(edges=edges1, faces=faces1)
mdb.models['Model-1'].EncastreBC(name='BC-1', createStepName='Initial', 
    region=region, localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, interactions=ON, constraints=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
    interactions=OFF, constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.370089, 
    farPlane=0.499354, width=0.00979553, height=0.00507942, 
    viewOffsetX=0.00658038, viewOffsetY=0.0675686)
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
pickedRegions = c.getSequenceFromMask(mask=('[#ff ]', ), )
p.setMeshControls(regions=pickedRegions, technique=SWEEP, 
    algorithm=ADVANCING_FRONT)
p = mdb.models['Model-1'].parts['Part-1']
p.seedPart(size=0.005, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Part-1']
p.generateMesh()
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.359121, 
    farPlane=0.510322, width=0.14764, height=0.0765577, 
    viewOffsetX=-0.00978134, viewOffsetY=0.0539329)
elemType1 = mesh.ElemType(elemCode=SC8R, elemLibrary=STANDARD, 
    secondOrderAccuracy=OFF, hourglassControl=DEFAULT)
elemType2 = mesh.ElemType(elemCode=SC6R, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=UNKNOWN_TET, elemLibrary=STANDARD)
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#ff ]', ), )
pickedRegions =(cells, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
    elemType3))
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.338003, 
    farPlane=0.54969, width=0.0710712, height=0.0367669, 
    viewOffsetX=-0.0388048, viewOffsetY=0.0242057)
mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
del mdb.jobs['Job-1']
mdb.models.changeKey(fromName='Model-1', toName='No delamination')
a = mdb.models['No delamination'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.Job(name='Job-1', model='No delamination', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Job Job-1: Analysis Input File Processor completed successfully.
#: Job Job-1: Abaqus/Standard completed successfully.
#: Job Job-1 completed successfully. 
o3 = session.openOdb(
    name='D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d solid extrusion/Job-1.odb')
#: Model: D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d solid extrusion/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       9
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
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['No delamination'].parts['Part-1']
p.deleteMesh()
p = mdb.models['No delamination'].parts['Part-1']
p.seedPart(size=0.001, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['No delamination'].parts['Part-1']
p.generateMesh()
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON, mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
layupOrientation = None
p = mdb.models['No delamination'].parts['Part-1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#40 ]', ), )
region1 = regionToolset.Region(cells=cells)
p = mdb.models['No delamination'].parts['Part-1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#20 ]', ), )
region2 = regionToolset.Region(cells=cells)
p = mdb.models['No delamination'].parts['Part-1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#80 ]', ), )
region3 = regionToolset.Region(cells=cells)
p = mdb.models['No delamination'].parts['Part-1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#8 ]', ), )
region4 = regionToolset.Region(cells=cells)
p = mdb.models['No delamination'].parts['Part-1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#10 ]', ), )
region5 = regionToolset.Region(cells=cells)
p = mdb.models['No delamination'].parts['Part-1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#2 ]', ), )
region6 = regionToolset.Region(cells=cells)
p = mdb.models['No delamination'].parts['Part-1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#4 ]', ), )
region7 = regionToolset.Region(cells=cells)
p = mdb.models['No delamination'].parts['Part-1']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region8 = regionToolset.Region(cells=cells)
compositeLayup = mdb.models['No delamination'].parts['Part-1'].compositeLayups['CompositeLayup-1']
compositeLayup.orientation.setValues(additionalRotationType=ROTATION_NONE, 
    angle=0.0)
compositeLayup.deletePlies()
compositeLayup.suppress()
compositeLayup.CompositePly(suppressed=False, plyName='Ply-1', region=region1, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=1.0, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-2', region=region2, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=1.0, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-3', region=region3, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=1.0, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-4', region=region4, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=1.0, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-5', region=region5, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=1.0, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-6', region=region6, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=1.0, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-7', region=region7, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=1.0, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-8', region=region8, 
    material='Material-1', thicknessType=SPECIFY_THICKNESS, thickness=1.0, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
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
    name='D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d solid extrusion/Job-1.odb')
#: Model: D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis/3d solid extrusion/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       9
#: Number of Node Sets:          1
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
