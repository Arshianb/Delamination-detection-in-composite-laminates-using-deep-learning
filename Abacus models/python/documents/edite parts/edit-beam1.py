mdb.models['Delamination-Case-2'].ConstrainedSketch(name='__edit__', 
    objectToCopy=
    mdb.models['Delamination-Case-2'].parts['Beam1'].features['Shell planar-1'].sketch)
mdb.models['Delamination-Case-2'].parts['Beam1'].projectReferencesOntoSketch(
    filter=COPLANAR_EDGES, sketch=
    mdb.models['Delamination-Case-2'].sketches['__edit__'], upToFeature=
    mdb.models['Delamination-Case-2'].parts['Beam1'].features['Shell planar-1'])




# another example
mdb.models['Delamination-Case-3'].ConstrainedSketch(name='__edit__', 
    objectToCopy=
    mdb.models['Delamination-Case-3'].parts['Beam1'].features['Shell planar-1'].sketch)
mdb.models['Delamination-Case-3'].parts['Beam1'].projectReferencesOntoSketch(
    filter=COPLANAR_EDGES, sketch=
    mdb.models['Delamination-Case-3'].sketches['__edit__'], upToFeature=
    mdb.models['Delamination-Case-3'].parts['Beam1'].features['Shell planar-1'])
mdb.models['Delamination-Case-3'].sketches['__edit__'].dimensions[5].setValues(
    value=0.128)
mdb.models['Delamination-Case-3'].parts['Beam1'].features['Shell planar-1'].setValues(
    sketch=mdb.models['Delamination-Case-3'].sketches['__edit__'])
del mdb.models['Delamination-Case-3'].sketches['__edit__']
mdb.models['Delamination-Case-3'].parts['Beam1'].regenerate()