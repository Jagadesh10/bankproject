Given 2 numbers N and M add both the numbers and check whether the sum is odd or even.
Sample Testcase :
INPUT
9 2
OUTPUT
odd

x,y=input().split()
x=int(x)
y=int(y)
z=x+y
if(z%2==0):
  print("even")
else:
  print("odd")
