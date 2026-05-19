infile = open('/Users/dechakool/infile/ID.txt', 'r')
n = int(infile.readline())
s = 0
for k in range(n) :
    sid, sc = infile.readline().strip().split()
    s += float(sc)
print("number =", n)
print("avg =", s/n)

