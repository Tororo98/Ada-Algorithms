from sys import stdin
import time

#Autor: Sebastian Toro
#Ayuda en explicacion: David Hernandez, Nicolas Ortiz, William


AlphabetF = {'a':[],'b':[],'c':[],'d':[],'e':[],
     'f':[],'g':[],'h':[],'i':[],'j':[],
     'k':[],'l':[],'m':[],'n':[],'o':[],
     'p':[],'q':[],'r':[],'s':[],'t':[],
     'u':[],'v':[],'w':[],'x':[],'y':[],'z':[],
     'A':[],'B':[],'C':[],'D':[],'E':[],
     'F':[],'G':[],'H':[],'I':[],'J':[],
     'K':[],'L':[],'M':[],'N':[],'O':[],
     'P':[],'Q':[],'R':[],'S':[],'T':[],
     'U':[],'V':[],'W':[],'X':[],'Y':[],'Z':[]}

A = [3,4,6]

x = 0 #aaaaxxxxxax

def binarySearch(A, x):
  lo, hi = 0, len(A)
  if len(A) == 0:
    return -1
  else:
    while lo+1 != hi:
      mid = (lo + hi)>>1
      if A[mid]>x:
        hi = mid
      else:
        lo = mid        
    if A[lo]<x and lo != len(A)-1:
      return A[hi]        
    if A[lo] == x and lo != len(A)-1:
      return A[lo+1] 
    if A[lo]>x:
      return  A[lo]
    else:
      return -1



def solve(text, p):
  #y = time.time()
  ans,first,last = None,None,None
  Indexcounter, counter = 0,0
  temp = []
  for i in p:
    if counter == 0:
      if len(AlphabetF[i]) != 0:  #first letter of string
        temp.append(AlphabetF[i][Indexcounter])
      else:
        return ans, first, last
    else: 
      Indexcounter = binarySearch(AlphabetF[i], temp[counter-1])        #every letter after the first one
      if Indexcounter != -1:
        temp.append(Indexcounter)
        ans = True
        #first, last = min(temp), max(temp)
      else:
        ans = False
        #first, last = min(temp), max(temp)
        return ans,first,last

    counter += 1
  first, last = min(temp), max(temp)
  return ans,first,last

def main():
  #y = time.time()
  text = stdin.readline().strip()
  tcnt = int(stdin.readline())
  tmp = 0
  for i in text:
    AlphabetF[i].append(tmp)  #dictionary with 52 chars

    tmp += 1
  while tcnt!=0:
    p = stdin.readline().strip()
    ans,first,last = solve(text, p)
    if ans: print('Matched {0} {1}'.format(first, last))
    else: print('Not matched')
    tcnt -= 1
  #print(time.time()-y)

main()

#print(binarySearch(A, x))
