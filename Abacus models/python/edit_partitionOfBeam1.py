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


def EditPartitionBEam1(model_name, DelaminationCase = 4, part_size = 250/1000):
    try:
        mdb.models['{}-{}'.format(model_name,DelaminationCase)].ConstrainedSketch(name='__edit__', 
            objectToCopy=
            mdb.models['{}-{}'.format(model_name,DelaminationCase)].parts['Beam1'].features['Partition face-2'].sketch)
        mdb.models['{}-{}'.format(model_name,DelaminationCase)].sketches['__edit__'].delete(objectList=(
            mdb.models['{}-{}'.format(model_name,DelaminationCase)].sketches['__edit__'].geometry[2], 
            mdb.models['{}-{}'.format(model_name,DelaminationCase)].sketches['__edit__'].geometry[3]))
    except:
        pass
    if DelaminationCase < 11:
        mdb.models['{}-{}'.format(model_name,DelaminationCase)].sketches['__edit__'].Line(point1=(part_size/10*(DelaminationCase-1), 
            9*part_size/10), point2=(part_size/10*(DelaminationCase), 9*part_size/10 + part_size/10))
        mdb.models['{}-{}'.format(model_name,DelaminationCase)].sketches['__edit__'].Line(point1=(part_size/10*(DelaminationCase-1), 
            9*part_size/10 + part_size/10), point2=(part_size/10*(DelaminationCase), 0.9*part_size))

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
        mdb.models['{}-{}'.format(model_name,DelaminationCase)].sketches['__edit__'].Line(point1=(part_size/10*(cte_num-1), 
            (cte_num2)*part_size/10), point2=(part_size/10*(cte_num), (cte_num2)*part_size/10 + part_size/10))
        mdb.models['{}-{}'.format(model_name,DelaminationCase)].sketches['__edit__'].Line(point1=(part_size/10*(cte_num-1), 
            (cte_num2)*part_size/10+ part_size/10), point2=(part_size/10*(cte_num), (cte_num2)*part_size/10))
    mdb.models['{}-{}'.format(model_name,DelaminationCase)].parts['Beam1'].features['Partition face-2'].setValues(
        sketch=mdb.models['{}-{}'.format(model_name,DelaminationCase)].sketches['__edit__'])
    del mdb.models['{}-{}'.format(model_name,DelaminationCase)].sketches['__edit__']
    mdb.models['{}-{}'.format(model_name,DelaminationCase)].parts['Beam1'].regenerate()