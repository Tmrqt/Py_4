def sum(a,b):
    if b == 0:
        return 1
    else:
        return a+sum(1,b-1)

print(sum(12,7))