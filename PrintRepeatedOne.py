def most_common(lst):
    return max(lst, key=lst.count)

list = ["ram","ram","ram","sham","mohann"]
print(most_common(list))
