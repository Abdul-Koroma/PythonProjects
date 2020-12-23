import random

class Vertex(object):
    def __init__(self, value):
        self.value = value # value will be the word
        self.adjacent = {}  # nodes that have an edge from this vertex
        self.neighbors = []
        self.neighbors_weights = []

    def __str__(self):
        return self.value + ' '.join([node.value for node in self.adjacent.keys()])

    def add_edge_to(self, vertex, weight=0):
        self.adjacent[vertex] = weight # adding an edge to the vertext we input with weight user may input

    def increment_edge(self, vertex):
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1 # incrementing the weight of the edge

    def get_adjacent_nodes(self):
        return self.adjacent.keys()

    # initializes probability map
    def get_probability_map(self):
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbors_weights.append(weight)

    def next_word(self):
        return random.choices(self.neighbors, weights=self.neighbors_weights)[0] # randomly select the next word based on weights



class Graph(object):
    def __init__(self):
        self.vertices = {}

    def get_vertex_values(self):
        return set(self.vertices.keys()) # returns all possible words

    def add_vertex(self, value):
        self.vertices[value] = Vertex(value) 

    def get_vertex(self, value):
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value] # get vertex of the value; If not here just add it in

    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()
