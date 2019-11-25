Given a string s swap the even and odd characters.Assume the index starts from 0.
Input Size : |s| <= 10000000(complexity O(n))
Sample Testcase :
INPUT
codekata
OUTPUT
ocedakat

s = input()
y=''.join([ s[x:x+2][::-1] for x in range(0, len(s), 2) ])
print(y)
