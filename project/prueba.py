from sys import stdin
"""
  Autor: Sebastian Toro
  codigo: 8931567
  codigo de honor: 
  Como miembro de la comunidad académica de la 
  Pontificia Universidad Javeriana Cali me comprometo a seguir 
  los más altos estándares de integridad académica.

"""

def comp(cad):
  ans = ""
  for c in cad:
    ans = ans + "1" if c == "0" else ans + "0"
  return ans

def left(cad,pos_i):
  find = False
  i = pos_i
  while i >= 0 and not find:
    if cad[i] == "1": find = True
    i-=1
  return (i+1,find)
  # low = (int_type & -int_type)
  # lowBit = -1
  # while (low):
  #   low >>= 1
  #   lowBit += 1
  # return(lowBit)

def right(cad,pos_i):
  find = False
  i = pos_i
  while i < n and not find:
    if cad[i] == "1": find = True
    i+=1
  return (i-1,find)

def solve(inv,cad):
  global n
  n = len(cad)
  ans = str(cad)
  for v in inv:
    a,b = v
    a,b = a-1,b-1
    tmp = comp(ans[a:b+1])
    tmp_l,tmp_r = ans[:a], ans[b+1:]
    if tmp[0] == "1":
      l0,f = left(ans,a)
      if f: tmp_l = ans[:l0] + comp(ans[l0:a])
    if tmp[-1] == "1":
      l1,f = right(ans,b+1)
      if f: tmp_r = comp(ans[b+1:l1+1]) + ans[l1+1:]
    ans = str(tmp_l + tmp + tmp_r)
  return ans

def bin2(cad,bits): return bin(int(cad,16))[2:].zfill(bits)

def hexa(cad): return hex(int(cad,2))[2:].upper()

# def main2():
#   cad = "000110010011100000"
#   print(cad)
#   inv = [(5,12),(10,11),(5,8),(3,6),(1,17)]
#   print(hexa(solve(inv,cad)))

def main():
  cnt = int(stdin.readline())
  while cnt!=0:
      K,M = map(int, stdin.readline().split())
      sh = stdin.readline().strip()
      seconds = 0
      sb = bin2(sh,K)
      inv = list()
      while seconds<M:
        a,b = map(int, stdin.readline().split())
        inv.append((a,b))
        seconds+=1
      print(hexa(solve(inv,sb)))
      cnt-=1
main()