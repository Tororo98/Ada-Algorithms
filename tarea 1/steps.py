from sys import stdin
import math
import time

#Autor: Sebastian Toro
#Ayudado por: Christian Roman

def solve(x, y):
  ans = 0
  steps = 0
  diff =  abs(y-x)

  if diff == 0:
  	ans = 2*steps
  	return ans
  elif diff < 2 * (steps + 1):
  	if (steps + 1) >= diff:
  		ans = 2 * steps+1
  	else:
  		asn = 2 * steps+2
  		return ans
  else:
  	ans = math.sqrt(4*diff) -1
  	ans = math.ceil(ans)
  steps += 1
  diff = y - x - steps * (1+steps)

  return ans

def main():
  tcnt = int(stdin.readline())
  while tcnt!=0:
    tok = stdin.readline().split()
    print(solve(int(tok[0]), int(tok[1])))
    tcnt -= 1

main()
