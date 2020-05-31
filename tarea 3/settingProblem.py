#Solving the setting problem situation
#By sebastian toro
#Using greedy algorithms
#Helped by Christian Roman (explanation)

from sys import stdin

def solve(S, G):										
	a = 0									
	b = 0									
	suma = 0
	S.sort()
	G.sort()
	G.reverse()
	for i in range(len(S)):
		a = a + S[i]
	a = a + G[len(G)-1]
	for i in range(len(G)):
		b = b + G[i]
	b = b + S[0]
	suma = max(a,b)
	return suma

def main():
	n = stdin.readline()
	# tcnt = 2
	while n != "":
		S = list(map(int, stdin.readline().split()))
		G = list(map(int, stdin.readline().split()))
		n = stdin.readline()
		print(solve(S,G))
	# S = [8,1,6]
	# G = [1,6,3]
	# S.sort()
	# G.sort()
	# G.reverse()
	# print(solve(S,G))

main()

