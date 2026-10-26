"""Actividad 4: BFS y DFS en un laberinto. Python 3,"""
from collections import deque
import time
M=[[0,0,1,0,0,0,1],[1,0,1,0,1,0,1],[0,0,0,0,1,0,0],
   [0,1,1,0,0,0,1],[0,0,0,0,1,0,0],[1,1,0,0,0,0,1],[0,0,0,1,1,0,0]]
START=(0,0); GOAL=(6,6); MOVES=[(1,0),(-1,0),(0,1),(0,-1)]
def neighbors(p):
 r,c=p
 return [(r+dr,c+dc) for dr,dc in MOVES
         if 0<=r+dr<len(M) and 0<=c+dc<len(M[0]) and M[r+dr][c+dc]==0]
def restore(parent):
 path=[];p=GOAL
 while p is not None:path.append(p);p=parent[p]
 return path[::-1]
def bfs():
 frontier=deque([START]);parent={START:None};expanded=0
 while frontier:
  u=frontier.popleft();expanded+=1
  if u==GOAL:return restore(parent),expanded
  for v in neighbors(u):
   if v not in parent:parent[v]=u;frontier.append(v)
 return [],expanded
def dfs():
 frontier=[START];parent={START:None};expanded=0
 while frontier:
  u=frontier.pop();expanded+=1
  if u==GOAL:return restore(parent),expanded
  for v in reversed(neighbors(u)):
   if v not in parent:parent[v]=u;frontier.append(v)
 return [],expanded
if __name__=="__main__":
 for name,fn in [("BFS",bfs),("DFS",dfs)]:
  path,n=fn();t=time.perf_counter()
  for _ in range(250):fn()
  ms=(time.perf_counter()-t)*1000/250
  print(name,"ruta:",path,"pasos:",len(path)-1,"nodos expandidos:",n,"tiempo promedio ms:",round(ms,6))
