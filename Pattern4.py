n = int(input())

x = 65
for i in range(n):
    for j in range(i+1):
        print(chr(x+j),end="")
    print()
    x+=1
    

Input: 5    
Output:
A
BC
CDE
DEFG
EFGHI
