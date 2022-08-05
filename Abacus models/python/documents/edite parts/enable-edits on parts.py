mdb.models['Delamination-Case-2'].parts['Beam1'].features['Shell planar-1'].setValues(
    sketch=mdb.models['Delamination-Case-2'].sketches['__edit__'])
del mdb.models['Delamination-Case-2'].sketches['__edit__']

mdb.models['Delamination-Case-2'].parts['Beam1'].regenerate()