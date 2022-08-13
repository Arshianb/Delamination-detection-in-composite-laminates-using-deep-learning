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

model_name = "Delamination-Case"
part_size = 250.0/1000
for i in range(38, 51):
    # copy_the_caseDelamination1(model_name, i)
    # move_delamination_onBeam1(model_name, i, part_size)
    # moveBeam2(model_name, i, part_size)
    # EditPartitionBEam1(model_name, i, part_size)
    # edit_mesh(i)
    # time.sleep(0.5)
    Submit_the_job(model_name, i)
    while os.path.exists('C:\\Users\\arshi\\OneDrive\\Desktop\\Delamination-detection-in-composite-laminates-using-deep-learning\\Abacus models\\Base Vibration for smaller parts/Job-{}.023'.format(i)) == False:
        time.sleep(0.1)
    while os.path.exists('C:\\Users\\arshi\\OneDrive\\Desktop\\Delamination-detection-in-composite-laminates-using-deep-learning\\Abacus models\\Base Vibration for smaller parts/Job-{}.023'.format(i)):
        time.sleep(0.1)


