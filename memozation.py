import time
def fibonacci_mem(n, memo={}):
    if n<=1:
        return n
    if n in memo:
        return memo[n]
    memo[n]=fibonacci_memo(n-1,memo)+fibonacci_memo(n-2,memo)
    return memo[n]


#test
n=int(input('Enter a positive integer: '))

start_time = time.time_ns()
result = fibonacci_memo(n)
end_time = time.time_ns()

print(f'f({n}) = {result}')
print(f'Execution time: {end_time-start_time} ns')
