n = int(input())

x = 65

for i in range(n):
    for j in range(i+1):
        if i==0:
            print(chr(x),end="")
        else:
            print(chr(x+i),end="")
    print()
    
    
Input:
4

Output:
 A
 BB
 CCC
 DDDD
