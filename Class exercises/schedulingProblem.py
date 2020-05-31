#solving the scheduling problem 
#By sebastian Toro
#Using greedy algorithms

activities = [(4,6),(0,2),(1,3),(1,6),(3,4)]

newact = [(7,7.9),(7.2,7.6),(7.65,9),(10,11),(10,12),(12,13)]

def solve(A):
	ans = 0
	lo,hi = ans, len(A)
	A.sort()
	reference = A[0][1]
	while lo+1 != hi:
		if A[lo][1] >= reference:
			ans += 1
			reference = A[lo][1]
		lo += 1
	return	ans

print(solve(newact))