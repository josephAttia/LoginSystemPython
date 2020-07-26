import time
import random


selection = 0
answer1 = "N/A"
answer2 = "N/A"
answer3 = "N/A"
username = "N/A"
password = "N/A"
rpassword = "N/A"
restart = "N/A"

print("What is your name")
fn = input(":")
print("What is your last name")
ln = input(":")

#Prompts Security Questions
print("Choose One Security Question for Future Login")
time.sleep(1)

for x in range(10):
    print("*" , end = '')
    time.sleep(0.01)
print("\n")
print("1. Name of your first pet")
print("2. Mother's Maiden Name")
print("3. First School you attended")

selection = int(input("Selection: "))

if selection == 1:
    
        #Load
    for x in range(10):
        print("*" , end = '')
        time.sleep(0.01)

        
    #Prompt
    print("\n")
    print("1. Name of your first pet")
    answer1 = input("Answer: ")
    print("👍")
    
elif selection == 2:
    
        #Load
    for x in range(10):
        print("*" , end = '')
        time.sleep(0.01)

        
    #Prompt
    print("\n")
    print("2. Mother's Maiden Name")
    answer2 = input("Answer: ")
    print("👍")
    
else:
    
    #Load
    for x in range(10):
        print("*" , end = '')
        time.sleep(0.01)
        
   #Prompt
    print("\n")
    print("3. First School you attended")
    answer3 = input("Answer: ")
    print("👍")

#Time for the Password
print("Make your password")
for x in range(30):
        print("*" , end = '')
        time.sleep(0.01)
print("\n")
password = input("Password:")
rpassword = input("Re-type Password:")

while password == rpassword:
    print("Password Set 👍")
    break
if password != rpassword:
    print("Due to security reasons you get one last try to set a password")
    restart = input("Type R to Try again: ")

if restart == "R":
    for x in range(30):
        print("*" , end = '')
        time.sleep(0.01)
    print("\n")
    password = input("Password:")
    rpassword = input("Re-type Password:")
    print("Password Set 👍")

print("Genertaing Easy (But Secure) Username, Please be patient")
time.sleep(2)
for x in range(300):
        print("*" , end = '')
        time.sleep(0.01)
print("\n")
username = fn[:1] + ln + str(random.randint(1,20))
print("Your Username: " + username)
print("Your Password: " + password)
    
    
    
    

