from sys import stdin

ans = "".join(str(i) for i in range(32000))

def solve(n, limtotal):
  return ans[(n-limtotal[0])]

def lim():
  i = 1
  serie = [0 for i in range(32000)]
  cont = 0
  while i<len(serie):
    cont += len(str(i))
    serie[i] = cont + serie[i-1]
    i += 1
  return serie

def find(x, serie):
  low, hi = 0,len(serie)
  while(low+1 != hi):
    mid = (low+hi)>>1
    if serie[mid]>x:
      hi = mid
    else:
      low = mid

  if serie[hi-1]==x:
    return [serie[hi-2], serie[hi-1], hi%10]

  return [serie[hi-1], serie[hi], hi]
  
def main():
  tcnt = int(stdin.readline().strip())
  getlim = lim()
  for i in range(tcnt):
    tcnt2 = int(stdin.readline().strip())
    limtotal = find(tcnt2, getlim)
    print(solve(tcnt2, limtotal))

main()
