# from typing import Dict, Union, List, Iterable
import numpy as np

class Vertex:
    def __init__(self, id: int, desc: str):
        self.id = id
        self.desc = desc
        self.adjacent = []

    def __str__(self):
        return "id={}, desc={}".format(self.id, self.desc)

    def add_neighbor(self, neighbor_id: int, weight: int):
        self.adjacent.append({'id': neighbor_id, 'weight': weight})

    def get_connections(self):
        return self.adjacent


class UndirectedWeightedGraph:

    def __init__(self, size):
        self.adj_mat = []
        for i in range(size):
            self.adj_mat.append([0 for i in range(size)])
        self._size = size
        self.vertices_lst = []
        self._num_vertices = 0
        self._num_edges = 0

    @property
    def Size(self):
        return self._size

    @property
    def num_vertices(self):
        return self._num_vertices

    @num_vertices.setter
    def num_vertices(self, value: int):
        self._num_vertices = value

    @property
    def num_edges(self):
        return self._num_edges

    @num_edges.setter
    def num_edges(self, value: int):
        self._num_edges = value

    def add_vertex(self, v: Vertex):
        if self.num_vertices < self.Size:
            if self.find_vertex(v.id) is None:
                self.vertices_lst.append(v)
                self.num_vertices += 1
            else:
                print("Vertex ID = {} already existed.".format(v.id))
        else:
            print("Reach maximum number of vertices {}. Abort!".format(self.Size))


    def add_edge(self, v1: Vertex, v2: Vertex, weight: int):
        if v1.id == v2.id:
            print("Same vertex id={}. Abort!".format(v1.id))
        elif self.adj_mat[v1.id][v2.id] == weight:
            print("Edge between vetices id={} and id={} already existed. Abort!".format(v1.id, v2.id))
        else:
            self.adj_mat[v1.id][v2.id] = weight
            self.adj_mat[v2.id][v1.id] = weight
            self.num_edges += 1

    def print_graph(self):
        # for row in self.adj_mat:
        #     for val in row:
        #         print("{:4}".format(val))
        print(np.array(self.adj_mat))

    def print_vertices(self):
        for v in self.vertices_lst:
            print(v, end='\n')

    def is_vertex_existed(self, vertex_ID: int):
        for v in self.vertices_lst:
            if v.id == vertex_ID:
                return True
        return False

    def find_vertex(self, vertex_ID: int):
        for v in self.vertices_lst:
            if v.id == vertex_ID:
                return v
        return None

