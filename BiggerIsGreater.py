import sys

def nextGreater(word):
    number = getNumberForString(word)
    pos = findFirstPosFromRightWhereLeftIsSmallerThanRight(number)
  
    if pos == -1:
        print "no answer"
    elif pos == len(number)-1:
        number = swapLastTwoDigits(number)
        printFinalWord(number)
    else:
        number = reArrangeNumber(number, pos)
        printFinalWord(number)

def reArrangeNumber(number, pos):
    digitX = number[pos-1]
    
    firstHalf = buildFirstHalf(number, pos, digitX)

    smallestGreaterThanDigitXPos = findSmallestGreaterThanDigitX(number, digitX, pos)
    del number[smallestGreaterThanDigitXPos]

    secondHalf = buildSecondHalf(number, pos, digitX)

    reArrangedNumber = firstHalf + secondHalf
    return reArrangedNumber
    
def buildFirstHalf(number, pos, digitX):
    firstHalf = number[0:pos-1]

    smallestGreaterThanDigitXPos = findSmallestGreaterThanDigitX(number, digitX, pos)
    firstHalf.append(number[smallestGreaterThanDigitXPos])

    return firstHalf

def buildSecondHalf(number, pos, digitX):
    secondHalf = number[pos:]

    reversedSecondHalf = []
    for val in reversed(secondHalf):
        reversedSecondHalf.append(val)

    reversedSecondHalf = placeDigitXAtCorrectPosition(reversedSecondHalf, digitX)

    return reversedSecondHalf

def placeDigitXAtCorrectPosition(reversedSecondHalf, digitX):
    correctlyPlaced = []
    placed = False
    for ele in reversedSecondHalf:
        if ele >= digitX and not placed:
            correctlyPlaced.append(digitX)
            placed = True
        correctlyPlaced.append(ele)
    if not placed:
        correctlyPlaced.append(digitX)
    
    return correctlyPlaced
    
    
def findSmallestGreaterThanDigitX(number, digitX, pos):
    smallestGreaterThanDigitX = -1
    smallestGreaterThanDigitXPos = -1

    number = number[pos:]
    for idx, val in enumerate(number):
        if val > digitX and (val < smallestGreaterThanDigitX or smallestGreaterThanDigitX == -1):
            smallestGreaterThanDigitX = val
            smallestGreaterThanDigitXPos = idx
    return smallestGreaterThanDigitXPos + pos;
            
    

def printFinalWord(number):
    for digit in number:
        sys.stdout.write(chr(digit))
    print    

def swapLastTwoDigits(number):
    temp = number[len(number)-2]
    number[len(number)-2] = number[len(number)-1]
    number[len(number)-1] = temp
    return number
    
def findFirstPosFromRightWhereLeftIsSmallerThanRight(number):
    prevDigit = 1
    for idx, val in enumerate(reversed(number)):
        if val < prevDigit:
            return len(number) - (idx)
        prevDigit = val
    return -1    
        

def getNumberForString(string):
    number = []
    for c in string:
        number.append(ord(c))
    return number    
    
t = raw_input()
words = []
for i in range(1,int(t)+1):
    words.append(raw_input())
for word in words:
    nextGreater(word)
