############################################################
# This is a implementation of DEEPWALK
#
############################################################
import numpy as np
import random


class DeepWalk:
  # 'This is DeepWalk!!!'


  def __init__(self, graph, walks_per_node, walk_length, window_size, embedding_size, learning_rate):
    self.graph = graph
    self.walks_per_node = walks_per_node
    self.walk_length = walk_length
    self.window_size = window_size
    self.embedding_size = embedding_size
    self.learning_rate = learning_rate
    self.delta = None
    self.start_deep_walk()

  def init(self):
    print('hello')
    # sample delta from U^|V|x|d|
    pass


  def create_binary_tree(self):
    pass


  def random_walk(self, root):
    vertices = []
    neigh_bors = root.neigh_bors()
    for i in range(self.walk_length):
      new_vertex = random.choice(neigh_bors)
      vertices.append(new_vertex)
      neigh_bors = new_vertex.neigh_bors()
    return vertices

    # Do a RandomWalk with root is root
    pass


  def derivative(self, J_delta):
    pass


  def probability(self, u_k, delta):
    pass


  def skip_gram(self, walk):
    for j in range(len(walk)):
      for u_k in walk[j - self.window_size : j + self.window_size]:
        J_delta = -np.log(self.probability(u_k, self.delta[j]))
        self.delta = self.delta - self.learning_rate * self.derivative(J_delta)
    pass


  def start_deep_walk(self):
    self.init()
    tree = self.create_binary_tree()
    for i in range(self.walks_per_node):
      shuffle_list = graph.shuffle()
      for vertex in shuffle_list:
        walk = self.random_walk(vertex)
        self.skip_gram(walk)
    pass

a = DeepWalk(None, None, None, None, None)

