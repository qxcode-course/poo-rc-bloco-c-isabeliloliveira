class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome

    def getNome(self):
        return self.nome
    
    def toString(self):
        return f"{self.nome}"
    
class Mercado:
    def __init__(self, n_cad: int) -> None:
        self.espera: list[Pessoa]=[]
        self.caixas: list[Pessoa | None]=[]
        for _ in range(n_cad):
            self.caixas.append(None)
        
    def chegarC(self, pessoa:Pessoa):
        self.espera.append(pessoa)
    
    def chamarC(self, index: int):
        if index < 0 or index >= len(self.caixas):
            print("index invalido")
            return
        
        if self.caixas[index] is not None:
            print("caixa ocupado")
            return

        if len(self.espera)==0:
            print("ninguém esperando")
            return
        
        self.caixas[index]=self.espera[0]

        del self.espera[0]
        
    def finalizarA(self, ):
        

    def __str__(self):
        caixas=","
        # def to_str(pessoa: Pessoa | None) -> str:
        #     if Pessoa is None:
        #         return "-----"
        #     return str(pessoa)
        

def main ():
    mercado = Mercado("")

    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "finish":
            # break
        elif args[0] == "show":
            print(mercado)
            
        elif args[0] == "init":
main()