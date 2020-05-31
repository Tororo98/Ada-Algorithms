import math 
  
# def setBitNumber(n): 
      
#     # To find the position of 
#     # the most significant  
#     # set bit 
#     k = int(math.log(n, 2)) 
      
#     # To return the value  
#     # of the number with set  
#     # bit at k-th position 
#     print("l",len(n ))
#     return k 
  
# Driver code 
n = 19        
# print(setBitNumber(n)) 

def lowestSet(int_type):
	low = (int_type & -int_type)
	lowBit = -1
	while (low):
		low >>= 1
		lowBit += 1
	return(lowBit)

def bin2(cad): return bin(int(cad))[2:]

def int2(cad): return int(cad,2)

def bin2a(cad,bits): return bin(int(cad,16))[2:].zfill(bits)

def hexa(cad): return hex(int(cad,2))[2:].upper()

print(bin2("163")) #normal bin

#print(bin2a("80",16)) #filled bin

print(163&(-163))

l = 163>>6		#bit_length - a gives me how much places i need to shift the number

# print(int2("10100011")) --> 163  | this is the reversed string:
#					 1 --> 1

ll = str(l)

print(bin2(ll))

r = 197>>7

rr = str(r)

print(bin2(rr))

print(bin2("-164"))

def rev(n): return int(bin(n)[:1:-1], 2) #reverse the binary string 

print(rev(163))

#print(lowestSet(80))

#l = bin2("80")

#print(l)

#print(math.log(16,2))

a = 3 #101
b = 2 #010 

c = (a ^ b)
print(bin(c))

a = 4
K = 17



print(bin(17)[2:])
print(bin(17>>3)[2:])
a=5
print(a.bit_length())