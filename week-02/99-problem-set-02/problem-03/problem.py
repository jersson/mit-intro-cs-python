balance = 999999
annualInterestRate = 0.18
#code to be evaluated begin here
months = 12
monthlyPaymentRate = annualInterestRate / months
minimumPayment = balance / months
maximumPayment = (balance / months) * (1 + monthlyPaymentRate) ** months

def getRemainingBalance(balance, annualInterestRate, minimumPayment):
    month = 1
    remainingBalance = balance
    while month <= 12:
        unpaidBalance = remainingBalance - minimumPayment
        interest = annualInterestRate * unpaidBalance / 12.0
        remainingBalance = unpaidBalance + interest
        month += 1
    remainingBalance = round(remainingBalance, 2)
    return remainingBalance

monthlyPaymentRate = (minimumPayment + maximumPayment) / 2
remainingBalance = getRemainingBalance(balance, annualInterestRate, monthlyPaymentRate) 

while remainingBalance != 0:
    if remainingBalance <= 0:
        maximumPayment = monthlyPaymentRate
    else:
        minimumPayment = monthlyPaymentRate

    monthlyPaymentRate = (minimumPayment + maximumPayment) / 2
    remainingBalance = getRemainingBalance(balance, annualInterestRate, monthlyPaymentRate) 
print("Lowest Payment: {}".format(round(monthlyPaymentRate,2)))