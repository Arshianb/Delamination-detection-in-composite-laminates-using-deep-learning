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

def edit_mesh_with_meshNum(DelaminationCase = 4, i = 0.1, model_1_name = "mesh-Size"):
    mdb.models['{}-{}'.format(model_1_name, DelaminationCase)].parts['Beam1'].seedEdgeBySize(
        deviationFactor=0.1, edges=
        mdb.models['{}-{}'.format(model_1_name, DelaminationCase)].parts['Beam1'].edges.getSequenceFromMask(
        ('[#ffffffff:7 #f ]', ), ), minSizeFactor=0.1, size=i)
    mdb.models['{}-{}'.format(model_1_name, DelaminationCase)].parts['Beam1'].generateMesh()

    mdb.models['{}-{}'.format(model_1_name, DelaminationCase)].parts['Beam2'].seedEdgeBySize(constraint=
        FINER, deviationFactor=0.1, edges=
        mdb.models['{}-{}'.format(model_1_name, DelaminationCase)].parts['Beam2'].edges.getSequenceFromMask(
        ('[#ff ]', ), ), minSizeFactor=0.1, size=i)
    mdb.models['{}-{}'.format(model_1_name, DelaminationCase)].parts['Beam2'].generateMesh()

    mdb.models['{}-{}'.format(model_1_name, DelaminationCase)].parts['Beam3'].seedEdgeBySize(constraint=
        FINER, deviationFactor=0.1, edges=
        mdb.models['{}-{}'.format(model_1_name, DelaminationCase)].parts['Beam3'].edges.getSequenceFromMask(
        ('[#ff ]', ), ), minSizeFactor=0.1, size=i)
    mdb.models['{}-{}'.format(model_1_name, DelaminationCase)].parts['Beam3'].generateMesh()

    