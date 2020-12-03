i,k,Line=0,0,""

for i in range(2,10):
    Line = Line + ("#    %d단   #" % i)

print(Line)

for i in range(1,10):
    Line = ""
    for k in range(2,10):
        Line = Line + str("%2d X %2d = %2d" % (k, i, k*i))
    print(Line)