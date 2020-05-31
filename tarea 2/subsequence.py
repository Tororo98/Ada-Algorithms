from sys import stdin
import time

#Solving the Maximum Subsequence Problem
#Sebastian Toro
#Code highly based on a tutorial found at: https://www.youtube.com/watch?v=vtJvbRlHqTA


def Solve(a):
	ans = a[0]
	current_max_product =  a[0]
	prev_max_product = a[0]
	prev_min_product = a[0]
	for i in range(1, len(a)):
		current_max_product = max(prev_max_product*a[i], prev_min_product*a[i], a[i])
		current_min_product = min(prev_max_product*a[i], prev_min_product*a[i], a[i])
		ans = max(ans, current_max_product)

		prev_max_product =  current_max_product
		prev_min_product = current_min_product

	return ans

def main():
	tcnt = list(map(int, stdin.readline().split()))
	text=[]
	while len(tcnt)!=0:
  		if (tcnt[len(tcnt)-1]) == -999999:
  			tcnt.pop()
  			print(Solve(tcnt))
  			tcnt = []
  		text = list(map(int, stdin.readline().split()))
  		tcnt = tcnt + text
main()

#a = [56479,41050,11054,73036,74990,81434,89440,-31157,-32501,-76413,9393,-48247,-88581,-20675,68061,54456,-62745]
#a = [-1,6,2,0,7,9]
#print(Solve(a))
	