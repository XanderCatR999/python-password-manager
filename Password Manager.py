

program_name = input("Input Your program name   :")
inputted_username = input("Input Your Username   :")
inputted_password = input("Input Your Password   :")

#creates a file and appends it
with open("usernames_and_passwords.txt", "a") as file:
    file.write(program_name)
    file.write(" = ")
    file.write(inputted_username)
    file.write(" - ")
    file.write(inputted_password)
    file.write("\n")