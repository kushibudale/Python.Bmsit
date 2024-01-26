#Defined as a function F as Fn = Fn-1 + Fn-2. Write a Python program which accepts a value for N (where N >0) as input and pass this value to the function. Display suitable error message if the condition for input value is not followed.
def Fibonacci(n):
     fib_seq=[0,1]
     while len(fib_seq)<n:      
        fib_seq.append(fib_seq[-1]+fib_seq[-2])  
     return fib_seq
n=int(input('Enter the value of n:'))
if n<0:
    print('Invalid Input.Enter positive number:')
res=Fibonacci(n)
print(res)
