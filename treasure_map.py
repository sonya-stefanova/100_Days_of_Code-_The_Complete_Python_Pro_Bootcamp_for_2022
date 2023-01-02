row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

horizontal_value = int(position[0])
vertical_value = int(position[1])

map[vertical_value - 1][horizontal_value - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
