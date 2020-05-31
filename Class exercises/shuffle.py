#What the function does is return true if the word C is a
#shuffle of A and B, otherwise false.

def Shuffle(A,B,C):

	#Get the len of the two strings A and B.
	M = len(A)
	N = len(B)

	#Then, create a 2 dimensions table to store the solutions
	#of the subproblems. C[i][j] will be true if C[0...i+j-1] is
	#a shuffle of A[0...i-1] and B[0...j-1].

	#Initialize all values as false
	ans = [[False for _ in range(N+1)] for _ in range(M+1)]

	#C can be a suffle of A and B only if the sum of
	#the lens of A and B is equal to the len of C.
	if (M+N) != len(C):
		return False

	#Process all characters of A and B.
	i,j = 0,0

	while i <= M:
		j = 0
		while j <= N:

			#Two empty strings have an empty string as shuffle
			if i==0 and j==0:
				ans[i][j] = True

			#case when A is empty
			elif i==0:
				ans[i][j] = ans[i][j-1] and B[j-1]==C[j-1]

			#case when B is empty
			elif j == 0:
				ans[i][j] = ans[i-1][j] and A[i-1]==C[i-1]

			#case when the current letter of C matches with A and not B, B and not A or Both
			else:
				ans[i][j] = (ans[i-1][j] and A[i-1] == C[i+j-1]) or (ans[i][j-1] and B[j-1]== C[j+i-1])

			j+=1
		i+=1
	return ans[M][N]

def test(A,B,C):
    if (Shuffle(A,B,C)):
        print(C, "is shuffle of ",A," and ",B) 
    else:
    	print(C, "is not shuffle of ",A," and ", B)   
#Driver program to test above functions 
def main(): 
	test("", "ANANAS", "ONANAS")
    # test("BANANA","ANANAS","BANANAANANAS"); 
    # test("XY","WZ","WZXY"); 
    # test ("XY","X","XXY"); 
    # test ("YX","X","XXY"); 
    # test ("XXY","XXZ","XXXXZY"); 
    # test ("DYNAMIC","PROGRAMMING","PRODGYRNAMAMMIINCG");
#print(Shuffle("BANANA","ANANAS","BANANAANANAS"))
main()