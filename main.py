username = input("Enter your Username: \n")
password = input("Enter your Password: \n")

print("Fine, I created the file pws.txt. ")

file = open("pws.txt", "a")

file.write("----------------------")
file.write("\n")
file.write("Username: ")
file.write(username)
file.write("\n")
file.write("Password: ")
file.write(password)
file.write("\n")
file.close()

