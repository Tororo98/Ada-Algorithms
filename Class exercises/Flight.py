from sys import stdin
"""
Basado en la funcion Phi de Camilo Rocha expuesta en clase
Colaborador: Nicolas Alvarez 
"""
INF = float('inf')
mem = []

for i in range(0,10):
  mem.append([INF]*1000)
mem[0][0] = 0

def solve(L,n): 
  i, j = 1, 0
  while i <= n:
    for j in range(10):
      if i!=0 and j==0:
        mem[j][i] = min(mem[j][i-1]+30-L[j][i-1],mem[j+1][i-1]+20-L[j+1][i-1])
        
      elif i!=0 and j==9:
        mem[j][i] = min(mem[j][i-1]+30-L[j][i-1],mem[j-1][i-1]+60-L[j-1][i-1])
        
      elif i!=0 :
        mem[j][i] = min(mem[j][i-1]+30-L[j][i-1],mem[j+1][i-1]+20-L[j+1][i-1],mem[j-1][i-1]+60-L[j-1][i-1])
        
    i += 1
  return mem[0][n]
  
def main():
  i = int(stdin.readline())
  while i!=0:
    stdin.readline()
    n = int(stdin.readline())
    millas = int(n/100)
    L = []
    for j in range(0,10):
      dato = list(map(int, stdin.readline().split()))
      L.append(dato)
    L.reverse()

    print(solve(L,millas))
    print("")
    i -= 1

main()