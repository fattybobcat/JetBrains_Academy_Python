import math
import sys
import argparse

def select():
    print('''What do you want to calculate? 
    type "n" - for count of months, 
    type "a" - for annuity monthly payment,
    type "p" - for credit principal:''')
    type_calc = input()
    return type_calc

def countMonth(): # n 
    print('Enter credit principal:') 
    credit_principal = int(input())
    print('Enter monthly payment:')
    monthly_payment = int(input())
    print('Enter credit interest:')
    credit_interest = float(input())
    nominal_interest = nominalInterestRate(credit_interest) #credit_interest / (12 * 100)

    years , month = divmod(math.ceil(countsPeriod(credit_principal, monthly_payment, nominal_interest)), 12)
    print(f'You need {years} years and {month} months to repay this credit!')

def annuityPayment(): #a
    print('Enter credit principal:') 
    credit_principal = int(input())
    print('Enter count of periods:')
    count_periods = int(input())
    print('Enter credit interest:')
    credit_interest = float(input())
    annuity_payment = math.ceil(mAnnuityPayment(credit_principal, count_periods, credit_interest))
    print(f'Your annuity payment = {annuity_payment}!')

def creditPrincipal(): # p
    print('Enter monthly payment:')
    monthly_payment = float(input())
    print('Enter count of periods:')
    count_periods = int(input())
    print('Enter credit interest:')
    credit_interest = float(input())
    credit_principal = mCreditPrincipal(monthly_payment, count_periods, credit_interest)
    print(f'Your credit principal = {credit_principal}!')

def mCreditPrincipal(annuity_payment, count_periods, credit_interest):
    i_n = nominalInterestRate(credit_interest)
    credit_principal = annuity_payment / ((i_n * pow((1 + i_n), count_periods)) / (pow((1 + i_n), count_periods) - 1))
    return credit_principal

def mAnnuityPayment(credit_principal, count_periods, credit_interest):
    i_n = nominalInterestRate(credit_interest)
    annuity_payment = credit_principal * (i_n * pow((1 + i_n), count_periods)) / (pow((1 + i_n), count_periods) - 1)
    return annuity_payment

def nominalInterestRate(credit_interest):
    return float(credit_interest / (12 * 100))

def countsPeriod(credit_principal, monthly_payment, nominal_interest):
    x = monthly_payment / (monthly_payment - nominal_interest * credit_principal)
    count_period = math.log(x, 1 + nominal_interest)
    return count_period
def myerror():
    print('Incorrect parameters')
def main():
    parser = argparse.ArgumentParser()
    parser.error = ''
    parser.add_argument('--type', type=str, choices=['diff','annuity'], help="The type of payments: 'annuity' or 'diff'", required=True)
    parser.add_argument('--principal', type=int, help="Used for calculation of payment", required=True)
    parser.add_argument('--periods', type=int, help="parameter denotes the number of month or/and years needed to replay the credit", required=True)
    parser.add_argument('--interest', type=float, help="is specified without a percent sign", required=True)
    try:
        my_namespace = parser.parse_args()
        #print(my_namespace.type_calc)
        #print(my_namespace.principal)
        #print(my_namespace.periods)
        #print(my_namespace.interest)
        print(my_namespace)
    except :
        print('Incorrect parameters')   

if __name__ == '__main__':
    main()