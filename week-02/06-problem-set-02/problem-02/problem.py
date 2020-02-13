balance = 3329
annualInterestRate = 0.2
# output>Lowest payment: 310
#program to be pasted begin here
lowestPayment = 0
remainingBalance = balance
while remainingBalance >= 0:
    month = 1
    remainingBalance = balance
    lowestPayment += 10
    while month <= 12:
        unpaidBalance = remainingBalance - lowestPayment
        interest = annualInterestRate * unpaidBalance / 12.0
        remainingBalance = unpaidBalance + interest
        month += 1
print("Lowest payment: " +  str(lowestPayment))
