import random
import pprint

bingoCard = []
def randomNumbers():
  number = random.randint(1,90)
  return number

def prettyPrint():
  for row in bingoCard:
    print(row)

numbers = []
for i in range(8):
  number = random.randint(1,90)
  if number not in numbers:
    numbers.append(randomNumbers())
numbers.sort()

bingoCard = [[numbers[0], numbers[1], numbers[2]], [numbers[3], "BINGO", numbers[4]],[numbers[5], numbers[6], numbers[7]]]

prettyPrint()


  


    




































































#import random
#import pprint

#bingoCard = []
#def randomNumbers():
  #number = random.randint(1,90)
  #return number
  


#def prettyPrint():
  #for row in bingoCard :
    #print(row)

#numbers = []
#for i in range(8):
  #number = random.randint(1,90)
  #if number not in numbers:
    #numbers.append(randomNumbers())
#numbers.sort()

#bingoCard = [[numbers[0], numbers[1], numbers[2]], [numbers[3], "BINGO", numbers[4]], [numbers[5], numbers[6], numbers[7]]]

#prettyPrint()












        

