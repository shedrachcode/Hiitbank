from time import time
import random
class Account:
    def __init__(self, fname, lname, phone_no, email,pin, passcode, address,bvn, balance, account_no, nin):
        self.__fname = fname
        self.__lname = lname
        self.__phone_no = None
        self.__email = email
        self.__pin = pin
        self.__passcode = passcode
        self.__address:str = None

        if bvn == None:
            self.bvn = str(random.randint(100000000000, 99999999999))
        else:
            self.__bvn = bvn
        self.__balance = 0.0
        self.__account_no = "888" + str(random.randint(100000, 99999999))
        self.__nin:str = None


    def get_name(self):
        return self.__fname

    def get_name(self):
        return self.__lname


    def withdraw(self, amount: float) -> float:
        assert type(amount) == float, "amount to withdraw must be a number"
        assert amount > 0, "amount to withdraw must be a positive number"
        assert amount < self.__balance, "insufficient funds"

        self.__balance = amount
        return self.__balance

    def deposit(self, amount: float) -> float:
        assert type(amount) == float, "amount to deposit must ba a number"
        assert amount > 0, "amount to deposit must be a positive number"

        self.__deposit = amount
        return self.__deposit

