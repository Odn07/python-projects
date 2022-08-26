from datetime import date
import csv, datetime, os.path, re
from termcolor import *
import colorama
colorama.init()


def main():
    prodQty = 0
    totalCost = 0
    costPrice = 0

# display sales summary
def sales(username, password):
    # current date
    trans_date = str(date.today())
    x = datetime.datetime.now()
    # quantity of product
    qty = get_quantity() 
    if username and password:        
        cprint("SALES INFORMATION", "green")
        cprint("Please type the year and month of sales information needed (yyyy, mm)", "yellow")
        # year
        yy = input("Year: ")
        # month
        mm = input("Month: ")
        # year and month
        year_and_month = yy + "-" + mm
        # read and collect data from sales-record
        # file name is created every first day of the month
        sales_file = year_and_month + "-" + str(0) + str(1) + 'S.csv'    
        product_name = []
        price_product = []
        total_sales_quantity = []
        total_total_amount = []
        sales_record = []    
        counter = 0  
        try:
            with open(sales_file) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    product_name.append(row["prod_name"])
                    price_product.append(row["sell_price"])                                                  
                    sales_record.append(row)  
                    total_sales_quantity.append(row["qty"])
                    total_total_amount.append(row["sell_price"])          
        except:
            pass
        cprint("\nSALES", "green", end="")        
        for sales in sales_record:
            counter += 1 
            sales_date = sales["trans_date"]
            sold_product = sales["prod_name"] 
            cost_price = sales["cost_price"]
            selling_price = sales["sell_price"] 
            qty_sold = sales["qty"] 
            expected_profit = sales["expected_profit"]  
            print()
            print("|trans_date", "|prod_name", "|cost_price", "|sell_price", "|qty", "|expected_profit", "|status")
            print("|", sales_date, "|", sold_product, "|", cost_price, "|", selling_price, "|", qty_sold, "|", expected_profit, "|sold")        
        # dispay sales summary                
        cprint("\nSUMMARY OF SALES", "green")    
        print("|QUANTITY OF PRODUCT SOLD: ", end="")
        print(sum(int(list) for list in total_sales_quantity), end="\n")
        print("|TOTAL AMOUNT OF PRODUCT SOLD: #", end="")
        print(sum(float(list) for list in total_total_amount), end="\n")
            


        # read and collect data from expired product record
        expired_product = []
        total_expired_quantity = []
        total_cost_expired_product = []    
        counter = 0 
        expired_product_file = year_and_month + "-" + str(0) + str(1) + 'E.csv'
        try:
            with open(expired_product_file) as file:
                reader = csv.DictReader(file)
                for row in reader:                                               
                    expired_product.append(row)
                    total_expired_quantity.append(row["expired_qty"])
                    total_cost_expired_product.append(row["total_cost"])
        except:
            pass        
        for product in expired_product:
            counter += 1 
            expired_product = product["prod_name"]
            expired_qty = product["expired_qty"]    
            expired_total_cost = product["total_cost"]
            exp_date = product["exp_date"]
            mfg_date = product["mfg_date"]
            print("|S/N", "|mfg_date", "|exp_date", "|prod_name", "|exp_qty", "|cost_exp", "|expired")
            print("|", counter, "|", mfg_date, "|", exp_date, "|", expired_product,
                "|", expired_qty, "|", expired_total_cost)
        # display expired product summary    
        cprint("\nSUMMARY OF EXPIRED PRODUCT", "green")
        print("TOTAL QUANTITY OF EXPIRED PRODUCT: ", sum(int(list) for list in total_expired_quantity))
        print("TOTAL COST PRICE OF EXPIRED PRODUCT: #", sum(float(list) for list in total_cost_expired_product))


        # read and collect data from damage product record
        damage_product= []
        total_damaged_quantity = []
        total_total_cost = []    
        damage_product_file = year_and_month + "-" + str(0) + str(1) + 'D.csv'
        try:
            with open(damage_product_file) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    damage_product.append(row)
                    total_damaged_quantity.append(row["damaged_qty"])
                    total_total_cost.append(row["total_cost"])
        except:
            pass        
        for product in damage_product:
            damage_desc = product["prod_desc"]       
            damaged_qty = product["damaged_qty"]
            cost_damaged = product["total_cost"]
            damage_product = product["prod_name"]
            date_damaged = product["date_damaged"]     
            # display damaged product
            print("|dam_desc", "|date_dam", "|prod_name", "|dam_qty", "|total_cost", "|damaged", "yellow")
            print("|", damage_desc, "|", date_damaged, "|", damage_product, 
            "|", damaged_qty, "|", cost_damaged)
        # display damaged product summary    
        cprint("\nSUMMARY OF DAMAGED PRODUCT", "green")   
        print("TOTAL QUANTITY OF DAMAGED PRODUCT: ", sum(int(list) for list in total_damaged_quantity))
        print("TOTAL COST PRICE OF DAMAGED PRODUCT: #", sum(float(list) for list in total_total_cost))


        # read and collect data from damage product record
        price_product = []
        t_qty = []
        total_cost_price = []
        expected_profit = []    
        try:
            with open(sales_file) as file:
                reader = csv.DictReader(file)
                for row in reader:                         
                    price_product.append(row["sell_price"])                                  
                    t_qty.append(row["qty"])
                    total_cost_price.append(row["cost_price"])
                    expected_profit.append(row["expected_profit"])
                    total_expected_profit = sum(float(list) for list in expected_profit)
                    total_cost_price_sold = sum(float(list) for list in total_cost_price)
                    total_quantity_sold = sum(int(list) for list in t_qty)
                    total_sell_price_sold = sum(float(list) for list in price_product)
                    total_amount_sold = total_quantity_sold * total_sell_price_sold
                    total_expected_profit = total_expected_profit * total_quantity_sold
                    profit_loss = total_amount_sold - (total_cost_price_sold * total_quantity_sold)
        except:
            pass
        # display profit/ loss
        cprint("\nPROFIT/LOSS", "green") 
        try:
            print("|Total Qty sold: ", total_quantity_sold)
            print("|Total Amount sold: #", total_amount_sold)
            print("|Expected Profit: #", total_expected_profit)
            if profit_loss >= total_expected_profit:
                print("|Profit: #", profit_loss)
            else:
                print("|Loss: #", profit_loss)
        except NameError:
            pass
        # save/ print sales summary
        cprint("\nDo you want to save/print this file?", "yellow")
        while True:
            try:
                response = input("Type save/print? ").title()
                if response:
                    break
            except:
                pass

        match response:
            case "Save":
                ...
            case "Print":
                ...


# create sales record file name every first day of the month yyyy-mm-1S.csv
def sales_file_name():
    current_date = date.today()
    first_day_of_month = date(current_date.year, current_date.month, 1)
    ext = "S.csv"
    return f"{str(first_day_of_month) + ext}"

    
# create expired product record file name every first day of the month yyyy-mm-1E.csv
def expired_file_name():
    current_date = date.today()
    first_day_of_month = date(current_date.year, current_date.month, 1)
    ext = "E.csv"
    return f"{str(first_day_of_month) + ext}"


# create damaged product record file name every first day of the month yyyy-mm-1D.csv
def damage_file_name():
    current_date = date.today()
    first_day_of_month = date(current_date.year, current_date.month, 1)
    ext = "D.csv"
    return f"{str(first_day_of_month) + ext}"



class Admin:
    def __init__(self, admin_username, admin_password):
        if not admin_username:
            raise ValueError("You're not an Admin!")
        if not admin_password:
            raise ValueError("You're not an Admin!")            
        self.admin_username = admin_username
        self.admin_password = admin_password

    def __str__(self):
        return f"{self.admin_username}, {self.admin_password}"
    
    @classmethod
    def admin_signin_credentials(cls):
        try:
            admin_username = input("Username: ")
            admin_password = input("Password: ")        
            return cls(admin_username, admin_password)           
        except:
            cprint("You're not an Admin!", "red")


    @classmethod
    def admin_signin_credentials_to_signup(cls):       
        try:
            admin_username = input("Old Username: ")
            admin_password = input("Old Password: ")        
            return cls(admin_username, admin_password)           
        except:
            cprint("You're not an Admin!", "red")


    @classmethod
    def admin_signup_credentials(cls):
        try:
            admin_username = input("E-mail: ")
            admin_password = input("New Password: ")        
            return cls(admin_username, admin_password)           
        except:
            cprint("You're not an Admin!", "red")

    @classmethod
    def user_authentication(cls):
        cprint("SignIn", "yellow")
        try:
            email = input("Forgot password? Enter e-mail: ")
        except:
            pass


        credentials = []
        try:
            with open("admin-credentials.csv") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    credentials.append(row)
        except:
            pass 

        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9]+(\.[A-Z|a-z]{2,})+')        
        for cred in credentials: 
            admin_username = cred["username"]  
            admin_password = cred["password"]
        if re.fullmatch(regex, email) and email == admin_username:
            print("Your password: ", admin_password)                        
        elif not re.fullmatch(regex, email):
            cprint("Invalid email!", "red")
            admin_credentials = Admin.admin_signin_credentials()               
            try:                     
                if admin_credentials.admin_username == cred["username"] and admin_credentials.admin_password == cred["password"]:                                    
                    return cls(admin_username, admin_password)           
            except:
                pass
        


    @classmethod
    def user_authentication_signup(cls):
        cprint("SignUp", "yellow")
        credentials = []
        try:
            with open("admin-credentials.csv") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    credentials.append(row)
        except:
            pass        
        admin_credentials = Admin.admin_signin_credentials_to_signup()
        for cred in credentials: 
            admin_username = cred["username"]  
            admin_password = cred["password"] 
        if admin_credentials.admin_username != cred["username"] or admin_credentials.admin_password != cred["password"]:
            pass                                
        elif admin_credentials.admin_username == cred["username"] and admin_credentials.admin_password == cred["password"]:                                    
            return cls(admin_username, admin_password)
        


def create_admin_signin_credentials(default_username, default_password):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9]+(\.[A-Z|a-z]{2,})+')     
    if default_username and default_password:
        try:
            admin_credentials = Admin.admin_signup_credentials()  
            if re.fullmatch(regex, admin_credentials.admin_username):   
                with open("admin-credentials.csv", "a") as file:
                    fieldnames = ["username", "password"]
                    writer = csv.DictWriter(file, fieldnames = fieldnames)
                    #If file does not exist create header.            
                    if file.tell() == 0:
                        writer.writeheader()
                    writer.writerow({"username": admin_credentials.admin_username, "password": admin_credentials.admin_password})    
        except:
            cprint("SignUp unsuccessful! Check the email your entered.", "red")

    
'''
Stock record names are not hardcoded they are given as per users discretion. Each time new products
are stocked they are added to a new record or a previous one depending on the choice of the user.
stockrecord_filename function creates a csv file where stock record names are stored. This
will enable the users to keep track of filenames.
'''
def stockrecord_filename(recordname):
    try:
        with open("stockrecord-filename.csv", "a") as file:
            fieldnames = ["date", "stockrecord_filename"]
            writer = csv.DictWriter(file, fieldnames = fieldnames)
            #If file does not exist create header.            
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow({"date": date.today(), "stockrecord_filename": recordname})
    except FileNotFoundError:
        print("Warning! Stockrecord-filename not created!!")
    

'''
THIS FUNCTION WILL READ AND PRINT OUT THE CONTENT OF THE FILE CREATED BY 'list_stockrecord_filename()'
THE list_stockrecord_filename() STORES NAMES OF STOCK RECORD FILES.
'''
def read_stockrecord_filename():
    stockrecord_filename1 = []
    stockrecord_filename2 = []
    try:
        with open("stockrecord-filename.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                stockrecord_filename1.append(row)
                stockrecord_filename2.append(row["stockrecord_filename"])
    except FileNotFoundError:
        pass
    cprint("\nEXISTING STOCK RECORD", "green")   
    for stockrecord1 in stockrecord_filename1:
        for stockrecord2 in stockrecord_filename2:
            stock_filename = stockrecord2[0:-4]
            print("|DATE: ", stockrecord1["date"], "|FILENAME: ", stock_filename)
        break

'''
FUNCTION TO IDENTITY THE STOCK RECORD FILE THAT CONTAINS PRODUCT-> THIS FUNCTION LOOPS 
THROUGH THE LIST OF STOCK RECORD FILE NAME STORED BY THE PROGRAM AND THEN FETCHES PRODUCT 
DETAILS FROM ANY OF THE FILES THAT CONTAINS THE PRODUCT THAT MATCHES THE BATCH NUMBER ENTERED.
'''
def active_stockfile(batch_no):
    #batch_no = input("batch number: ")
    stockrecord_filename_list = []
    try:
        with open("stockrecord-filename.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:            
                stockrecord_filename_list.append(row)            
    except FileNotFoundError:
        print("Warning! Stockrecord-filename not found!!")

    '''
    NOTEE: ADD A FUNCTIONALITY IN THE FUNCTION THAT CREATES STOCK RECORD FILE TO STOP DUPLICATION OF FILE
    NAME.
    '''
    for row in stockrecord_filename_list:    
        stockrecord_data = []    
        file_name = row["stockrecord_filename"]        
        with open(file_name) as file:
            reader = csv.DictReader(file)
            for row in reader:
                stockrecord_data.append(row)
        for stockrecord in stockrecord_data:
            if batch_no == stockrecord["batch_no"]: 
                return file_name 


# temp file to be deleted at the conclusion of every sale
def temp_file():
    tempfile_ext = ".csv"
    return f"{'tempfile_name' + tempfile_ext}"


'''
FUNCTION TO DISPLAY CURRENT SALES SUMMARY-> THIS FUNCTION READS A TEMPORARY FILE WHERE SALES MADE
ARE SENT TO BEFORE THEY ARE DISPLAYED FOR THE SALLER TO MAKE A DECISION. AFTER THE SALES THE 
CONTENT OF FILE IS DELETED FOR ANOTHER SALE TO BE RECORDED. 
'''
def display_sales_summary():
    counter = 0    
    price_product = []
    t_qty = []
    product_name = []    
    try:
        with open(temp_file()) as file:
            reader = csv.DictReader(file)
            for row in reader:                                    
                product_name.append(row)            
                price_product.append(row["sell_price"])                                  
                t_qty.append(row["qty"])
        cprint("\n|SALES SUMMARY:", "green")
        for prod_name in product_name:
            counter += 1 
            print("|s/n.", counter, "|", prod_name["prod_name"], "#",prod_name["sell_price"], "per item.")          
        print("\n")
        cprint("|TOTAL: ", "green")     
        print("|Total Qty: ", sum(int(list) for list in t_qty), sep="")
        print("|Total Amount: #", sum(float(list) for list in price_product), "\n", sep="")        
        # product balance in stock
        product_balance()      
        # delete temporary file after printing the current sales details
        delete_file()             
    except:
        pass       

         
'''
RETURN TOTAL QUANTITY OF EACH NAMED PRODUCT STOCKED IN STOCK FILE

Notee: This function does not calculate quantity of product with batch_no it uses the name of the product. 
For now am using batch_no that i assigned to identify products. But the final product will use the bar code
number on the product to identify product. 

So what this function does is that it loops through all stock files,
the file that contains the batch_no becomes the active file. It loops through the active file, graps all products
that have similar name and then calculate their quantity. 

This applies to function that calculates total_quantity_stocked, total_quantity_sold, total_quantity_expired,
and total_quantity_damaged.
'''
def total_quantity_stocked(prod_name, batch_no):         
    stocked_product = []
    try:
        with open(active_stockfile(batch_no)) as file:
            reader = csv.DictReader(file)
            for row in reader:
                if prod_name == row["prod_name"]:
                    stocked_product.append(row["qty"])               
    except:
        pass
    return sum(int(list) for list in stocked_product)

'''
CALCULATES THE TOTAL QUANTITY OF A NAMED PRODUCT SOLD
'''
def total_quantity_sold(prod_name):
    sold_product = []         
    try:
        with open(sales_file_name()) as file:
            reader = csv.DictReader(file)
            for row in reader:
                if prod_name == row["prod_name"]:
                    sold_product.append(row["qty"])                        
    except:
        pass
    return sum(int(list) for list in sold_product)


'''
CALCULATES QUANTITY OF NAMED PRODUCT EXPIRED
'''
def total_quantity_expired(prod_name): 
    expired_product = []       
    try:
        with open(expired_file_name()) as file:
            reader = csv.DictReader(file)
            for row in reader:
                if prod_name == row["prod_name"]:
                    expired_product.append(row["qty"])                       
    except:
        pass
    return sum(int(list) for list in expired_product) 

'''
RETURNS QUANTITY OF NAMED DAMAGED PRODUCT
'''
def total_quantity_damaged(prod_name):
    damaged_product = [] 
    try:
        with open(damage_file_name()) as file:
            reader = csv.DictReader(file)
            for row in reader:
                if prod_name == row["prod_name"]:
                    damaged_product.append(row["qty"])                        
    except:
        pass
    return sum(int(list) for list in damaged_product)



def delete_file():
    '''
    To delete a csv file
    first check if file exists
    call remove method to delete the csv file
    '''
    file = temp_file()
    if(os.path.exists(file) and os.path.isfile(file)):
        os.remove(file) 


def product_balance():
    products = []
    try:
        with open(temp_file()) as file:
            reader = csv.DictReader(file)
            for row in reader:                                    
                products.append(row)    
        cprint("|PRODUCT BALANCE IN STOCK:", "green") 
        for prod in products:
            batch_no = prod["batch_no"] 
            prod_name = prod["prod_name"]             
            if total_quantity_stocked(prod_name, batch_no) == total_quantity_sold(prod_name) + total_quantity_expired(prod_name) + total_quantity_damaged(prod_name):            
                print("|",prod_name, "Out of stock!")
            else:  
                pass                             
                print(f"|{prod_name}", "=",  total_quantity_stocked(prod_name, batch_no) - total_quantity_sold(prod_name) - total_quantity_expired(prod_name) - total_quantity_damaged(prod_name), "remaining in stock.")
    except:
        pass
                   

'''
THIS FUNCTION CREATES STOCK RECORD FILE NAME TO AVOID USING ONE STOCK RECORD FOR BOTH OLD AND NEW
PRODUCT STOCKED. SO WITH THE AID OF THIS FUNCTION EVERY TIME NEW PRODUCTS ARE STOCKED A NEW FILE
NAME IS CREATED.
'''
def create_stock_file():      
    stock_filename = input("ENTER A FILENAME: ")
    ext = ".csv"
    return f"{stock_filename + ext}"


 
'''
Add a functionality to get user input
some attributes of the damaged product are already in the stock record
create function to retrieve the values from stock record if a condition is met
example if batch number of damaged product matches stock record, get the below values
the only user input will be quantity of damaged product and maybe a discription.
CREATE DAMAGED PRODUCT FILE
'''
def get_damaged_product(trans_date):
    '''
    OPEN STOCK FILE TO READ PRODUCT ATTRIBUTE TO CREATE DAMAGED PRODUCT FILE
    '''    
    damaged_products = []
    try:
        with open(active_stockfile(batch_no)) as file:
            reader = csv.DictReader(file)
            for row in reader:
                damaged_products.append(row)
        cprint("=>CREATE DAMAGED PRODUCT FILE\n", "green")
        batch_no = input("|BATCH NO: ")
        damaged_qty = input("|QTY: ")
        damage_desc = input("|WHAT HAPPENED TO THE PRODUCT?: ")
        for product in damaged_products:
            if batch_no == product["batch_no"]:
                '''
                CREATE DAMAGED PRODUCT RECORD IF THE CONDITION ABOVE IS MET
                '''
                with open(damage_file_name(), "a") as file:
                    fieldnames = ["batch_no", "damage_desc", "date_damaged", "prod_name", "prod_desc", "damaged_qty", "cost_price", "total_cost"]
                    writer = csv.DictWriter(file, fieldnames = fieldnames)
                    #If file does not exist create header.            
                    if file.tell() == 0:
                        writer.writeheader() 
                    writer.writerow({"batch_no": batch_no, "damage_desc": damage_desc, "date_damaged": trans_date, "prod_name": product["prod_name"], "prod_desc": product["prod_desc"], "damaged_qty": damaged_qty, "cost_price": product["cost_price"], "total_cost": f'{damaged_qty * float(product["cost_price"])}'})
    except:
        pass

'''
FUNCTION TO PRINT OUT STOCK RECORD.
'''
def read_stocked_product_record(username, password):
    if username and password:
        stocked_product = []
        cost_price = [] 
        sell_price = []
        expected_profit = []
        counter = 0       
        # display list of stock record filename previously created 
        read_stockrecord_filename()
        cprint("\nVIEW STOCK RECORD", "yellow") 
        try:           
            with open(create_stock_file()) as file:
                reader = csv.DictReader(file)
                for row in reader:                                               
                    stocked_product.append(row)
                    cost_price.append(row["cost_price"]) 
                    sell_price.append(row["sell_price"])  
                    expected_profit.append(row["expected_total_profit"])     
            cprint("\nCONTENT OF STOCK RECORD", "green")
            for product in stocked_product: 
                counter += 1                       
                print("|DATE STOCKED: ", product["datetime_stocked"], "|BATCH NO: ", product["batch_no"], "|MFG DATE: ", product["mfg_date"], "|EXP DATE: ", product["exp_date"], "|PROD NAME: ", product["prod_name"], "|PROD DESC: ", product["prod_desc"], "|PROD QTY: ", product["qty"], "|COST PRICE: #", product["cost_price"], "|TOTAL COST: #", product["total_cost"], "|SELL PRICE: #", product["sell_price"], "|EXPECTED UNIT PROFIT: #", product["expected_profit"], "|EXPECTED TOTAL PROFIT: #", product["expected_profit"], sep="")  
                continue
            cprint("\nSUMMARY OF STOCK RECORD", "green")
            print("|TOTAL COST PRICE: ", sum(float(list) for list in cost_price))
            print("|TOTAL SELLING PRICE: ", sum(float(list) for list in sell_price))
            print("|EXPECTED PROFIT: ", sum(float(list) for list in expected_profit))
        except:
            pass

    '''
    CREATE A FUNCTION TO GROUP SIMILAR ITEM BY NAME AND BY DATE.
    '''

#Create stock record
def stocked_product(username, password):
    if username and password:
        try:
            read_stockrecord_filename()
            cprint("\nINSTRUCTION", "green")
            print("1. Enter a unique file name to create new stock record.", "\n2. To add product to an existing stock record, enter file name of the stock record.",
            "\n3. Don't reuse file names, use a unique file name for each new stock.", 
            "\n4. Except you intend adding a new stock to an old stock record")  
            cprint("\nCREATE NEW STOCK RECORD", "green")          
            stock_record_filename = create_stock_file()           
            stockrecord_filename(stock_record_filename)
            batch_no = input("BATCH NO: ")       
            cprint("Date format => yyyy-mm-dd", "yellow")
            mfg_date = input("Manufacturing date: ")
            cprint("Date format => yyyy-mm-dd", "yellow")
            exp_date = input("Expiry date: ")    
            datetime_stocked = date.today()
            prod_name = input("Product name: ").title()
            prod_desc = input("Product description: ").title()
            qty = int(input("Quantity of product: "))
            cost_price = float(input("Cost price(#Naira) per product: #"))
            # total worth of product stocked
            total_cost = qty * cost_price
            sell_price = float(input("Selling price(#Naira) per product: #"))
            expected_profit = sell_price - cost_price
            expected_total_profit = (sell_price * qty) - (cost_price * qty)        
            with open(stock_record_filename, "a") as file:
                fieldnames = ["batch_no", "mfg_date", "exp_date", "datetime_stocked", "prod_name", "prod_desc", "qty", "cost_price", "total_cost", "sell_price", "expected_profit", "expected_total_profit"]
                writer = csv.DictWriter(file, fieldnames = fieldnames)
                #If file does not exist create header.
                if file.tell() == 0:
                    writer.writeheader()
                writer.writerow({"batch_no": batch_no, "mfg_date": mfg_date, "exp_date": exp_date, "datetime_stocked": datetime_stocked, "prod_name": prod_name,
                                "prod_desc": prod_desc, "qty": qty, "cost_price": cost_price, "total_cost": total_cost, "sell_price": sell_price, "expected_profit": expected_profit, "expected_total_profit": expected_total_profit})
        except:
            pass


#Function to calculate quantity of product
def get_quantity():
    number_of_product = []
    quantity =0
    quantity += 1
    number_of_product.append(quantity)
    qty = int(number_of_product[-1])
    return qty



def sell_product():
    #Display sales record, create sales record, create expired product record, display sales summary
    cprint("|SELL PRODUCT", "green")                 
    products = []
    trans_date = str(date.today())
    x = datetime.datetime.now()
    while True:
        try:
            batch_no = input("|BATCH NO: ")
            if not batch_no:
                break
            with open(active_stockfile(batch_no)) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    products.append(row)
        except :
            pass         
        for product in products:
            if batch_no == product["batch_no"] and trans_date != product["exp_date"]:
                qty = get_quantity()
                prod_name = product["prod_name"]
                print("|",trans_date, "|", product["prod_name"], "|PRICE:#", product["sell_price"], "|QTY:", qty, sep="")
                break
            elif batch_no == product["batch_no"] and trans_date == product["exp_date"]: 
                qty = get_quantity()                
                # product is expired and an expired product file is immedialtely created
                try:   
                    with open(expired_file_name(), "a") as file:
                        fieldnames = ["batch_no", "mfg_date", "exp_date", "datetime_stocked", "prod_name", "prod_desc", "expired_qty", "cost_price", "total_cost"]                
                        writer = csv.DictWriter(file, fieldnames=fieldnames)

                        #If file does not exist create header.
                        if file.tell() == 0:
                            writer.writeheader() 
                        writer.writerow({"batch_no": batch_no, "mfg_date": product["mfg_date"], "exp_date": product["exp_date"], "datetime_stocked": product["datetime_stocked"], "prod_name": prod_name , "prod_desc": product["prod_desc"], "expired_qty": qty, "cost_price": product["cost_price"], "total_cost": qty * float(product["cost_price"])})
                        cprint(f"{prod_name}, Warning! Product is expired!", "red")
                        break
                except FileNotFoundError:
                    pass
                    break                    
        else:
            cprint(f"{batch_no}, Warning! Product number not recognised.", "red")         
        # if product is still in stock and not yet expired a sales file is created to hold details
        try:                
            with open(sales_file_name(), "a") as file:                
                
                fieldnames = ["batch_no", "mfg_date", "exp_date", "trans_date", "prod_name", "cost_price", "sell_price", "qty", "expected_profit"]                
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                #If file does not exist create header.            
                if file.tell() == 0:
                    writer.writeheader() 
                writer.writerow({"batch_no": batch_no, "mfg_date": product["mfg_date"], "exp_date": product["exp_date"], "trans_date": trans_date, "prod_name": product["prod_name"], "cost_price": product["cost_price"], "sell_price": product["sell_price"], "qty": qty, "expected_profit": product["expected_profit"]})                       
                
        except:
            pass        
        # create a temp file to display sales summary        
        try:             
            with open(temp_file(), "a") as file:                
                fieldnames = ["batch_no", "mfg_date", "exp_date", "trans_date", "prod_name", "sell_price", "qty"]                
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                #If file does not exist create header.            
                if file.tell() == 0:
                    writer.writeheader() 
                writer.writerow({"batch_no": batch_no, "mfg_date": product["mfg_date"], "exp_date": product["exp_date"], "trans_date": trans_date, "prod_name": product["prod_name"], "sell_price": product["sell_price"], "qty": qty})                       
                
        except FileNotFoundError:
            pass 
        except NameError:
            print(f"{batch_no}, Warning! Product number not recognise!!", "red")
        except ValueError:
            pass    
    # display a summary of sales details
    display_sales_summary()              



if __name__ == "__main__":
    main()




