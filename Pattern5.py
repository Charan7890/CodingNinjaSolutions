n = int(input())

x = 64 + n

for i in range(n):
    for j in range(i+1):
        print(chr(x+j),end="")
    print()
    x-=1
    
Input: 4
  
Output:
D
CD
BCD
ABCD
