from inventory_lib import *


cprint("\n|INVENTRY MANAGEMENT SYSTEM\n", "green")  
print("|MENU =>", "|Stock", "|Sales", "|SignUp")

print("\n")
#Display sales record, create sales record, create expired product record, display sales summary
sell_product()
print("\n")

# menu
while True:
    try:
        menu = input("|MENU =>: ").title()
        if menu in ["Stock", "Sales", "Signup"] or not menu:
            break
    except ValueError:
        pass


match menu:    
    case "Stock":
        # require authentication to access stock record 
        while True:
            try:  
                authentication_credentials_for_signin = Admin.user_authentication()       
                if authentication_credentials_for_signin.admin_username and authentication_credentials_for_signin.admin_password:
                    break
            except:
                pass       

        # create stock record         
        # Create/view stock record        
        while True:
            try:
                response_0 = input("Type 'Y' to create stock file and 'N' to view stock file Y/N: ").title()
                if response_0:
                    break                
            except:
                cprint("Type Y/N!", "red")

        match response_0:                  
            case "Y":
                #CREATE STOCK FILE
                stocked_product(authentication_credentials_for_signin.admin_username, authentication_credentials_for_signin.admin_password)                       
            case "N":
                #READ STOCK FILE
                read_stocked_product_record(authentication_credentials_for_signin.admin_username, authentication_credentials_for_signin.admin_password)
            case _:
                cprint("Type Y/N","red")   

    case "Sales":
        # require authentication to access stock record 
        while True:
            try:  
                authentication_credentials_for_signin = Admin.user_authentication()       
                if authentication_credentials_for_signin.admin_username and authentication_credentials_for_signin.admin_password:
                    break
            except:
                pass        
        sales(authentication_credentials_for_signin.admin_username, authentication_credentials_for_signin.admin_password )

    case "Signup":
        while True:
            try:
                 authentication_credentials_for_signup = Admin.user_authentication_signup()
                 if authentication_credentials_for_signup.admin_username and authentication_credentials_for_signup.admin_password:
                    break
            except:
                pass              
        # create account for administrative access
        create_admin_signin_credentials(authentication_credentials_for_signup.admin_username, authentication_credentials_for_signup.admin_password)      
    case _:
        pass





