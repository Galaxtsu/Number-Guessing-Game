import random
import time
import json # just for printing the high score at the end (learned it last minute)

high_score: dict[str, dict[str, int | float |None]] = {
    "Easy" : {
        'Time' : None,
        'Attempts' : None
    },
    "Medium" : {
        'Time' : None,
        'Attempts' : None
    },
    "Hard" : {
        'Time' : None,
        'Attempts' :None
    }
}

def play_round(chances): #includes the time
    guess_correctly = False
    user_num = 0
    attempts = 0
    random_num = random.randint(1, 100)
    start_time = time.time()
    while int(user_num) != random_num and attempts < chances:
        try:
            user_num = int(input("Guess a number between 1 and 100: "))
            attempts += 1
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.\n")
            continue
        if user_num < 1 or user_num > 100:
            print("Invalid input. Please enter a number between 1 and 100.\n")
            continue
        if user_num > random_num:
            print("Your guess is too high.\n")
        elif user_num < random_num:
            print("Your guess is too low.\n")
        else:
            print(f"You guessed the number! You got it in {attempts} attempts.")
            guess_correctly = True
    if attempts == chances and int(user_num) != random_num:
        print("You have run out of attempts. The number was", random_num,"\n")
    end_time = time.time()
    time_taken = end_time - start_time
    return attempts, time_taken, guess_correctly

def update_high_score():
    # this section is for attempts:
    global attempts_easy, attempts_medium, attempts_hard, dif_level, time_taken, guess_correctly, time_taken_easy, time_taken_medium, time_taken_hard
    if guess_correctly:
        if dif_level == "Easy":
            if high_score['Easy']['Attempts'] is None or attempts_easy < high_score['Easy']['Attempts']:
                high_score['Easy']['Attempts'] = attempts_easy
                print(f"New high score on easy: {high_score['Easy']['Attempts']} attempts\n")
            else:
                print("Nice try beating your score, loser.\n")
        elif dif_level == "Medium":
            if high_score['Medium']['Attempts'] is None or attempts_medium < high_score['Medium']['Attempts']:
                 high_score['Medium']['Attempts'] = attempts_medium
                 print(f"New high score on medium: {high_score['Medium']['Attempts']} attempts\n")
            else:
                print("Nice try beating your score, loser.\n")
        elif dif_level == "Hard":
            if high_score['Hard']['Attempts'] is None or attempts_hard < high_score['Hard']['Attempts']:
                high_score['Hard']['Attempts'] = attempts_hard
                print(f"New high score on hard: {high_score['Hard']['Attempts']} attempts\n")
            else:
                print("Nice try beating your score, loser.\n")
    # this section is for time:
        if dif_level == "Easy":
            if high_score['Easy']['Time'] is None or time_taken_easy < high_score['Easy']['Time']:
                high_score['Easy']['Time'] = time_taken_easy
        elif dif_level == "Medium":
            if high_score['Medium']['Time'] is None or time_taken_medium < high_score['Medium']['Time']:
                high_score['Medium']['Time'] = time_taken_medium
        elif dif_level == "Hard":
            if high_score['Hard']['Time'] is None or time_taken_hard < high_score['Hard']['Time']:
                high_score['Hard']['Time'] = time_taken_hard
 
print("Welcome to the number guessing game! The numbers you have to guess are 1-100. Good luck!\n\n")
#Actual guessing part of the code:
while True:
    dif_level = input("\nWhat difficulty level would you like to choose:\nEasy (10 chances)\nMedium (5 chances)\nHard (3 chances)\n\n ")
    
    if dif_level == "Easy":
        attempts_easy, time_taken_easy, guess_correctly = play_round(10)
        update_high_score()
        
    elif dif_level == "Medium":
        attempts_medium, time_taken_medium, guess_correctly = play_round(5)
        update_high_score()
        
    elif dif_level == "Hard":
        attempts_hard, time_taken_hard, guess_correctly = play_round(3)
        update_high_score()
    else:
        print("Invalid input. Please enter Easy, Medium, or Hard.\n")

    again = input("\nWould you like to play again? Yes or No: ")
    if again == "No":
        break

print("Thank you for playing! Here are your high scores:\n")
for level, scores in high_score.items():
    scores_str = json.dumps(scores, indent=4)
    print(f"-------{level}------- high score:\n{scores_str}\n")
