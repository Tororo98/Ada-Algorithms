import math

l = [10.22, 12.64, 11.31, 11.16, 13.23, 11.35, 11.57, 
	12.60, 11.69, 9.77, 12.04, 11.62, 12.94, 13.59, 11.32, 11.64, 12.55, 13.60,
	11.30, 11.02, 11.75, 11.66, 13.19]

l.sort()

vMax = max(l)

vMin = min(l)

rango = vMax - vMin

numClases = 1 + 3.322 + math.log(25)

print(rango)
print(math.ceil(numClases))
print(rango/math.ceil(numClases))
print(l)
print(len(l))