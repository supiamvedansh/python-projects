scissors=('''        _                        
 ___  ___(_)___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \
|___/\___|_|___/___/\___/|_|  |___/
 ''')

rock=(''' ____            _    
|  _ \ ___   ___| | __
| |_) / _ \ / __| |/ /
|  _ < (_) | (__|   < 
|_| \_\___/ \___|_|\_''')

paper=('''

 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
|_|         |_|              

''')
game_images=[rock,paper,scissors]
user_choice=(int(input ("What do you choose ? Type 0 for rock , 1 for paper and 2 for scissors\n") )) #type casted because then only we can compare user choice and computer choice

print(game_images[user_choice])

import random
computer_choice=random.randint(a=0,b=2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice==computer_choice:
    print("Its a draw")
elif user_choice==0 and computer_choice==1:
    print("you lose")
elif user_choice==0 and computer_choice==2:
    print("you win")
elif user_choice==1 and computer_choice==0:
    print("you win")
elif user_choice==1 and computer_choice==2:
    print("you lose")
elif user_choice==2 and computer_choice==0:
    print("you lose")
elif user_choice==2 and computer_choice==1:
    print("you win")
else:
    print("wrong choice , you lose")