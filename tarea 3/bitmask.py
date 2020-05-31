#Solving the bitmask problem
#By sebastian Toro
#Using greedy algorithms
#Helped by Christian Roman and Nicolas Ortiz
from sys import stdin
import time

def solve(N,L,U):
	i,M = 31,0 
	while(i >= 0):
		mask = M|(1<<i)
		if( (((N>>i)&1) == 0 and mask <= U) or mask<=L ):
			M=mask
		i-=1 
	return M 

def main():
	global N,L,U
	line = stdin.readline().strip()
	# x = list(map(int, stdin.readline().split()))
	while line!="":
		N,L,U = list(map(int, line.split()))
		print(solve(N,L,U))
		line = stdin.readline().strip()
main()

#print(solve(2131282801, 18845542, 394960420))
