import numpy as np
from math import sqrt, log

def mc_random_Q(simulator):
<<<<<<< Updated upstream
=======
    """
    Please modify the body of this function according to the description in exercise 3.1
    """
>>>>>>> Stashed changes
    k = simulator.getNumActions()
    q_a = np.zeros(k)
    n_a = np.zeros(k)
    a = np.array([-1, 1])
    counter = 0
    while counter < 10_000:
        y = simulator.reset()
        random_a = np.random.choice(a)
        first_action = random_a
        r, y, done = simulator.step(random_a)
        counter += 1
        total_r = r
        while not done and counter < 10_000:
            random_a = np.random.choice(a)
            r, y, done = simulator.step(random_a)
            counter += 1
            total_r += r
        if first_action == -1:
            q_a[0] += total_r
            n_a[0] += 1
        else:
            q_a[1] += total_r
            n_a[1] += 1
    return q_a[0]/n_a[0], q_a[1]/n_a[1]
<<<<<<< Updated upstream
=======


class Node:
    def __init__(self, parent=None):
        self.q_value = 0  # Total reward
        self.visits = 0  # Number of times it's been visited
        self.children = {}  # Child nodes
        self.parent = parent  # Parent node
>>>>>>> Stashed changes

def mc_uct_Q(simulator):
    beta = 2
    root = Node()

    for _ in range(10000):
        node = root
        path = []

        # Selection and expansion
        simulator.reset()
        while node.children:
            if len(node.children) < simulator.getNumActions():
                a = len(node.children)
                node.children[a] = Node(parent=node)
            else:
                a = ucb1_select(node, beta)
            path.append((node, a))
            _, _, done = simulator.step(2 * a - 1)
            node = node.children[a]

        # Simulation
        r_total = 0
        done = False
        while not done:
            a = np.random.choice(simulator.getNumActions())
            r, _, done = simulator.step(2 * a - 1)
            r_total += r

        # Backpropagation
        for node, a in path:
            node.visits += 1
            node.children[a].visits += 1
            node.children[a].q_value += r_total

    return np.array([root.children[a].q_value / root.children[a].visits if a in root.children else 0 for a in range(simulator.getNumActions())])

def ucb1_select(node, beta):
    return max(node.children, key=lambda a: node.children[a].q_value / node.children[a].visits + beta * np.sqrt(np.log(node.visits) / node.children[a].visits))