def add(x,y):
	return x + y

import unittest

class test_add(unittest.TestCase):

	def test_add(self):
		result = add(3,2)
		message = "Failed add test"
		self.assertEqual(result,5,message)