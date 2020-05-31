#sum it up sequence

from sys import stdin
import itertools


def solve(S, t, ans, idx):
	if t == 0:
		print(ans)
	elif idx < len(S):
		if t-S[idx]>=0:
			solve(S, t-S[idx], ans+[S[idx]], idx+1)
			solve(S,t,ans,idx+1)
	return ans

def main():
	S = [4,3,2,2,1,1]
	t = 4
	S.reverse()
	ans = []
	m = solve(S,t,ans,0)
	m.sort()
	[list(tupl) for tupl in {tuple(item) for item in m }]
main()