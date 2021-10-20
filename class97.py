intro = input("Enter you introduction: ")

character = 0
word = 1

for x in intro :
    character = character + 1
    if x == " " :
        word = word + 1

print ("Number of words: ", word)
print("")
print("Number of characters: ", character)