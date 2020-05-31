#solving the transportation problem
#2nd term

from sys import stdin
import time

def judge(i,idx,train,orders,capacity):			#judge is my function to determine if i can add passengers
	oks = False									#Since it was taking more compiling time i dont use it.
	if train[i]+orders[idx][2]>capacity:		#Instead a calculate the value to compare with capacity previous to conditional.
		oks = True
	return oks

def solve2(mx,idx,train,numOrders,orders,capacity):
	global ans
	ok = True
	if idx == numOrders:
		ans = max(mx,ans)
	elif idx < numOrders:
		tmp = list(train)
		i = orders[idx][0]
		while i < orders[idx][1]:	
			can = train[i]+orders[idx][2]		
			if can>capacity:
				ok = False
				i = orders[idx][1]
			else:
				train[i] = train[i]+orders[idx][2]
			i+=1
		if(ok):
			solve2(mx+(orders[idx][2]*(orders[idx][1]-orders[idx][0])),idx+1,train,numOrders,orders,capacity)
		train = tmp
		solve2(mx,idx+1,train,numOrders,orders,capacity)
	return ans

def main():
	y = time.time()
	global ans
	capacity,stations,numOrders = map(int,stdin.readline().split())
	while capacity!=0 or stations!=0 or numOrders!=0: #capacity,stations,numOrders
		orders = []
		train = []
		mx = 0
		ans = 0
		for i in range(numOrders):
			s,d,p = list(map(int,stdin.readline().split()))
			orders.append([s,d,p])
		train = [0 for _ in range(stations+1)]
		print(solve2(mx,0,train,numOrders,orders,capacity))
		capacity,stations,numOrders = map(int,stdin.readline().split())
	print(time.time()-y)
main()