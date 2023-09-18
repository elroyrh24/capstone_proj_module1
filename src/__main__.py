import csv 
import sys
import os
import employeefunctions as ef
import pyinputplus as pyi

#Prompt for showing menu options
preMenuPrompt = '''
==========================================================
     Welcome to the Generic Company Employee Database 
==========================================================
1. Show the database
2. Add a new record to the database
3. Delete a record from the database
4. Update a record from the database
5. Exit the company database
==========================================================
'''
#Prompt for main menu 
menuPrompt = 'Please enter which menu you want to enter (number): '


def clear_screen():
    """

    Function that cleans UI

    """
    #Windows ver
    if os.name == 'nt':
        _ = os.system('cls')
    #Linux and Mac ver
    else:
        _ = os.system('clear')

def start_db():
    """

    Function to startup the database

    """
    with open(path,'r',newline='') as file:
        #Reads the csv
        dbReader = csv.reader(file,delimiter=";")

        #Determines header of csv with next
        header = next(dbReader)

        #Defines actual database 
        database={'column':header}

        #Adds every row to dictionary with loop
        for row in dbReader:
            Emp_ID, Project_Name, Job_Title, FirstName,LastName, Sex, Age = row
            database.update({int(Emp_ID): [int(Emp_ID), Project_Name, Job_Title, FirstName,LastName, Sex, int(Age)]})

        #Returns the database to be used
        return database


def mainMenu():
    """

    Function that prompts user to choose an option from the main menu

    Updates csv file up to date with the dictionary in python every loop

    Breaks the loop and stops when exit is chosen

    """   
    while True:
        #Resets the screen
        clear_screen()

        #Prompts user with Menu
        print(preMenuPrompt)
        menu = pyi.inputInt(prompt=menuPrompt, min=1, max=6)
        #Checks if user exits
        if menu == 5:
            break
        else:
            #Executes choice by user 
            if menu == 1:
                menu = 'Show'
                ef.Show(db)
            if menu == 2:
                menu = 'Add'
                ef.Add(db)
            if menu == 3:
                menu = 'Delete'
                ef.Delete(db)
            if menu == 4:
                menu = 'Update'
                ef.Update(db)

            while True:
                #Asks if user wants to go back to main menu everytime a function ends
                backToMainMenu = pyi.inputYesNo(prompt='\nBack to the main menu? (yes/no): ')
                
                #If they do, stop the function and go back to main menu
                if backToMainMenu == 'yes':
                    clear_screen()
                    break

                #If they dont, run the function again
                else:
                    clear_screen()
                    eval(f'ef.{menu}(db)')
        
        #Keeps csv file updated to python dict
        with open(path,'w',newline='') as file:
            dbWriter = csv.writer(file,delimiter = ';')
            dbWriter.writerows(db.values())

if __name__ == '__main__':
    """

    Kickstarts the program when file is run

    """

    #Clean the screen...
    clear_screen()

    #Set the filepath to the database
    if getattr(sys, 'frozen', False):
        path = sys._MEIPASS
        path = os.path.join(path, 'ProjectData\data\data.csv') 
    else:
        path = os.getcwd()
        path = os.path.join(path, 'ProjectData\data\data.csv') 

    #Define the database
    db = start_db()

    #Starts the program
    mainMenu()    
    
