import re

def checkMessage(M):
    for digit in M:
        if digit != '0' and digit != '1':
            print("Wrong Message")
            return False
                
    return True

def definePolynomial():
    print("Insert Polynomial:")
    P = input().lstrip('0')
    print()
    return P
    
def checkPolynomial(P):
    for coefficient in P:
        if coefficient != '0' and coefficient != '1':
            print("Wrong Polynomial")
            return False
                
    return True

def extendMessage(M, P):
    return M + '0' * (len(P) - 1)

def XOR(a, b):
    result = ""
    for i in range(len(b)):
        if int(a[i]) == int(b[i]):
            result += '0'
        else:
            result += '1'
    for i in range(len(b), len(a)):
        result += a[i]
    return result.lstrip('0')

def reverseXOR(a, b):
    result = ""
    for i in range(len(a) - len(b)):
        result += a[i]
    for i in range(len(a) - len(b), len(a)):
        if int(a[i]) == int(b[i - len(a) + len(b)]):
            result += '0'
        else:
            result += '1'
    return result

def calculateCRC(M, P):
    extendedM = extendMessage(M, P)
    remainder = XOR(extendedM, P).lstrip('0')
    while len(remainder) >= len(P):
        remainder = XOR(remainder, P).lstrip('0')
        print("Remainder: ",remainder)
    
    result = reverseXOR(extendedM, remainder)
    return result

def main():
    print("Insert Message:")
    M = input()
    print()
    if checkMessage(M) == False:
        return
    P = definePolynomial()
    if checkPolynomial(P) == False:
        return
    if len(M) < len(P):
        print("Message length should be greater than or equal to polynomial length.")
        return
    finalMessage = calculateCRC(M, P)
    print()
    print("Result: ", finalMessage)
    print()

main()