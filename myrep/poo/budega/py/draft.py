class Pessoa:
    def __init__(self) -> None:
        
class Mercado:
    def __init__(self, n_cad: int) -> None:
        self.espera: list[Pessoa]=[]
        self.caixas: list[Pessoa | None]=[]
        for _ in range(n_cad):
            self.caixas.append(None)
        
    def chegarC(self, pessoa:Pessoa):
        self.espera.append(pessoa)
    
    def chamarC(self, index: int):

    def finalizarA(self):


    def __str__(self):
        def to_str(pessoa: Pessoa | None) -> str:
            if Pessoa is None:
                return "-----"
            return str(pessoa)