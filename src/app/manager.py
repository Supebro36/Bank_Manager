from src.app.storage import load_accounts,save_accounts,save_transaction
from src.config import RUPEE
from src.app.error import AccountNotFound

from src.models import generate_id,Account,Transaction

class BankManager:
    def __int__(self):
        self.__accounts=load_accounts
    def create(self,name:str,balance:float=0)->Account:
        acc=Account(
            generate_id(),
            name,
            balance
        )
        self.__accounts.append(acc)
        save_accounts(self.__accounts)

        return acc
    
    def find_account(self,acc_id:str)->Account:
        for acc in self.__accounts:
            if acc._id==acc_id:
                return acc
        raise AccountNotFound(f"{acc_id}does not Exists.")
    
    def deposit(self,acc_id:str,amount:float)->str:
        acc=self.find_account(acc_id)

        acc.deposite(amount)
        txn=Transaction(
            "deposite",
            amount,
            acc._id,
        )
        save_accounts(self.__accounts)
        save_transaction(txn)

        return f"Deposited ! New balance :{RUPEE}{acc.balance}"

    def withdraw(self,acc_id:str,amount:float)->str:
        acc=self.find_account(acc_id)
        
        acc.withdraw(amount)
        txn=Transaction(
            "deposite",
            amount,
            acc._id,
        )
        save_accounts(self.__accounts)
        save_transaction(txn)

        return f"withdraw ! New balance :{RUPEE}{acc.balance}"

    def withdraw(self,acc_id:str,trg_id:str,amount:float)->str:
        acc=self.find_account(acc_id)
        trg=self.find_account(trg_id)

        acc.withdraw(amount)
        trg.deposite(amount)

        txn=Transaction("transfer",amount,acc._id,trg._id)

        save_accounts(self.__accounts)
        save_transaction(txn)

        return f"Transfers{RUPEE}{amount}!New balance :{RUPEE}{acc.balance()}"