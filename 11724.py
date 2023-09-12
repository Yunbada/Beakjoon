#정점의 개수 N 간선 M
#M개의 줄에 간선의 양 끝점 u 와 v 가 주어짐 같은 간선은 한번만 주어짐
#첫째 줄에 연결 요소의 개수를 출력(연결요소란 그래프의 개수 또는 영역의 개수)
#[입력]
#6 5
#1 2
#2 5
#5 1
#3 4
#4 6
#[출력]
#2

#DFS or BFS 사용 

from collections import deque
import time
#런타임 에러 발생하기 때문에 재귀횟수 임의로 지정
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(graph, start, visited):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not (visited[i]):
                queue.append(i)
                visited[i] = True
                
    
#n,m을 받고 graph 를 만들기 위해 작업
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

#연결 요소의 개수는 cnt로 확인
cnt = 0
#정점+1개만큼 False생성 서로 인접할 경우 생각
visited = [False] * (n+1)

st = time.time()
for i in range(1, n+1):
    if not visited[i]:
        dfs(graph, i, visited)
        cnt += 1
et = time.time()

tt=et-st
print(cnt,tt)
#시간상 DFS가 더 빠름 
#맞았습니다!

        