#new transportation

from sys import stdin


# def compare(i,j,k,l):	#both i and j are start stations, j and k are destination stations
# 	ok = None
# 	if i<j:
# 		ok = True
# 	elif i==j and k<l:
# 		ok = True
# 	return ok

def judge(idx):
	oks = False
	if train[idx]+orders[idx][2]>n:
		oks = True
	return oks

def accept(curr,mx):
	global ans, train
	if curr == numOrders:
		ans = max(mx,ans)
	elif curr < numOrders:
		for i in range(orders[idx][0],orders[idx][1])
	

def main():
	global asc,dsc,orders,n,stations,numOrders,train,ans
	n = 10
	stations,numOrders = 3,4
	orders = [[0,2,1],[1,3,5],[1,2,7],[2,3,10]]
	train = [0 for _ in orders]
	mx = 0
	ans = 0
	print(accept(0,0,ans,train))

main()