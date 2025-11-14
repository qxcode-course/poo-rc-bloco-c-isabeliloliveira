class Cliente:
    def __init__(self, nome: str):
        self.nome = nome

    def getNome(self):
        return self.nome
    
    def toString(self):
        return f"{self.nome}"
    
class Mercado:
    def __init__(self, n_caix: int) -> None:
        self.espera: list[Cliente]=[]
        self.caixas: list[Cliente | None]=[]
        for _ in range(n_caix):
            self.caixas.append(None)
        
    def chegarC(self, cliente:Cliente): 
        self.espera.append(cliente)
    
    def chamarC(self, index: int):

        if self.caixas[index] is not None:
            print("fail: caixa ocupado")
            return

        if len(self.espera)==0:
            print("fail: sem clientes")
            return
        
        self.caixas[index]=self.espera[0]

        del self.espera[0]
        
    def finalizarA(self,index: int ):
        if index < 0 or index >= len(self.caixas):
            print("fail: caixa inexistente")
            return None
    
        if self.caixas[index] is None:
            print("fail: caixa vazio")
            return None

        aux=self.caixas[index]
        self.caixas[index]=None
        return aux
    
    # def sair(self, nome:str) -> Cliente | None:


    def __str__(self):
        caixas=",",join([str(x) if x else "----" for x in self.caixas])
        espera = ", ".join([str(x) for x in self.espera]),
        return f"Caixas: [{caixas}]\nEspera: [{espera}]"
    
        # def to_str(cliente: Cliente | None) -> str:
        #     if cliente is None:
        #         return "-----"
        #     return str(cliente)
        

def main ():
    mercado = Mercado()

    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "finish":
            # break
        elif args[0] == "show":
            print(mercado)
            
        elif args[0] == "init":

        # elif args[0] == "call":

        # elif args[0] == "enter":
        
        # elif args[0] == "arrive":
        #     Mercado.chamarC(args[1])


main()