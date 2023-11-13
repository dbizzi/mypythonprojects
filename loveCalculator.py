print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
names = name1 + name2
names = names.lower()

t_count = names.count("t")
r_count = names.count("r")
u_count = names.count("u")
e_count = names.count("e")

trueCount = str(t_count + r_count + u_count + e_count)

l_count = names.count("l")
o_count = names.count("o")
v_count = names.count("v")
e_count = names.count("e")

loveCount = str(l_count + o_count + v_count + e_count)

loveScore = int(trueCount + loveCount)

if loveScore < 10 or loveScore > 90:
  print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif loveScore >= 40 and loveScore <= 50:
  print(f"Your score is {loveScore}, you are alright together.")
else:
  print(f"Your score is {loveScore}.")
