import read
import write
def Buy(StockInfo):
     Item_Cart=[]
     while True:
        try:
            Employee_Name=input("Enter Employee Name: ")
            Employee_Contact=int(input("Enter Employee Contact Info: "))
            if Employee_Name=="" or str(Employee_Contact)=="":
                print("Please Fill All The Fields!")
                continue
            elif len(str(Employee_Contact)) != 10:
                print("Contact Number must be 10 digits!")
                continue
            read.ReadStock()
            print("Note: Shipping Cost will not be added while buying from manufacturer!\n")
            while True:
                Item_Added=[]
                Product_ID=input("Enter The Product Id: ")
                if int(Product_ID) <=0 or int(Product_ID) > 6:
                    print("Please Enter Valid Product ID!")
                    continue

                ProductQuantity=int(input("Enter Quantity: "))
                if ProductQuantity <=0 :
                    print("Quantity cannot be zero or negative!")
                    continue
                Product_Price=(StockInfo[int(Product_ID)-1][4]).replace("$", "")
                Item_Added.append(Product_ID)
                Item_Added.append(ProductQuantity)
                Item_Added.append(Product_Price)
                Item_Cart.append(Item_Added)
                print("Items has been added successfully!")
                Buy_Again=input("Do you want to purchase more item?(Y/N) ")

                if Buy_Again=="N" or Buy_Again=="n":
                    Total_Price=0
                    for J in range(len(Item_Cart)):
                        Total_Price=Total_Price+int(Item_Cart[J][2])*int(Item_Cart[J][1])
                        Stock_Increase=int(StockInfo[int(Item_Cart[J][0])-1][3])+Item_Cart[J][1]
                        StockInfo[int(Item_Cart[J][0])-1][3]=" "+str(Stock_Increase)
                    Grand_Total=Total_Price+0.13*Total_Price    
                    print("Grand Total:",Grand_Total)
                    print("Items has been successfully purchased!\n")
                    write.Update_Stock(StockInfo)
                    write.generateInvoice(Employee_Name, Employee_Contact, Item_Cart, Total_Price, Grand_Total)
                    break
            if Buy_Again=="N" or Buy_Again=="n":
                break
        except ValueError:
           print("Please Enter Numeric Value!")


def Sell(StockInfo):
    Item_Cart=[]
    while True:
        try:
            Customer_Name=input("Enter the name of Customer: ")
            Customer_Contact=int(input("Enter Contact Info of Customer: "))
            if Customer_Name=="" or Customer_Contact=="":
                print("Please Fill All The Fields!")
                continue
            elif len(str(Customer_Contact)) != 10:
                print("Contact number should be 10 digits!")
                continue
            read.ReadStock()
            print("Shipping cost is $25 for each delivery.\n")
            while True:
                Item_Added=[]
                Product_ID=input("Enter The Product Id: ")
                if int(Product_ID) <=0 or int(Product_ID) > 6:
                    print("Please Enter Valid Product ID!")
                    continue
                Stock_Quantity=int(StockInfo[int(Product_ID)-1][3])
                if Stock_Quantity==0:
                    print("Unavailable Stock!")
                    continue

                ProductQuantity=int(input("Enter Quantity: "))
                if ProductQuantity <=0 :
                    print("Quantity cannot be zero or negative!")
                    continue
                elif ProductQuantity>Stock_Quantity:
                    print("Ordered item quantity is not available in stock right now!")
                    continue
            
                Product_Price=(StockInfo[int(Product_ID)-1][4]).replace("$", "")
                Item_Added.append(Product_ID)
                Item_Added.append(ProductQuantity)
                Item_Added.append(Product_Price)
                Item_Cart.append(Item_Added)
                print("Items has been added successfully!")
                Sell_Again=input("Do you want to sell more item?(Y/N) ")

                if Sell_Again=="N" or Sell_Again=="n":
                    Total_Price=0
                    for J in range(len(Item_Cart)):
                        Total_Price=Total_Price+int(Item_Cart[J][2])*int(Item_Cart[J][1])
                        Stock_Decrease=int(StockInfo[int(Item_Cart[J][0])-1][3])-Item_Cart[J][1]
                        StockInfo[int(Item_Cart[J][0])-1][3]=" "+str(Stock_Decrease)
                    Grand_Total=Total_Price+0.13*Total_Price+25   
                    print("Grand Total:",Grand_Total)
                    print("Items has been successfully sold!\n")
                    write.Update_Stock(StockInfo)
                    write.generateInvoice(Customer_Name, Customer_Contact, Item_Cart, Total_Price, Grand_Total)
                    break
            if Sell_Again=="N" or Sell_Again=="n":
                break
        except ValueError:
            print("Please Enter Numeric Value!")


