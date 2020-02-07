#copyright catfat832
print("beta version")
print("welcome to the game")
print ("do you want to play the game y or n")
play_game = input()
if play_game == "y":
    print("are you sure?")
print("y or n")
game_play = input()
if game_play == "y":
    print("loading")
print("you are in a forest you can go right, left and forward. Which one will you chose? You have to put your answer in three times")
print("if you die it will quit the game")
right_for = input()
left_for =input()
forward_for = input()
if right_for == "right":
    print("you found a house look for a key you can look under the mat or behind a chest also for the chest tipe in chest and type in mat for mat")
elif left_for == "left":
    print("you were killed by a bear you lose")
    if left_for == "left":
        quit()
elif forward_for == "forward":
    print("you dround in the lake")
if forward_for == "forward":
    quit()

mat_house = input()
if mat_house == "mat":
    print("you lose")
if mat_house == "mat":
    quit()
chest_house = input()
if chest_house == "chest":
    print("you found a key you go inside the house you find a swich a button and a torch")
swich_house = input()
if swich_house == "swich":
    print("you were squshed to death by a anvile")
if swich_house == "swich":
    quit()
button_house = input()
if button_house == "button":
    print("you fell through a trap door and slowle roted away")
if button_house == "button":
    quit()
torch_house = input()
if torch_house == "torch":
    print("a door opens opens so you go in and you find the ruby and leave the house you win")
print("type quit to exit game")
guit_game = input()
if quit_game == "quit":
    quit()

    


