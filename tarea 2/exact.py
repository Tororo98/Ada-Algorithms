from sys import stdin
import time

#Solving the Exact change problem
#By Sebastian Toro\
#Helped by Christian Roman: explaining the main

ptive_inf = float('inf')

def solve(coins, N, payable):
	struct = [ptive_inf for _ in range(10001)]
	struct[0] = 0
	i = 0
	while i != N:
		j = 10000 - coins[i]
		while j >= 0:
			if struct[j] != ptive_inf and struct[j]+1 < struct[j+coins[i]]:
				struct[j+coins[i]] = min(struct[j]+1, struct[j+coins[i]])		#struct[j] = struct[j - coins[i]] + 1
			j -= 1
		i += 1

	i = payable
	while struct[i] == ptive_inf:
		i += 1
		
	return i, struct[i]



def main():
  tcnt = int(stdin.readline())
  while tcnt!=0:
    total = lo = 0
    valor = int(stdin.readline())
    monedas = int(stdin.readline())
    X = [int(stdin.readline()) for i in range(monedas)]
    total, lo = solve(X, monedas, valor)
    print('{0} {1}'.format(total, lo))
    tcnt -= 1

main()