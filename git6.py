Given 3 numbers A,B,C.Print yes if they can form the sides of a triangle otherwise no.
Input Size : A,B,C <= 100000
Sample Testcase :
INPUT
3 4 5
OUTPUT
yes

def checkValidity(a, b, c):   
    if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
        return False
    else: 
        return True         
a = int(input())
b = int(input())
c = int(input())
if checkValidity(a, b, c): 
    print("yes")  
else: 
    print("no") 
