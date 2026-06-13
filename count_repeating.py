mat=[[1, 2, 1, 4, 8],
       [3, 7, 8, 5, 1],
       [8, 7, 7, 3, 1],
       [8, 1, 2, 7, 9]]

dp=dict()
for i in range(len(mat[0])):
    dp[mat[0][i]]=1

for i in range(len(mat)):
    for j in range(len(mat[0])):
        if(mat[i][j] in dp and dp[mat[i][j]]==i):
            dp[mat[i][j]]+=1
for i,j in dp.items():
    if (j==4):
        print(i)
