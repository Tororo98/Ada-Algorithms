from sys import stdin

#Solving the Train sorting Problem
#Sebastian Toro

#A = [10,3,0,8,2,4,1,6,7,2,11]

#A = [10,3,13,1,4,9,8,12,6,14,5,7,2,0,11]

def Solve(A, n):
	lis, lds = [None for _ in range(n)], [None for _ in range(n)]
	ans = 0
	for i in range(n):
		lis[i] = lds[i] = 1
		for j in range(i):
			if A[j]<=A[i] and lis[j]>=lis[i]:
				lis[i] = lis[j]+1

			if A[j]>=A[i] and lds[j]>=lds[i]:
				lds[i] = lds[j]+1

		ans = max(lis[i]+lds[i]-1, ans)

	return ans


def main():
	tcnt = int(stdin.readline())
	print(tcnt)
	while tcnt != 0:
		tcnt2 = int(stdin.readline())
		arr = []
		lena = tcnt2
		while tcnt2 != 0:
			num = list(map(int, stdin.readline().split()))
			arr=arr+num
			tcnt2 -= 1
		if lena == 0:return 0
		else: 
			arr.reverse()
			print(Solve(arr, lena))
		tcnt -= 1

main()

#print(Solve(A, len(A)))

