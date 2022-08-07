# start it
mdb.models['Delamination-Case-2'].ConstrainedSketch(name='__edit__', 
    objectToCopy=
    mdb.models['Delamination-Case-2'].parts['Beam1'].features['Partition face-1'].sketch)
mdb.models['Delamination-Case-2'].parts['Beam1'].projectReferencesOntoSketch(
    filter=COPLANAR_EDGES, sketch=
    mdb.models['Delamination-Case-2'].sketches['__edit__'], upToFeature=
    mdb.models['Delamination-Case-2'].parts['Beam1'].features['Partition face-1'])


# delete ALL Diameter of rec
mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[32].getSize()
# 0.0724077345449619
mdb.models['Delamination-Case-2'].sketches['__edit__'].delete(objectList=(
    mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[32], ))

for i in mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry.keys():
     if abs(mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[i].getSize() - 0.0724077343935)<0.00001:
        mdb.models['Delamination-Case-2'].sketches['__edit__'].delete(objectList=(
        mdb.models['Delamination-Case-2'].sketches['__edit__'].geometry[i], ))

# put a line Diameters
mdb.models['Delamination-Case-2'].sketches['__edit__'].Line(point1=(-0.39, 0.3)
    , point2=(-0.3225, 0.225))

# finish section
mdb.models['Delamination-Case-2'].parts['Beam1'].features['Partition face-1'].setValues(
    sketch=mdb.models['Delamination-Case-2'].sketches['__edit__'])
del mdb.models['Delamination-Case-2'].sketches['__edit__']
mdb.models['Delamination-Case-2'].parts['Beam1'].regenerate()




# another example
mdb.models['Delamination-Case-3'].ConstrainedSketch(name='__edit__', 
    objectToCopy=
    mdb.models['Delamination-Case-3'].parts['Beam1'].features['Partition face-2'].sketch)
mdb.models['Delamination-Case-3'].sketches['__edit__'].delete(objectList=(
    mdb.models['Delamination-Case-3'].sketches['__edit__'].geometry[5], ))
mdb.models['Delamination-Case-3'].sketches['__edit__'].delete(objectList=(
    mdb.models['Delamination-Case-3'].sketches['__edit__'].geometry[4], ))
mdb.models['Delamination-Case-3'].sketches['__edit__'].Line(point1=(0.1024, 
    0.4608), point2=(0.1536, 0.512))
mdb.models['Delamination-Case-3'].sketches['__edit__'].Line(point1=(0.1024, 
    0.512), point2=(0.1536, 0.4608))
mdb.models['Delamination-Case-3'].parts['Beam1'].features['Partition face-2'].setValues(
    sketch=mdb.models['Delamination-Case-3'].sketches['__edit__'])
del mdb.models['Delamination-Case-3'].sketches['__edit__']
mdb.models['Delamination-Case-3'].parts['Beam1'].regenerate()