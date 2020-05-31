#solving the gas stations problem
#2nd term ADA 2019-1

from sys import stdin

def solve(L,radius,a):
 a.sort()
 ans,N = list(),len(a)
 low,n = L,0
 ok = True
 while ok and low<radius and n!=N:
  ok = a[n][0]<=low                                                   #we are looking for the next best circle that fulfill the requirements
  best,n = n,n+1                                                      #1) the circle's left limit is within the range of the previous circle
  while ok and n!=N and a[n][0]<=low:                                 #2) the circle's right limit is the farthest one from the actual circle's right limit
   if a[n][1]>a[best][1]:                                            #3) the circle's upper limit is greater than that of w/2
    best = n                                                        #only then that circle can be considered to be added to ans
   n += 1
  ans.append(best)
  low = a[best][1]
 ok = ok and low>=radius
 if ok==False:
  ans = list()
 return ans

def main():
 n= stdin.readline()
 while n!= "" :
  lenght, gasStations=[ int(x) for x in n.split() ]       #int(line[0]),int(line[1]),int(line[2])
  if lenght!= 0 and gasStations!=0:
   intervalos=[] 
   for i in range(gasStations):
    ubicacion, radio = map(int, stdin.readline().strip().split())
    intervalos.append([ubicacion-radio,ubicacion+radio])
   # intervalos.sort()
   ans = solve(0,lenght,intervalos)
   if len(ans)==0:print(-1)
   else:print(gasStations-len(ans))
  n = stdin.readline().strip()

main()