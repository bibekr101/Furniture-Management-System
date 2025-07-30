import read
import operation
def main():
    while True:
        StockDetails=read.ReadStockData()
        print("\n")
        print("\n")
        print("\t \t \t \t  BRJ Furniture Store ")
        print("\n")
        print("\t \t \t Kamalpokhari, Kathmandu | Phone No: 9800000101 ")
        print("\n")

        print("-------------------------------------------------------------------------------------------------------------------------")
        print("\t \t  Welcome to the system Admin! I hope you have a good day ahead!")
        print("-------------------------------------------------------------------------------------------------------------------------")
        print("\n")

        print("Enter 1: To Buy From Manufacturer")
        print("Enter 2: To Sell The Product To The Customer")
        print("Enter 3: To Exit\n")
        try:
            UserInput=int(input("Select Option From Above: "))
            print()
            if UserInput==3:
                print("Thank You For Visiting.See you Soon!")
                break
            elif UserInput==1:
                operation.Buy(StockDetails)
            elif UserInput==2:
                operation.Sell(StockDetails)
            else:
                print("Option", UserInput,"is invalid as per our requirement.Please look at the options and try again. ")
                print("\n")
           
        except ValueError:
            print("Error: Please Enter A Numeric Value!")    
          
main()          
