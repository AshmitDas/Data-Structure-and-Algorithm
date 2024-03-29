class Graph:

    def __init__(self) -> None:
        self.adj_list = {}

    def add_vertex(self, vertex):
        """Big O: O(1)"""
        # Adds a node to the Graph.
        
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        """Big O: O(1)"""
        # connect two nodes in a graph

        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        """Big O: O(|E|)"""
        # Removes a connection between two nodes.

        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        """Big O: O(|V|+|E|)"""
        # Removes a node from the graph.

        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

    def print_graph(self):
        """Big O: O(|V|+|E|)"""
        # Prints the whole graph
        
        for vertex in self.adj_list:
            print(vertex, ":",self.adj_list[vertex])



mygraph = Graph()

mygraph.add_vertex('A')
mygraph.add_vertex('B')
mygraph.add_vertex('C')
mygraph.add_vertex('D')

mygraph.add_edge('A', 'B')
mygraph.add_edge('A', 'C')
mygraph.add_edge('A', 'D')
mygraph.add_edge('B', 'D')
mygraph.add_edge('C', 'D')

# mygraph.remove_edge('A', 'D')
mygraph.remove_vertex('D')

mygraph.print_graph()