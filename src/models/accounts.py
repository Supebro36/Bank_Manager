from src.models import generate_id
from src.app.error import InvalidAmount
from src.config import RUPEE 


class Account:
    def __init__(self,_id:str,name:str,balance :float=0):
        self._id = _id #protected attribute
        self.name = name # public attribute
        self.__balance = balance #private attribute

    def deposite(self,value:float):
        if value <10:
            raise InvalidAmount(f"Deposite Amount must be more than {RUPEE}10")
        self.__balance += value
        
        return self.__balance
    
    def withdraw (self,value:float):
        if value <10:
            raise InvalidAmount(f"Deposite Amount must be more than {RUPEE}10")

        if self.__balance<value:
            raise InvalidAmount(f"Amount must within {RUPEE}{self.__balance}")
        
        self.__balance-=value
        
        return self.__balance
    
    def balance(self):
        return self.__balance

    def to_dict(self):
        
        return {
            "id":self._id,
            "name":self.name,
            "balance":self.__balance,
        }
    @classmethod
    def from_dict(cls,data:dict[str,str | float]):
        return cls(data["id"],data["name"],data["balance"])

        