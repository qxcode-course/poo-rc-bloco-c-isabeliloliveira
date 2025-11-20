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

    def __str__(self) -> str:
        return f"[{self.__thickness}:{self.__hardness}:{self.__size}]"
    
class Pencil:
    def __init__(self, thickness: float=0, lead:Lead|None=None):
        self.__thickness=thickness
        self.__tip=lead
        self.__barrel: list[Lead] = []

    def set_thickness(self, thickness: float):
        self.__thickness = thickness

    def insert(self, lead: Lead):
        if lead.getThickness()!=self.__thickness:
            print("fail: calibre incompatível")
            return
        self.__barrel.append(lead) 

    def remove(self):
        if self.__tip is None:
            print("fail: nao existe grafite no bico")
            return
        self.__tip=None

    def write(self):
        if self.__tip is None:
            print("fail: nao existe grafite no bico")
            return

        if self.__tip.getSize() <= 10:
                self.__tip=None
                print("fail: tamanho insuficiente")
                return

        nsize=self.__tip.getSize()-self.__tip.usagePerSheet()

        if nsize<10:
            print("fail: folha incompleta")
            self.__tip.setSize(10)
            return
        self.__tip.setSize(nsize)


    def pull(self):
        if self.__tip is not None:
            print("fail: ja existe grafite no bico")
            return
        if not self.__barrel:
            print("fail: tambor vazio ")
            return
        self.__tip=self.__barrel.pop(0)
    
    def __str__(self) -> str:
        tip= "[]" if self.__tip is None else str(self.__tip)
        barrel= "".join(str(x) for x in self.__barrel)
        barrel=f"{barrel}"
        return f"calibre: {self.__thickness}, bico: {tip}, tambor: <{barrel}>"
    
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


        elif args[0]=="remove":
            pencil.remove()

        elif args[0]=="write":
            pencil.write()

        elif args[0]=="pull":
            pencil.pull()

        elif args[0]=="init":
            pencil.set_thickness(float(args[1]))

        else:
            print("fail: comando invalido")
main()