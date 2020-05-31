from sys import stdin

def phi(A, K, n, k):
	ans = None
	if n == 0:
		ans = (k == 0)
	else:
		ans = phi(A, K, n-1, (k+A[n-1])%K) or phi(A, K, n-1, (k-A[n-1])%K)

	return ans

def main():
	ans = phi(A, K, n, k)
	if(ans): 
		print("yes") 
	else: 
		print("no")

A = [7541, 60524, 75240, 45526, 55511, 76517, 748, 77494, 70347, 80716, -6583, 94627, 90517, 84719, 42744, 24421, 52506]
K = 78
n = len(A)
k = 0

main()