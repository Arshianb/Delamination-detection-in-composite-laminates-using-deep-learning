

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


def Intraction(model_1_name = "", DelaminationCase = 4, i = 0.1):

    mdb.models['{}-{}'.format(model_1_name, DelaminationCase)].constraints['Constraint-1'].setValues(
        positionTolerance=i)

    mdb.models['{}-{}'.format(model_1_name, DelaminationCase)].constraints['Constraint-2'].setValues(
        positionTolerance=i)   