import re
fname = input("Enter the file name :")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    temp = re.findall('[0-9]+',line)
    if temp == [] :
        continue
    lst = lst + temp
count = 0
for val in lst:
    count = count + int(val)
print(count)