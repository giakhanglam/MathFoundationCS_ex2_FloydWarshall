import numpy as np
# from utils import log, DEBUG
import sys

INF = np.inf

def print_sol_mat(mat):
    pass

# Floyd Warshall algorithm
def floyd_warshall(mat_graph, num_vertices):

    # init solution matrix is a 3D matrix NxNx2
    # each cell [i][j] = [val, idx] where:
    #   + val = mat_graph[i][j]
    #   + idx = -1. idx will be updated with the 'id' of intermediate vertex
    #           leads to shortest path between i & j (ex: i -> idx -> j)
    distance = []
    for k in range(num_vertices):
        distance.append([INF for k in range(num_vertices)])
    for i in range(num_vertices):
        for j in range(num_vertices):
            distance[i][j] = [mat_graph[i][j], -1]

    # Choose each vertex as intermediate vertex
    for k in range(num_vertices):
        # Choose each vertex as source
        for i in range(num_vertices):
            # Choose each vertex as destination
            for j in range(num_vertices):
                if distance[i][k][0] + distance[k][j][0] < distance[i][j][0]:
                    # update shortest value
                    distance[i][j][0] = distance[i][k][0] + distance[k][j][0]
                    # update intermediate value
                    distance[i][j][1] = k

    return distance


# Recursive retrieve the path from source vertex to destination vertex
def retrive_path(graph_obj, sol_mat, src, dest):
    int_v_id = sol_mat[src.id][dest.id][1]

    # base condition
    if int_v_id == -1:
        print(src)
        return

    int_vertex = graph_obj.find_vertex(int_v_id)
    if int_vertex is None:
        print("Cannot find intermediate id={}".format(int_v_id))
        sys.exit(1)

    retrive_path(graph_obj, sol_mat, src, int_vertex)
    retrive_path(graph_obj, sol_mat, int_vertex, dest)
 
# Function to print the shortest path
# between given source & destination vertices
def print_solution(graph_obj, sol_mat, src_v_id, dest_v_id):
    # retrieve src vertex
    src_v = graph_obj.find_vertex(src_v_id)
    if src_v is None:
        print("Cannot find source id={}".format(src_v_id))
        sys.exit(1)

    # retrieve dest vertex
    dest_v = graph_obj.find_vertex(dest_v_id)
    if dest_v is None:
        print("Cannot find destination id={}".format(dest_v_id))
        sys.exit(1)

    print("Length of shortest path from '{}' to '{}': {}".format(src_v.desc, dest_v.desc, sol_mat[src_v_id][dest_v_id][0]))
    print("Details:\n")
    retrive_path(graph_obj, sol_mat, src_v, dest_v)
    print(dest_v)


if __name__ == '__main__':
    pass
