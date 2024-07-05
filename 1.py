# Spiral 3 x 3 Matrix print
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

order = 3
n = 9
leftRight = 3
topBottom = 3
rightLeft = 2
bottomTop = 3

# Left to right
for i in range(order):
	print(m[order - leftRight][i], end=" ")
	n -= 1
bottomTop -= 1
while (n > 0):
	# Top to bottom
	for i in range(1, order):
		print(m[i][topBottom - 1], end=" ")
		n -= 1
	leftRight -= 1
	# Right to left
	for i in range(rightLeft - 1, -1, -1):
		print(m[rightLeft][i], end=" ")
		n -= 1
	topBottom -= 1
	# Bottom to top
	for i in range(bottomTop - 1, order - bottomTop, -1):
		print(m[i][order - bottomTop - 1], end=" ")
		n -= 1
	rightLeft -= 1
	# Left to right
	for i in range(0, order - leftRight + 1):
		print(m[order - leftRight][i], end=" ")
		n -= 1
	bottomTop -= 1
print()
