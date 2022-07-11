fname = input()
fh = open(fname)
lst = list()
for line in fh:
    if not line.startswith('From '):
        continue
    k = line.split()
    f = k[1]
    lst.append(f)
dct = dict()
for mail in lst:
    if mail not in dct:
        dct[mail] = 1
    else:
        dct[mail] = dct[mail] + 1
ke = list(dct.keys())
val = list(dct.values())
pos = val.index(max(val))
print(ke[pos],val[pos])