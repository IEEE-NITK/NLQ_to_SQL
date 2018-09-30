# n fibinocci numbers

def fib(n):
    if n>1:
        A[1]=1
    for i in range(n):
        if(i<2):
            continue
        A[i]=A[i-1]+A[i-2]

n=int(input("enter n:"))
A=[0]*n
fib(n)
for i in range(n):
    print(A[i],end=" ")