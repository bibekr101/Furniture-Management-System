def ReadStock():
   with open("Stock.txt", "r") as f:
        lines = f.read()
        print("\n")
        print("-----------------------------------------------------------------------------------------------------------------------------")
        print("\n")
        print(" Following Furniture Stock Available:")
        print()
        print(lines)
        print()  
#Transfer all the product data into 2D list from the files.           
def ReadStockData():
   StockData=[] 
   with open("Stock.txt", "r") as g:
        for each in g:
           lines = each.replace("\n","")
           StockData.append(lines.split(","))
   return StockData    

           
        
            
        



