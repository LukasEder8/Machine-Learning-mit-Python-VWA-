# -*- coding: utf-8 -*-
#!/urs/bin/python

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib_array = []
for i in range(0, 11):
    fib_array.append(fib(i))
    
print(fib_array)
    
    