# Make a Love Calculator! 
# .lower() and .count()
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_case_one = name1.lower()
lower_case_two = name2.lower()

print("T", lower_case_one.count("t") + lower_case_two.count("t") , "L", lower_case_one.count("l") + lower_case_two.count("l"))
print("r", lower_case_one.count("r") + lower_case_two.count("r") , "o", lower_case_one.count("o") + lower_case_two.count("o"))
print("u", lower_case_one.count("u") + lower_case_two.count("u") , "v", lower_case_one.count("v") + lower_case_two.count("v"))
print("e", lower_case_one.count("e") + lower_case_two.count("e") , "e", lower_case_one.count("e") + lower_case_two.count("e"))

love_score_one = lower_case_one.count("t") + lower_case_two.count("t") + lower_case_one.count("r") + lower_case_two.count("r") + lower_case_one.count("u") + lower_case_two.count("u") + lower_case_one.count("e") + lower_case_two.count("e")
lover_score_two = lower_case_one.count("l") + lower_case_two.count("l") + lower_case_one.count("o") + lower_case_two.count("o") + lower_case_one.count("v") + lower_case_two.count("v") + lower_case_one.count("e") + lower_case_two.count("e")

print(f"Your score is {love_score_one}{lover_score_two}% you are meant to be together!")

# Emin.lower()
# Emin.count("e")
# lower_case_name = "Emin".lower()
# lower_case_name.count("e")