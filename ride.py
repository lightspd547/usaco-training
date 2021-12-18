"""
ID: lsun0541
LANG: PYTHON2
TASK: ride
"""

fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')

g = fin.readline()
u = fin.readline()
#test
value_g = 1
value_u = 1
for x in g:
    v = (ord(x) - 64)
    if v > 0:
        value_g *= v
for x in u:
    v = (ord(x) - 64)
    if v > 0:
        value_u *= v
if (value_g % 47 == value_u % 47):
    fout.write("GO\n")
else:
    fout.write("STAY\n")

fin.close()
fout.close()