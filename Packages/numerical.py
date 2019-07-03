
import sympy

def numberOfPrimeFactors(n):
    c=0
    for i in range(2,n):
        #print(sympy.isprime(i))
        if(sympy.isprime(i) and n%i==0):
            c=c+1
    return c
def isSpecialNumber(n,p):
    if(numberOfPrimeFactors(n)>=p):
        return True
    else:
        return False
if __name__=="__main__":
    p=int(input())
    for _ in range(int(input())):
        if(isSpecialNumber(int(input()),p)):
            print("YES")
        else:
            print("NO")