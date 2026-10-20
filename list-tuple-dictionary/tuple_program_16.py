# Tuple Program 16
st = ('Pen', 'Marker', 'Pencil', 'Eraser', 'Scale')
rev = ()
for s in st:
    rev = rev + (s[::-1],)
print(rev)
