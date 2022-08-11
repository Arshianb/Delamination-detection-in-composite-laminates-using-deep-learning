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
def initial(path = "C:/Users/795593/OneDrive/Desktop/Delamination-detection-in-composite-laminates-using-deep-learning/Abacus models/python"):
	sys.path.insert(1, path)