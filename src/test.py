#!/usr/bin/python3.4

import unittest

from triangle import Triangle

class TriangleTest(unittest.TestCase):

	def test_maximumTotal_return_true_result(self):
		triangle = [[6],[3,5],[9,7,1],[4,6,8,4]]
		T = Triangle(triangle)
		(val, path) = T.maximumTotal()
		self.assertEqual(val,26)
		self.assertEqual(path, [0, 1, 1, 2] )

        def test_maximumTotal_return_true_result2(self):
                triangle = [[6],[3,5]]
                T = Triangle(triangle)
                (val, path) = T.maximumTotal()
                self.assertEqual(val,11)
                self.assertEqual(path, [0, 1] )

	def test_if_list_is_a_triangle(self):
		triangle = [1]
		T = Triangle(triangle)
		(res) = T.maximumTotal()
		self.assertEqual(res,False)

	def test_if_list_is_empty(self):
		triangle = []
		T = Triangle(triangle)
		(res) = T.maximumTotal()
		self.assertEqual(res,False)


if __name__ == '__main__':
	unittest.main()
