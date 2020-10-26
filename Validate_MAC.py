def isMAC48Address(inputString):
    if inputString.count(":")!=5:
        return False
    for i in inputString.split(":"):
        for j in i:
            if j>"F" or (j<"A" and not j.isdigit()) or len(i)!=2:
                return False
    return True 

print(isMAC48Address("a0:12:90:00:80:43"))
