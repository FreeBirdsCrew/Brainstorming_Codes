# program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.

values=raw_input()
l=values.split(",")
t=tuple(l)
print l
print t