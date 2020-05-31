#Solving knuth's permutation

from sys import stdin
from collections import deque


def toString(List):
 return ''.join(List) 
 
# def solve(a, l, r): 
#  if l==r:
#   print(toString(a))
#  for i in range(l,r+1): 
#   a[l], a[i] = a[i], a[l] 
#   solve(a, l+1, r) 
#   a[l], a[i] = a[i], a[l] # backtrack 

# def solve2(s, idx, end):
#  ans = []
#  i = idx
#  if idx == 0:
#   for i in range(len(s)):
#    ans[i] = s[i]
#   ans[i],ans[end] = s[end],s[i]
#   print(toString(ans))
#  else:
#   if idx == end:
#    print(toString(ans))
#   else:
#    s.reverse()
#    for i in range(end+1):
#     if i == end:
#      ans[i-1], ans[i] = s[i], s[i-1]
#      print(ans)
#     else:
#      ans[i], ans[i+1] = s[i+1], s[i]
#      print(ans)

    # solve2(s,idx+1,end)

def solve2(s):
 s.reverse()
 first,second = deque(), deque()
 first.insert(0,[])
 mylist=[first,second]
 idx = 0
 while(s):
  knuth(mylist[idx],mylist[not idx],s.pop())
  idx=not idx

 while(mylist[idx]):
  ans=mylist[idx].popleft()
  last=toString(ans)
  print(last)

def knuth(first, second, last):
 while(first):
  myTmpList=first.popleft()
  n = len(myTmpList)
  for i in range(n+1):
   idx=myTmpList[:]
   idx.insert(i,last)
   second.append(idx)

def main():
 counter = stdin.readline().strip()
 # n = len(counter)
 while (len(counter) != 0):
  ans = list(counter)
  solve2(ans)
  counter = stdin.readline().strip()
  if counter != "": 
   print()

main()