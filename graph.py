from stack_array import *  # Needed for Depth First Search
from queue_array import *  # Needed for Breadth First Search


class Vertex:
    '''Add additional helper methods if necessary.'''

    def __init__(self, key, id, adjacent_to=[], color=None):
        '''Add other Attributes as necessary'''
        self.color = color
        self.key = key
        self.adjacent_to = adjacent_to
        self.visited = [False, False]
        self.id = id


class Graph:
    '''Add additional helper methods if necessary.'''

    def __init__(self, filename):
        vertices = open(filename, "r")
        self.graph = {}
        pair = vertices.readline()
        while pair != '':
            vertice = pair.split()
            for v in vertice:
                self.add_vertex(v)
            self.add_edge(vertice[0], vertice[1])
            pair = vertices.readline()
        vertices.close()





        # '''reads in the specification of a graph and creates a graph using an adjacency list representation.
        #    You may assume the graph is not empty and is a correct specification.  E.g. each edge is
        #    represented by a pair of vertices.  Note that the graph is not directed so each edge specified
        #    in the input file should appear on the adjacency list of each vertex of the two vertices associated
        #    with the edge.'''
        # This method should call add_vertex and add_edge!!!

    def add_vertex(self, key):
        if key not in self.graph:
            self.graph[key] = Vertex(key, 0, [])

        # Should be called by init
        # '''Add vertex to graph only if the vertex is not already in the graph.'''

    def add_edge(self, v1, v2):
        self.graph[v1].adjacent_to.append(v2)
        self.graph[v2].adjacent_to.append(v1)
        # Should be called by init
        # '''v1 and v2 are vertex ID's. As this is an undirected graph, add an
        #    edge from v1 to v2 and an edge from v2 to v1.  You can assume that
        #    v1 and v2 are already in the graph'''

    def get_vertex(self, key):
        if key in self.graph:
            return self.graph[key]
        return None
        # '''Return the Vertex object associated with the ID. If ID is not in the graph, return None'''

    def get_vertices(self):
        id = []
        for key in self.graph:
            id.append(key)
        id.sort()
        return id

        # '''Returns a list of ID's representing the vertices in the graph, in ascending order'''
    def conn_components(self):
        stack = Stack(len(self.graph))
        id = -1

        for vert in self.get_vertices():
            if not self.graph[vert].visited[0]:
                # self.graph[vert].visited[0] = True
                stack.push(self.graph[vert])
                self.conn_help(self.graph[vert], stack)
                id += 1

            while not stack.is_empty():
                v = stack.pop()
                v.id = id

        size = id + 1
        print("size:", size)
        components = [ [] for i in range(id + 1) ]
        print("len:", len(components))
        for vert in self.graph:
            idx = self.graph[vert].id
            components[idx] += [self.graph[vert].key]
        for lst in components:
            lst.sort()
        print(components)
        return components


    def conn_help(self, vert, stack):
        vert.visited[0] = True
        for v in vert.adjacent_to:
            if not self.graph[v].visited[0]:
                # self.graph[v].visited[0] = True
                stack.push(self.graph[v])
                self.conn_help(self.graph[v], stack)







    # def conn_components2(self):
    #     stack = Stack(len(self.graph))
    #     id = 0
    #     for vert in self.graph:
    #         if self.graph[vert].visited[0] == False:
    #             self.add_to_stack(self.graph[vert], stack, id)
    #             id += 1
    #
    #     components = [[]] * id
    #     for vert in self.graph:
    #         components[self.graph[vert].id].append(vert)
    #     for lst in components:
    #         lst.sort()
    #     return components
    #
    # def add_to_stack(self, vert, stack, id):
    #     print(vert.key)
    #     if vert.visited[0] == False:
    #         stack.push(vert)
    #         vert.visited[0] = True
    #         vert.id = id
    #     dead_end = True
    #     for verts in vert.adjacent_to:
    #         if self.graph[verts].visited[0] == False:
    #             dead_end = False
    #             self.add_to_stack(self.graph[verts], stack, id)
    #     if dead_end:
    #         print(stack.pop().key)
    #         if not stack.is_empty():
    #             self.add_to_stack(stack.peek(), stack, id)

        # '''Return a Python list of lists.  For example: if there are three connected components
        #    then you will return a list of three lists.  Each sub list will contain the
        #    vertices (in ascending alphabetical order) in the connected component represented by that list.
        #    The overall list will also be in ascending alphabetical order based on the first item in each sublist.'''
        # This method MUST use Depth First Search logic!

    def is_bipartite(self):
        q = Queue(len(self.graph) + 1)
        for vert in self.graph:
            current = self.graph[vert]
            if current.visited[1] == False:
                q.enqueue(current)
                self.graph[vert].visited[1] = True
                self.graph[vert].color = 1
                self.add_to_queue(q.dequeue(), q)

        for vert in self.graph:
            for adj in self.graph[vert].adjacent_to:
                if self.graph[adj].color == self.graph[vert].color:
                    return False
        return True
        # '''Return True if the graph is bipartite, False otherwise.'''
        # This method MUST use Breadth First Search logic!

    def add_to_queue(self, vert, q):
        if vert.color == 1:
            color = 0
        elif vert.color == 0:
            color = 1
        for verts in vert.adjacent_to:
            if self.graph[verts].visited[1] == False:
                self.graph[verts].visited[1] = True
                self.graph[verts].color = color
                q.enqueue(self.graph[verts])
        if not q.is_empty():
            self.add_to_queue(q.dequeue(), q)

