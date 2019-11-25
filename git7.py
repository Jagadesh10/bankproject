Given 3 numbers A,B,C find if they can form the sides of a scalene triangle.
Input Size : A,B,C <= 100000
Sample Testcase :
INPUT
3 4 5
OUTPUT
yes

a,b,c=[int(x) for x in input().split()]
if a!=b and b!=c and c!=a:
	print("yes")
else:
	print("no")

