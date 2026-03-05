##identification the currency
JPY=0.005 
TRY=0.02 
EUR=0.8 
#Coordination the line
For=int(input("How many times do you want the process to be repeated: "))
for i in range(For):
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("welcome you to the program currency exchange")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$","\n")
    NAME=str(input("Whats your name: "))
    #We question type the currency
    From=input("What do you want to exchange from (JPY,TRY,EUR):  ")
    Amount=float(input("How mach= "))  
    To=input("What do you want to exchange to(JPY,TRY,EUR):  ")
    if Amount<0:
        print("Unacceptable value")
        exit()
    #We set the condition
    if From==To: 
    #It is very important to make indents
        print(f"you will keep your amount as it is,({Amount}{From})")  
        exit()
    elif From=="JPY" and To=="EUR":  
        OneAmount=Amount*EUR
    #We define the outcomes
        print("The total value= ")
        print(OneAmount)
        FinancialFees=OneAmount * 3/100
        print("The fees= ")
        print(FinancialFees)

    elif From=="JPY"and To=="TRY": 
        OneAmount=Amount*TRY
        print(" The total value= ")
        print(OneAmount)
        FinancialFees=OneAmount * 3/100
        print("The fees= ")
        print(FinancialFees)

    elif From=="EUR" and To=="JPY":
        OneAmount=EUR / Amount 
    #We print result (OneAmount)
        print("The total value= ")
        print(OneAmount)
        FinancialFees=OneAmount * 3/100
    ##We print result (FinancialFees)
        print("The fees= ")
        print(FinancialFees)

    elif From=="EUR" and To=="TRY":
        OneAmount=Amount / EUR*TRY
        print("The total value= ")
        print(OneAmount)
        FinancialFees=OneAmount * 3/100
        print("The fees= ")
        print(FinancialFees)

    elif From=="TRY"and To=="JPY":
        OneAmount= Amount / JPY
        print("The total value= ")  
        print(OneAmount)
        FinancialFees=OneAmount * 3/100
        print("The fees= ")
        print(FinancialFees)

    elif From=="TRY"and To=="EUR":
        OneAmount=Amount/TRY*EUR
        print("The total value= ")  
        print(OneAmount)
        FinancialFees=OneAmount * 3/100
        print("The fees= ")
        print(FinancialFees)

    else:
        print("Please try again ")
        exit()
    #We print value if the condition does not exist
    print(f"{NAME} your will give {Amount} {From}, and your will take {OneAmount} {To}")
