N = int(input())
frequencies = list(map(int, input().split()))
K = int(input())
keysize = list(map(int, input().split()))

frequencies.sort(reverse=True)
cost=[]

for i in range(K):
    for j in range(1,keysize[i]+1):
        cost.append(j)
cost.sort()

if(len(cost)<N):
    print(-1)
else:
    ans=0

    for i in range(N):
        ans+=frequencies[i]*cost[i] 
    print(ans)
