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


def EditPartitionBEam1(DelaminationCase = 4):
    try:
        mdb.models['Delamination-Case-{}'.format(DelaminationCase)].ConstrainedSketch(name='__edit__', 
            objectToCopy=
            mdb.models['Delamination-Case-{}'.format(DelaminationCase)].parts['Beam1'].features['Partition face-2'].sketch)
        mdb.models['Delamination-Case-{}'.format(DelaminationCase)].sketches['__edit__'].delete(objectList=(
            mdb.models['Delamination-Case-{}'.format(DelaminationCase)].sketches['__edit__'].geometry[4], 
            mdb.models['Delamination-Case-{}'.format(DelaminationCase)].sketches['__edit__'].geometry[5]))
    except:
        pass
    if DelaminationCase < 11:
        mdb.models['Delamination-Case-{}'.format(DelaminationCase)].sketches['__edit__'].Line(point1=(0.0512*(DelaminationCase-1), 
            0.4608), point2=(0.0512*(DelaminationCase), 0.4608 + 0.0512))
        mdb.models['Delamination-Case-{}'.format(DelaminationCase)].sketches['__edit__'].Line(point1=(0.0512*(DelaminationCase-1), 
            0.4608 + 0.0512), point2=(0.0512*(DelaminationCase), 0.4608))

    if DelaminationCase < 21 and DelaminationCase > 10:
        cte_num = DelaminationCase - 10
        cte_num2 = 8
    if DelaminationCase < 31 and DelaminationCase > 20:
        cte_num = DelaminationCase - 20
        cte_num2 = 7
    if DelaminationCase < 41 and DelaminationCase > 30:
        cte_num = DelaminationCase - 30
        cte_num2 = 6
    if DelaminationCase < 51 and DelaminationCase > 40:
        cte_num = DelaminationCase - 40
        cte_num2 = 5
    if DelaminationCase < 61 and DelaminationCase > 50:
        cte_num = DelaminationCase - 50
        cte_num2 = 4
    if DelaminationCase < 71 and DelaminationCase > 60:
        cte_num = DelaminationCase - 60
        cte_num2 = 3
    if DelaminationCase < 81 and DelaminationCase > 70:
        cte_num = DelaminationCase - 70
        cte_num2 = 2
    if DelaminationCase < 91 and DelaminationCase > 80:
        cte_num = DelaminationCase - 80
        cte_num2 = 1
    if DelaminationCase < 101 and DelaminationCase > 90:
        cte_num = DelaminationCase - 90
        cte_num2 = 0
    if DelaminationCase > 10:
        mdb.models['Delamination-Case-{}'.format(DelaminationCase)].sketches['__edit__'].Line(point1=(0.0512*(cte_num-1), 
            (cte_num2)*0.0512), point2=(0.0512*(cte_num), (cte_num2)*0.0512 + 0.0512))
        mdb.models['Delamination-Case-{}'.format(DelaminationCase)].sketches['__edit__'].Line(point1=(0.0512*(cte_num-1), 
            (cte_num2)*0.0512 + 0.0512), point2=(0.0512*(cte_num), (cte_num2)*0.0512))
    mdb.models['Delamination-Case-{}'.format(DelaminationCase)].parts['Beam1'].features['Partition face-2'].setValues(
        sketch=mdb.models['Delamination-Case-{}'.format(DelaminationCase)].sketches['__edit__'])
    del mdb.models['Delamination-Case-{}'.format(DelaminationCase)].sketches['__edit__']
    mdb.models['Delamination-Case-{}'.format(DelaminationCase)].parts['Beam1'].regenerate()