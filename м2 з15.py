fib_cache = {}

def fibonacci(n):
    if n in fib_cache:
        return fib_cache[n]
    
    if n == 1 or n == 2:
        result = 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
    
    fib_cache[n] = result
    return result

n = int(input())

# вычисляем n-е число Фибоначчи и выводим его
print(fibonacci(n))