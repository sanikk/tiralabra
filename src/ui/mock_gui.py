class Mock_Gui:
    def __init__(self):
        pass

    def update_gui(self, kierros, heap_size, kasitellyt, etaisyydet):
        print(f"""Kierros: {kierros}\n 
            Keon koko: {heap_size}\n
            Etaisyydet: {etaisyydet}\n
            Kasitelty: {kasitellyt}""")
