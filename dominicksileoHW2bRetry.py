import random 

playerScore = 0
computerScore = 0

def getComputerHand():
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
       computerHand = 's'
    elif randomNumber == 2:
       computerHand = 'r'
    else:
       computerHand = 'p'
    return computerHand    
    
def getPlayerHand():
    playerHand = input ('Make a move (r/p/s?) or type sc for the score.' )
    while playerHand not in ['r','p','s']:
        if playerHand == 'sc':
            print('Your score is ' + str(playerScore) + ' Computer score is ' + str(computerScore))
        else:       
            print("That's not what I asked.")
        playerHand = input('Make a move (r/p/s?) or type sc for the score.')
    return playerHand

def playerResults(playerHand, computerHand):
    global playerScore
    global computerScore
    if playerHand == 'r' and computerHand == 's':
        print('You chose rock and the computer chose scissors. You win!')
        playerScore = playerScore + 1
        
    elif playerHand == 's' and computerHand == 'p':
        print('You chose scissor and the computer chose paper. You win!')
        playerScore = playerScore + 1
        
    elif playerHand == 'p' and computerHand == 'r':
        print('You chose paper and the computer chose rock. You win!')
        playerScore = playerScore + 1

    elif playerHand == 'r' and computerHand == 'p':
        print('You chose rock and the computer chose paper. You lose!')
        computerScore = computerScore + 1
        
    elif playerHand == 's' and computerHand == 'r':
        print('You chose scissors and the computer chose rock. You lose!')
        computerScore = computerScore + 1
        
    elif playerHand == 'p' and computerHand == 's':
        print('You chose paper and the computer chose scissors. You lose!')
        computerScore = computerScore + 1
    else:
        print("It's a draw!")

replayInput = 'y'
while replayInput == 'y':
    playerHand = getPlayerHand()
    computerHand = getComputerHand()
    playerResults(playerHand, computerHand)
    print('Play Again? y/n?')
    replayInput = input()
print('Thanks, bye!')
        

#Ask rps 
#show result
#ask if they want to play again
# replay or end game
# show score 


#create 6 inputs r p s 
#program needs to create rps
#create scoreboard and display it
#create y n loop for replaying game