fname = input('Enter the file name: ')
fh = open(fname)
lst = list()
for line in fh:
    if not line.startswith('From '):
        continue
    gh = line.rstrip()
    kh = gh.split()
    lh = kh[5]
    mh = lh.split(':')
    nh = mh[0]
    lst.append(nh)
counts = dict()
for word in lst:
    counts[word] = counts.get(word,0)+1
ij = counts.items()
lj = list(ij)
kj = sorted(lj)
for k,v in kj:
    print(k,v)