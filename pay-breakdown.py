def pay_breakdown(income):
    '''
    breaks down paycheck amount to show how much money
    goes to different accounts. After deducting static amounts for
    student loans and other bills, shows what is left to go to savings and checking and then the 
    extra amount going toward student loans.
    '''
    fedloan = xxx
    fedloan_xtra = 0
    discover = xxx
    discover_xtra = 0
    checking = 0
    savings = 0
    bills = xxx
    net = 0
    
    net = (income) - (fedloan + discover + bills)
    checking = net * 0.3
    savings = net * 0.2
    fedloan_xtra = net * 0.10
    discover_xtra = net * 0.4
   
    print("$" + str("%.2f" % net) + " is your net income after initial standard loan and bill deductions.")
    print("$" + str("%.2f" % checking) + " goes into your checking account.")
    print("$" + str("%.2f" % savings) + " goes into your savings account.")
    print("$" + str("%.2f" % (fedloan_xtra + fedloan)) + " goes toward your federal student loan.")
    print("$" + str("%.2f" % (discover_xtra + discover)) + " goes toward your discover student loan.")
    

