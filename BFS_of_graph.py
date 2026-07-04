class Solution:
    def bfs(self, adj):
        queu=[0]
        ans=[]
        is_visited=[False for _ in range(len(adj))]
        is_visited[0]=True
        while(len(queu)!=0):
            store=queu.pop(0)
            ans.append(store)
            for i in adj[store]:
                if not is_visited[i]:
                    queu.append(i)
                    is_visited[i]=True
        return ans
