import math

print("Welcome to the Mortgage Calculator!")

price_check = True

while price_check:
    price = input("Please insert the loan amount: ")
    if price.isdigit():
        price = float(price)
        if price <= 0:
            print("Has to be greater than zero ")
        else:
            price_check = False
    else:
        print("Has to be a number ")

dp_check = True
while dp_check:
    dp = input("what is your percent down payment?: ")
    if dp.isdigit():
        dp = float(dp)
        if dp <= 0:
            print("Has to be greater than zero ")
        if dp > 100:
            print("Has to be less than 100 ")
        else:
            dp_check = False
    elif "%" in dp:
        print("Without the percent sign please ")
    else:
        print("Has to be a number ")

dpa = (price * dp) / 100
ddpa = "${:,.2f}".format(dpa)

print("Your down payment amount is:", ddpa)

ir_check = True
while ir_check:
    ir = input("What is the interest rate?: ")
    if "%" in ir:
        print("Without the percent sign please ")
    elif not any(c.isalpha() for c in ir):
        ir = float(ir)
        if ir <= 0:
            print("Has to be greater than zero ")
        if ir > 100:
            print("Has to be less than 100 ")
        else:
            ir_check = False
            ir /= 100

    else:
        print("Has to be a number ")

mir = (ir / 12)

lt_check = True
while lt_check:
    lt = input("What is the Loan term? (years fixed): ")
    if lt.isdigit():
        lt = float(lt)
        if lt <= 0:
            print("Has to be greater than zero ")
        else:
            lt_check = False
    else:
        print("Has to be a number ")

tac_check = True
while tac_check:
    tac = input("Please add all additional monthly costs if any (Property tax, Home Insurance, HOA) : ")
    if tac.isdigit():
        tac = float(tac)
        tac_check = False
    else:
        print("Has to be a number ")

# M = P[r(1+r)^n/((1+r)^n)-1)]
principal = price - dpa
n = lt * 12
mp = (principal * mir * ((1 + mir) ** n)) / (((1 + mir) ** n) - 1)
mp_extra = mp + tac
dmp = "${:,.2f}".format(mp_extra)

print("Your monthly payment is:", dmp)
