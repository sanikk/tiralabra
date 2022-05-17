class Mock_Gui:
    """ Mock GUI with update_gui method for printing """

    def __init__(self, give_output=False):
        self.list_of_inputs = []
        self.give_output = give_output

    def update_dijkstra(self, round, heap, handled, distances):
        self.list_of_inputs.append(
            (round, heap, distances, handled))
        if self.give_output:
            print(f"""{round=}\n 
            {len(heap)=}
            {heap[0]=}
            {distances=}
            {handled=}""")

    def update_ida(self, path, cost_here, estimated_cost):
        if self.give_output:
            print(f"""Round: {len(path)}\n
            {path=}
            {cost_here=}
            {estimated_cost=}""")

    def get_input_from_round(self, round: int):
        """ For testing: returns the inputs of update_gui on round (round)
        """
        if round > 0 and round < self.list_of_inputs:
            return self.list_of_inputs[round - 1]
        return None
