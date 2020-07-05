x = 10
y = 23
print("Before Swapping -> x -",x,"and y -",y)
def Swap(x,y):
    x = x + y   
    y = x - y  
    x = x - y
    return x, y

x, y = Swap(x,y)
print("After Swap -> x -",x,"and y -",y)
