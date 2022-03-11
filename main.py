import yaml
import os

from utils import log, DEBUG
from graph import Vertex, UndirectedWeightedGraph
from floyd_warshall import floyd_warshall, print_solution, print_sol_mat


if __name__ == '__main__':

    with open('data.yaml', 'r') as db_yaml:
        data = yaml.load(db_yaml, Loader=yaml.FullLoader)

    # read all vertices
    vertices_lst = []
    for record in data:
        v = Vertex(int(record['id']), record['desc'])
        if record.get('adjacent_list') is not None:
            for e in record['adjacent_list']:
                v.add_neighbor(e['id'], e['weight'])

        vertices_lst.append(v)

    # init graph
    g = UndirectedWeightedGraph(len(vertices_lst))

    # add vertices
    for v in vertices_lst:
        g.add_vertex(v)

    # add edges
    for v1 in g.vertices_lst:
        for item in v1.adjacent:
            v2 = g.find_vertex(item['id'])
            if v2 is None:
                log("No vertex id={} in graph.".format(item['id']))
                sys.exit(1)
            g.add_edge(v1, v2, item['weight'])

    ### graph summary ###
    log(g.num_vertices)
    log(g.num_edges)
    # g.print_vertices()
    # g.print_graph()


    sol_mat = floyd_warshall(g.adj_mat, g.num_vertices)
    # print_sol_mat(sol_mat)
    print_solution(g, sol_mat, 0, 1)

    