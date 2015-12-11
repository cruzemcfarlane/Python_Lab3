#Question 1
def powers(n):
    if n<=0:
        return 0
    else:
        return n**n

#Question 2
def sumSeries(n):
    if n==0:
        return 0
    else:
        return powers(n) + sumSeries(n-1)
    
#Question 3
def div(a,b):
    if a>=b:
        return (1+div(a-b,b))
    else:
        return 0

def mod(a,b):
    if a<b:
        return a
    else:
        return mod(a-b,b)

#Question 4
def lastDigit(x):
    return mod(x,10)

def allButlast(x):
    return div(x,10)

def sumDigits(n):
    if n<10:
        return n
    else:
        return lastDigit(n) + sumDigits(allButlast(n))

#Question 5        
def is_valid(n):
    if n in range(1000,7000) and sumDigits(n)%7==0:
        return True
    else:
        return False
