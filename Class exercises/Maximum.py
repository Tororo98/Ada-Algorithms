from sys import stdin
"""
Basado en Sahil Thakur
https://www.youtube.com/watch?v=vtJvbRlHqTA
"""

def solve(A):
  hi = hipre = lo = lopre = ans = A[0]
  for i in range(1,len(A)):
    hi = max(hipre*A[i], lopre*A[i], A[i])
    lo = min(hipre*A[i], lopre*A[i], A[i])
    ans = max(ans, hi)
    hipre = hi
    lopre = lo
  return ans

def main():
  tcnt = list(map(int, stdin.readline().split()))
  text=[]
  while tcnt!=[]:
    if (tcnt[len(tcnt)-1]) == -999999:
      tcnt.pop()
      print(solve(tcnt))
      tcnt = []
    text = list(map(int, stdin.readline().split()))
    tcnt = tcnt + text

main()