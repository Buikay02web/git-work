import ATM_functions

print ("welcome To Buikay ATM Gallery" )
default_acct_no = 7049200387
Default_pin = 2008
default_balance = 100000
attempts = 0
print ("1.check balance")
print ("2.withdrawal")
print ("3.deposit")
print ("4.transfer")
trans = int(input("choose an option: "))
if trans == 1:
    print ("enter ATM card pin")
    while attempts < 3: 
        ATM_PIN = int(input(""))
        if ATM_functions.atm_pin(ATM_PIN) == True :
            print (f"current balance:${default_balance} ")
            print ("Thank you for using our ATM")
        else:
            print ("Incorrect Pin!!")
            print ("Try Again")
            attempts += 1 
    if attempts == 3: 
        print("Too many failed attempts. Try again later.") 
        "continue"   
        print("Do you want to perform other option")
        print ("yes/no")
        
elif trans == 2:
    print ("enter withdrawal amount")
    withdrawal_amount=int(input("$ "))  #this  lines of codes allows you to withdrawl money from your 
    print ("enter ATM card pin")        # account only with the right password and only if you have up 
    while attempts < 3:                 # up to the amount you want to withdrawl
        ATM_PIN = int(input("   "))
        if (ATM_PIN == Default_pin):
            if (default_balance >= withdrawal_amount):
                print (f"dispence cash: ${withdrawal_amount}" )
                print (f"current balance: ${default_balance - withdrawal_amount}")
            else:
                print ("Insufficent fund")
        else:
            print ("Incorrect pin")
            print("try again")
            attempts += 1 
    if attempts == 3: 
        print("Too many failed attempts. Try again later.")  
elif trans == 3:
    print ("enter amount to be deposited")
    Amt_dep = int(input("$ ")) 
    print ("enter account to be deposited")
    acct_no = int(input( "  " ) )
    if (acct_no == default_acct_no):
        print ("Account name: Okechukwu chioma christabel" )
        print ("Enter ATM card pin")
        while attempts < 3:    
            ATM_PIN = int (input ("  "))
            if ( ATM_PIN == Default_pin):
                New_bal = default_balance + Amt_dep
                print (f"current balance: {New_bal}" )
                print ("Thank you for using our ATM")
            else:
                print ("incorrect pin")
                print ("try again")
                attempts += 1 
        if attempts == 3: 
            print("Too many failed attempts. Try again later.")   
    else:
        print ("odunbayo great")    
        print ("Enter ATM card pin")
        while attempts < 3:    
            ATM_PIN = int (input ("  "))
            if ( ATM_PIN == Default_pin):
                New_bal = default_balance + Amt_dep
                print (f"current balance: ${New_bal}" )
                print ("Thank you for using our ATM")
            else:
                print ("incorrect pin")
                print ("try again")
                attempts += 1 
        if attempts == 3: 
            print("Too many failed attempt. try again later.")       
elif trans == 4:
    print ("enter receivers account number")
    rec_acct = int(input("  ") )
    print ("enter bank name")
    bank_na = str (input (" ") )
    print ("enter amount to be sent")
    amt_sent = int(input("$  ") )
    print ("enter ATM card pin")
    while attempts < 3:
        ATM_PIN = int (input("  ") )
        if (ATM_PIN == Default_pin):
            print ("SUCCESSFUL")
            New_bal = default_balance - amt_sent
            print(f"current balance:${New_bal}") 
            print ("Thank you for using our ATM") 
        else:
                print ("incorrect pin")
                print ("try again")
                attempts += 1 
    if attempts == 3: 
            print("Too many failed attempt. try again later.")               
else:
    print ("Invalide option")       
    


