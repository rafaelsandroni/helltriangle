#!/usr/bin/env python
import sys
import time
from triangle import Triangle

arr = [[6],[3,5],[9,7,1],[4,6,8,4]]

t = time.time()

Triangle = Triangle(arr)
(sum,path) = Triangle.maximumTotal()

t = time.time() - t

print("========== results ==========")
print(" triangle: %s " % (arr))
print(" maximum total: %d" % (sum))
print(" path: %s " % (path))
print(" execution time: %fs" % (t))
print("=============================")
