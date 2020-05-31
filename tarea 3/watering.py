#Solving the watering grass problem
#By sebastian toro
#Using greedy algorithms
#Based on the code by Professor Camilo Rocha at: https://bitbucket.org/snippets/hquilo/z6KbA

from sys import stdin
from math import *

def solve(L,H,a):
  a.sort()
  ans,low,n,ok,N = list(),L,0,True,len(a)
  while ok and low<H and n!=N:
    ok = a[n][0]<=low													#we are looking for the next best circle that fulfill the requirements
    best,n = n,n+1														#1) the circle's left limit is within the range of the previous circle
    while ok and n!=N and a[n][0]<=low:									#2) the circle's right limit is the farthest one from the actual circle's right limit
      if a[n][1]>a[best][1]:											#3) the circle's upper limit is greater than that of w/2
        best = n                   										#only then that circle can be considered to be added to ans
      n += 1
    ans.append(best)
    low = a[best][1]
  ok = ok and low>=H
  if ok==False:
    ans = list()
  return ans



def main():
  n= stdin.readline()
  while n!= "" :
    #line= n.split()
    intervalos=[]
    casos, dist_total, ancho=map(int, n.split())							#int(line[0]),int(line[1]),int(line[2])
    
    for i in range(casos):
      ubicacion, radio = map(int, stdin.readline().strip().split())
      if radio*2>ancho:
        z= sqrt( (radio**2) - ((ancho/2)**2))
        intervalos.append([ubicacion-z,ubicacion+z])

    intervalos.sort()
    ans = solve(0,dist_total,intervalos)
    #print(ans)
    if len(ans)==0:
      print(-1)
    else:
      print(len(ans))

    n = stdin.readline().strip()
    

main()