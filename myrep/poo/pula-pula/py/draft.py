class Kid:
    def __init__(self, name:str, age:int):
        self.__age = age
        self.__name = name    

    def get_age(self):
        return self.__age
    
    def get_name(self):
        return self.__name
    
    def set_age(self, age:int):
        self.__age=age

    def set_name(self, name:str):
        self.__name=name

    def __str__(self):
          return f"{self.__name}:{self.__age}"





class Trampoline:
    def __init__(self):
        self.__playing:list[Kid|None]=[]
        self.__waiting:list[Kid|None]=[]

    def arrive(self, name:str, age:int):
        self.__waiting.insert(0, Kid(name, age))

    def enter(self):
        if not self.__waiting:
            print(f"fila vazia")
        self.__playing.insert(0, self.__waiting[len(self.__waiting)-1])
        self.__waiting.pop(len(self.__waiting)-1)


    def leave(self):

    def removeKid(self, name: str) -> Kid|None:

    def __str__(self):
        ps=", ".join(str(k) for k in self.__playing)
        ws=", ".join(str(k) for k in self.__waiting))
        return f"[{ws}]=>[{ps}]"



def main():
    trampoline=Trampoline()
    while True:
        line=input()
        print("$"+line)
        args=line.split(" ")

        if args[0]=="end":
            break
        elif args[0]=="show":
            print(trampoline)
        elif args[0]=="enter":
            return
        elif args[0]=="arrieve":
            trampoline.arrive(args[1], int(args[2]))

        elif args[0]=="leave":
            trampoline.leave()
        
        elif args[0]=="remove":
            trampoline.removeKid(args[1])

        else:
            print("fail: comando invalido")

main()
