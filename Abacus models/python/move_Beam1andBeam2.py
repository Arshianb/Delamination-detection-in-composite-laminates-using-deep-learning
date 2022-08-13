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


def moveBeam2(model_name, caseDelaminationNum=4, part_size = 250/1000):
    if caseDelaminationNum<11:
        mdb.models['{}-{}'.format(model_name,caseDelaminationNum)].rootAssembly.translate(instanceList=(
        'Beam2-1', ), vector=(part_size/10*(caseDelaminationNum-1), 0.0, 0.0))
        mdb.models['{}-{}'.format(model_name,caseDelaminationNum)].rootAssembly.translate(instanceList=(
        'Beam3-1', ), vector=(part_size/10*(caseDelaminationNum-1), 0.0, 0.0))
    if caseDelaminationNum>10:
        if caseDelaminationNum>10 and caseDelaminationNum<21:
            cte_num = caseDelaminationNum - 10
            cte_num2 = -1
        if caseDelaminationNum>20 and caseDelaminationNum<31:
            cte_num = caseDelaminationNum - 20
            cte_num2 = -2
        if caseDelaminationNum>30 and caseDelaminationNum<41:
            cte_num = caseDelaminationNum - 30
            cte_num2 = -3
        if caseDelaminationNum>40 and caseDelaminationNum<51:
            cte_num = caseDelaminationNum - 40
            cte_num2 = -4
        if caseDelaminationNum>50 and caseDelaminationNum<61:
            cte_num = caseDelaminationNum - 50
            cte_num2 = -5
        if caseDelaminationNum>60 and caseDelaminationNum<71:
            cte_num = caseDelaminationNum - 60
            cte_num2 = -6
        if caseDelaminationNum>70 and caseDelaminationNum<81:
            cte_num = caseDelaminationNum - 70
            cte_num2 = -7
        if caseDelaminationNum>80 and caseDelaminationNum<91:
            cte_num = caseDelaminationNum - 80
            cte_num2 = -8
        if caseDelaminationNum>90 and caseDelaminationNum<101:
            cte_num = caseDelaminationNum - 90
            cte_num2 = -9
        mdb.models['{}-{}'.format(model_name,caseDelaminationNum)].rootAssembly.translate(instanceList=(
        'Beam2-1', ), vector=(part_size/10*(cte_num-1), cte_num2*part_size/10, 0.0))
        mdb.models['{}-{}'.format(model_name,caseDelaminationNum)].rootAssembly.translate(instanceList=(
        'Beam3-1', ), vector=(part_size/10*(cte_num-1), cte_num2*part_size/10, 0.0))
    # if caseDelaminationNum>20 and caseDelaminationNum<31:
    #     cte_num = caseDelaminationNum - 20
    #     mdb.models['Delamination-Case-{}'.format(caseDelaminationNum)].rootAssembly.translate(instanceList=(
    #     'Beam2-1', ), vector=(0.0512*(cte_num-1), -2*0.0512, 0.0))
    #     mdb.models['Delamination-Case-{}'.format(caseDelaminationNum)].rootAssembly.translate(instanceList=(
    #     'Beam3-1', ), vector=(0.0512*(cte_num-1), -2*0.0512, 0.0))