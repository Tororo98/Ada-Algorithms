from sys import stdin
import time

#Code adquired via explanation given by the professor
#which then was explain to me by Christian Roman, Jonathan Asprilla



INF = float('inf') * -1

def solve(a,ext,hrs):
  global  A , L, hrshrs
  ans = 0
  if (a,ext,hrs) in A:
    ans = A[(a,ext,hrs)]
  else:    
    if (a == 0 and ext == 0):
      ans = 0
      A[(a,ext,hrs)] = ans
    elif(a != 0 and ext == 0):
      ans = INF
      A[(a,ext,hrs)] = ans
    elif (a != 0 and ext != 0 and L[a-1][ext-1] < 5 ):
      ans = solve(a, ext-1, hrs)
      A[(a, ext, hrs)] = ans
    elif (a != 0 and ext != 0 and L[a-1][ext-1] >= 5 and hrs<ext ):
      ans = solve(a, ext-1, hrs)
      A[(a, ext, hrs)] = ans
    elif a != 0 and ext != 0 and L[a-1][ext-1] >= 5 and hrs>=ext:
      ans = max(solve(a, ext-1, hrs), solve(a-1, hrs, hrs-ext) + L[a-1][ext-1])
      A[(a, ext, hrs)] = ans
  return ans

def main():
  #y = time.time()
  global A, L, hrs
  i = int(stdin.readline())
  while i != 0:
    filasXhrs = stdin.readline().split()
    filas = int(filasXhrs[0])
    hrs = int(filasXhrs[1])
    cont = filas
    L = []
    while filas != 0:
      datos = list(map(int, stdin.readline().split()))
      L.append(datos)
      filas = filas - 1

    A = {}
    grades = solve(cont, hrs, hrs) 
    finalGrade = grades / cont
    if finalGrade >= 5:
      print ("Maximal possible average mark - {0:.2f}".format(finalGrade)+'.')
    else:
      print ("Peter, you shouldn't have played billiard that much.")
    
    i -=1
  #print(time.time()-y)

main()
