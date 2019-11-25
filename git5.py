Given a number N, find its factorial.
Input Size : N <= 20
Sample Testcase :
INPUT
5
OUTPUT
120

def factorial(n):
  return 1 if (n==1 or n==0) else n * factorial(n-1);
num=int(input())
a=factorial(num)
print(a)
