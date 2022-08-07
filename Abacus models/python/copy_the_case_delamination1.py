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
def copy_the_caseDelamination1(NewCaseDelamination_num):
    mdb.Model(name='Delamination-Case-{}'.format(NewCaseDelamination_num), objectToCopy=
    mdb.models['Delamination-Case-1'])