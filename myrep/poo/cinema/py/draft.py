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
            return False
        
        if self.__seats[index] is not None:
            print("fail: cadeira ja esta ocupada")
            return False
        
        if id in self.__search:
            print("fail: cliente ja esta no cinema")
            return False
        
        client=Client(id, phone)
        self.__seats[index] = client
        self.__search[index]=id
        return True
    
    def cancel(self, id:str):
        if id not in self.__search:
            print("fail: cliente nao esta no cinema")
            return
        index = self.__search.index(id)
        self.__search[index] = None
        self.__seats[index] = None
        return
    
        
    
    def __str__(self):
        return "[" + " ".join("-" if c is None else str(c) for c in self.__seats) + "]"
        

def main():
    theater=Theater(0)

    while True:
        line=input()
        args=line.split(" ")
        print(f"${line}")
        if args[0]=="end":
            break
        elif args[0]=="show":
            print(theater)
        elif args[0]=="init":
            theater=Theater(int(args[1]))
        elif args[0]=="reserve":
            theater.reserv(args[1], int(args[2]), int(args[3]))
        elif args[0]=="cancel":
            theater.cancel(args[1])

        else:
            print("fail: comando invalido")

main()