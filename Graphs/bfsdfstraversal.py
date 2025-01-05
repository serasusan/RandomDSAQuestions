from collections import deque
class Solution:
    def dfsOfGraph(self, V, adj):
        vis = [0]*V
        ans = []

        for i in range(V):
            if vis[i]!=1:
                self.dfs(i,adj,vis,ans)
        return ans
        
    def bfsOfGraph(self, V, adj):
        vis = [0]*V
        ans = []

        for i in range(V):
            if vis[i]!=1:
                self.bfs(i,adj,vis,ans)
        return ans
    def dfs(self,node,adj,vis,ans):
        vis[node]=1
        ans.append(node)

        for neighbour in adj[node]:
            if not vis[neighbour]:
                self.dfs(neighbour,adj,vis,ans)
    def bfs(self,node, adj,vis, ans):
        vis[node]=1
        q = deque()
        q.append(node)

        while q:
            i = q.popleft()

            ans.append(i)

            for neighbour in adj[i]:
                if not vis[neighbour]:
                    vis[neighbour]=1
                    q.append(neighbour)
