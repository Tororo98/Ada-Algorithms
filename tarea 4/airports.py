#Solving the airports problem
#By Sebastian Toro
#Based on the code found at: http://www.camilorocha.info/teaching/ada/2019-1

from sys import stdin

class dforest(object):
  """implements an union-find with path-compression and ranking"""

  def __init__(self, size=100):
    self.__parent = [ i for i in range(size) ]
    self.__rank = [ 1 for _ in range(size) ]
    self.__csize = [ 1 for _ in range(size) ]
    self.__ccnt = self.__size = size

  def __str__(self):
    """return the string representation of the forest"""
    return str(self.__parent)

  def __len__(self):
    """return the number of elements in the forest"""
    return self.__size

  def ccnt(self):
    """return  the numnber of components"""
    return self.__ccnt

  def csize(self, x):
    """return the number of elements in the component of x"""
    return self.__csize[self.find(x)]
  
  def find(self, x):
    """return the representative of the component of x"""
    if self.__parent[x]!=x:
      self.__parent[x] = self.find(self.__parent[x])
    return self.__parent[x]
  
  def union(self, x, y):
    """computes the union of the components of x and y, if they are different"""
    fx,fy = self.find(x),self.find(y)
    if fx!=fy:
      rx,ry = self.__rank[fx],self.__rank[fy]
      if rx>=ry:
        self.__parent[fy] = fx
        self.__csize[fx] += self.__csize[fy]
        if rx==ry:
          self.__rank[fy] += 1        
      else:
        self.__parent[fx] = fy
        self.__csize[fy] += self.__csize[fx]
      self.__ccnt -= 1

dfo = None

def kruskal(graph, lenv,A):
  global dfo
  ans = list()
  graph.sort(key = lambda x: x[2])
  dfo,i = dforest(lenv),0
  while i!=len(graph):
    u,v,dist = graph[i]
    if dfo.find(u)!=dfo.find(v) and dist<A:         #Here I see weight as distance for better comprehension of statement
      ans.append((u, v, dist))
      dfo.union(u, v)
    i += 1
  return ans
    
def main():
  global dfo
  n = int(stdin.readline())
  for i in range(n):
    # A : what costs me to build an airport
    N,M,A = map(int,stdin.readline().split())
    G = list() ; cnt,a = 0,0
    for k in range(M):
      # c : what costs me to build a road
      x,y,c = map(int,stdin.readline().split())
      G.append((x-1,y-1,c))  
    ans = kruskal(G,N,A)
    for j in range(N):
      if j==dfo.find(j): a+=1
    for j in range(len(ans)): cnt += ans[j][2]
    cnt += a*A
    print("Case #{0}: {1} {2}".format(i+1, cnt,a))
  return
main()