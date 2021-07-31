def started (integers) :
    sumResult = 0
    for n in integers :
        sumResult = sumResult + n
    return sumResult 
print(started([40,5,67,3,8,9,10,7]))


sumResult = started ([40,5,67,3,8,9,10,7]) 
def finish(sumResult) :  
    final = []
    for n in range(0,8):
        final.append(sumResult)
    print(final)
    return final
finish(sumResult)    
   


