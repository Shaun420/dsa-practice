# Spiral 5 x 5 Matrix print
m = []
for j in range(5):
	a = []
	for k in range(5*j+1, 5*j+6):
		a.append(k)
	m.append(a)

order = 5
n = 25
leftRight = 5
topBottom = 5
rightLeft = 4
bottomTop = 4

# Left to right
for i in range(order):
	print(m[order - leftRight][i], end=" ")
	n -= 1

while (n > 0):
	# Top to bottom
	for i in range(order - topBottom + 1, topBottom):
		print(m[i][topBottom - 1], end=" ")
		n -= 1
	leftRight -= 1
	# Right to left
	# print("rightleft loop: {0}".format(list(range(rightLeft - 1, order - rightLeft - 1, -1))))
	for i in range(rightLeft - 1, order - rightLeft - 1, -1):
		print(m[rightLeft][i], end=" ")
		n -= 1
	topBottom -= 1
	# print("topBottom: {0} bottomTop: {1}".format(topBottom, bottomTop))
	# Bottom to top
	for i in range(bottomTop, order - bottomTop - 1, -1):
		print(m[i][order - bottomTop - 1], end=" ")
		n -= 1
	rightLeft -= 1
	# Left to right
	for i in range(order - leftRight, leftRight):
		print(m[order - leftRight][i], end=" ")
		n -= 1
	bottomTop -= 1
print()
