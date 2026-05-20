infile = open('/Users/dechakool/infile/ID.txt', 'r')
n = int(infile.readline())
s = 0
for k in range(n) :
    sid, sc = infile.readline().strip().split()
    s += float(sc)
print("number =", n)
print("avg =", s/n)
for k in range(n) :
    sid, sc = infile.readline().strip().split()
    if float(sc) > s/n :
        print(sid, sc)
a = infile.readline().strip()
if a == 'A' :   
    print("A")
elif a == 'B' :
    print("B")
elif a == 'C' :
    print("C")
elif a == 'D' :
    print("D")
else :   
    print("F")
infile.close()
