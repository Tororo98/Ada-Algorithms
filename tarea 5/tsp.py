#solving collecting beepers problem
#using hamiltonian path algorithm 
#Highly based on the TSP problem
#Sebastian Toro

from sys import stdin
import time

INF = float("inf")

# def tsp_bf(v,A,vs):
# 	ans = INF
# 	if A == (1<<n)-1:
# 		ans = adj[v][vs]
# 	else:
# 		for i in range(n):
# 			if i != v and (A&(1<<i))==0:
# 				ans = min(ans,adj[v][i]+tsp_bf(i,(A | (1<<i)),vs))
# 	return ans

def tsp_dp(v,A,vs,adj):
	ans = INF
	if (v,A) in memo:
		ans = memo[(v,A)]
	else:
		if A == (1<<n+1)-1:
			ans = adj[v][vs]
		else:
			for i in range(n+1):
				if i != v and (A&(1<<i))==0:
					ans = min(ans,adj[v][i]+tsp_dp(i,(A | (1<<i)),vs,adj))
		memo[(v,A)] = ans
	return ans		


def main():
	global n,memo
	memo = dict()
	# points = [(2,3), (5,5), (9,4), (6,5)]
	# src = (1,1)
	# n = len(points)
	# points.append(src)
	# adj = [[0 for _ in range(n+1)] for _ in range(n+1)]
	# for i in range(n+1):
	# 	for j in range(n+1):
	# 		adj[i][j] = abs((points[i][0]-points[j][0]))+abs((points[i][1]-points[j][1]))
	# ans_fb = tsp_bf(0,1,0)
	# ans_dp = tsp_dp(0,0,0)
	# print("The shortest path has length ",ans_dp)
	tcnt = int(stdin.readline())
	while tcnt!=0:
		memo = dict()
		stdin.readline()
		x,y = map(int, stdin.readline().strip().split())
		src = (x,y)
		beepers = int(stdin.readline())
		points = []
		n = beepers
		while beepers!=0:
			new_x,new_y = map(int, stdin.readline().strip().split())
			beep = (new_x,new_y)
			points.append(beep)
			beepers-=1
		points.append(src)
		adj = [[0 for _ in range(n+1)] for _ in range(n+1)]
		for i in range(n+1):
			for j in range(n+1):
				adj[i][j] = abs((points[i][0]-points[j][0]))+abs((points[i][1]-points[j][1]))
		ans_dp = tsp_dp(0,0,0,adj)
		print("The shortest path has length",ans_dp)
		tcnt-=1
main()