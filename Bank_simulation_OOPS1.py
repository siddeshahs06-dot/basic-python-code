class Account:
    def __init__(self,id,holder_name):
        self.id=id
        self.holder_name=holder_name
        self._balance = 0  #Encapsulation

    def check_balance(self):
        print(f"Account balance will be {self._balance}")

    def Deposite(self,amount):
        self._balance+=amount
        print(f"Account balance afer deposite will be: {self._balance}")

    def withdraw(self,amount): 
        if(self._balance > amount):
            self._balance-=amount
            print(f"withdraw successfull,\n available balance is {self._balance}")
        else:
            print("Asked amount more less than balance")


class saving_account(Account): #Inheritence
    def calucalte_interset(self):
        INTERSET_RATE=0.04
        interset=self._balance * INTERSET_RATE
        print(f"Interset for saving account balance is {interset}")
class current_account(Account):
    def withdraw(self,amount): #polymorphism
        OVER_DRAFT=1000
        if(self._balance + OVER_DRAFT > amount):
            self._balance-=amount
            print(f"withdraw successfull,\n available balance is {self._balance}")
        else:
            print("Asked amount more less than balance")

class Bank:
    def __init__(self,bname,branch):
        self.bname=bname
        self.branch=branch
        self.__account={}

    def create_account(self,id,holder_name,type):
        if(type == "saving"):
            new_account=saving_account(id,holder_name)
        elif type == "current":
            new_account=current_account(id,holder_name)
        self.__account[id]=new_account
        print("acoount creation successfull")
        return new_account
    
    def get_account(self,id):
        if id not in self.__account:
            print("Account not available")
        else:
            account=self.__account[id]
            print(f"\n ID: {account.id} \n Holder name {account.holder_name}")                    
            return account
        
sbk = Bank("Siddesh bank of karanataka","chitradurga") 
s1=sbk.create_account(1,"siddesh","saving")       
c1=sbk.create_account(2,"sindhu","current")

s1.Deposite(1000)
c1.Deposite(10)

s1.withdraw(2000)
c1.withdraw(20)

s1.calucalte_interset()
sbk.get_account(1)

