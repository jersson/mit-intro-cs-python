balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
# output>Remaining balance: 31.38
#program to be pasted begin here
month = 1
remainingBalance = balance
while month <= 12:
    minimumPayment = remainingBalance * monthlyPaymentRate
    unpaidBalance = remainingBalance - minimumPayment
    interest = annualInterestRate * unpaidBalance / 12.0
    remainingBalance = unpaidBalance + interest
    month += 1
remainingBalance = round(remainingBalance, 2)
print("Remaining balance: {}".format(remainingBalance))
