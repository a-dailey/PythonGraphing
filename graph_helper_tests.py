import unittest
from graph import *

class TestList(unittest.TestCase):

    def test_01(self):
        g = Graph('test10.txt')
        self.assertEqual(g.get_vertex('v8').key, 'v8')
        self.assertEqual(g.get_vertex('1000'), None)

if __name__ == '__main__':
   unittest.main()