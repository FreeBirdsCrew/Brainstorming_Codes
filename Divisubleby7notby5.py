# Divisile by 7 but Not by 5 in a Particular Range 

list=[]
for i in range(1, 1000):
    if (i%7==0) and (i%5!=0):
        list.append(str(i))

print ','.join(list)