mdb.models['Delamination-Case-2'].ConstrainedSketch(name='__edit__', 
    objectToCopy=
    mdb.models['Delamination-Case-2'].parts['Beam1'].features['Shell planar-1'].sketch)
mdb.models['Delamination-Case-2'].parts['Beam1'].projectReferencesOntoSketch(
    filter=COPLANAR_EDGES, sketch=
    mdb.models['Delamination-Case-2'].sketches['__edit__'], upToFeature=
    mdb.models['Delamination-Case-2'].parts['Beam1'].features['Shell planar-1'])