#top-down (memorization)

def fib(n):
	assert 0 <= n
	ans = None 
	if n<=1:
		ans = n
	else:
		ans = fib(ans - 2) + fib(ans - 1)
	return ans

#now let's use memorization

def fib_dp(n, mem):
	assert 0 <= n
	ans =  None
	if n in mem:
		ans = mem[n]
	else:
		if n<=1:
			ans = n
		else:
			ans = fib_dp(n-1, mem) + fib_dp(n-2, mem)
			mem[n] = ans
			print(ans)
			print(mem)


	return ans

mem = dict()
print(fib_dp(6, mem))

