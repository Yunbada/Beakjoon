#첫째 줄: 컴퓨터 수 (N<=100)
#둘째 줄: 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
#셋째 줄 부터: 네트워크상에서 직접 연결되어있는 컴퓨터 번호 쌍
#[입력]
#7
#6
#1 2
#2 3
#1 5
#5 2
#5 6
#4 7
#[출력]
#4
from collections import deque

n = int(input())
m = int(input())

#양방향 간선만들기
graph = [[] for _ in range(n+1)]
for i in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
    
#bfs 너비우선탐색 사용
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not (visited[i]):
                queue.append(i)
                visited[i] = True
                
                
                
cnt = 0
visited = [False] * (n+1)

for i in range(1,n+1):
    if not visited[i]:
        bfs(graph, i, visited)
        
        
print(cnt)