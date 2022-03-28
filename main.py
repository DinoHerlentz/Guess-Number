import random as rd

print("Guess number 1-100")

while True:
    num = rd.randint(1, 100)
    
    for i in range(5):
        # print(num)
        
        try:
            guess = int(input("Enter your guesses : "))
        except Exception as err:
            print(err)
            break
        
        if guess == num:
            print("Congratulations! You guessed the number!")
            break
        
        elif guess <= 0:
            print("Number 1-100 only!")
            break
        
        elif guess > 100:
            print("Number 1-100 only!")
            break
        
        elif guess < num:
            print("Hint : The number is higher.")
        
        elif guess > num:
            print("Hint : The number is lower.")
    
    else:
        print("Times up! The number i was thinking of was {}".format(num))
    
    play_again = input("Play again? (y/n) : ")
    
    if play_again in ("NO", "No", "no", "n"):
        print("Thank you for playing!")
        break
    elif play_again not in ("YES", "Yes", "yes", "y"):
        print("Invalid option!")
        break
