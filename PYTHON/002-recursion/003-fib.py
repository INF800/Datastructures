

def func(n):
    if n==1:
        return 1
    if n==2:
        return 2
    
    prev = func(n-1)
    next = func(n-2)
    return (prev + next)

n=7
print(func(n-1))