from ui.mock_gui import Mock_Gui
from entities.graph import Edge, Graph
# Verkon mallia pitää miettiä että saan sen tänne kätevästi käyttöön.
#
# Miten tehdä heuristiikka funktio tän hetkiselle verkolle? goal# - node#


class Ida_star:

    def __init__(self, GUI: Mock_Gui, graph: Graph, root=-1, goal=-1):
        self.graph = graph
        self.root = root
        self.goal = goal
        self.GUI = GUI

    def is_goal(self, node):
        return self.goal == node

    def h(self, node):
        """ the heuristic function for DIA*
        First mock this with pythagorean calculation of distance to goal or something
        """
        arvio = (self.goal-node) * self.graph.average_weight * \
            (self.graph.vertices / self.graph.number_of_edges)
        return abs(self.goal-node)

    def search(self, path: list, cost_here, bound):
        """
        path = current search path (acts as stack)
        node = current node
        bound = 
        """
        node = path[-1]
        cheapest_estimate = cost_here + self.h(node)
        self.GUI.update_ida(path, cost_here, cheapest_estimate)
        if cheapest_estimate > bound:
            return cheapest_estimate
        if self.is_goal(node):
            return 'FOUND'
        minimi = -1
        ss = self.search
        for edge in self.graph.give_edges(node):
            # successors(node):
            if edge.end not in path:
                path.append(edge.end)  # korvattu push appendilla
                t = ss(path, cost_here + edge.weight, bound)
                if t == 'FOUND':
                    return 'FOUND'
                if minimi == -1 or t < minimi:
                    minimi = t
                path.pop()
        return minimi

    def process(self, root):
        bound = self.h(root)
        path = [root]
        print(f'{path=}')
        while True:
            t = self.search(path, 0, bound)
            if t == 'FOUND':
                return (path, bound)
            if t == -1:
                return 'NOT_FOUND'
            bound = t

    # Setters for changing class values
    def change_graph(self, graph):
        self.graph = graph

    def change_goal(self, node):
        self.goal = node

    def change_root(self, node):
        self.root = node
