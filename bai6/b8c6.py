print("Sipnh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

class Bank:
    """Class mô phỏng tài khoản ngân hàng và các chức năng ATM cơ bản."""
    def __init__(self, name, Account_Number, balance=0):
        self.name = name
        self.Account_Number = Account_Number
        self.balance = balance
        self.Account_type = "Savings"
        self.location = "Guntur"

    def deposit(self):
        """Phương thức nạp tiền."""
        amount = int(input("Please Enter Desired amount to Deposit: "))
        self.balance += amount
        print("Your transaction is successfull!!")
        print(f"Current Balance: {self.balance}")

    def withdraw(self):
        """Phương thức rút tiền."""
        amount = int(input("Please Enter Desired amount to Withdraw: "))
        if amount > self.balance:
            print("Your transaction is cancelled due to insufficient amount in account!!")
        else:
            self.balance -= amount
            print("Your transaction is successfull!!")
            print(f"Current Balance: {self.balance}")

    def balance_inquiry(self):
        """Phương thức kiểm tra số dư."""
        print(f"Current Balance for account ({self.Account_Number}): {self.balance}")

    def customer_info(self):
        """Phương thức in thông tin đối tượng."""
        print(f"Account Name: {self.name}, Account Number: {self.Account_Number}")


# Khởi tạo đối tượng
t1 = Bank('Phan Dinh Hai',245752021610016,5000)
print("--Ban Dau--")
print(t1)
t1.deposit()
t1.withdraw()
t1.balance_inquiry()