line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()  # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
position = position.lower()
listPosition = list(position)
abc = ["a", "b", "c"]
letterIndex = abc.index(listPosition[0])

####MySolution#####
#if listPosition[0] == "a":
#  x = 0
#elif listPosition[0] == "b":
#  x = 1
#elif listPosition[0] == "c":
#  x = 2
#else:
#  print("Out of Range")

x = letterIndex
y = int(listPosition[1])-1


map[y][x] = "X"
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
