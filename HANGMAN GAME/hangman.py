import random
import hangman_stages
word_list = ['apple','beautiful','canvas']
lives=6
chosen_word = random.choice(word_list)

display=[]
for i in range (len(chosen_word)):
    display +='_'
print(display)
game_over=False
while not game_over:
     guessed_letter=input("Guess a letter :").lower()     #p  _ p p _ _
     for position in range (len(chosen_word)):   #0 1 2 3 4   #apple
         letter = chosen_word[position]
         if letter==guessed_letter:  #p == x
            display[position] = guessed_letter
     print(display)

     if guessed_letter not in chosen_word:
        lives -= 1
        print(lives,"chances left")
        if lives == 0:
            game_over = True
            print("YOU LOSE!!")
     if '_' not in  display:
        game_over = True
        print("YOU WIN!!") 
     print(hangman_stages.stages[lives])
           



        

