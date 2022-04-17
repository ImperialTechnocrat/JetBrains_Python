import argparse
import math


def loan_principal(payment, n, interest):
    interest = interest / 100 / 12
    principal = payment / ((pow(interest + 1, n) * interest) / (pow(interest + 1, n) - 1))
    principal = math.floor(principal)
    print(f"Your loan principal = {principal}!")
    print(f"Overpayment = {payment * n - principal}")


def monthly_payment(principal, n, interest):
    interest = interest / 100 / 12
    payment = principal * (interest * pow(1 + interest, n) / (pow(1 + interest, n) - 1))
    payment = math.ceil(payment)
    print(f"Your monthly payment = {payment}!")
    print(f"Overpayment = {payment * n - principal}")


def how_many_payment(principal, payment, interest):
    interest = interest / 100 / 12
    n = math.log((payment / (payment - interest * principal)), interest + 1)
    n = math.ceil(n)
    if n >= 24:
        if n % 12 == 0:
            print("It will take {} years to repay this loan!".format(n // 12))
        elif n % 12 == 1:
            print("It will take {} years and 1 month to repay this loan!".format(n // 12))
        else:
            print("It will take {} years and {} month to repay this loan!".format(n // 12, n % 12))
    elif n < 12:
        if n == 1:
            print("It will take 1 month to repay this loan!")
        else:
            print("It will take {} months to repay this loan!".format(n))
    else:
        if n == 12:
            print("It will take 1 year to repay this loan!")
        elif n == 13:
            print("It will take 1 year and 1 month to repay this loan!")
        else:
            print("It will take 1 year and {} months to repay this loan!".format(n % 12))
    print(f"Overpayment = {payment * n - principal}")


def diff(data):
    # --type=diff --principal=500000 --periods=8 --interest=7.8
    # 0-Principal, 1-interest, 3-period
    principal = data[0]
    interest = data[1] / 100 / 12
    period = data[3]
    repayment = 0
    for m in range(1, period + 1):
        payment = (principal / period) + interest * (principal - (principal * (m - 1) / period))
        payment = math.ceil(payment)
        print(f"Month {m}: payment is {payment}")
        repayment += payment
    print(f"Overpayment = {repayment - principal}")


def annuity(data):
    # 0-Principal, 1-interest, 2-payment, 3-period
    if data[0] == None:
        loan_principal(data[2], data[3], data[1])
    elif data[2] == None:
        monthly_payment(data[0], data[3], data[1])
    elif data[3] == None:
        how_many_payment(data[0], data[2], data[1])


def validation(listed):
    count = 0
    for i in data:
        if i == None:
            count += 1
    if data[1] == None:
        return 0
    return count == 1


parser = argparse.ArgumentParser()

parser.add_argument("-t", "--type")
parser.add_argument("-p", "--principal", type=int)
parser.add_argument("-i", "--interest", type=float)
parser.add_argument("-pay", "--payment", type=int)
parser.add_argument("-per", "--periods", type=int)

args = parser.parse_args()

data = [args.principal, args.interest, args.payment, args.periods]

if validation(data):
    if args.type == "diff":
        diff(data)
    elif args.type == "annuity":
        annuity(data)
else:
    print("Incorrect parameters")