import time
from initial import initial
initial()
from delamination_hole_onBeam1 import move_delamination_onBeam1
from move_Beam1andBeam2 import moveBeam2
from edit_partitionOfBeam1 import EditPartitionBEam1
from edit_mesh import edit_mesh
from submit_TheJob import Submit_the_job
from copy_the_case_delamination1 import copy_the_caseDelamination1

# i = 91
for i in range(20, 101):
    # copy_the_caseDelamination1(i)
    # move_delamination_onBeam1(i)
    # moveBeam2(i)
    # EditPartitionBEam1(i)
    # edit_mesh(i)
    Submit_the_job(i)
    # time.sleep(1500)
