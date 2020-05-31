#Solving the moliu problem
#by Sebastian Toro
#Greedy altogrithms

from sys import stdin

def checkIt(n):
	#num = 0
	num = n+1
	num2 = n-1
	cnt = 0
	if(n == 3):
		num = 2
	if(n-1 == 0):
		num = n-1
	#num = n+1
	while(num%2 == 0 and num):
		num = num/2
		cnt +=1
	#num = n-1
	while(num2%2 == 0 and num2):
		num2 = num2/2
		cnt -=1
	if(cnt > 0):
		n = n+1
	else:
		n = n-1
	return n

def solve(n):
	ans = 0
	if(n <= 1):
		ans = n
	elif(n%2):
		ans = solve(checkIt(n))+1
	else:
		ans = solve(n//2)+1
	return ans

def main():
	line = stdin.readline()
	while(len(line)!=0):
		n = int(line)
		print(int(solve(n)))
		# m = stdin.readline()
		line = stdin.readline()
main()

#print(solve(2146367706))
#print(solve(140117))
#print(solve(893786))