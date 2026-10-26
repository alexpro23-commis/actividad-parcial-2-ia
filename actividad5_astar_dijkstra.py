"""Actividad 5: A* vs Dijkstra sobre una red vial didáctica.
Los kilómetros son ficticios y no deben usarse para navegación real.
Requisito: pip install matplotlib
"""
import math,heapq
import matplotlib.pyplot as plt
P={"Atlautla":(0,0),"Ozumba":(2,1),"Amecameca":(4,3),"Chalco":(7,2),
"Ixtapaluca":(9,1),"Tlalmanalco":(5,5),"Cocotitlan":(7,5),"CDMX":(12,0)}
E=[("Atlautla","Ozumba",8),("Atlautla","Amecameca",14),("Ozumba","Amecameca",7),
("Ozumba","Tlalmanalco",12),("Amecameca","Tlalmanalco",6),("Amecameca","Chalco",16),
("Tlalmanalco","Cocotitlan",5),("Cocotitlan","Chalco",7),("Chalco","Ixtapaluca",8),
("Ixtapaluca","CDMX",22),("Chalco","CDMX",34),("Cocotitlan","Ixtapaluca",13),
("Tlalmanalco","Chalco",14),("Ozumba","Chalco",20)]
G={n:[] for n in P}
for u,v,w in E:G[u].append((v,w));G[v].append((u,w))
def heuristic(n,goal): return math.dist(P[n],P[goal])
def shortest(use_astar,src="Atlautla",goal="CDMX"):
 q=[(heuristic(src,goal) if use_astar else 0,0,src)]
 dist={src:0};parent={src:None};closed=set();expanded=0
 while q:
  _,g,u=heapq.heappop(q)
  if u in closed:continue
  closed.add(u);expanded+=1
  if u==goal:break
  for v,w in G[u]:
   ng=g+w
   if ng<dist.get(v,float("inf")):
    dist[v]=ng;parent[v]=u
    heapq.heappush(q,(ng+(heuristic(v,goal) if use_astar else 0),ng,v))
 path=[];x=goal
 while x is not None:path.append(x);x=parent[x]
 return path[::-1],dist[goal],expanded
def dashboard(a,d):
 fig,ax=plt.subplots(1,2,figsize=(9,4))
 ax[0].bar(["A*","Dijkstra"],[a[1],d[1]]);ax[0].set_title("Costo de ruta (km didácticos)")
 ax[1].bar(["A*","Dijkstra"],[a[2],d[2]]);ax[1].set_title("Nodos expandidos")
 fig.tight_layout();fig.savefig("A5_dashboard.png",dpi=170);plt.show()
if __name__=="__main__":
 a=shortest(True);d=shortest(False)
 print("A*:",a);print("Dijkstra:",d)
 print("Heurística: distancia euclidiana. Es admisible en este grafo didáctico porque cada peso de arista es al menos la distancia euclidiana entre sus extremos.")
 dashboard(a,d)
