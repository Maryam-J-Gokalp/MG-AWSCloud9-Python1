l = int(input('beginning of interval: '))
u = int(input('end of the interval: '))
#create a for loop inThe range to see if is prime number
#4LoopWeCheckIfRangel=1 & u=100 itGoes1 to 99)2 getWholerangeWeSay u+1 
for num in range(l, u + 1): 

 #CheckIf num >1:coz all primeNumberGreater >1 ifLessThan1 isNot PrimeNumber
    if num > 1: 

#2d 4LoopCheckEachNumbertoSee IfIsPrime in range(2, num): CodeBelowCheck between1 to100 is divisableBy100 4LoopBreak ifNum%i == 0: means is not primeNumber
        for i in range(2, num):  
            if num%i == 0: 
                break
              
#OrIfNotBreakOut PrintNum means was a PrimeNumber IsGoingToPrintItOut
        else:
            print(num)
            
            

#for n in range(1, 251):
#   for x in range(2, n):
 
#       if n % x == 0:
#          break
#  else:
#     print(n)
        
##Output = 250
#233, 239, 241
#primes number= (3, 5, 7, 11, 13, 17, 19, ...and so on)