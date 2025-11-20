class Client:
    def __init__(self, id:str, phone:int):
        self.__id=id
        self.__phone=phone
        
    def getPhone(self):
        return self.__phone
    
    def setPhone(self, phone:int):
        self.__phone=phone

    def getId(self):
        return self.__id
    
    def setId(self, id:str):
        self.__id=id

    def __str__(self):
        return f"{self.__id}:{self.__phone}"


class Theater:
    def __init__(self, capacity:int):
        self.__seats = [None]*capacity
        self.__search=[None]*capacity
        self.__verifyIndex=capacity
    
    def reserv(self, id:str, phone:int, index:int):
        if index<0 or index>=self.__verifyIndex:
            print("fail: cadeira nao existe")
            return
        elif self.__seats[index] is not None:
            print("fail: cadeira ja esta ocupada")
            return False
        elif id in self.__search:
            print("fail: cliente ja esta no cinema")
            return
            
        client=Client(id, phone)
        self.__seats[index] = client
        return
    
    def __str__(self):
        print("[", end="")
        x=" ".join("-" if i is None else str(i) for i in self.__seats)
        x+="]"
        return x
        

def main():
    theater=Theater(0)

    while True:
        line=input()
        args=line.split(" ")
        if args[0]=="end":
            break
        elif args[0]=="show":
            print(theater)
        elif args[0]=="init":
            theater=Theater(int(args[1]))
        elif args[0]=="reserve":
            theater.reserv(args[1], int(args[2]), int(args[3]))
        # elif args[0]=="cancel":

        else:
            print("fail: comando invalido")
