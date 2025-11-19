class Kid:
    def __init__(self):
        self.__age: int
        self.__name:str    

    def get_age(self):
        return self.__age
    
    def get_name(self):
        return self.__name
    
    def set_age(self, age:int):
        self.__age=age

    def set_name(self, name:str):
        self.__name=name

    def __str__(self):
          return f""





class Trampoline:
    def __init__(self):
        self.playing: list[Kid]
        self.waiting: list[Kid]

    def arrive(self, kid:Kid):

    def enter(self):


    def leave(self):

    def removeKid(name: str) -> Kid|None:


def main():
    trampoline=Trampoline()
    while True:
        line=input()
        print("$"+line)
        args=line.split("")

        if args[0]=="end":
            break
        elif args[0]=="show":
            print(trampoline)
        elif args[0]=="enter":
            
