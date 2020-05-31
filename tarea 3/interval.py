#Solving the interval problem
#By sebastian Toro
#Using greedy algorithms

from sys import stdin


def solve(l,h,S):
	ans, lo, n, = list(), l, 0
	N = len(S)
	while lo <= h and n != N:
		best, n = n, n+1
		while n != N and S[n][0] <= lo:
			if S[n][1] > S[best][1]:
				best = n
			n+=1
		ans.append(S[best])
		lo = S[best][1]
	return ans



S = [(1,2),(3,5),(1,5),(2,4),(4,5),(3,6),(2,7),(7,9),(4,8),(1,3)]

S.sort()

#print(S)

print("The minimum required intervals are: ", solve(1,9,S))




	