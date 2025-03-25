import art
import game_data
import random

print(art.logo)

is_game_end=False
score=0

computer_select=[]

def randomSelect():
    global computer_select
    while len(computer_select)<2:
        random_choice=random.choice(game_data.data)
        if random_choice not in computer_select:
            computer_select.append(random_choice)
        random_choice=0
    return computer_select

randomSelect()
first_choice=computer_select[0]
second_choice=computer_select[1]

while not is_game_end:
    user_guess=int(input("Who has more followers 1 or 2 ? : "))
   
    
    if user_guess==1 and first_choice['follower_count']>second_choice['follower_count']:
        print(f"You guessed right! {first_choice['name']} has more followers ({first_choice['follower_count']}) than {second_choice['name']}({second_choice['follower_count']}).")
        score+=1

    elif user_guess==2 and second_choice['follower_count']>first_choice['follower_count']:
        print(f"You guessed right! {second_choice['name']} has more followers ({second_choice['follower_count']}) than {first_choice['name']}({first_choice['follower_count']}).")
        score+=1

    else:
        print(f"Sorry, that's wrong! {first_choice['name']} actually has more followers than {second_choice['name']}.")
        is_game_end=True
        print(f"Your score is {score}")
    
    first_choice=second_choice
    second_choice=random.choice(game_data.data)






