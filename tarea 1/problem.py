from sys import stdin
import time

#Autor Sebastian Toro

#Ayudado por: Christian Roman, German Caycedo

def solve(k):
  ans, nNumbers = 0, 0
  k = abs(k)
  lo, hi = 0, 65000
  while lo+1 != hi:
    mid = (lo +hi)>>1
    if((mid)*(mid+1)>>1) == k:
      ans = mid 
      lo = hi-1
    elif((mid)*(mid+1)>>1) > k:
      ans = mid
      hi = mid
    else:
      lo = mid
  nNumbers = ans
  while(((nNumbers*(nNumbers+1))//2-k)%2 != 0):
    nNumbers += 1
  if k == 0:
    nNumbers = 3
  elif k == 1:
    nNumbers = 1
  return nNumbers

def main():
  y = time.time()
  tcnt,first = int(stdin.readline()),True
  while tcnt!=0:
    stdin.readline()
    if first==False: print()
    first = False
    print(solve(int(stdin.readline())))
    tcnt -= 1
  print(time.time()-y)

main()
