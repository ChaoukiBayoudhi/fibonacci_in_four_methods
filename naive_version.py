import time
def fibonacci_naive(n):
    if n<=1:
        return n
    return fibonacci_naive(n-1) + fibonacci_naive(n-2)

#test
n=int(input('Enter a positive integer: '))
start_time = time.time_ns()
result = fibonacci_naive(n)
end_time = time.time_ns()
#print('f(',n,')=',fibonacci_naive(n))
print(f'f({n}) = {result}')
print(f'Execution time: {end_time-start_time} ns')
#print('f(%d) = %d'%(n,fibonacci_naive(n)))