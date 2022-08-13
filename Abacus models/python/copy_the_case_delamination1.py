import sys
import os

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
def copy_the_caseDelamination1(model_name, NewCaseDelamination_num):
    mdb.Model(name='{}-{}'.format(model_name, NewCaseDelamination_num), objectToCopy=
    mdb.models['{}-1'.format(model_name)])


def copy_the_caseDelamination1_ForModealAnalysis(NewCaseDelamination_num, model_1_name):
    mdb.Model(name='{}-{}'.format(model_1_name, NewCaseDelamination_num), objectToCopy=
    mdb.models['{}-1'.format(model_1_name)])