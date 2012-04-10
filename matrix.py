def max_pos(col):
	""" How many positions in output needed to show this column. """	
	ans = 0	
	for i in range(0, len(col)):
		if(len(str(col[i])) > ans):
			ans = len(str(col[i]))
	return ans

def is_matrix(A):
	""" Checking is it a matrix? """
	for i in range(1, len(A)):
		if(len(A[i]) != len(A[0])):
			return False
	return True

def print_matrix(A):
	""" Prints out matrix A with correct indents. """
	n = len(A)
	m = len(A[0])	
	pos = []
	for j in range (0, m):
		col = []
		for i in range (0, n):
			col.append(A[i][j])
		pos.append(max_pos(col))

	for i in range (0, n):
		for j in range (0, m):
			print str(A[i][j]).rjust(pos[j]+1),
		print ""

def mult_matrix(A, B):
	""" Multiply matrix A on matrix B, return matrix. """
	m = len (A)
	n = len (A[0])
	if (not is_matrix(A) or not is_matrix(B)):
		print "A or B is not a matrix."
		print "Don't joke with me, buddy."
		raise AssertionError
	if (n != len(B)):
		print "Matrix dimensions must agreeeeeeeee!!!!!!!!!!!! (c) Matlab"
		raise AssertionError
	q = len (B[0])
	
	answer = []
	for i in range(0, m):
		answer.append([])
		for j in range(0, q):
			answer[i].append(0)
			for r in range(0, n):
				answer[i][j] += A[i][r]*B[r][j]
	return answer

#A = [ [2,3], [0, -2], [-1, 4] ]
#B = [ [1, -1, 0, 3], [2, 1, -2, -4] ]
A = [ [1, 2, -3], [6, 0, 2] ]
B = [ [1, 2, 0, -1], [2, 1, 1, -2], [3, 1, 0, 2] ]

C = mult_matrix(A,B);
print_matrix(C)

