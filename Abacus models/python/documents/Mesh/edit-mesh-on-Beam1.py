# make all sweep type elements
mdb.models['Delamination-Case-2'].parts['Beam1'].setMeshControls(regions=
    mdb.models['Delamination-Case-2'].parts['Beam1'].faces.getSequenceFromMask(
    ('[#ffffffff:3 #7f ]', ), ), technique=SWEEP)


mdb.models['Delamination-Case-2'].parts['Beam1'].seedEdgeBySize(deviationFactor=0.1, edges=
    mdb.models['Delamination-Case-2'].parts['Beam1'].surfaces['surf 0,1']
    , minSizeFactor=0.1, size=1)