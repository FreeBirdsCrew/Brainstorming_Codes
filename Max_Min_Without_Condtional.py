def Maximum(a,b,c):
    maxx = a
    if maxx < b:
        maxx = b
    if maxx < c:
        maxx = c

    return maxx;

def Minimum(a,b,c):
    minn = a
    if minn > b:
        minn = b
    if minn > c:
        minn = c

    return minn;


print(Maximum(2,33,5))
print(Minimum(2,1,32))
