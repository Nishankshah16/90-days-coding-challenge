#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

placeholder="[name]"
with open("./DAY24/Input/Names/invited_names.txt") as file:
    name= file.readlines()
    print(name)

with open("./DAY24/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents=letter_file.read()
    for names in name:
        stripped_name=names.strip()
        new_letter=letter_contents.replace(placeholder,stripped_name)
        print(new_letter)
        with open(f"./DAY24/Output/ReadyToSend/letter_for_{stripped_name}.docx",mode="w") as completed_letter:
            completed_letter.write(new_letter)
