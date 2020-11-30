print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction=input("You're at the cross road. Where do you want to go?\nType 'left' or 'right'\n").lower()
if(direction)=="left":
  middle_of_lake=input('\nYou come to a lake. There is an island in the middle of the lake.\nType "wait" to wait for a boat or Type "swim" to swim across\n').lower()
  if(middle_of_lake == "wait"):
    door_color=input("\nYou arrive at the island unharmed. There is a house with 3 doors.\nOne red,one yellow and one blue.\nWhich color do you choose?\n").lower()
    if door_color == "yellow":
      print("\n~~You win!~~")
    elif door_color == "red":
      print("\nBurned by fire.\n~~GAME OVER~~")
    elif door_color == "blue":
      print("\nEaten by beasts.\n~~GAME OVER~~")
    else:
      print("\n~~GAME OVER~~")
  else:
    print("\nAttacked by trout.\n~~GAME OVER~~")
else:
  print("\nfall into a hole.\n~~GAME OVER~~")
