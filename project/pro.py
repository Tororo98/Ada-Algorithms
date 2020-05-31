from sys import stdin

def solve(mi,A):
	s = list(mi)
	for i in A:
		if s[i[0]] == 0:
			j = i[0]
			while j>0:
				if s[j] == 1:
					i[0] = j
					j = 0
				j -= 1
		if s[i[1]] == 0:
			j = i[1]
			while j<len(s):
				if s[j] == 1:
					i[1] = j
					j = len(s)
				j += 1

		ite = i[1]-i[0]
		for j in range(ite+1):
			if s[i[0]+j] == "1":
				s[i[0]+j] = "0"
			else: 
				s[i[0]+j] = "1"
			
	ans = ''.join(s)
	return ans

def convert(s,bits):
	scale = 16
	return bin(int(s,scale))[2:].zfill(bits)

def main():
	tcnt = int(stdin.readline())
	while(tcnt > 0):
		K, M = map(int, stdin.readline().split())
		ex = stdin.readline()
		s = convert(ex,K)
		i = 0
		interval = list()
		while i < M:
			interval.append((map(int, stdin.readline().split())))	
			i += 1
		ans = solve(s, interval)
		ans = hex(int(ans,2))[2:]
		print(ans)	
		tcnt -= 1
main()
"""
64E0 = 000110010011100000

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
0 0 0 1 1 0 0 1 0 0  1  1  1  0  0  0  0  0

5, 12
0 0 0 1 *0 1 1 0 1 1  0  0*  1  0  0  0  0  0

10, 11
0 0 0 1 0 1 1 0 1 *0  1  1  0*  0  0  0  0  0

5, 8
0 0 0 *0 1 0 0 1 0* 0  1  1  0  0  0  0  0  0

3, 6
0 0 *1 1 0 1 1 0* 0 0  1  1  0  0  0  0  0  0

1, 17
*1 1 0 0 1 0 0 1 1 1  0  0  1  1  1  1  1*  0 = 3273E """