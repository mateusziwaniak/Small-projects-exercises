import decimal

def pi():

    decimal.getcontext().prec += 2  # extra digits for intermediate steps
    three = decimal.Decimal(3)      # substitute "three=3.0" for regular floats
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n + na, na + 8
        d, da = d + da, da + 32
        t = (t * n) / d
        s += t
    decimal.getcontext().prec -= 2
    return +s               # unary plus applies the new precision

while True:

    n = int(input("How many digits after coma you want?"))
    if n > 1000:
        print("Max number is 1000, please enter it again: ")
    else:
        break


decimal.getcontext().prec = n+1
pi = pi()

print(pi)