# Homework 2b - Dominick Sileo

import random

playerScore = 0
ComputerScore = 0

#gameTime = True

#while gameTime = True:

def generateRandomNumber():
     randomNumber = random.randint(1,3)
     return randomNumber

def getComputerHand( randomNumber ):
    if randomNumber == 1:
       computerHand = 's'
    elif randomNumber == 2:
       computerHand = 'p'
    else randomNumber == 3:
       computerHand = 'p'

     return computerHand

def getPlayerHand():
    playerHand = input ('Make a move (r/p/s?) or type sc for the score' )
    return playerHand

   if computerHand == 'r' and playerHand == 's':
        print ('You win!')
        computerScore = computerScore + 1
   elif computerHand == 's' and playerHand == 'r':
	print ('You win!')
        PlayerScore = PlayerScore + 1
   if computerHand == 's' and playerHand == 'p':
        print ('Computer chose scissors, you chose paper. You lose!')
	computerScore = computerScore + 1
   elif computerHand == 'p' and playerHand == 's':
	print ('Computer chose paper, you chose scissors. You win!')
        PlayerScore = PlayerScore + 1
   if computerHand == 'p' and playerHand == 'r':
        print ('Computer chose paper, you chose rock. You lose!')
        computerScore = computerScore + 1
   elif computerHand == 'r' and playerHand == 'p':
	print ('Computer chose rock, you chose paper. You win!')
        PlayerScore = PlayerScore + 1

return playerScore, computerScore

def gameScore( playerScore,  computerScore):
    if input ('sc')
    print ('The score is', gameScore)


#playAgain = input('Play again (y/n?)')
#if playAgain = 'y'
  #pass
#if playAgain = 'n'
  # print('Thanks, bye!')
   #gameTime = False