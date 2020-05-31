from sys import stdin
"""
Basado en codigo de Rocha
"""

INF = float('inf') * -1

def solve(a,e,h):
  global  A , L, horas
  ans = 0
  if (a,e,h) in A:
    ans = A[(a,e,h)]
  else:    
    if (a == 0 and e == 0):
      ans = 0
      A[(a,e,h)] = ans
    elif(a != 0 and e == 0):
      ans = INF
      A[(a,e,h)] = ans
    elif (a != 0 and e != 0 and L[a-1][e-1] < 5 ):
      ans = solve(a, e-1, h)
      A[(a, e, h)] = ans
    elif (a != 0 and e != 0 and L[a-1][e-1] >= 5 and h<e ):
      ans = solve(a, e-1, h)
      A[(a, e, h)] = ans
    elif a != 0 and e != 0 and L[a-1][e-1] >= 5 and h>=e:
      ans = max(solve(a, e-1, h), solve(a-1, horas, h-e) + L[a-1][e-1])
      A[(a, e, h)] = ans 
  return ans

def main():
  global A, L, horas
  i = int(stdin.readline())
  while i != 0:
    filasXhoras = stdin.readline().split()
    filas = int(filasXhoras[0])
    horas = int(filasXhoras[1])
    cont = filas
    L = []
    while filas != 0:
      datos = list(map(int, stdin.readline().split()))
      L.append(datos)
      filas = filas - 1

    A = {}
    notas = solve(cont, horas, horas) 
    notaTotal = notas / cont
    if notaTotal >= 5:
      print ("Maximal possible average mark - {0:.2f}".format(notaTotal)+'.')
    else:
      print ("Peter, you shouldn't have played billiard that much.")
    
    i -=1

main()
