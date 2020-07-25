import math
import sys
import argparse


def differ(p, n, r):
    i = r / (100 * 12)
    cal = p / n
    s = 0
    for m in range(1, n + 1):
        D = cal + i * (p - (p * (m - 1)) / n )
        s += math.ceil(D)
        print(f'Month {m}: paid out {math.ceil(D)}')              
    print('Overpayment =', int(s) - int(p))

def cred_pri(n, A, r):

    i = r / (100 * 12)
    val = pow((1 + i), n)
    p = math.ceil(A / ((val * i) / (val - 1)))
    
    print(f'Your credit principal = {p}!')
    print('Overpayment =', (n * A) - p)


def month_count(p, A, r):
    i = r / (100 * 12)
    base = 1 + i
    x = A / (A - (i * p))
    n = math.ceil(math.log(x, base))
    
    if n < 12:
        print(f'You need {n} months to repay this credit!')
    elif n % 12 == 0:
        years = n//12
        print(f'You need {years} years to repay this credit!')
    else:
        years = n // 12
        months = n - years * 12 
        print(f'You need {years} years and {months} months to repay this credit!')
    print('Overpayment =', int(n * A - p))


def annuity(p, n, r):
    i = r / (100 * 12)
    val = pow((1 + i), n)
    A = math.ceil(p * ((i * val) / (val - 1)))
    print(f'Your annuity payment = {A}!')
    op = (n * A) - p
    print('Overpayment =', op)
    
    
parser = argparse.ArgumentParser()
parser.add_argument("--type", type = str)
parser.add_argument('--principal', type = float)
parser.add_argument('--periods', type = int)
parser.add_argument('--interest', type = float)
parser.add_argument('--payment', type = float)
args = parser.parse_args() 
if len(sys.argv) < 4 or args.type is None or args.type not in ['annuity', 'diff'] or (args.interest is None or args.interest < 0):
    print('Incorrect parameters.')
else:
    if args.type == 'diff':
        if args.payment is not None or (args.principal is None or args.principal < 0) or (args.periods is None or args.periods < 0):
            print('Incorrect parameters.')
        else:
            differ(args.principal, args.periods, args.interest)

    elif args.type == 'annuity':
        argument_list = [args.principal, args.periods, args.interest, args.payment]
        ctr = 0
        for i in argument_list:
            if i is None or i < 0:
                ctr += 1
                
        if ctr >= 2:
            print('Incorrect parameters.')
        else:
            if args.principal is not None and args.payment is not None:
                month_count(args.principal, args.payment, args.interest)
            elif args.periods is not None and args.payment is not None:
                cred_pri(args.periods, args.payment, args.interest)
            elif args.periods is not None and args.principal is not None:
                annuity(args.principal, args.periods, args.interest)
