fname = input("Enter file name:")
fh = open(fname)
c = list()
for line in fh:
    a = line.rstrip()
    b = a.split()
    c = c + b
lst = list()
for w in c:
    if w not in lst:
        lst.append(w)
lst.sort()
print(lst)