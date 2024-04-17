from distutils import core
import random

def checkMessage(M):
    if len(M) % 7 != 0:
        print("Wrong Message")
        return False
    
    for digit in M:
        if digit != '0' and digit != '1':
            print("Wrong Message")
            return False
                
    return True

def messageToMatrix(M):
    noOfRows = len(M) // 7 + 1
    noOfColumns = 8
    messageMatrix = [['0' for i in range(noOfColumns)] for j in range(noOfRows)]
    
    for i in range(len(M)):
        row = i // (noOfColumns - 1)
        col = i % (noOfColumns - 1)
        messageMatrix[row][col] = M[i]
        
    for i in range(noOfRows - 1):
        sum = 0
        for j in range(noOfColumns - 1):
            sum += int(messageMatrix[i][j])
        if sum % 2 != 0:
            messageMatrix[i][7] = '1'
            
    for i in range(noOfColumns):
        sum = 0
        for j in range(noOfRows - 1):
            sum += int(messageMatrix[j][i])
        if sum % 2 != 0:
            messageMatrix[j + 1][i] = '1'
            
    return messageMatrix

def bitCorruption(messageMatrix):
    noOfRows = len(messageMatrix)
    randomRow = random.randint(0, noOfRows - 2)
    print("Row:",randomRow + 1)
    randomCol = random.randint(0, 6)
    print("Column:",randomCol + 1)
    print()
    if messageMatrix[randomRow][randomCol] == '0':
        messageMatrix[randomRow][randomCol] = '1'
    else:
        messageMatrix[randomRow][randomCol] = '0'
    return messageMatrix

def findCorruptedBit(messageMatrix):
    noOfRows = len(messageMatrix)
    noOfColumns = 8
    corruptedRow = 0
    corruptedColumn = 0
    
    for i in range(noOfRows - 1):
        sum = 0
        for j in range(noOfColumns - 1):
            sum += int(messageMatrix[i][j])
        if sum % 2 != int(messageMatrix[i][noOfColumns - 1]):
            corruptedRow = i + 1
            break
        
    for i in range(noOfColumns):
        sum = 0
        for j in range(noOfRows - 1):
            sum += int(messageMatrix[j][i])
        if sum % 2 != int(messageMatrix[noOfRows - 1][i]):
            corruptedColumn = i + 1
            break
    
    return corruptedRow, corruptedColumn

def getPosition(corruptedRow, corruptedColumn, noOfColumns):
    position = (corruptedRow - 1) * noOfColumns + corruptedColumn
    return position

def main():
    print("Insert Message:")
    M = input()
    print()
    if checkMessage(M) == False:
        return
    initialMessageMatrix = messageToMatrix(M)
    print("Initial Message Matrix:")
    for row in initialMessageMatrix:
        print(row)
    print()
    messageMatrix = bitCorruption(initialMessageMatrix)
    print("Corrupted Message Matrix:")
    for row in messageMatrix:
        print(row)
    print()
    corruptedRow, corruptedColumn = findCorruptedBit(messageMatrix)
    print("Corrupted Row:",corruptedRow)
    print("Corrupted Column:",corruptedColumn)
    position = getPosition(corruptedRow, corruptedColumn, 8)
    print("Position of Corrupted Bit:",position)
    print()
        
main()