#!/bin/python2


def In():
	N = int( input())
	expList = []
	for i in range(N):
		exp = raw_input()
		expList.append( exp )
	return expList


def Transform(exp):
	'''
	Transform algebraic expression into RPN form
	'''
	expLen = len(exp)
	for i in range( expLen):
		pass
		


def main():
	expList = In()
	print expList

if __name__ == "__main__":
	main()
