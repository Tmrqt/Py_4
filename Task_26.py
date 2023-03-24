def func(a,b):
    if b > 0:
        if b == 1:
            return a
        else:
            return a*func(a,b-1)
    else:
        if abs(b) == 1:
            return 1/a
        else:
            return (1/a)*func(a,b+1)


print(func(3,-2))
