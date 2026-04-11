import random 
choices={"snake":1,"water":-1,"gun" :0}
rev_choices={1:"snake",-1:"water",0:"gun"}

print("Welcome to the snake , water , gun !")

user_input=(input("enter choice(snake/water/gun) :")).lower()

if user_input in choices :
   user_value=choices[user_input]

   user_string=(rev_choices[user_value])
   com=random.choice(list(choices.values()))
   com_string=(rev_choices[com])

   if (com==user_value) :
    print('tie')
   elif(user_value==0 and com==1) or \
    (user_value==1 and com==-1 ) or \
    (user_value==-1 and com==0 ) :
    print("you won")
    
   else:
    print("you lose")  
       
else:
    print("Invalid choice! Please run the game again and type snake, water, or gun.")

if user_input in choices :
   user_value=choices[user_input]
   print(f"your choice :{user_string} \ncom choice:{com_string}")
