n = int(input())

for i in range(n):
    for j in range(i+1):
        if i==0 or i==1:
            print(1,end="")
        else:
            if(i>1 and ((j==i) or (j==0))):
                print(i,end="")
            else:
                print(0,end="")
    print()
    
    
Input:5   
output:
1
11
202
3003
40004
   
