import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


class Neuron:
    def __init__(self, n_inputs, bias=0., weights=None):
        self.b = bias
        if weights:
            self.ws = np.array(weights)
        else:
            self.ws = np.random.rand(n_inputs)

    def _f(self, x):
        return max(x * .1, x)

    def __call__(self, xs):
        return self._f(xs @ self.ws + self.b)

class NeuralNetwork:
    def __init__(self, layers):
        self.layers = layers
        self.network = self._build_network()

    def _build_network(self):
        network = []
        for i, (n_inputs, n_neurons) in enumerate(self.layers):
            layer = []
            for _ in range(n_neurons):
                layer.append(Neuron(n_inputs))
            network.append(layer)
        return network

    def forward(self, inputs):
        for layer in self.network:
            outputs = []
            for neuron in layer:
                outputs.append(neuron(inputs))
            inputs = outputs
        return inputs

    def visualize(self):
        G = nx.DiGraph()
        layer_sizes = [layer[1] for layer in self.layers]

        max_layer_size = max(layer_sizes)
        pos = {}
        node_labels = {}

        for i, size in enumerate(layer_sizes):
            for j in range(size):
                node_id = f"L{i}_N{j}"
                G.add_node(node_id)
                pos[node_id] = (i, -j + (max_layer_size - size) / 2)
                #node_labels[node_id] = f"N{j}"

        for i in range(len(layer_sizes) - 1):
            for j in range(layer_sizes[i]):
                for k in range(layer_sizes[i + 1]):
                    G.add_edge(f"L{i}_N{j}", f"L{i + 1}_N{k}")

        nx.draw(G, pos, with_labels=True, labels=node_labels, node_size=2000, node_color='skyblue', font_size=10, font_color='black', font_weight='bold')
        plt.title('Neural Network Structure')
        plt.show()

layers = [(2, 3), (3, 4),(4,4),(4,1)]
nn = NeuralNetwork(layers)

input_data = np.array([1.0, 2.0])
result = nn.forward(input_data)
print("result:", result)

nn.visualize()
