import tabulate as tbt
import pyinputplus as pyi


#Prompts for functions
showMenuPrompt='''
==========================================================
                       Show Menu 
==========================================================
1. Show the entire database
2. Find specific records
3. Cancel
==========================================================
'''
updateMenuPrompt='''
==========================================================
                      Update Menu 
==========================================================
1. Field 
2. Row
3. Projects
4. Cancel
==========================================================
'''
specificUpdatePrompt='''
==========================================================
                       Field List 
==========================================================
1. Project_Name
2. Job_Title
3. First Name
4. Last Name
5. Sex
6. Age
7. Cancel
==========================================================
'''
columnUpdatePrompt='''
==========================================================
                  List of Editable Values
==========================================================
'''
findPrompt='''
==========================================================
                  List of Findable Values
==========================================================
1. Emp_ID
2. Project_Name
3. Job_Title
4. First Name
5. Last Name
6. Sex
7. Age
8. Cancel
==========================================================
'''
addPrompt='''
==========================================================
                        Add Menu
==========================================================
1. Add a new record
2. Cancel
==========================================================
'''

def Show_All(database, title='\nList of Employees\n'):
        """

        Args:
            database (Dict): Database to be shown
        
        Returns:
            Returns a printed table of the database using tabulate module

            
        """
        if len(database) > 0:
                #Get header data
                column_data = database.get("column", [])
                filtered_dict = {key: value for key, value in database.items() if key != "column"}
        
                #Sorts by Emp_ID
                sorted_data = dict(sorted(filtered_dict.items(), key=lambda item: item[1][0], reverse=False))

                #Merge header and sorted data
                sorted_database = {"column": column_data, **sorted_data}

                #Define header and data for table
                data = list(sorted_database.values())[1:]
                header = sorted_database['column']

                #Actually prints the table
                print(tbt.tabulate(data,header, tablefmt='outline'))
                print('\n')
        else:
                print("Database not found.")
        


def FindAdvanced(database, dataval, id):

        """
        Function that finds inputted value in the database

        Also checks if the data is actually in the database or not

        Returns:
            resultHeader: Header part of table for printing with tabulate
            resultData: Actual data of the table for printing with tabulate
        """        
        #Checks if data appears once in the column
        found = False
        for key, data_values in database.items():
                if dataval == data_values[id]:
                        found = True
                        break

        #Initializes dictionary for showing the records
        resultList = {}

        #Starts find process if data appears once
        if found:

                #Iterates through the database
                for i, v in list(database.items()):

                        #Adds header and skips
                        if i == "column":
                                resultList.update({"column": v})
                                continue

                        #Adds data that match user input
                        if v[id] == dataval:
                                resultList.update({i : v})

                #Defines data and header of result table
                resultHeader = resultList["column"]
                resultData = list(resultList.values())[1:]

                #Prints the table of records matching the user input
                print(tbt.tabulate(resultData,resultHeader,tablefmt="outline"))

        #Returns user with data that isnt found in the database
        else:
                print(f"\n{dataval} not found in database.")
        



def Find(database):
        """

        Menu for all the possible find options the user could use on the database

        """        
        #Prints options 
        print(findPrompt)

        #Asks which column to search
        findAsk = pyi.inputInt(prompt="Enter what filter you want to use: \n",
                               min = 1,
                               max = 8
                                )


        #Inputs necessary data for the actual find function

        #Emp_ID
        if findAsk == 1:
                FindAdvanced(database, dataval =pyi.inputInt(
                        prompt="Enter the ID number of the employee record you want to find: "
                ),id = 0)

        #Project
        if findAsk == 2:
                FindAdvanced(database, dataval =pyi.inputStr(
                        prompt="Enter the name of the project you want to find (with spaces, leave blank if none): ",
                        applyFunc = lambda x: x.title(),
                        default = "N/A",
                        limit = 1
                ),id = 1)

        #Job
        if findAsk == 3:
                FindAdvanced(database, dataval =pyi.inputStr(
                        prompt="Enter the name of the job title you want to find (with spaces): ",
                        applyFunc = lambda x: x.title(),
                ),id = 2)

        #First name
        if findAsk == 4:
                FindAdvanced(database, dataval =pyi.inputStr(
                        prompt="Enter the first name you want to find: ",
                        applyFunc = lambda x: x.title(),
                ),id = 3)
        
        #Last name
        if findAsk == 5:
                FindAdvanced(database, dataval =pyi.inputStr(
                        prompt="Enter the last name you want to find: ",
                        applyFunc = lambda x: x.title(),
                ),id = 4)

        #Sex
        if findAsk == 6:
                FindAdvanced(database, dataval =pyi.inputChoice(
                        prompt="Enter the gender you want to find (m/f): ",
                        applyFunc = lambda x: x.title(),
                        choices=["M","F"]
                ),id = 5)

        #Age
        if findAsk == 7:
                FindAdvanced(database, dataval =pyi.inputInt(
                        prompt="Enter the age of the employees you want to find: "
                ),id = 6)
        
        elif findAsk == 8:
                Show(database)

        #If user picks cancel which is 8, function ends and goes back to the prompt asking if they want to go back to the main menu.

def Show(database):
        print(showMenuPrompt)
        showMenu = pyi.inputInt(prompt="How much do you want to show? (number): ", min=1,max=3)

        if showMenu == 1:
                Show_All(database)
        if showMenu == 2:
                Find(database)



def Add(database):
        """

        Args:
            database (Dict): Database to be appended to

        Adds new row to the end of the database with values

        """        
        id_list = []
        for idx, vals in list(database.items()):
                if idx == "column":
                        continue
                elif vals[0] not in id_list:
                        id_list.append(vals[0])

        print(addPrompt)
        addPreCheck = pyi.inputInt(prompt="Do you want to add data to the database? (number): ",min=1,max=2)

        if addPreCheck == 1:

                #Automatically determines Employee ID
                Emp_ID = pyi.inputInt(prompt="Enter the ID of the employee: ",min=0)
                if Emp_ID in id_list:
                        print("Employee ID is already being used.")
                else:   
                        tempsave_data = {}

                        #Asks for input
                        Project_Name = pyi.inputStr(
                                prompt="Enter the name of the project the employee is assigned to (Leave blank if none): ",
                                applyFunc=lambda x: x.title(),
                                blockRegexes=[r"[0-9]"],
                                default='N/A',
                                limit = 1
                        )
                        Job_Title = pyi.inputStr(
                                prompt="Enter the job title of the employee: ",
                                applyFunc=lambda x: x.title(),
                                blockRegexes=[r"[0-9]"],
                        )
                        FirstName = pyi.inputStr(
                                prompt="Enter the first name of the employee: ",
                                applyFunc=lambda x: x.title(),
                                blockRegexes=[r"[0-9]"],
                        )
                        LastName = pyi.inputStr(
                                prompt="Enter the last name of the employee: ",
                                applyFunc=lambda x: x.title(),
                                blockRegexes=[r"[0-9]"],
                        )
                        Sex = pyi.inputChoice(
                                choices=["M","F"],
                                prompt="Enter the sex of the employee: "
                        )
                        Age = pyi.inputInt(
                                prompt="Enter the age of the employee: "
                        )

                        tempsave_data.update({"column":database["column"]})
                        tempsave_data.update({Emp_ID: [Emp_ID, Project_Name, Job_Title, FirstName, LastName, Sex, Age]})

                        print("New Record: ")
                        print(tbt.tabulate(list(tempsave_data.values())[1:],tempsave_data["column"],tablefmt="outline"))

                        addCheck = pyi.inputYesNo(prompt="Are you sure you want to save this data? (yes/no) ") 
                        if addCheck == 'yes':
                                #Adds the data to the dictionary
                                database.update(
                                        {Emp_ID: [Emp_ID, Project_Name, Job_Title, FirstName, LastName, Sex, Age]}
                                )

                                print("Data saved.")
                        else:
                                Add(database)

                        #Shows the database
                        Show_All(database)

        #Back to menu
        return database

def Delete(database):
        """

        Function that deletes a record from the database by matching their employee id

        """        

        #Shows user the database 
        Show_All(database)

        #Asks user for which record to delete with their Emp_ID
        targetID = pyi.inputInt(prompt="Enter the employee ID of the record you want to remove: ",max=(len(database)-2))

        #If the index is actually valid, proceeds
        if targetID <= len(database)-2:

                #Shows record that is to be deleted
                print(database[targetID])

                #Makes sure user wants to delete the record
                removeCheck = pyi.inputYesNo(prompt="Are you sure you want to remove this record? (yes/no): ")

                #If they do...
                if removeCheck == 'yes':

                        #Iterate through the database
                        for idx, val in list(database.items()):
                                #Skip the header
                                if idx == "column":
                                        continue
                                
                                #Delete the data matching the index
                                if targetID == val[0]:
                                        del database[idx]

                        #Shows database after deletion
                        Show_All(database)
        #If data isnt actually valid
        else:
                #Returns prompt informing user the employee ID is invalid
                print(f"Record with Emp_ID of {targetID} is not in the database.")

def specificUpdate(database):
        """
        Function that updates one specific value of the database based on their employee ID
        
        Args:
            database (Dict): Database to be updated
        """

        #Prints options user has on which fields they can change
        print(specificUpdatePrompt)

        #Asks user to pick which field to change
        specifyUpdate = pyi.inputInt(prompt="Which field do you want to change (number)? ",min=1,max=7)

        #If they dont choose to cancel...
        if specifyUpdate != 7 :

                #Ask the user what is the ID of the record they want to change
                specifyID = pyi.inputInt(prompt="ID of record to be updated: ")

                #Define the dictionaries to be used for comparing the data before and after the change
                oldRecord = {}
                newRecord = {}

                #Iterates through the database
                for i, v in list(database.items()):
                        #Adds header to the comparison dicts then continues
                        if i == 'column':
                                oldRecord.update({"column":v})
                                newRecord.update({"column":v})
                                continue
                        
                        #If the data is actually the one the user wants
                        if i == specifyID:

                                #First, updates the old record with the data before being altered
                                oldRecord.update({i:v})
                                print(f"Current value: \n")

                                #Prints old record before any changes
                                print(tbt.tabulate(list(oldRecord.values())[1:],oldRecord["column"],tablefmt="outline"))

                                #Asks user what the new value will be if its a string field
                                if type(v[specifyUpdate]) == str:
                                        specifyField = pyi.inputStr(prompt="Enter new field value: ",
                                                        applyFunc = lambda x: x.title()
                                                        )
                                #And same but if its an integer field
                                elif type(v[specifyUpdate]) == int:
                                        specifyField = pyi.inputInt(prompt="Enter new field value: ",
                                                        )
                                        
                                #Actually changes the value 
                                v[specifyUpdate] = specifyField

                                #Updates the comparison record
                                newRecord.update({i:v})

                                #Show the new value in the table
                                print(f"New value: \n")
                                print(tbt.tabulate(list(newRecord.values())[1:],newRecord["column"],tablefmt="outline"))   

        #If user chooses to cancel, it just goes back to the main update function after prompting user if they want to go back to the main menu                    

def rowUpdate(database):
        """
        Function that updates an entire record (except ID) from the database

        Args:
            database (Dict): Database to be updated
        """        

        #Make sure the user wants to update a full row
        rowUpdateCheck = pyi.inputYesNo(prompt="Are you sure you want to update an entire row? (yes/no) ")

        #If they are...
        if rowUpdateCheck == 'yes':

                #Ask which record to be updated
                specifyID = pyi.inputInt(prompt="ID of record to be updated: ",max=(len(database)-2))

                #Define the comparison records
                oldRecord = {}
                newRecord = {}

                #Iterates through the database
                for i, v in list(database.items()):
                        #If header...
                        if i == 'column':

                                #Adds headers to records for comparison
                                oldRecord.update({"column":v})
                                newRecord.update({"column":v})

                                #Continues loop
                                continue

                        #If it's the record the user wants...
                        if i == specifyID:

                                #Creates a copy and shows current record before any changes
                                oldRecord.update({i:v})
                                print(f"Current values: \n")
                                print(tbt.tabulate(list(oldRecord.values())[1:],oldRecord["column"],tablefmt="outline"))

                                #Iterates through the row
                                for indx, field in enumerate(v):

                                        #Skips ID of record
                                        if indx == 0:
                                                continue
                                        #Asks the user what they want to change the record to, with the default being the old values
                                        elif indx < 5:
                                                specifyField = pyi.inputStr(prompt=f"Enter new field value (currently {field}, leave blank if unchanged): ",
                                                                applyFunc = lambda x: x.title(),
                                                                default = field,
                                                                limit = 1
                                                                        )
                                        #Special input for the sex field due to it being only M OR F
                                        elif indx == 5:
                                                specifyField = pyi.inputChoice(prompt=f"Enter new field value (currently {field}, leave blank if unchanged): ",
                                                                applyFunc = lambda x: x.title(),
                                                                default = field,
                                                                limit = 1,
                                                                choices=["M","F"]
                                                                        )
                                        #Special input for the age field due to it being integer
                                        elif indx == 6:
                                                specifyField = pyi.inputInt(prompt=f"Enter new field value (currently {field}, leave blank if unchanged): ",
                                                                default = field,
                                                                limit = 1,
                                                                min = 1
                                                                        )
                                        
                                                #Actually updates the record
                                                v[indx] = specifyField

                                #Updates comparison record to be up-to-date
                                newRecord.update({i:v})

                                #Prints record after changes
                                print(f"New values: \n")
                                print(tbt.tabulate(list(newRecord.values())[1:],newRecord["column"],tablefmt="outline")) 

def columnUpdate(database):
        """
        Function that updates records that have the same values in a column

        Args:
            database (Dict): Database to be updated
        """        

        #Prepare list of all possible values to alter
        uniqueValueList = []
        #Adds 1 value to it for simpler indexing later
        uniqueValueList.append("nullvalue")

        #Makes sure user actually wants to update an entire column
        specifyColumn = pyi.inputYesNo(prompt="Are you sure you want to update multiple projects? (yes/no): ")

        #If they do...
        if specifyColumn == 'yes':

                #Iterate through copy of database
                for i, v in list(database.items()):
                        #Skip the header
                        if i == "column":
                                continue

                        #If the value is not already in the unique values list, add it
                        if v[1] not in uniqueValueList:
                                uniqueValueList.append(v[1])

                #Print all the unique values nicely
                for number, uniqueVal in enumerate(uniqueValueList):
                        if number > 0:
                                print(f"{number}. {uniqueVal}")

                #Adds a cancel option
                print(f"{len(uniqueValueList)}. Cancel")
                print("==========================================================")

                #User chooses which value to edit
                updateColumnSpecify = pyi.inputInt(prompt="Enter value to be edited (number): ",min=1,max=(len(uniqueValueList)))

                if updateColumnSpecify != (len(uniqueValueList)):

                        #Defines a variable by indexing from the value list
                        columnToBeUpdated = uniqueValueList[updateColumnSpecify]

                        #Use the variable for the dataval arg in FindAdvanced, to show the user all records with the value
                        FindAdvanced(database, columnToBeUpdated, id=1)

                        #Really make sure user wants to update them
                        updateColumnCheck = pyi.inputYesNo(prompt=f"Are you sure you want to edit all rows with the project {columnToBeUpdated}? (yes/no) ")
                        if updateColumnCheck == 'yes':

                                #Ask user for what they want the value to be, default is N/A if they leave it blank
                                resultColumnUpdate = pyi.inputStr(prompt=f"Enter new project for all records with the project {columnToBeUpdated}? (leave blank if none) ",
                                                                applyFunc= lambda x: x.title(),
                                                                default="N/A",
                                                                limit = 1
                                                                )
                                #Define the result table to be shown
                                resultTable = {}

                                #Iterate through database
                                for indx, val in list(database.items()):
                                        #Adds the header to the result table
                                        if indx == "column":
                                                resultTable.update({"column": val})
                                                continue

                                        #If the project name actually matches the user wants to update
                                        if val[1] == columnToBeUpdated:

                                                #Change it to new value
                                                val[1] = resultColumnUpdate

                                                #Add it to the result table
                                                resultTable.update({indx: val})

                                #Show the records that have been changed 
                                print(tbt.tabulate(list(resultTable.values())[1:],resultTable["column"],tablefmt="outline"))

def Update(database):
        """
        Function that asks user how much they want to update and chooses the sub function they want

        Args:
            database (Dict): Database to be updated
        """        

        #Show all of the database to the user
        Show_All(database)

        #Show user the options they have for editing the database
        print(updateMenuPrompt)

        #Ask the user which option they choose
        updateMenu = pyi.inputInt(prompt="How much do you want to update at once? ",min=1,max=4)

        #Run the specific function the user wants
        if updateMenu == 1:
                specificUpdate(database)

        if updateMenu == 2:
                rowUpdate(database)
                
        if updateMenu == 3:
                columnUpdate(database)
        

