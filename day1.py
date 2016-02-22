'''We have 50 numbers from 1 to 50 on a whiteboard. At a time, we can erase 2 numbers, and add the gap between the 2 numbers back to the board. Example, if we erase 15 and 20, then we add 5 back. Repeat above until you only have 1 number on the board. Which of below are possible to be the last number?'''

import random
NUM = 50

def reduce(seq):
    maxIndex = len(seq) - 1
    firstChoiceIndex = random.randint(0,maxIndex)
    firstChoice = seq[firstChoiceIndex]
    del seq[firstChoiceIndex]
    maxIndex = len(seq) - 1
    secondChoiceIndex = random.randint(0,maxIndex)
    secondChoice = seq[secondChoiceIndex]
    del seq[secondChoiceIndex]
    seq.append(abs(firstChoice - secondChoice))

seq = [x + 1 for x in range(NUM)]

lastNums = [ ]
for i in range(5000):
    seq = [x + 1 for x in range(NUM)]
    while(len(seq) > 1):
        reduce(seq)
    lastNums.append(seq[0])
    print "Last Num",i,seq
    
print set(lastNums)

