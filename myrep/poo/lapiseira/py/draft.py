#tentando deixar tudo em inglês pelo menos uma vez na vida.

class Lead:
    def __init__(self, hardness: str, thickness: float, size: int):
        self.__hardness = hardness
        self.__thickness = thickness
        self.__size = size

    def usagePerSheet(self):
        if self.__hardness == "HB":
            return 1
        elif self.__hardness=="2B":
            return 2
        elif self.__hardness=="4B":
            return 4
        elif self.__hardness=="6B":
            return 6
        else:
            return 0

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
        self.__thickness= None
        self.__tip= Lead|None
        self.__barrel: list[Lead] = []

    def set_thickness(self, thickness: float):
        self.__thickness = thickness

    def insert(self, lead: Lead):
        if lead.getThickness()!=self.__thickness:
            print("fail: calibre invalido")
            return
        self.__barrel.append(lead) 

    
    def __str__(self) -> str:
        return f"calibre: {self.__thickness}, bico: [{self.__tip}], tambor: <{self.__barrel}>"
    
def main():
    pencil = Pencil()
 
    while True:
        line = input()
        print("$"+line)
        args= line.split(" ")
        if args[0]=="end":
            break
        elif args[0]=="show":
            print(pencil)
        
        elif args[0]=="insert":
            lead=Lead(args[2], float(args[1]), int(args[3]))
            pencil.insert(lead)

        elif args[0]=="init":
            pencil.set_thickness(float(args[1]))
main()