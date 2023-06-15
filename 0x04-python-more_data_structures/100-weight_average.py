#!/usr/bin/python3

def weight_average(my_list=[]):
	"""
	Write a function that returns the weighted average of all integers tuple (<score>, <weight>)
	"""
	if len(my_list) == 0:
		return 0
	scores = [score*weight for (score, weight) in my_list]
	return sum(scores) / sum([weight for (score, weight) in my_list])
