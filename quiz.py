score = 0 
answer1 = str(input("What is the capital of france? "))
answer2 = str(input("What is 2 + 2? "))
answer3 = str(input("What color is the sky? "))
if answer1 == "paris":
    print("Correct!!")
    score = score + 1
else:
    print("Wrong!!")
if answer2 == "4":
    print("Correct!!")
    score = score + 1
else:
    print("Wrong!!")
if answer3 == "blue":
    print("Correct!!")
    score = score + 1
else:
    print("Wrong!!")
print("You got " + str(score) + " out of 3!!")
