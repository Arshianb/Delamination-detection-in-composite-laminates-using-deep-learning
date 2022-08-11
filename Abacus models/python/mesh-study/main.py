from math import floor
import time
from initial import initial
initial()
from delamination_hole_onBeam1 import move_delamination_onBeam1
from move_Beam1andBeam2 import moveBeam2
from edit_partitionOfBeam1 import EditPartitionBEam1
from edit_mesh import edit_mesh, edit_mesh_with_meshNum
from submit_TheJob import Submit_the_job
from copy_the_case_delamination1 import copy_the_caseDelamination1, copy_the_caseDelamination1_ForModealAnalysis
import numpy as np
from intraction import Intraction
import os
# i = 91
index = 1
# for i in np.arange(0.1, 0.001, 1000):
last_mesh = 0

for i in np.linspace(0.04, 0.005, 10000):
    
    current_mesh = round(0.0512/i)
    if current_mesh!=last_mesh:
        print("i = ", i)
        file = open("text.txt", "a") 
        copy_the_caseDelamination1_ForModealAnalysis(index)
        edit_mesh_with_meshNum(index, i)
        Intraction(index, i)
        Submit_the_job(index)
        # time.sleep(5)
        while os.path.exists('C:\\Users\\795593\OneDrive\\Desktop\\Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/Mesh study/Job-{}.023'.format(index)) == False:
            time.sleep(0.1)
        while os.path.exists('C:\\Users\\795593\OneDrive\\Desktop\\Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/Mesh study/Job-{}.023'.format(index)):
            time.sleep(0.1)
            # print(os.path.exists('C:/Users/795593/OneDrive/Desktop/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/modal analysis Project/Job-{}.023'.format(index)))
        index = index + 1
        file.write("index = {} and i = {} \n".format(index, i)) 
        file.close()
        last_mesh = round(0.0512/i)