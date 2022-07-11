# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
go = fh.read()
rf = go.upper()
print(rf.rstrip())