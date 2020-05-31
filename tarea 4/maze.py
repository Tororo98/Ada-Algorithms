from sys import stdin
from heapq import heappop, heappush

INF = float('inf')

def solve(G, source):
	time = [ INF for _ in G ] ; time[source] = 0
	visited = [ False for _ in G ]
	heap = [ (0, source) ]
	while len(heap)!=0:
		t,u = heappop(heap)
		if visited[u] == False:
			for v,tv in G[u]:
				if time[v]>t+tv:
					time[v] = t+tv
					heappush(heap, (time[v], v))
			visited[u] = True
	return time

def main():
	n = int(stdin.readline())
	for i in range(n):
		ans = 0
		stdin.readline()
		CELL = int(stdin.readline())			# cantidad de celdas
		GRAPH = [ list() for _ in range(CELL) ] 
		EX = int(stdin.readline()) - 1		# celda de la salida
		TIME = int(stdin.readline())			# tiempo límite
		CONN = int(stdin.readline())			# número de arcos / conexiones
		for j in range(CONN):
			u,v,d = map(int, stdin.readline().split())
			GRAPH[v-1].append((u-1,d))
			# print(GRAPH)
		m = solve(GRAPH,EX)
		# print(CONN)
		for k in m: ans = ans + 1 if k <= TIME else ans
		print(ans)
		if i != n-1:
			print()
main()