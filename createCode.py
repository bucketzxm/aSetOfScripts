#!/bin/python3

import uuid

def create_code(number=200):
	'''
	generate some unique code 
	'''
	result = []
	for i in range(0,number):
		temp = str(uuid.uuid4()).replace('-','')
		if temp not in result:
			result.append(temp)
	
	return result

result = create_code()
print(result)
