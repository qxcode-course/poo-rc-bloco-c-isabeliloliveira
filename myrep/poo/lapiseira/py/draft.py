#tentando deixar tudo em inglês pelo menos uma vez na vida.

class Lead:
    def __init__(self, hardness: str, thickness: float, size: int):
        self.__hardness = hardness
        self.__thickness = thickness
        self.__size = size

    def usagePerSheet(self):
        if self.__hardness == "HB":
            return 1
        elif self.__hardness

    def getHardness(self):
        return self.__hardness
    
    def getThickness(self):
        return self.__thickness
    
    def getSize(self):
        return self.__size
    
    def setSize(self, size: int):
        self.__size=size

    # def __str__(self) -> str:
    #     return f"[{self.__thickness}:{self.__hardness}:{self.__size}]"
    
class Pencil:
    def __init__(self):
        self.__thickness: int 
        self.__tip: Lead | None
        # self.__barrel: 
    
    def insert(self, Lead: Lead):
        self.__thickness: 

    
    def __str__(self) -> str:
        return f"calibre: {self.__thickness}, bico: [{self.__hardness}], tambor: <[{self.__barrel}]>"
    
def main(self):
    pencil = Pencil()
 
    while True:
        line = input()
        print("$"+line)
        if args[0]=="end":
            break
        elif args[0]=="show":
            print(pencil)
        
        elif args[0]=="insert":
            lead=Lead(float(args[1]), args[2], int(args[3]))
            pencil.insert(lead)
        
main()
