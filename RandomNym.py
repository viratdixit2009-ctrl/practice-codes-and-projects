import random #Now  you can tell computer to pick random a num. btw your range . For me it will be (1-100)

print("Welcome to super fun number guessing game")

#now for more good experience i am gonna add feature to select difficuilty of a game.

difficuilty = input("How hard you wanna go (easy/medium/hard").lower()
if difficuilty == "easy":
	max_attempts = 7
elif difficuilty == "medium":
	max_attempts = 3
else :
	max_attempts= 1
#now using variable tell computer to pick a random number.
secret_num = random.randint(1 , 100)	
attempts = 0 
while attempts < max_attempts :
	guess = int(input("guess the number btw 1 to 100"))
	attempts = +1
	if guess < secret_num:
		print("Too Low !!!")
	elif guess > secret_num:
		print("Too High!!!")
	else:
		print(f"***||||||:Congratulations you have guessed the right number :||||||***")
	print("you've got it in {attempts} tries ")
  break 
	  
	else:
		print(f"sorry you are out of attempt ! the number was {secret_num}.")
		
