from sys import stdin
"""
  Autor: Sebastian Toro
  codigo: 8931567
  codigo de honor: 
  Como miembro de la comunidad académica de la 
  Pontificia Universidad Javeriana Cali me comprometo a seguir 
  los más altos estándares de integridad académica.

"""

def comp(int_type,int_type2):
                                   #here i flip the interval that i need
  return (int_type ^ int_type2)    #making an xor between my string and a string full of ones
                                   #will toggle the bits on the string                                    
def left(int_type,a):
  ans = (int_type&(-int_type)).bit_length()
  a = a+ans
  return a                         #returns the first 1 occurrence from a limit and updates a limit

def right(int_type,b):
  ans = int_type.bit_length()
  if ans==0:
    ans=b
  return ans                       #returns the first 1 occurrence since b limit 

def solve(inv,int_type):
  for v in inv:                    #v is my list of intervals
    a,b = v                        #a is lower limit and b is higher limit
    mask = 1<<a-1                     
    if int_type&mask==0:           #with mask i check wether limit a is off              
      a = left(int_type>>a,a)      #here i call my left function
    mask = 1<<b-1
    if int_type&mask==0:           #here i call right function
      tmp2 = (1<<b)-1 
      b = right(int_type&tmp2,b) 
    int_type = comp(int_type,((1<<a)-1)^((1<<(b-1))-1))      #now to apply the flip
  return int_type

"""
  Input: There are cnt cases and for each case the first line will represent K which is the length of the christmas
  ligths's line (the total of lights represented as bits) and M which is the total of seconds whilst the line will
  change its state (2<=K<=10^6,0<=M<=10^4). The next line will contain the hexadecimal string using: ‘0123456789ABCDEF’
  with no leading zeros.
  Note: if the hexadecimal string requires less than K bits in binary notation it will be filled with leading zeros 
  until K length is reached.
"""
"""
  Output: For eacht test case cnt, a single line will be printed describing the state of the string at second,
  using the same notation as given by input: ‘0123456789ABCDEF’.
"""

def main():
  global K,M
  cnt = int(stdin.readline())
  while cnt!=0:
      K,M = map(int, stdin.readline().split())
      sh = int(stdin.readline().strip(),16)   #convert hex to int using python's help
      seconds = 0
      inv = list()
      while seconds<M:
        a,b = map(int, stdin.readline().split())
        a,b = K-a+1,K-b+1                     #invert the order of my limits as a result of python's way of reading binaries
        inv.append((a,b))
        seconds+=1
      print(hex(solve(inv,sh))[2:].upper())   #unconvert the int to hex 
      cnt-=1
main()

"""
REFERENCES THAT HELPED ME SOLVED THE PROJECT:
- https://stackoverflow.com/questions/2654149/bit-length-of-a-positive-integer-in-python
- https://stackoverflow.com/questions/791328/how-does-the-bitwise-complement-operator-tilde-work
- https://wiki.python.org/moin/BitwiseOperators
- https://stackoverflow.com/questions/1476/how-do-you-express-binary-literals-in-python
- https://stackoverflow.com/questions/14526584/what-does-the-xor-operator-do
- https://www.geeksforgeeks.org/toggle-bits-given-range/
"""
