#!/usr/bin/python3
def square_matrix_map(matrix=[]):
	"""
	Write a function that computes the square value of all integers of a matrix using map
	"""
	return list(map(lambda rows: list(map(lambda x: x ** 2, rows)), matrix))
