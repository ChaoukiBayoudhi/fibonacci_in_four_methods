import time
def multiply_matrix(A,B):
    #C=[[0,0],[0,0]] #in the case of Fibonacci
    C=[[0 for _ in range(len(B[0]))] for _ in range(len(A))] #initialize the matrix in the general case
    for i in range(len(A)):
        for j in range(len(B[i])):
            for k in range(len(B)):
                C[i][j]+=A[i][k]*B[k][j]
    return C


def power_matrix(M,n):
    result=[[1,0],[0,1]]
    while n>0:
        if n%2!=0:
            result=multiply_matrix(result,M)
        M=multiply_matrix(M,M)
        n//=2
    return result

#test
n=int(input("Enter a positive number : "))
start_time=time.time_ns()
result=power_matrix([[1,1],[1,0]],n-1)
print(result)
end_time=time.time_ns()

print(f'F({n}) = {result[0][0]}')

print(f"The calculation took {end_time-start_time} nanoseconds")
    
