inFp = None
inStr = ""
inFp = open("file/data1.txt", "r")
inStr = inFp.readline()
print(inStr, end="")

inStr = inFp.readline()
print(inStr, end="")
inStr = inFp.readline()
print(inStr, end="")

inFp.close()