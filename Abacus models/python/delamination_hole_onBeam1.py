
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


def move_delamination_onBeam1(caseDelamination = 4):
    mdb.models['Delamination-Case-{}'.format(caseDelamination)].ConstrainedSketch(name='__edit__', 
        objectToCopy=
        mdb.models['Delamination-Case-{}'.format(caseDelamination)].parts['Beam1'].features['Shell planar-1'].sketch)
    mdb.models['Delamination-Case-{}'.format(caseDelamination)].parts['Beam1'].projectReferencesOntoSketch(
        filter=COPLANAR_EDGES, sketch=
        mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__'], upToFeature=
        mdb.models['Delamination-Case-{}'.format(caseDelamination)].parts['Beam1'].features['Shell planar-1'])
    for i in mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__'].dimensions.keys():
        if mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__'].dimensions[i].value == 0.0256:
            print("here1")
            mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__'].delete(objectList=(
                mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__'].dimensions[i], ))
            circle_index = 0
            origin_index = 0
            for j in mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__'].vertices.keys():
                if abs(mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__'].vertices[j].coords[0] - 0.0256
                )<0.0001 and abs(mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__'].vertices[j].coords[1] - 0.4864) < 0.0001:
                    print("here2")
                    circle_index = j
                if mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__'].vertices[j].coords == (0, 0):
                    print("here3")
                    origin_index = j
            mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__'].HorizontalDimension(
                textPoint=(0.00633746385574341, -0.0928356051445007), value=0.0256*(caseDelamination*2-1), 
                vertex1=mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__'].vertices[circle_index], 
                vertex2=mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__'].vertices[origin_index])
            mdb.models['Delamination-Case-{}'.format(caseDelamination)].parts['Beam1'].features['Shell planar-1'].setValues(
            sketch=mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__'])
            del mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__']
            mdb.models['Delamination-Case-{}'.format(caseDelamination)].parts['Beam1'].regenerate()
            break