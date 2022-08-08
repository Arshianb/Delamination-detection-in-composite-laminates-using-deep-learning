
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
        try:
            if mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__'].dimensions[i].value == 0.0256:
                mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__'].delete(objectList=(
                    mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__'].dimensions[i], ))
            # else:
            if abs(mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__'].dimensions[i].value - (0.0512*9+0.0256)) < 0.0001:
                mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__'].delete(objectList=(
                    mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__'].dimensions[i], ))
        except:
            pass
    circle_index = 0
    origin_index = 0

    for j in mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__'].vertices.keys():
        if abs(mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__'].vertices[j].coords[0] - 0.0256
        )<0.0001 and abs(mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__'].vertices[j].coords[1] - 0.4864) < 0.0001:
            circle_index = j
        if mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__'].vertices[j].coords == (0, 0):
            origin_index = j
    if caseDelamination>10:
        if caseDelamination>10 and caseDelamination<21:
            cte_num2 = 8
        if caseDelamination>20 and caseDelamination<31:
            cte_num2 = 7
        if caseDelamination>30 and caseDelamination<41:
            cte_num2 = 6
        if caseDelamination>40 and caseDelamination<51:
            cte_num2 = 5
        if caseDelamination>50 and caseDelamination<61:
            cte_num2 = 4
        if caseDelamination>60 and caseDelamination<71:
            cte_num2 = 3
        if caseDelamination>70 and caseDelamination<81:
            cte_num2 = 2
        if caseDelamination>80 and caseDelamination<91:
            cte_num2 = 1
        if caseDelamination>90 and caseDelamination<101:
            cte_num2 = 0
    mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__'].VerticalDimension(
        textPoint=(0.00633746385574341, -0.0928356051445007), value=(cte_num2*0.0512+0.0256), 
        vertex1=mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__'].vertices[circle_index], 
        vertex2=mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__'].vertices[origin_index])

    if caseDelamination < 11:
        cte_num = caseDelamination
    if caseDelamination > 10 and caseDelamination < 21:
        cte_num = caseDelamination-10
    if caseDelamination > 20 and caseDelamination < 31:
        cte_num = caseDelamination-20
    if caseDelamination > 30 and caseDelamination < 41:
        cte_num = caseDelamination-30
    if caseDelamination > 40 and caseDelamination < 51:
        cte_num = caseDelamination-40
    if caseDelamination > 50 and caseDelamination < 61:
        cte_num = caseDelamination-50
    if caseDelamination > 60 and caseDelamination < 71:
        cte_num = caseDelamination-60
    if caseDelamination > 70 and caseDelamination < 81:
        cte_num = caseDelamination-70
    if caseDelamination > 80 and caseDelamination < 91:
        cte_num = caseDelamination-80
    if caseDelamination > 90 and caseDelamination < 101:
        cte_num = caseDelamination-90
    mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__'].HorizontalDimension(
        textPoint=(0.00633746385574341, -0.0928356051445007), value=0.0256*(cte_num*2-1), 
        vertex1=mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__'].vertices[circle_index], 
        vertex2=mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__'].vertices[origin_index])
    mdb.models['Delamination-Case-{}'.format(caseDelamination)].parts['Beam1'].features['Shell planar-1'].setValues(
    sketch=mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__'])
    del mdb.models['Delamination-Case-{}'.format(caseDelamination)].sketches['__edit__']
    mdb.models['Delamination-Case-{}'.format(caseDelamination)].parts['Beam1'].regenerate()
