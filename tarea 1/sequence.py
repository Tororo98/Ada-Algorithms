from sys import stdin
import math

#Autor Sebastian Toro

#Ayudado por: Christian ROman

ans = "".join(str(i) for i in range(31268))

def solve(n, limit):
  return ans[(n-limit[0])]

def lim():
  i = 1
  S = [0 for i in range(31268)]
  cont = 0
  while i<len(S):
    cont += len(str(i))
    S[i] = cont + S[i-1]
    i += 1
  return S

def find(S, x):
  low, hi = 0,len(S)
  while(low+1 != hi):
    mid = (low + hi)>>1
    if S[mid]>x:
      hi = mid
    else:
      low = mid

  if S[hi-1]==x:
    return [S[hi-2], S[hi-1], hi%10]

  return [S[hi-1], S[hi], hi]
  
def main():
  tcnt = int(stdin.readline().strip())
  getlim = lim()
  for i in range(tcnt):
    tcnt2 = int(stdin.readline().strip())
    limtotal = find(getlim, tcnt2)
    print(solve(tcnt2, limtotal))

main()

