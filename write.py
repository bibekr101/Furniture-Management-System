import random
import datetime
def Update_Stock(Stock_Info):
    with open("Stock.txt","w") as f:
        for i in range(len(Stock_Info)):
            f.write(Stock_Info[i][0]+","+Stock_Info[i][1]+","+Stock_Info[i][2]+","+Stock_Info[i][3]+","+Stock_Info[i][4]+"\n")

def generateInvoice(name, contact, itemcart, totalprice, finalprice):
    Invoice_No=random.randint(0000,9999)
    Invoice_Name = "invoice" + name.replace(" ", "_")+ str(Invoice_No) + ".txt"

    with open(Invoice_Name, "w") as file:
       
        file.write("BRJ Furniture Store\nInvoice "+ str(Invoice_No)+"\n" + "=" * 50 + "\n")
        print("BRJ Furniture Store\nInvoice "+ str(Invoice_No)+"\n" + "=" * 50 + "\n")
        x = datetime.datetime.now()
        print(x)
        file.write (str(x))
        file.write ("\n")
        file.write("Customer Name: " + name + "\nContact: " + str(contact) + "\n" + "=" * 50 + "\n")
        print("Customer Name: " + name + "\nContact: " + str(contact) + "\n" + "=" * 50 + "\n")
        
        file.write("Item ID | Quantity | Unit Price | Total Price\n" + "-" * 50 + "\n")
        print("Item ID | Quantity | Unit Price | Total Price\n" + "-" * 50 + "\n")

        for item in itemcart:
            item_id = item[0]
            quantity = item[1]
            unit_price = item[2]
            
            file.write(item_id +" "*(7-len(item_id))+ " | " + str(quantity) +" "*(9-len(str(quantity)))+ "| $"+ str(unit_price)+" "*(10-len(str(unit_price))) + "| $" + str(int(unit_price)*int(quantity))+" "*(9-len(str(quantity))) + "\n")
            print(item_id +" "*(7-len(item_id))+ " | " + str(quantity) +" "*(9-len(str(quantity)))+ "| $"+ str(unit_price)+" "*(10-len(str(unit_price))) + "| $" + str(int(unit_price)*int(quantity))+" "*(9-len(str(quantity))) + "\n")

        file.write("=" * 50 + "\n")
        print("=" * 50)

        file.write("Subtotal: $" + str(totalprice) + "\n")
        file.write("VAT (13%): $" + str(totalprice * 0.13) + "\n")
        file.write("Shipping Cost: $25(Only added while selling to the customers!)\n")
        file.write("Total: $" + str(finalprice) + "\n")
        
        print("Subtotal: $" + str(totalprice) + "\n")
        print("VAT (13%): $" + str(totalprice * 0.13) + "\n")
        print("Shipping Cost: $ 25(Only added while selling to the customers!)\n")
        print("Total: $" + str(finalprice) + "\n")
        
        file.write("=" * 50 + "\nThank you for shopping with us!\n")
        print("=" * 50 + "\nThank you for shopping with us!\n")
        