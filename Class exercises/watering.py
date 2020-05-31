#Solving the watering grass problem
#By sebastian toro
#Using greedy algorithms

from sys import stdin
import math

def solve(l,w,S):
	ans, lo, n  = list(), S[0][0]-S[0][1], 0																#S is my list of n circles S[n][0] =  the center, S[n][1] = radius
	N = len(S)
	while lo < l and lo <= 0 and n != N:																		#best is the current circle, the best i can do
		best, n = n, n+1																			#n will be the next circle to compare with
		while n != N and S[n][0]-S[n][1] < lo:
			if (S[n][0]+S[n][1]) > (S[best][0]+S[best][1]) and S[n][1] > w/2:
				best = n
				n+=1
		ans.append(S[best])
		lo = S[best][0]+S[best][1]
	return ans

S = [(5,3),(4,1),(1,2),(7,2),(10,2),(13,3),(16,2),(19,4)]
S.sort()
print(solve(20,2,S))

# S = [(3,5),(9,3),(6,1)]
# S.sort()

# S = [(5,3),(1,1),(9,1)]
# S.sort()

# print(solve(10,1,S))

def main():
	pass