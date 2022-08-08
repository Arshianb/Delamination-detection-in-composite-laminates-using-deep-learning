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


def edit_mesh(DelaminationCase = 4):
    mdb.models['Delamination-Case-{}'.format(DelaminationCase)].parts['Beam1'].setMeshControls(regions=
        mdb.models['Delamination-Case-{}'.format(DelaminationCase)].parts['Beam1'].faces.getSequenceFromMask(
        ('[#ffffffff:3 #7f ]', ), ), technique=SWEEP)


    mdb.models['Delamination-Case-{}'.format(DelaminationCase)].parts['Beam1'].generateMesh()