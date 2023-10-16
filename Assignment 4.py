## Question 1
import random
print("Welcome to Bank Of Jamaica.....")

class Account():
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def account_detail(self):
        print("\n----------ACCOUNT DETAIL----------")
        print(f"Account Holder: {self.name.upper()}")
        print(f"Account Number: {self.account_number}")
        print(f"Available balance: # {self.balance}\n")

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current account balance: $", self.balance)
        print()

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient fund!")
            print(f"Your balance is $ {self.balance} only.")
            print("Try with lesser amount than balance.")
            print()
        else:
            self.balance = self.balance - self.amount
            print(f"${amount} withdrawal successful!")
            print("Current account balance: $", self.balance)
            print()

    def check_balance(self):
        print("Available balance: $", self.balance)
        print()

    def transaction(self):
        print("""
            TRANSACTION
        *********************
            Menu:
            1. Account Detail
            2. Check Balance
            3. Deposit
            4. Withdraw
            5. Exit
        *********************
        """)

        while True:
            try:
                option = int(input("Enter 1, 2, 3, 4 or 5:"))
            except:
                print("Error: Enter 1, 2, 3, 4, or 5 only!\n")
                continue
            else:
                if option == 1:
                    atm.account_detail()
                elif option == 2:
                    atm.check_balance()
                elif option == 3:
                    amount = int(input("How much you want to deposit($):"))
                    atm.deposit(amount)
                elif option == 4:
                    amount = int(input("How much you want to withdraw($):"))
                    atm.withdraw(amount)
                elif option == 5:
                    print(f"""
                printing receipt..............
          ******************************************
              Transaction number: {random.randint(500, 200000)}
              Transaction is now complete.                        
              Account holder: {self.name.upper()}                 
              Account number: {self.account_number}               
              Available balance: ${self.balance}                   

              Thanks for choosing us as your bank                 
          ******************************************
          """)



print("**WELCOME TO BANK OF JAMAICA**")
print("___________________________________________________________\n")
print("----------ACCOUNT CREATION----------")
name = input("Enter your name: ")
account_number = input("Enter your account number: ")
print(" Account created successfully......\n")

atm = Account(name, account_number)

while True:
    trans = input("Do you want to do any transaction?(y/n):")
    if trans == "y":
        atm.transaction()
    elif trans == "n":
        print("""

    Thanks for choosing us as your bank 


        """)
        break
    else:
        print("Wrong command!  Enter 'y' for yes and 'n' for NO.\n")

# Question 2
class Box():

    # constructor __init__ method
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # render method
    def render(self):
        for i in range(self.width):
            for j in range(self.length):
                print("*", end="")
            print()

    # invert method
    def invert(self):
        self.temp = self.length
        self.length = self.width
        self.width = self.temp

    # get_area method
    def get_area(self):
        area = self.length * self.width
        print("Area of the box is", area)

    # get_perimeter method
    def get_perimeter(self):
        if self.length == self.width:
            perimeter = 4 * self.length
        else:
            perimeter = 2 * (self.length + self.width)
        print("Perimeter of the box is", perimeter)

    # double method
    def double(self):
        self.length = 2 * self.length
        self.width = 2 * self.width

    # __eq__ method
    def __eq__(self, other):
        if isinstance(other, Box):
            if other.length == self.length:
                if other.width == self.width:
                    return True
        return False

    # print_dim method
    def print_dim(self):
        print("Length of the box is", self.length)
        print("Width of the box is", self.width)

    # get_dim method
    def get_dim(self):
        dims = (self.length, self.width)
        return dims

    # combine method
    def combine(self, l, w):
        self.length = self.length + l
        self.width = self.width + w

    # get_hypot method
    def get_hypot(self):
        import math
        diagonal = math.sqrt(self.length ** 2 + self.width ** 2)
        return diagonal


# exercise02 function
def exercise02():
    # Instantiate 3 boxes of dimensions 5,10 , 3,4 and 5,10 and
    # assign to variables box1, box2 and box3 respectively
    box1 = Box(5, 10)
    box2 = Box(3, 4)
    box3 = Box(5, 10)

    # Print dimension info for each using print_dim()
    print("box1:")
    box1.print_dim()
    print("\nbox2:")
    box2.print_dim()
    print("\nbox3")
    box3.print_dim()
    print()

    #  Evaluate if box1 == box2, and
    # also evaluate if box1 == box3,
    # print True or False to the screen accordingly
    print("Is box1 == box2 ? -->", box1 == box2)
    print("Is box1 == box3 ? -->", box1 == box3)

    # Combine box3 into box1 (i.e. box1.combine())
    box1.combine(5, 10)
    print("\nbox1 after combining with box3:")
    box1.print_dim()

    # Double the size of box2
    box2.double()
    print("\nbox2 after doubling:")
    box2.print_dim()

    # Combine box2 into box1
    box1.combine(3, 4)
    print("\nbox1 after combining with box2:")
    box1.print_dim()

    # Using a for loop, iterate through and
    # print the tuple received from calling box2's get_dim()
    box2_tuple = box2.get_dim()
    print("\nDimensions of box2:")
    for dim in box2_tuple:
        print(dim)

    # Find the size of the diagonal of box2
    print("\nDiagonal of box2 is", box2.get_hypot())


# main
# calling the function
exercise02()