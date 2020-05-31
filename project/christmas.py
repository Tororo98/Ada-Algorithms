#Understanding the christmas lights problem
#ADA final project

from sys import stdin

def convert(s,bits):
	scale = 16
	return bin(int(s,scale))[2:].zfill(bits)

def limL(a,s):
	i = a
	good = True
	while s[i]!="1" and good:		#Function to calculate how much bits to the left I have to swap
		if i==0:
			good = False
			i = a
		# cnt+=1
		i-=1
	return i

def limR(b,s):
	i = b
	good = True
	while s[i]!="1" and good:		#Function to calculate how much bits to the right I have to swap
		if i==len(s):
			good = False
			i = b
		# scnt+=1
		i+=1
	return i

def check1L(a1,a,s):
	check = True
	leftSide = s[a1:a]				#Function to calculate if is safe to swap left section
	TleftSide = s[0:a]
	if len(leftSide) == len(TleftSide):
		check = False
	return check

def check1R(b1,b,s):
	n = K
	check = True
	rightSide = s[b:b1]				#Function to calculate if is safe to swap right section
	TrightSide = s[b:n]
	if len(rightSide) == len(TrightSide):
		check = False
	return check

def updateLeft(a1,a,s):
	tempL = s[a1:a]
	tempS = s[0:a1-1]
	tempL = tempL.replace("1", "x").replace("0", "1").replace("x", "0")
	return tempS+tempL

def updateRight(b,b1,s):
	tempR = s[b:b1]
	tempS = s[b1:K]
	tempR = tempR.replace("1", "x").replace("0", "1").replace("x", "0")
	return tempR+tempS

def updatePart(a,b,s):
	temp = s[a:b+1]
	return temp.replace("1", "x").replace("0", "1").replace("x", "0")

def update(a,b,s,temp,temp1):
	n = K
	# p1,p2 = s[0:a], s[b+1:n]
	if temp[0]=="0":
		# print("hola")
		a1 = limL(a,s)
		p2 = s[b+1:n]
		if check1L(a1,a,s):
			# p1 = s[a1:a-1]
			p1 = updateLeft(a1,a,s)
		new_s = p1+temp1+p2
	if temp[len(temp)-1]=="0":
		# print("hola")
		b1 = limR(b+1,s)
		# print(b1)
		p1 = s[0:a]
		# print(b1)
		if check1R(b1+1,b+1,s):
			# print("adios")
			# p2 = s[b:b1]
			# print(b+1,b1+1,s)
			p2 = updateRight(b+1,b1+1,s)
		new_s = p1+temp1+p2
	else:
		p1,p2 = s[0:a], s[b+1:n]
		new_s = p1+temp1+p2

	return new_s
	
def main():
	global K,M
	K = 18
	M = 5
	s = "64E0"
	ans = convert(s,K)
	# ans = "000101101100100000"
	a,b = 4,11						#these refers to the element position not the index, therefore i need to substract 1
	print(ans)
	temp = ans[a:b+1]
	temp1 = updatePart(a,b,ans)
	# print(temp)
	# print(update(a,b,ans,temp))
	print(update(a,b,ans,temp,temp1))
	# seconds = [(5,12),(10,11),(5,8),(3,6),(1,17)]
	# # tcnt = int(stdin.readline())
	# while tcnt!=0:
	# print(ans)
	# print(updateRight(0,4,ans))
	# 	K,M = map(int, stdin.readline().strip().split())
	# 	s = stdin.readline()
	# 	sec = 0
	# 	lights = []
	# 	while sec!=M:
	# 		lim1,lim2 = map(int, stdin.readline().strip().split())
	# 		mylight = (lim1,lim2)
	# 		lights.append(mylight)
	# 		sec+=1
	# 	tcnt-=1

	# s = "0001"
	# b = 0
	# print(limR(b,s))

main()