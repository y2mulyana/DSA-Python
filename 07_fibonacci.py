# Iteration method
def fibonacci(n):
    p, c = 0, 1 # p = previous value, c = current value
    if n < 2:
        print(n)
        return n
    else:
        for i in range(2, n+1):
            a = p # a catch old p before update
            p = c # previous value (p) updated with old current value(c)
            c += a # current value (c) updated with (old p)
    print(c)
    return c
    
    
"""
# Memoization method
def fibonacci(n, start_point = {0:0, 1:1}):
    
    if n in start_point:
        print(start_point[n])
        return start_point[n]
    else:
        start_point[n] = fibonacci(n-1, start_point) + fibonacci(n-2, start_point)
        print(start_point[n])
        return start_point[n]
    

# Recursion method
def fibonacci(n):
    if n < 2:
        return n
    else:
        a = fibonacci(n-1) + fibonacci(n-2)
        print(a)
        return a
"""
    
fibonacci(0) # 6 should be 8