#소스 구하기 

def primeNumber(maxNumber):
    primes = list(range(2, maxNumber))
    for i in primes:
        for j in primes:
            if j%i ==0 and j != i:
                primes.remove(j)
    
    return primes            
            

number = int(input("자연수를 입력해주세요."))

print("소수는 ", primeNumber(number))
