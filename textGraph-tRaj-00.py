'''
Program: TextGraph
Filename: textGraph-tRaj-00.py
Author: Tushar Raj
Description: The program generates a bar graph depending upon the users entry
Revisions: No revisions made
'''
import time # Import time module to use sleep method so that user can read the error message with sufficient time
#There are no literal constraint
#There are no class defined
#There are no function defined

### Step 1: Announce, prompt and get Response
print("TextGraph: Draw a bar graph using characters\n")

### Main Program starts here
#Prompt user to get the input for the graph
response = input("Enter up to 10 positive whole numbers less than 50: ")
print() # to give space between the user input and graph

### Step 2: Calculate and draw graph
#split the function on the basis of space delimiter and store them as form of list
if(int(len(response.split())) > 10):
    print("please enter the number of input less or equal to 10")
    print("\n\n****TextGraph program ended****") #Display the user that the TextGraph program have ended
    time.sleep(6) #wait for the 5 second before closing the terminal so that user can read the error message
    exit() #exit the program as user have given more than 10 input
else:
    numbers = response.split() #The split() method splits a string into a list. default is space if no delimeter is passed

for i in numbers:
    if(i.isdigit() == False or 0 > int(i) or int(i) > 50 ): #check if the value lies between 0 and 50 or it have anything else apart from digit
        print('?') #print ? as per the requirement of the program
        continue #continue with the next value of the for loop
    print(int(i)*'=') #print the = number of times the value entered by user, for multiplication operation value should be in interger data type

print("\n\n****TextGraph program ended****") #Display the user that the TextGraph program have ended
