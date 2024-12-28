#without recursion

def generate_fibonacci_series(terms):
    a, b = 0, 1
    for _ in range(terms):
        print(a, end=" ")
        a, b = b, a + b

n_terms = 10  
generate_fibonacci_series(n_terms)


#Using recursion

def fibonacci_series(n, a=0, b=1):
    if n == 0:
        return
    print(a, end=" ")
    fibonacci_series(n - 1, b, a + b)

n_terms = 10  
fibonacci_series(n_terms)


#using recursion 2

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def generate_fibonacci_series(terms):
    for i in range(terms):
        print(fibonacci(i), end=" ")

n_terms = 10
generate_fibonacci_series(n_terms)
