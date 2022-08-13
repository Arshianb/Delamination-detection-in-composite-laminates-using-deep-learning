# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-22.27.30 176069
# Run by arshi on Sat Aug 13 12:03:36 2022
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
    pathName='C:/Users/arshi/OneDrive/Desktop/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/Base vibration model/main-model.cae')
#: The model database "C:\Users\arshi\OneDrive\Desktop\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\main-model.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Delamination-Case-1'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Delamination-Case-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
o3 = session.openOdb(
    name='C:/Users/arshi/OneDrive/Desktop/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/Base Vibration for smaller parts/Job-1.odb')
#: Model: C:/Users/arshi/OneDrive/Desktop/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/Base Vibration for smaller parts/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     3
#: Number of Meshes:             3
#: Number of Element Sets:       5
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.497145, 
    farPlane=0.954772, width=0.566353, height=0.226537, viewOffsetX=0.0276173, 
    viewOffsetY=0.0344526)
o1 = session.openOdb(
    name='C:/Users/arshi/OneDrive/Desktop/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/Base vibration model/Job-1.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: C:/Users/arshi/OneDrive/Desktop/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/Base vibration model/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     3
#: Number of Meshes:             3
#: Number of Element Sets:       5
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.10982, 
    farPlane=1.86342, width=0.49194, height=0.196772, viewOffsetX=-0.0865392, 
    viewOffsetY=0.151602)
o1 = session.openOdb(
    name='C:/Users/arshi/OneDrive/Desktop/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/be careful/Job-1.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: C:/Users/arshi/OneDrive/Desktop/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/be careful/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     3
#: Number of Meshes:             3
#: Number of Element Sets:       5
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
p = mdb.models['Delamination-Case-1'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
openMdb(
    pathName='C:/Users/arshi/OneDrive/Desktop/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/Base Vibration for smaller parts/main-model.cae')
#: The model database "C:\Users\arshi\OneDrive\Desktop\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base Vibration for smaller parts\main-model.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
a = mdb.models['Delamination-Case-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
p = mdb.models['Delamination-Case-46'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
a = mdb.models['Delamination-Case-46'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Delamination-Case-46'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.503972, 
    farPlane=0.947944, width=0.522762, height=0.209964, 
    viewOffsetX=-0.00310664, viewOffsetY=0.00467694)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Delamination-Case-46'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Delamination-Case-1'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Delamination-Case-1'].parts['Beam2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Delamination-Case-1'].parts['Beam3']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.Viewport(name='Viewport: 2', origin=(122.515, -2.27344), width=122.515, 
    height=98.0104)
session.viewports['Viewport: 1'].restore()
session.viewports['Viewport: 1'].setValues(origin=(0, -2.27344), width=122.515, 
    height=98.0104)
p = mdb.models['Delamination-Case-1'].parts['Beam3']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#8 ]', ), )
region = regionToolset.Region(faces=faces)
detp = section.MdbPlyStackPlot(part=p, region=region)
session.viewports['Viewport: 2'].setValues(displayedObject=detp)
session.viewports['Viewport: 2'].viewportAnnotationOptions.setValues(
triadColor='Yellow', triadLabels=NUMBERS)
session.viewports['Viewport: 2'].view.setViewpoint(viewVector=(1, -1, 1), 
    cameraUpVector=(0, 0, 1))
session.viewports['Viewport: 2'].view.setValues(nearPlane=2.22896, 
    farPlane=5.30916, width=1.76534, height=1.32436, viewOffsetX=0.0403166, 
    viewOffsetY=-0.0212046)
p = mdb.models['Delamination-Case-1'].parts['Beam2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.Viewport(name='Viewport: 3', origin=(122.515, -2.27344), width=122.515, 
    height=98.0104)
session.viewports['Viewport: 1'].restore()
session.viewports['Viewport: 1'].setValues(origin=(0, -2.27344), width=122.515, 
    height=98.0104)
p = mdb.models['Delamination-Case-1'].parts['Beam2']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#2 ]', ), )
region = regionToolset.Region(faces=faces)
detp = section.MdbPlyStackPlot(part=p, region=region)
session.viewports['Viewport: 3'].setValues(displayedObject=detp)
session.viewports['Viewport: 3'].viewportAnnotationOptions.setValues(
triadColor='Yellow', triadLabels=NUMBERS)
session.viewports['Viewport: 3'].view.setViewpoint(viewVector=(1, -1, 1), 
    cameraUpVector=(0, 0, 1))
session.viewports['Viewport: 3'].view.setValues(nearPlane=2.22896, 
    farPlane=5.30916, width=1.76534, height=1.32436, viewOffsetX=0.0122298, 
    viewOffsetY=-0.00628549)
p = mdb.models['Delamination-Case-1'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del session.viewports['Viewport: 3']
del session.viewports['Viewport: 2']
session.viewports['Viewport: 1'].maximize()
a = mdb.models['Delamination-Case-1'].rootAssembly
a.regenerate()
a = mdb.models['Delamination-Case-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, 
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.573144, 
    farPlane=0.878772, width=0.0502418, height=0.0200963, 
    viewOffsetX=-0.0588104, viewOffsetY=0.106369)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    renderBeamProfiles=ON, renderShellThickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.57038, 
    farPlane=0.881536, width=0.0744554, height=0.0297816, 
    viewOffsetX=-0.0516805, viewOffsetY=0.105867)
a = mdb.models['Delamination-Case-1'].rootAssembly
f1 = a.instances['Beam2-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#f ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Delamination-Case-1'].rootAssembly
f1 = a.instances['Beam3-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#f ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.556014, 
    farPlane=0.895902, width=0.153129, height=0.0612503, viewOffsetX=-0.043303, 
    viewOffsetY=0.100821)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Delamination-Case-1'].rootAssembly
f1 = a.instances['Beam1-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#0 #200600 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
a = mdb.models['Delamination-Case-1'].rootAssembly
f1 = a.instances['Beam1-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#80000007 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.573699, 
    farPlane=0.878218, width=0.0458365, height=0.0183343, 
    viewOffsetX=-0.0602103, viewOffsetY=0.10906)
p = mdb.models['Delamination-Case-1'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Delamination-Case-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.573222, 
    farPlane=0.878694, width=0.0487218, height=0.0194883, 
    viewOffsetX=-0.058632, viewOffsetY=0.108514)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.504639, 
    farPlane=0.947277, width=0.520154, height=0.208058, viewOffsetX=0.0546163, 
    viewOffsetY=0.0285615)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
import sys
sys.path.insert(8, 
    r'c:/SIMULIA/EstProducts/2022/win_b64/code/python2.7/lib/abaqus_plugins/amplitudePlotter')
import amplitudeTools
amplitudeTools.plotAmplitudes(amplitudeNameList=(('Amp-1', ), ), needXmin=0, 
    needXmax=0, needSaveXYPlot=0, displayLegend=1, applySmoothingFactor=0)
del session.viewports['Viewport: Amplitude Plotter']
session.viewports['Viewport: 1'].makeCurrent()
del session.xyPlots['Amplitude Plotter-1']
del session.xyDataObjects['_temp_ap_Amp-1']
session.viewports['Viewport: 1'].view.setValues(width=0.548702, 
    height=0.219477, viewOffsetX=0.063614, viewOffsetY=0.0229928)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.526639, 
    farPlane=0.925277, width=0.330893, height=0.132901, viewOffsetX=0.00882539, 
    viewOffsetY=0.0566231)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/arshi/OneDrive/Desktop/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/be careful/Job-1.odb'])
o3 = session.openOdb(
    name='C:/Users/arshi/OneDrive/Desktop/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/Base Vibration for smaller parts/Job-1.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=TIME_HISTORY)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.487822, 
    farPlane=0.964095, width=0.575032, height=0.230008, viewOffsetX=0.0013037, 
    viewOffsetY=0.0084746)
odb = session.odbs['C:/Users/arshi/OneDrive/Desktop/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/Base Vibration for smaller parts/Job-1.odb']
xy1 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Spatial acceleration: A3 PI: BEAM1-1 Node 32 in NSET OUTPUTS', 
    steps=('Step-1', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c1 = session.Curve(xyData=xy1)
xyp = session.XYPlot('XYPlot-1')
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
odb = session.odbs['C:/Users/arshi/OneDrive/Desktop/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/Base Vibration for smaller parts/Job-1.odb']
xy1 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Spatial acceleration: A3 PI: BEAM1-1 Node 70 in NSET OUTPUTS', 
    steps=('Step-1', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c1 = session.Curve(xyData=xy1)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
mdb.save()
#: The model database has been saved to "C:\Users\arshi\OneDrive\Desktop\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base Vibration for smaller parts\main-model.cae".
