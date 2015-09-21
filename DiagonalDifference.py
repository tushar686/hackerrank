def sumOfFirstDiagonal(Matrix, size):
	sum = 0
	start = 0
	while start < size:
		sum += Matrix[start][start]
		start += 1
	return sum

def sumOfSecondDiagonal(Matrix, size):
	sum = 0
	start = 0
	end = size-1
	while end >= 0:
		sum += Matrix[end][start]
		start += 1
		end -= 1
	return sum	


N = int(raw_input())
Matrix = []

rowIdx = 0
while rowIdx < N:
	row = [int(ele) for ele in raw_input().split()]
	Matrix.append(row)
	rowIdx += 1

sumOfFirstDiagonal = sumOfFirstDiagonal(Matrix, N)

sumOfSecondDiagonal = sumOfSecondDiagonal(Matrix, N)
print abs(sumOfFirstDiagonal - sumOfSecondDiagonal)