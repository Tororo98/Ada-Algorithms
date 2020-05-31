from sys import stdin,setrecursionlimit
setrecursionlimit(11000)

#Autor: Sebastian Toro
#Basado en el codigo explicado en clase por el profesor Camilo Rocha

N,K,num = None,None,None


def solve(N, K, num, k):
  global mem
  ans = None
  if N == 0:
    ans = (k == 0)
  else:
    if (N,k) in mem:
      ans = mem[(N,k)]
    else:
      ans = solve(N-1, K, num, (k+num[N-1])%K) or solve(N-1, K, num, (k-num[N-1])%K)
      mem[(N,k)] = ans

  return ans

def main():
  global N,K,num,mem
  k = 0
  tcnt = int(stdin.readline())
  while tcnt!=0:
    N,K = map(int, stdin.readline().split())
    num = list(map(int, stdin.readline().split()))
    mem = dict()
    print('Divisible' if solve(N,K,num,k) else 'Not divisible')
    tcnt -= 1

main()
