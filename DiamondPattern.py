## Read input as specified in the question.
## Print output as specified in the question.

n = int(input())
l=[]
z=[]
for i in range(n):
    for j in range(n//2-i):
        print(" ",end="")
        l.append(" ")
    if i<=n//2:
        for k in range(2*i+1):
            print("*",end="")
            l.append("*")
            m = l.copy()
        print()
        z.append(m)
        l.clear()
a = n - len(z)
z = z[:a]       
# print(z)
z.reverse()
# print(z)


for x in range(a):
    for y in range(len(z[x])):
        print(z[x][y],end="")
        # ind+=1
      
    print()
        
QUESTION:
  
Print the following pattern for the given number of rows.
Note: N is always odd.


Pattern for N = 5


The dots represent spaces.



Input format :

N (Total no. of rows and can only be odd)

Output format :

Pattern in N lines

Constraints :

1 <= N <= 49

Sample Input 1:

5

Sample Output 1:

  *
 ***
*****
 ***
  *

Sample Input 2:

3

Sample Output 2:

  *
 ***
  *

