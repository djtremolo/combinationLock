### sub functions
def convertToTuple(valueAsInt):
    valueAsZeroPaddedString = str(valueAsInt).zfill(3)
    return tuple(int(d) for d in valueAsZeroPaddedString)

def howManyDigitsAreRight(valueAsTuple, tupleToCompareAgainst):
    totalMatches = 0
    for a in valueAsTuple:
        totalMatches += tupleToCompareAgainst.count(a)
    return totalMatches

def howManyDigitsAreInCorrectPlace(valueAsTuple, tupleToCompareAgainst):
    # creates a tuple of booleans to indicate if the elements match between value tuples, eg: (True, False, True)
    matches = tuple(i == j for i, j in zip(valueAsTuple, tupleToCompareAgainst))
    return matches.count(True)

def condition(valueAsTuple, comparisionValueAsInt, rightDigits, rightDigitsInCorrectPlace):
    # returns True if the given conditions have an exact match
    comparisionValueAsTuple = convertToTuple(comparisionValueAsInt)

    ret = False
    rightDigitsFound = howManyDigitsAreRight(valueAsTuple, comparisionValueAsTuple)
    correctlyPlacedDigitsFound = howManyDigitsAreInCorrectPlace(valueAsTuple, comparisionValueAsTuple)

    if (rightDigitsFound == rightDigits) and (correctlyPlacedDigitsFound == rightDigitsInCorrectPlace):
        ret = True

    return ret

def checkConditions(valueAsInt):
    if not (0 <= valueAsInt < 1000):
        print ("checkConditions: illegal input\r\n")
        return False

    # returns True if the value fulfills all given criteria
    valueAsTuple = convertToTuple(valueAsInt)
    
    # 682: one digit is right and in its place
    if(not condition(valueAsTuple, 682, 1, 1)):
        return False

    # 614: one digit is right but in the wrong place
    if(not condition(valueAsTuple, 614, 1, 0)):
        return False

    # 206: two digits are right but both are in the wrong place
    if(not condition(valueAsTuple, 206, 2, 0)):
        return False

    # 738: all digits are wrong
    if(not condition(valueAsTuple, 738, 0, 0)):
        return False

    # 380: one digit is right but in the wrong place
    if(not condition(valueAsTuple, 380, 1, 0)):
        return False

    #otherwise, we have found it!
    return True


### main function
for valueToTry in range(1000):
    if checkConditions(valueToTry):
        print ("Found: %d.\r\n" % valueToTry)

### done






