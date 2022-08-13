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
import glob
import csv


# historyRegions_keys = ["Node BEAM1-1.32", "Node BEAM1-1.70", 'Node BEAM1-1.74', 'Node BEAM1-1.108']

outputType = "V3"
for i in glob.glob("C:\\Users\\arshi\\OneDrive\\Desktop\\Delamination-detection-in-composite-laminates-using-deep-learning\\Abacus models\\Base Vibration for smaller parts/*.odb"):
    if "Job" in i:
        # print(i)
        num_job = int(i[i.find("Job-")+len("Job-"):i.find(".odb")])
        name = i[i.find("Job-"):]
        print(name)
        d = session.openOdb(name=name)
        outputs1 = d.steps['Step-1'].historyRegions[d.steps['Step-1'].historyRegions.keys()[0]].historyOutputs[outputType].data
        outputs2 = d.steps['Step-1'].historyRegions[d.steps['Step-1'].historyRegions.keys()[1]].historyOutputs[outputType].data
        outputs3 = d.steps['Step-1'].historyRegions[d.steps['Step-1'].historyRegions.keys()[2]].historyOutputs[outputType].data
        outputs4 = d.steps['Step-1'].historyRegions[d.steps['Step-1'].historyRegions.keys()[3]].historyOutputs[outputType].data
        for j in range(len(outputs1)):
            with open('C:/Users/arshi/OneDrive/Desktop/Delamination-detection-in-composite-laminates-using-deep-learning/Outputs-baseVibrationSmallerSize/{}-job-{}.csv'.format(outputType, num_job), 'a',) as file:
                writer = csv.writer(file)
                writer.writerow([outputs1[j][0], outputs1[j][1], outputs2[j][1], outputs3[j][1], outputs4[j][1]])