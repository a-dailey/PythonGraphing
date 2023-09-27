import unittest
from graph import *

class TestList(unittest.TestCase):
    # def test_0111(self):
    #     g = Graph('test10.txt')
    #     self.assertEqual(g.get_vertex('v8').key, 'v8')
    #     self.assertEqual(g.get_vertex('1000'), None)

    def test_01(self):
        g = Graph('test1.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())
        self.assertEqual(g.get_vertices(), ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9'])
        
    def test_02(self):
        g = Graph('test2.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(g.is_bipartite())


    def test_03(self):
        g = Graph('test3.txt')
        self.assertEqual(g.conn_components(), [['1', '2', '3', '4', '5', '6', '7', '8']])
        self.assertFalse(g.is_bipartite())

    def test_04(self):
        g = Graph('test4.txt')
        self.assertEqual(g.conn_components(), [['1', '10', '2', '3', '5', '6', '7', '8', '9'], ['11', '12', '13', '14', '15'],
                                               ['a', 'b', 'c', 'd', 'e', 'f']])
        self.assertTrue(g.is_bipartite())

    def test_05(self):
        g = Graph('test5.txt')
        
        self.assertEqual(g.get_vertex('1000'), None)
        self.assertEqual(g.conn_components(), [['1', '10', '2', '3', '5', '6', '7', '8', '9'], ['100', '200', '300', '400', '500', '600'],
                                               ['11', '12', '13', '14', '15'], ['a', 'b', 'c', 'd', 'e', 'f']])
        self.assertFalse(g.is_bipartite())

    def test_06(self):
        g = Graph('test6.txt')
        self.assertEqual(g.conn_components(), [['a', 'b', 'c']])
        self.assertFalse(g.is_bipartite())

    def test_07(self):
        g = Graph('test7.txt')
        self.assertEqual(g.conn_components(), [['1', '2']])
        self.assertTrue(g.is_bipartite())

    def test_08(self):
        g = Graph('test8.txt')
        self.assertEqual(g.conn_components(), [['dog', 'file', 'hi', 'house', 'pearl', 'red']])
        self.assertTrue(g.is_bipartite())

    def test_09(self):
        g = Graph('test9.txt')
        self.assertEqual(g.conn_components(), [['bye', 'green', 'hello', 'part'], ['dog', 'file', 'hi', 'house', 'pearl', 'red']])
        self.assertFalse(g.is_bipartite())

    def test_10(self):
        g = Graph('test10.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())

    def test_11(self):
        g = Graph('test11.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4'], ['v10', 'v11', 'v12', 'v13', 'v14', 'v15', 'v16', 'v17', 'v18', 'v19', 'v20', 'v5', 'v6', 'v7', 'v8', 'v9'], ['v991', 'v992', 'v993', 'v994', 'v995', 'v996']])
        self.assertTrue(g.is_bipartite())

    def test_03b(self):
        g = Graph('test3_crown.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5', 'v6']])
        self.assertTrue(g.is_bipartite())

    def test_07b(self):
        g = Graph('test7_grid.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5', 'v6']])
        self.assertTrue(g.is_bipartite())



if __name__ == '__main__':
   unittest.main()
