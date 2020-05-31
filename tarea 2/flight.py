from sys import stdin
import time

#solving the flight planner problem
#By sebastian Toro
#Based on the explanation given on class by the professors
#and explanations by Christian Roman and Nicolas Alvarez

ptive_inf = float('inf')
memory = []

for i in range(0,10):
  memory.append([ptive_inf]*1000)

memory[0][0] = 0

def solve(La,miles): 
  i, j = 1, 0
  while i <= miles:
    for j in range(10):
      if i!=0 and j==0:
        memory[j][i] = min(memory[j][i-1]+30-La[j][i-1],memory[j+1][i-1]+20-La[j+1][i-1])
        
      elif i!=0 and j==9:
        memory[j][i] = min(memory[j][i-1]+30-La[j][i-1],memory[j-1][i-1]+60-La[j-1][i-1])
        
      elif i!=0 :
        memory[j][i] = min(memory[j][i-1]+30-La[j][i-1],memory[j+1][i-1]+20-La[j+1][i-1],memory[j-1][i-1]+60-La[j-1][i-1])
        
    i += 1
  return memory[0][miles]
  
def main():
  #y = time.time()
  tcnt = int(stdin.readline())
  while tcnt!=0:
    stdin.readline()
    num = int(stdin.readline())
    miles = int(num/100)
    La = []
    for j in range(0,10):
      dato = list(map(int, stdin.readline().split()))
      La.append(dato)
    La.reverse()

    print(solve(La,miles))
    print("")
    tcnt -= 1
  #print(time.time()-y)

main()