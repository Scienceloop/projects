print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
horizontal= int(position[0])
vertical = int(position[1])
row= map[vertical-1]
row[horizontal-1] = "X"
