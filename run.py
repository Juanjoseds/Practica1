# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)
print("Anchura: ")
print(search.breadth_first_graph_search(ab).path())
print("Profundidad: ")
print(search.depth_first_graph_search(ab).path())
print("Ramificación: ")
print(search.ramificacion_first_graph_search(ab).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
