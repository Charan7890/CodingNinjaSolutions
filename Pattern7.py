Print the following pattern for a given n.
For eg. N = 6

123456
  23456
    3456
      456
        56
          6
        56
      456
    3456
  23456
123456

Sample Input 1 :

4

Sample Output 1 :

1234
  234
    34
      4
    34
  234
1234


CODE:

n = int(input())

k,x=0,n-1
for i in range(2*n-1):
    if i<=n-1:
        for s in range(i):
            print(" ",end="")

        for j in range(i+1,n+1):
            print(j,end="")
    else:
        for p in range(n-2-k):
            print(" ",end="")

        for q in range(x,n+1):
            print(q,end="")
        
        k+=1
        x-=1
    
    
        
    print()
