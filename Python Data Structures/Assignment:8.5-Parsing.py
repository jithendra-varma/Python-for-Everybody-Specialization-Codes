fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith('From '):
        continue
    count = count + 1
    b = line.split()
    c = b[1]
    print(c)
print("There were", count, "lines in the file with From as the first word")