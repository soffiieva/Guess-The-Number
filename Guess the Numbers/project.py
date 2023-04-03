import random

def GuessNumber():
    NumberOfGuessing = 0
    CounterOfRightPositions = 0
    TryNumber = 1

    numbers = random.sample(range(0, 10), 4)
    numbersAnswer = ' '. join(map(str, numbers)) #String for displaying the given number without parentheses2

    while CounterOfRightPositions != 4 and NumberOfGuessing < 10:
        print("🎲ATTEMPT NUMBER: ", TryNumber)
        TryNumber+=1

        #Block for incorrect input
        try:
            userInput = list(map(int, input("Input 4 numbers: ").split()))
        except:
            return "🚩IT IS NOT NUMBER! TRY ANOTHER TIME"

        if len(userInput) != 4 or len(set(userInput)) == 1:
            return "🚩WRONG NUMBER! TRY ANOTHER TIME"
        
        #number of correct numbers
        RightNumbers = list(set(userInput) & set(numbers))
        CounterOfRightNumbers = len(list(set(userInput) & set(numbers)))
        print("CORRECT NUMBERS: ",CounterOfRightNumbers, end=" 🔹 ") 

        #number of correct numbers
        for num in RightNumbers: 
            if numbers.index(num) == userInput.index(num): CounterOfRightPositions+=1
        print("CORRECT POSITIONS: ",CounterOfRightPositions, end="\n\n")

        if CounterOfRightPositions < 4: CounterOfRightPositions = 0  #If there are less than 4 correct positions the counter is reset to zero

        NumberOfGuessing+=1

    #If after 10 attempts there was still no correct answer
    if CounterOfRightPositions != 4:
        print("❌GAME OVER!❌ MY NUMBERS WAS: ", end=" ")
        return numbersAnswer
    
    #Displayed when the answer is correct
    print("🎉YOU WIN!🎉 IT WAS: ", end = " ")
    return numbersAnswer
    

print(GuessNumber())


