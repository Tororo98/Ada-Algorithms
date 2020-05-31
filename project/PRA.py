#Understanding the christmas lights problem
#ADA final project
#Sebastian Toro
#codigo 8931567
"""

"""
from sys import stdin

def convert(s,bits):
	scale = 16
	return bin(int(s, scale))[2:].zfill(bits)


def unconvert(s):
	scale = 2
	return hex(int(s,scale))[2:]


def limR(sin,n):
	ok = True
	for j in range(n):
		if sin[j]=="1" and ok:
			tmpLSobrante = sin[j+1:n]
			tmpL1 = cbin[0:j+1]
			tmpL1Cambio = tmpL1.replace("1","x").replace("0","1").replace("x","0")
			ok=False
			return tmpL1Cambio+tmpLSobrante
	return cbin


def limL(sin,n):
	ok = True
	j = n
	while j!= 0:
		if sin[j-1]=="1" and ok:
			tmpS = sin[0:j-1]
			tmpR1 = sin[j-1:n]			
			tmpR1Cambio = tmpR1.replace("1","x").replace("0","1").replace("x","0")
			ok=False
			return tmpS+tmpR1Cambio
		j-=1
	return cbin

def ltoR(s,a,b,K):
	tmpM = s[a-1:b]
	tmpR = s[b:K]
	tmpL = s[0:a-1]
	tmpnew = tmpM.replace("1","x").replace("0","1").replace("x","0")
	if tmpM[0] == "0":
		tmpL = limL(tmpL, len(tmpL))
	if tmpM[len(tmpM)-1] == "0":
		tmpR = limR(tmpR, len(tmpR))
	return tmpL+tmpnew+tmpR


def main():
	tcnt = int(stdin.readline())
	while tcnt!=0:
		K,M = map(int, stdin.readline().split())
		sh = stdin.readline().strip()
		seconds=0
		sb = convert(sh,K)
		while seconds<M:
			a,b = map(int, stdin.readline().split())
			sb = ltoR(sb, a, b, K)
			seconds+=1
		print(unconvert(sb))
		tcnt-=1

main()