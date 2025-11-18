# a: list[str] 
#ordem de inserção é mportante
# b: dict[str, Algo] 
# Existe uma chave; ordem de inserção não é importante;

class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome=nome
        self.idade=idade
    
    def __str__(self):
        return f"{self.nome}:{self.idade}"
#chave - o que é uma chave

class Repositorio:
    def __init__(self):
        self.pessoas:dict[str, Pessoa]={}

    # crud

    def add_pessoa(self, pessoa:Pessoa):
        if pessoa.nome in self.pessoas:
            raise Exception(f"Pesssoa de nome {pessoa.nome} já existe")
        self.pessoas[pessoa.nome]=pessoa

    def get_pessoa(self, nome: str):
        try:
            return self.pessoas[nome]
        except KeyError as _:
            raise Exception(f"Pessoa de nome {nome} não existe")
        
    def del_pessoa(Self, nome:str):
        if nome not in self.pessoas:
            raise Exception(f"Pessoa de nome {nome} não existe")
        
        del self.pessoas[nome]


    def list_pessoas(self)->list[str]:
        output:list[Pessoa]=[Pessoa]
        for pessoa in self.pessoas.values():
            output.append(pessoa)
        def criterio(pessoa:Pessoa):
            return pessoa.nome

        # funções lambda
        # função anonima que carrega contexto
        output.sort(key=lambda pessoa:pessoa.nome, reverse=False)
        return output


        return list(self.pessoas.values())
    
def main():
    rep = Repositorio()
    while true:
        print("$", end="")
        line=input()
        args=line.split(" ")
        try:
            if args[0]=="end":
                break
            elif args[0]=="add":
                rep.add_pessoa(Pessoa(args[1]), int(args[2]))
            elif args[0]=="get":
                print(rep.get_pessoa(Pessoa(args[1]), int(args[2]))

        Exception