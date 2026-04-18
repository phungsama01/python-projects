file = open("colors.txt", "w'")
file.write("my favorite color red")
file.close()
file = open("colors.txt", "r")
text = file.read()
file.close()
print(text)

