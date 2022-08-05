# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-22.27.30 176069
# Run by arshi on Fri Aug  5 18:03:46 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=202.471450805664, 
    height=117.713539123535)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
openMdb(
    pathName='D:/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/Base vibration model/model num 1.cae')
#: The model database "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Model-1'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models.changeKey(fromName='Model-1', toName='Delamination-Case-1')
p = mdb.models['Delamination-Case-1'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.Model(name='Delamination-Case-2', 
    objectToCopy=mdb.models['Delamination-Case-1'])
#: The model "Delamination-Case-2" has been created.
p = mdb.models['Delamination-Case-2'].parts['Beam1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Delamination-Case-2'].parts['Beam1']
s = p.features['Shell planar-1'].sketch
mdb.models['Delamination-Case-2'].ConstrainedSketch(name='__edit__', 
    objectToCopy=s)
s1 = mdb.models['Delamination-Case-2'].sketches['__edit__']
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s1, 
    upToFeature=p.features['Shell planar-1'], filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.48418, 
    farPlane=1.85478, width=1.41761, height=0.679618, cameraPosition=(0.268651, 
    0.246191, 1.66948), cameraTarget=(0.268651, 0.246191, 0))
s1.unsetPrimaryObject()
del mdb.models['Delamination-Case-2'].sketches['__edit__']
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
p = mdb.models['Delamination-Case-2'].parts['Beam1']
s = p.features['Shell planar-1'].sketch
mdb.models['Delamination-Case-2'].ConstrainedSketch(name='__edit__', 
    objectToCopy=s)
s2 = mdb.models['Delamination-Case-2'].sketches['__edit__']
g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
s2.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s2, 
    upToFeature=p.features['Shell planar-1'], filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.60476, 
    farPlane=1.7342, width=0.495144, height=0.237377, cameraPosition=(0.117489, 
    0.417695, 1.66948), cameraTarget=(0.117489, 0.417695, 0))
s2.delete(objectList=(d[2], ))
s2.delete(objectList=(d[4], ))
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
s2.undo()
s2.undo()
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
s2.delete(objectList=(d[2], ))
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
cliCommand("""dimensions""")
#* NameError: name 'dimensions' is not defined
s2.undo()
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
s2.unsetPrimaryObject()
del mdb.models['Delamination-Case-2'].sketches['__edit__']
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
p = mdb.models['Delamination-Case-2'].parts['Beam1']
s = p.features['Shell planar-1'].sketch
mdb.models['Delamination-Case-2'].ConstrainedSketch(name='__edit__', 
    objectToCopy=s)
s1 = mdb.models['Delamination-Case-2'].sketches['__edit__']
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s1, 
    upToFeature=p.features['Shell planar-1'], filter=COPLANAR_EDGES)
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
s1.delete(objectList=(d[2], ))
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
cliCommand("""dimensions""")
#* NameError: name 'dimensions' is not defined
s1.undo()
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].delete(objectList=(
    mdb.models['Delamination-Case-2'].sketches['__edit__'].dimensions[2], ))""")
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].dimensions""")
#: mdb.models['Delamination-Case-2'].sketches['__edit__'].dimensions
cliCommand("""for i in mdb.models['Delamination-Case-2'].sketches['__edit__'].dimensions:
    print(i)
""")
#* TypeError: 'Repository' object is not iterable
cliCommand("""for i in mdb.models['Delamination-Case-2'].sketches['__edit__'].dimensions:



d""")
#*     d
#*     ^
#* IndentationError: expected an indented block
cliCommand("""for i in range(mdb.models['Delamination-Case-2'].sketches['__edit__'].dimensions)):""")
#*     for i in 
#* range(mdb.models['Delamination-Case-2'].sketches['__edit__'].dimensions)):
#*                                                                              
#*         ^
#* SyntaxError: invalid syntax
cliCommand("""for i in range(mdb.models['Delamination-Case-2'].sketches['__edit__'].dimensions):
    print(mdb.models['Delamination-Case-2'].sketches['__edit__'].dimensions[i])
""")
#* TypeError: range() integer end argument expected, got Repository.
cliCommand("""print(mdb.models['Delamination-Case-2'].sketches['__edit__'].dimensions)""")
#: {1: 'ConstrainedSketchDimension object', 4: 'ConstrainedSketchDimension object'}
cliCommand("""print(mdb.models['Delamination-Case-2'].sketches['__edit__'].dimensions[1])""")
#: ({'reference': OFF, 'value': 0.0256})
cliCommand("""print(mdb.models['Delamination-Case-2'].sketches['__edit__'].dimensions[2])""")
#* KeyError: 2
cliCommand("""print(mdb.models['Delamination-Case-2'].sketches['__edit__'].dimensions[4])""")
#: ({'reference': OFF, 'value': 0.02})
cliCommand("""for i in range(mdb.models['Delamination-Case-2'].sketches['__edit__'].dimensions):
    print(i)
""")
#* TypeError: range() integer end argument expected, got Repository.
cliCommand("""for i in mdb.models['Delamination-Case-2'].sketches['__edit__'].dimensions:
    print(i)
""")
#* TypeError: 'Repository' object is not iterable
cliCommand("""print(mdb.models['Delamination-Case-2'].sketches['__edit__'].dimensions)""")
#: {1: 'ConstrainedSketchDimension object', 4: 'ConstrainedSketchDimension object'}
cliCommand("""for i in mdb.models['Delamination-Case-2'].sketches['__edit__'].dimensions.keys():
    print(i)
""")
#: 1
#: 4
cliCommand("""for i in mdb.models['Delamination-Case-2'].sketches['__edit__'].dimensions.keys():
    print(mdb.models['Delamination-Case-2'].sketches['__edit__'].dimensions[i])
""")
#: ({'reference': OFF, 'value': 0.0256})
#: ({'reference': OFF, 'value': 0.02})
cliCommand("""for i in mdb.models['Delamination-Case-2'].sketches['__edit__'].dimensions.keys():
    print(mdb.models['Delamination-Case-2'].sketches['__edit__'].dimensions[i]['value'])
""")
#* TypeError: 'ConstrainedSketchDimension' object has no attribute '__getitem__'
cliCommand("""for i in mdb.models['Delamination-Case-2'].sketches['__edit__'].dimensions.keys():
    print(mdb.models['Delamination-Case-2'].sketches['__edit__'].dimensions[i]['value'])
""")
#* TypeError: 'ConstrainedSketchDimension' object has no attribute '__getitem__'
cliCommand("""for i in mdb.models['Delamination-Case-2'].sketches['__edit__'].dimensions.keys():
    print(mdb.models['Delamination-Case-2'].sketches['__edit__'].dimensions[i][0])
""")
#* TypeError: 'ConstrainedSketchDimension' object has no attribute '__getitem__'
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.51389, 
    farPlane=1.82507, width=1.05176, height=0.137692, cameraPosition=(0.055942, 
    0.476139, 1.66948), cameraTarget=(0.055942, 0.476139, 0))
cliCommand("""for i in mdb.models['Delamination-Case-2'].sketches['__edit__'].dimensions.keys():
    print(mdb.models['Delamination-Case-2'].sketches['__edit__'].dimensions[i].value)
""")
#: 0.0256
#: 0.02
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
s1.DistanceDimension(entity1=v[4], entity2=g[2], textPoint=(
    0.00760750845074654, 0.403899431228638), value=0.0512)
s1.undo()
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.61167, 
    farPlane=1.72729, width=0.390807, height=0.137275, cameraPosition=(
    0.0486053, 0.477569, 1.66948), cameraTarget=(0.0486053, 0.477569, 0))
s1.DistanceDimension(entity1=v[4], entity2=g[2], textPoint=(
    0.00478316470980644, 0.53359580039978), value=0.1024)
s1.undo()
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
s1.DistanceDimension(entity1=v[4], entity2=g[2], textPoint=(0.0112487189471722, 
    0.528191268444061), value=0.0768)
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices""")
#: mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices[0]""")
#: mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices[0]
cliCommand("""for i in mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices:
    print(i)
""")
#* TypeError: 'Repository' object is not iterable
cliCommand("""for i in mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices.keys:
    print(i)
""")
#* TypeError: 'AbaqusMethod' object is not iterable
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices""")
#: mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices
cliCommand("""for i in mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices.keys():
    print(i)
""")
#: 0
#: 1
#: 2
#: 3
#: 4
#: 5
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices[0].values""")
#* AttributeError: 'ConstrainedSketchVertex' object has no attribute 'values'
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices[0]""")
#: mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices[0]
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices.has_key()""")
#* TypeError: not all required arguments specified; expected 1, got 0
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices.items()""")
#: [(0, mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices[0]), (1, mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices[1]), (2, mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices[2]), (3, mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices[3]), (4, mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices[4]), (5, mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices[5])]
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices.findAt()""")
#* TypeError: not all required arguments specified; expected 1, got 0
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices.findAt(0)""")
#* TypeError: arg1; found int, expecting tuple
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices.findAt""")
#: <AbaqusMethod  mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices.findAt>
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices[0].coords""")
#: (0.0, 0.0)
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices[1].coords""")
#: (0.0, 0.512)
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices[2].coords""")
#: (0.512, 0.512)
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices[4].coords""")
#: (0.0768, 0.4864)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.58197, 
    farPlane=1.75699, width=0.591541, height=0.207785, cameraPosition=(
    0.0473024, 0.43739, 1.66948), cameraTarget=(0.0473024, 0.43739, 0))
s1.undo()
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices[4].coords""")
#: (0.0256, 0.4864)
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices[4].coords""")
#: (0.0256, 0.4864)
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[2]""")
#: mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[2]
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[2].getVertices""")
#: <AbaqusMethod  mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[2].getVertices>
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[2]""")
#: mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[2]
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[2].curveType""")
#: LINE
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[2].getPointAtDistance""")
#: <AbaqusMethod  mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[2].getPointAtDistance>
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[2].getPointAtDistance(0, 0)""")
#* TypeError: arg1; found int, expecting tuple
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[2].getPointAtDistance(0)""")
#* TypeError: arg1; found int, expecting tuple
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[2].getSize""")
#: <AbaqusMethod  mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[2].getSize>
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[2].getSize()""")
#: 0.512
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[2].getPointAtDistance()""")
#* TypeError: not all required arguments specified; expected 2, got 0
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[2].getPointAtDistance(0, 0)""")
#* TypeError: arg1; found int, expecting tuple
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[2].getPointAtDistance((0,0))""")
#* TypeError: not all required arguments specified; expected 2, got 1
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[2].getPointAtDistance((0,0), 0)""")
#: (0.0, 0.0)
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[2].getVertices()""")
#: (mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices[0], mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices[1])
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[2].pointOn""")
#: (0.0, 0.256)
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[2].pointOn""")
#: (0.0, 0.256)
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[2].pointOn""")
#: (0.0, 0.256)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.52159, 
    farPlane=1.81737, width=0.999712, height=0.351159, cameraPosition=(
    0.161395, 0.41959, 1.66948), cameraTarget=(0.161395, 0.41959, 0))
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[0].pointOn""")
#* KeyError: 0
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[1].pointOn""")
#* KeyError: 1
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry.keys""")
#: <AbaqusMethod  mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry.keys>
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry.keys()""")
#: [2, 3, 4, 5, 6]
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[3].pointOn""")
#: (0.256, 0.512)
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[3].id""")
#: 3
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[3].getPointAtDistance((0,0), 0)""")
#* The point provided must be the start or end vertex of the given sketch 
#* geometry object.
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[2].getPointAtDistance((0,0), 0)""")
#: (0.0, 0.0)
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[2].get""")
#* AttributeError: 'ConstrainedSketchGeometry' object has no attribute 'get'
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[2].getVertices()mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[2].getVertices()""")
#*     
#* mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[2].getVertices()mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[2].getVertices()
#*                                                                              
#*          ^
#* SyntaxError: invalid syntax
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[2].getVertices()""")
#: (mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices[0], mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices[1])
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.54664, 
    farPlane=1.79231, width=0.93973, height=0.33009, cameraPosition=(0.149773, 
    0.403444, 1.66948), cameraTarget=(0.149773, 0.403444, 0))
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.29074, 
    farPlane=2.04821, width=2.89748, height=1.01777, cameraPosition=(0.435101, 
    0.269127, 1.66948), cameraTarget=(0.435101, 0.269127, 0))
s1.HorizontalDimension(vertex1=v[4], vertex2=v[0], textPoint=(
    0.00633746385574341, -0.0928356051445007), value=0.0768)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.52875, 
    farPlane=1.81021, width=0.951311, height=0.334157, cameraPosition=(
    0.185455, 0.420411, 1.66948), cameraTarget=(0.185455, 0.420411, 0))
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices[0].coords""")
#: (0.0, 0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.37378, 
    farPlane=1.96518, width=2.26221, height=0.794624, cameraPosition=(0.295729, 
    0.28305, 1.66948), cameraTarget=(0.295729, 0.28305, 0))
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.54513, 
    farPlane=1.79383, width=0.840579, height=0.295262, cameraPosition=(
    0.144635, 0.42603, 1.66948), cameraTarget=(0.144635, 0.42603, 0))
s1.delete(objectList=(d[1], ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.28451, 
    farPlane=2.05445, width=2.94519, height=1.15129, cameraPosition=(0.444182, 
    0.169704, 1.66948), cameraTarget=(0.444182, 0.169704, 0))
s1.VerticalDimension(vertex1=v[4], vertex2=v[0], textPoint=(-0.219027519226074, 
    0.164273634552956), value=0.4864)
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.43385, 
    farPlane=1.90511, width=1.80264, height=0.704659, cameraPosition=(0.316276, 
    0.370206, 1.66948), cameraTarget=(0.316276, 0.370206, 0))
s1.unsetPrimaryObject()
p = mdb.models['Delamination-Case-2'].parts['Beam1']
p.features['Shell planar-1'].setValues(sketch=s1)
del mdb.models['Delamination-Case-2'].sketches['__edit__']
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
p = mdb.models['Delamination-Case-2'].parts['Beam1']
p.regenerate()
#: Warning: Mesh deleted in 5 regions due to geometry association failure.
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
p = mdb.models['Delamination-Case-2'].parts['Beam1']
s = p.features['Partition face-1'].sketch
mdb.models['Delamination-Case-2'].ConstrainedSketch(name='__edit__', 
    objectToCopy=s)
s2 = mdb.models['Delamination-Case-2'].sketches['__edit__']
g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
s2.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s2, 
    upToFeature=p.features['Partition face-1'], filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.33158, 
    farPlane=1.56473, width=0.788025, height=0.308042, cameraPosition=(
    0.153922, 0.397643, 1.44815), cameraTarget=(0.153922, 0.397643, 0))
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
s2.delete(objectList=(g[32], ))
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
s2.undo()
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[32]""")
#: mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[32]
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[32].curveType""")
#: LINE
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[32].getPointAtDistance((0,0))""")
#* TypeError: not all required arguments specified; expected 2, got 1
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[32].getPointAtDistance((0,0), 1)""")
#* The point provided must be the start or end vertex of the given sketch 
#* geometry object.
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[32].getPointAtDistance((0,0.512), 1)""")
#* The point provided must be the start or end vertex of the given sketch 
#* geometry object.
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[32].getPointAtDistance((0,0.0512), 1)""")
#* The point provided must be the start or end vertex of the given sketch 
#* geometry object.
cliCommand("""mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[32].getSize()""")
#: 0.0724077345449619
cliCommand("""len(mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry.keys())""")
#: 21
cliCommand("""for i in mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry.keys():
    print(mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[i].getSize())
""")
#: 0.511999999991
#: 0.511999999991
#: 0.511999999991
#: 0.511999999991
#: 0.511999999991
#: 0.511999999991
#: 0.511999999991
#: 0.511999999991
#: 0.511999999991
#: 0.511999999991
#: 0.511999999991
#: 0.511999999991
#: 0.511999999991
#: 0.511999999991
#: 0.511999999991
#: 0.511999999991
#: 0.511999999991
#: 0.511999999991
#: 0.0724077343935
#: 0.072407734545
#: 0.125663706144
s2.undo()
cliCommand("""for i in mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry.keys():
    if abs(mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[i].getSize() - 0.0724077343935)<0.00001:
        mdb.models['Delamination-Case-2'].sketches['__edit__'].delete(objectList=(
    mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[i], ))
""")
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.34787, 
    farPlane=1.54844, width=0.677945, height=0.212509, cameraPosition=(
    0.134748, 0.421151, 1.44815), cameraTarget=(0.134748, 0.421151, 0))
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
s2.Line(point1=(-0.20591, 0.25711), point2=(-0.15471, 0.20591))
s2.CoincidentConstraint(entity1=v[54], entity2=g[8], addUndoState=False)
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
s2.Line(point1=(-0.20591, 0.20591), point2=(-0.15471, 0.25711))
s2.CoincidentConstraint(entity1=v[55], entity2=g[27], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.43702, 
    farPlane=1.45929, width=0.0851537, height=0.0266923, cameraPosition=(
    0.0596515, 0.461325, 1.44815), cameraTarget=(0.0596515, 0.461325, 0))
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.37193, 
    farPlane=1.52438, width=0.583142, height=0.182792, cameraPosition=(
    0.126461, 0.498825, 1.44815), cameraTarget=(0.126461, 0.498825, 0))
s2.undo()
s2.undo()
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
s2.Line(point1=(-0.39, 0.3), point2=(-0.3225, 0.225))
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
s2.delete(objectList=(g[33], ))
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
s2.Line(point1=(-0.20591, 0.20591), point2=(-0.15471, 0.25711))
s2.CoincidentConstraint(entity1=v[56], entity2=g[27], addUndoState=False)
s2.Line(point1=(-0.20591, 0.25711), point2=(-0.15471, 0.20591))
s2.CoincidentConstraint(entity1=v[57], entity2=g[8], addUndoState=False)
s2.unsetPrimaryObject()
p = mdb.models['Delamination-Case-2'].parts['Beam1']
p.features['Partition face-1'].setValues(sketch=s2)
del mdb.models['Delamination-Case-2'].sketches['__edit__']
p = mdb.models['Delamination-Case-2'].parts['Beam1']
s = p.features['Partition face-1'].sketch
mdb.models['Delamination-Case-2'].ConstrainedSketch(name='__edit__', 
    objectToCopy=s)
s1 = mdb.models['Delamination-Case-2'].sketches['__edit__']
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s1, 
    upToFeature=p.features['Partition face-1'], filter=COPLANAR_EDGES)
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
s1.unsetPrimaryObject()
del mdb.models['Delamination-Case-2'].sketches['__edit__']
p = mdb.models['Delamination-Case-2'].parts['Beam1']
p.regenerate()
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
p = mdb.models['Delamination-Case-2'].parts['Beam1']
s = p.features['Partition face-1'].sketch
mdb.models['Delamination-Case-2'].ConstrainedSketch(name='__edit__', 
    objectToCopy=s)
s2 = mdb.models['Delamination-Case-2'].sketches['__edit__']
g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
s2.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s2, 
    upToFeature=p.features['Partition face-1'], filter=COPLANAR_EDGES)
s2.unsetPrimaryObject()
del mdb.models['Delamination-Case-2'].sketches['__edit__']
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
p = mdb.models['Delamination-Case-2'].parts['Beam1']
s = p.features['Partition face-1'].sketch
mdb.models['Delamination-Case-2'].ConstrainedSketch(name='__edit__', 
    objectToCopy=s)
s1 = mdb.models['Delamination-Case-2'].sketches['__edit__']
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s1, 
    upToFeature=p.features['Partition face-1'], filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.36691, 
    farPlane=1.5294, width=0.549192, height=0.240504, cameraPosition=(0.15419, 
    0.432052, 1.44815), cameraTarget=(0.15419, 0.432052, 0))
s1.delete(objectList=(g[35], ))
s1.delete(objectList=(g[34], ))
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
s1.unsetPrimaryObject()
p = mdb.models['Delamination-Case-2'].parts['Beam1']
p.features['Partition face-1'].setValues(sketch=s1)
del mdb.models['Delamination-Case-2'].sketches['__edit__']
p = mdb.models['Delamination-Case-2'].parts['Beam1']
p.regenerate()
p = mdb.models['Delamination-Case-2'].parts['Beam1']
s = p.features['Partition face-1'].sketch
mdb.models['Delamination-Case-2'].ConstrainedSketch(name='__edit__', 
    objectToCopy=s)
s2 = mdb.models['Delamination-Case-2'].sketches['__edit__']
g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
s2.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s2, 
    upToFeature=p.features['Partition face-1'], filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.36691, 
    farPlane=1.5294, width=0.549192, height=0.240504, cameraPosition=(0.163442, 
    0.424538, 1.44815), cameraTarget=(0.163442, 0.424538, 0))
s2.Line(point1=(-0.20591, 0.20591), point2=(-0.15471, 0.25711))
s2.CoincidentConstraint(entity1=v[60], entity2=g[27], addUndoState=False)
s2.Line(point1=(-0.20591, 0.25711), point2=(-0.15471, 0.20591))
s2.CoincidentConstraint(entity1=v[61], entity2=g[8], addUndoState=False)
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
cliCommand("""del mdb.models['Delamination-Case-2'].sketches['__edit__']""")
cliCommand("""mdb.models['Delamination-Case-2'].parts['Beam1'].regenerate()""")
#: 1
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.27662, 
    farPlane=1.61969, width=1.30294, height=0.570587, viewOffsetX=0.0782083, 
    viewOffsetY=-0.0268761)
p = mdb.models['Delamination-Case-2'].parts['Beam1']
s = p.features['Partition face-1'].sketch
mdb.models['Delamination-Case-2'].ConstrainedSketch(name='__edit__', 
    objectToCopy=s)
s1 = mdb.models['Delamination-Case-2'].sketches['__edit__']
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s1, 
    upToFeature=p.features['Partition face-1'], filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.3708, 
    farPlane=1.52551, width=0.522903, height=0.228991, cameraPosition=(
    0.145395, 0.409175, 1.44815), cameraTarget=(0.145395, 0.409175, 0))
s1.Line(point1=(-0.20591, 0.20591), point2=(-0.15471, 0.25711))
s1.CoincidentConstraint(entity1=v[60], entity2=g[27], addUndoState=False)
s1.Line(point1=(-0.20591, 0.25711), point2=(-0.15471, 0.20591))
s1.CoincidentConstraint(entity1=v[61], entity2=g[8], addUndoState=False)
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
s1.unsetPrimaryObject()
p = mdb.models['Delamination-Case-2'].parts['Beam1']
p.features['Partition face-1'].setValues(sketch=s1)
del mdb.models['Delamination-Case-2'].sketches['__edit__']
p = mdb.models['Delamination-Case-2'].parts['Beam1']
p.regenerate()
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
p = mdb.models['Delamination-Case-2'].parts['Beam1']
s = p.features['Partition face-1'].sketch
mdb.models['Delamination-Case-2'].ConstrainedSketch(name='__edit__', 
    objectToCopy=s)
s2 = mdb.models['Delamination-Case-2'].sketches['__edit__']
g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
s2.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s2, 
    upToFeature=p.features['Partition face-1'], filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.26655, 
    farPlane=1.62976, width=1.38933, height=0.60842, cameraPosition=(0.28158, 
    0.257439, 1.44815), cameraTarget=(0.28158, 0.257439, 0))
s2.delete(objectList=(g[38], ))
s2.delete(objectList=(g[37], ))
cliCommand("""mdb.models['Delamination-Case-2'].parts['Beam1'].features['Partition face-1'].setValues(
    sketch=mdb.models['Delamination-Case-2'].sketches['__edit__'])""")
#: 1
cliCommand("""del mdb.models['Delamination-Case-2'].sketches['__edit__']""")
cliCommand("""mdb.models['Delamination-Case-2'].parts['Beam1'].regenerate()""")
#: 1
p = mdb.models['Delamination-Case-2'].parts['Beam1']
s = p.features['Partition face-1'].sketch
mdb.models['Delamination-Case-2'].ConstrainedSketch(name='__edit__', 
    objectToCopy=s)
s1 = mdb.models['Delamination-Case-2'].sketches['__edit__']
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s1, 
    upToFeature=p.features['Partition face-1'], filter=COPLANAR_EDGES)
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.35621, 
    farPlane=1.5401, width=0.621539, height=0.272186, cameraPosition=(0.174706, 
    0.397328, 1.44815), cameraTarget=(0.174706, 0.397328, 0))
s1.Line(point1=(-0.20591, 0.20591), point2=(-0.15471, 0.25711))
s1.CoincidentConstraint(entity1=v[64], entity2=g[27], addUndoState=False)
s1.Line(point1=(-0.20591, 0.25711), point2=(-0.15471, 0.20591))
s1.CoincidentConstraint(entity1=v[65], entity2=g[8], addUndoState=False)
s1.unsetPrimaryObject()
p = mdb.models['Delamination-Case-2'].parts['Beam1']
p.features['Partition face-1'].setValues(sketch=s1)
del mdb.models['Delamination-Case-2'].sketches['__edit__']
p = mdb.models['Delamination-Case-2'].parts['Beam1']
p.regenerate()
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.28597, 
    farPlane=1.61034, width=1.23236, height=0.507866, viewOffsetX=0.0834849, 
    viewOffsetY=0.044237)
mdb.save()
#: The model database has been saved to "D:\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\Base vibration model\model num 1.cae".
p = mdb.models['Delamination-Case-2'].parts['Beam2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Delamination-Case-2'].parts['Beam3']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
