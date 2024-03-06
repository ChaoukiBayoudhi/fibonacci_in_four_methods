import time
#def Fib_bottom_up(n):
    
def Fib_bottom_up(n: int)->int:
    if n<=1:
        return n
    (f1,f2)=(0,1)
    #for x in range(2,n+1):
    for _ in range(2,n+1): #_ is used when the counter is not used inside the loop
        f1,f2=f2,f1+f2
    return f2

#test
n=int(input('Enter a positive integer: '))

start_time = time.time_ns()
result = Fib_bottom_up(n)
end_time = time.time_ns()

print(f'f({n}) = {result}')
print(f'Execution time: {end_time-start_time} ns')

        