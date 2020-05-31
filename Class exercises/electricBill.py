from sys import stdin


def p(w):
	ans = 0
	if w > 0:
		ans += min(w, 100) * 2
	if w > 100:

def consumption(a):
	ans = 0 
	if a <= 200:
		ans = a >>1
	elif a <= 29900:
		ans = 100 + (a - 200)//3
	elif a <= 4979900:
		ans = 10000 + (a - 29900)//5
	else:
		ans = 1000000 + (a - 4979900)//7
	return ans

def solve(a, b):
	cons =  consumption(a)
	lo, hi = 0, cons
	while lo+1 != hi and lo!+hi:
		mid = lo + ((hi-lo)>>1)


def main():
	a, b = map(int, stdin.readline.()split())
	while a + b > 0:
		ans = solve(a, b)
		print(ans)
		a, b = map(int, stdin.readline().split())

main()