from math import *

def print_matrix(matrix, n, m, alighn):
	for i in range(n):
		for j in range(m):
			print(str(matrix[i][j]).center(alighn), end=' ')
		print()
	print()

def completion(n):
	matrix_dist = []
	first_ways = []
	for i in range(n):
		print("Пути от вершины {} к вершинам от 1 до {}:".format(i+1,n))
		temp = input().split()
		if i==0:
			for elem in temp:
				if elem == '*':
					first_ways.append(inf)
				else:
					first_ways.append(int(elem))
			first_ways[0] = 0
		matrix_dist.append(temp)
	adjustment = [[False] for _ in range(n)]
	matrix_uv = [['-' for _ in range(n)] for _ in range(n)]
	for i in range(n):
		for j in range(n):
			if matrix_dist[i][j] == "*":
				matrix_dist[i][j] = inf
			else:
				matrix_uv[i][j] = first_ways[j] - first_ways[i]
				matrix_dist[i][j] = int(matrix_dist[i][j])
				if matrix_uv[i][j]>matrix_dist[i][j]:
					adjustment[i][0] = True
					new_value = matrix_dist[i][j] + first_ways[i]
					adjustment[i].append([j, new_value])
					first_ways[j] = new_value
	return (matrix_dist, first_ways, adjustment, matrix_uv)

def generate_first_table(n, matrix_uv, matrix_dist):
	matrix_1 = [[0 for _ in range(n)] for _ in range(n)]
	for i in range(n):
		for j in range(n):
			if matrix_uv[i][j] == '-':
				matrix_1[i][j] = '-'
			else:
				matrix_1[i][j] = "({},{})".format(matrix_uv[i][j], matrix_dist[i][j])
	return matrix_1

def second_table(n, matrix_1, matrix_uv, matrix_dist, first_ways):
	for i in range(n):
		for j in range(n):
			matrix_uv[i][j] = first_ways[j] - first_ways[i]
			if matrix_dist[i][j] == inf:
				matrix_1[i][j] = '-'
			else:
				matrix_1[i][j] = "({},{})".format(matrix_uv[i][j], matrix_dist[i][j])

def generate_ways(matrix_dist, adjustment):
	ways = []
	busy_path = []

	for i in range(len(matrix_dist[0])):
		if matrix_dist[0][i] == inf:
			busy_path.append(i+1)
		if adjustment[i][0] == True:
			for j in range(1, len(adjustment[i])):
				busy_path.append(adjustment[i][j][0]+1)
				ways.append([str(1), str(i+1), str(adjustment[i][j][0]+1), str(adjustment[i][j][1])])

	busy_path = set(busy_path)

	for i in range(1, n+1):
		if i not in busy_path:
			ways.append([str(1), str(i), str(matrix_dist[0][i-1])])

	return ways

n = int(input("Введите количество вершин: "))

arr = completion(n)
matrix_dist = arr[0]
first_ways = arr[1]
adjustment = arr[2]
matrix_uv = arr[3]

matrix_1 = generate_first_table(n, matrix_uv, matrix_dist)

print_matrix(matrix_1, n, n, 9)
print(adjustment, '\n')

second_table(n, matrix_1, matrix_uv, matrix_dist, first_ways)
print_matrix(matrix_1, n, n, 9)

ways = generate_ways(matrix_dist, adjustment)

for row in ways:
	print(' -> '.join(row[:-1]) + ', D = {}'.format(row[-1]))
