import random

game = ["stone", "paper", "scissor"]

computer=random.choice(game)

human = input("choose your choice: ").strip().lower()

final = (computer,human)

computer_win = 0

if final in [("scissor", "stone"),("paper","scissor"),("stone","paper")]:
    print("Human wins")

elif final in [("scissor", "scissor"),("paper","paper"),("stone","stone")]:
    print("Draw")

else :
    computer_win = 1
    print("Computer wins")
    
    

game_file = open(file="game.txt", mode="a")
game_file.write(f"\n{computer},{human},{computer_win}")
game_file.close()



#print(computer)


#parquet - apache file (hadhoop)

