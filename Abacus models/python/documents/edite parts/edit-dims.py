import mdb

for i in mdb.models['Delamination-Case-2'].sketches['__edit__'].dimensions.keys():
    print(mdb.models['Delamination-Case-2'].sketches['__edit__'].dimensions[i].value)

mdb.models['Delamination-Case-2'].sketches['__edit__'].delete(objectList=(
    mdb.models['Delamination-Case-2'].sketches['__edit__'].dimensions[2], ))

# output is center of the circle
mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices[4].coords


# attention to HorizontalDimension and VerticalDimension
mdb.models['Delamination-Case-2'].sketches['__edit__'].HorizontalDimension(
    textPoint=(0.00633746385574341, -0.0928356051445007), value=0.0768, 
    vertex1=mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices[4], 
    vertex2=mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices[0])

mdb.models['Delamination-Case-2'].sketches['__edit__'].VerticalDimension(
    textPoint=(-0.219027519226074, 0.164273634552956), value=0.4864, vertex1=
    mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices[4], 
    vertex2=mdb.models['Delamination-Case-2'].sketches['__edit__'].vertices[0])

