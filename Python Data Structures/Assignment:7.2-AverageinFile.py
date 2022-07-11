fname = input("Enter file name: ")
fh = open(fname)
count = 0
tot = 0
f = None
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count+1
    f = line.rstrip()
    g = f.find(':')
    pos = f[g+1:]
    sval = pos.rstrip()
    fval = float(sval)
    tot = tot + fval
aspamc = tot/count
print('Average spam confidence:',aspamc)