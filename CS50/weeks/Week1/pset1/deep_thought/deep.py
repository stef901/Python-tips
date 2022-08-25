# implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
answer = input("was ist die Antwort für die Leben?")

#if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
if answer.strip() == "42":
    print("Yes")
elif answer.lower().strip() == "forty-two":
    print("Yes")
elif answer.lower().strip() == "forty-two":
    print("Ja")
    # case insensitive:
# strip() removes arrays, function removes everything we want.
else:
    print("No")
