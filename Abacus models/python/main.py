import time
from initial import initial
initial()
from delamination_hole_onBeam1 import move_delamination_onBeam1
from move_Beam1andBeam2 import moveBeam2
from edit_partitionOfBeam1 import EditPartitionBEam1
from edit_mesh import edit_mesh
from submit_TheJob import Submit_the_job
from copy_the_case_delamination1 import copy_the_caseDelamination1
import os
for i in range(1, 101):
    # copy_the_caseDelamination1(i)
    # move_delamination_onBeam1(i)
    # moveBeam2(i)
    # EditPartitionBEam1(i)
    # edit_mesh(i)
    # time.sleep(0.5)
    Submit_the_job(i)
    while os.path.exists('C:\\Users\\795593\\OneDrive\\Desktop\\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\\Base vibration model/Job-{}.023'.format(i)) == False:
        time.sleep(0.1)
    while os.path.exists('C:\\Users\\795593\\OneDrive\\Desktop\\Delamination-detection-in-composite-laminates-using-deep-learning\Abacus models\\Base vibration model/Job-{}.023'.format(i)):
        time.sleep(0.1)


