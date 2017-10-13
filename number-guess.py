secretGuess = 42
low = 0
high = 100
ans = (high + low)/2.0

print("Please think of a number between 0 and 100!")
print("Is your secret number 50?")

while ans != secretGuess:
    bet = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guess correctly.")
    
    if bet == 'l':
        low = ans
        ans = (ans + high)/2.0
        print("Is your secret number " + str(round(ans)) + "?")
    
    elif bet == 'h':
        high = ans
        ans = (low + ans)/2.0
        print("Is your secret number " + str(round(ans)) + "?")

    elif bet == 'c':
        print("Game over. Your secret number is " + str(round(ans)) + ".")
        break
    
    else:
        print("Sorry, I did not understand your input")
        
while ans == secretGuess:
    print("Your secret number is: ", + ans)
