def pyramidSum(lower, upper, margin=0):
    blanks = " " * margin
    print(blanks, lower, upper)
    
    if lower > upper:
        print(blanks, 0)
        return 0
    else:
        result = lower + pyramidSum(lower + 1, upper, margin + 4)
        print(blanks, result)
        return result

pyramidSum(1, 4)