import yaml
import os

from graph import Vertex, UndirectedWeightedGraph

if __name__ == '__main__':
    with open('data.yaml', 'r') as db_yaml:
        data = yaml.load(db_yaml, Loader=yaml.FullLoader)

    # read all vertices
    vertices_lst = []
    for record in data:
        v = Vertex(int(record['id']), record['desc'])
        if record.get('linked_vertices') is not None:
            for e in record['linked_vertices']:
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
                print("No vertex id={} in graph.".format(item['id']))
                sys.exit(1)
            g.add_edge(v1, v2, item['weight'])

    ### graph summary ###
    print(g.num_vertices)
    print(g.num_edges)
    # g.print_vertices()
    g.print_graph()
    