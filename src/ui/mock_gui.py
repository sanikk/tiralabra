class Mock_Gui:
    """ Mock GUI with update_gui method for printing """

    def __init__(self):
        self.list_of_inputs = []

    def update_gui(self, round, heap_size, handled, distances):
        self.list_of_inputs.append((round, heap_size, distances, handled))
        print(f"""{round=}\n 
            {heap_size=}\n
            {distances=}\n
            {handled=}""")

    def get_input_from_round(self, round: int):
        """ For testing: returns the inputs of update_gui on round (round)
        """
        if round > 0 and round < self.list_of_inputs:
            return self.list_of_inputs[round - 1]
        return None
