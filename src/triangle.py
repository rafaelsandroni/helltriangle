#!/usr/bin/env python

""" Hell Triangle Challenge  """
""" Calcule the maximum total of a triangle """
""" Compares the left and right of next column in a list, and get the biggest value """
""" @author Rafael Sandroni"""

class Triangle:
	
	triangle = []
	path = []
	sum = 0
	lengthTriangle = 0

	def __init__(self,triangle):
		""" receive a list and set triangle and length of triangle """
		self.triangle = triangle
		self.lengthTriangle = len(triangle) - 1
		self.path = []
		self.sum = 0

	def verifyTriangle(self):
		""" verify if list is a triangle """
		if not self.triangle:
			return False
		elif self.lengthTriangle < 1:
			return False
		else:
			return True

	def maximumTotal(self):
		""" returns the sum and the path of the maximum total of a triangle """
		if not self.verifyTriangle():
			return False

		col = -1
		val = 0	
		for i in range(-1, self.lengthTriangle):
			(val,col) = self.maximumTotalAux(i+1,col)
			self.path.append(col)
			self.sum += val

		return (self.sum,self.path)

	def maximumTotalAux(self,i,col):
		""" compare and get biggest value on next column """
		if self.getLeftValueCol(i,col) > self.getRightValueCol(i,col):
			return (self.getLeftValueCol(i,col),col)
		else:
			return (self.getRightValueCol(i,col),col+1)

	def getRightValueCol(self,i,col):
		""" get right value on next column """
		return self.triangle[i][col+1]

	def getLeftValueCol(self,i,col):
		""" get left value on next column """
		return self.triangle[i][col]

