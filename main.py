#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as names:
    list_of_names = names.readlines()

with open("./Input/Letters/starting_letter.txt", mode="r") as mail:
    new_mail = mail.read()

for name in list_of_names:
    file_name = f"letter_to_{name.strip()}"
    n_mail = new_mail.replace("[name]", f"{name.strip()}")
    with open(f"./Output/ReadyToSend/{file_name}", mode="w") as file:
        file.write(n_mail)

