import tabulate as tbt
import pyinputplus as pyi


#Prompts for functions
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
1. Index
2. Project_Name
3. Job_Title
4. First Name
5. Last Name
6. Sex
7. Age
8. Cancel
==========================================================
'''
def Show(database, title='\nList of Employees\n'):
        """

        Args:
            database (Dict): Database to be shown
        
        Returns:
            Returns a printed table of the database using tabulate module

            
        """

        #Shows title of table
        print(title)

        #Defines header and data of table
        data = list(database.values())[1:]
        header = database['column']

        #Actually prints the table
        print(tbt.tabulate(data,header, tablefmt='outline'))
        print('\n')

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

                #Process if data inputted is a string
                if type(dataval) != int:
                        for i, v in list(database.items()):

                                #Adds header
                                if i == "column":
                                        resultList.update({"column": v})
                                        continue

                                #Adds data matching user input
                                if v[id] == (f"{dataval}"):
                                        resultList.update({i : v})
                                        resultHeader = resultList["column"]
                                        resultData = list(resultList.values())[1:]

                #Process if data inputted is NOT a string
                else:
                        for i, v in list(database.items()):

                                #Adds header
                                if i == "column":
                                        resultList.update({"column": v})
                                        continue

                                #Adds data matching user input (but without making it a string)
                                if v[id] == dataval:
                                        resultList.update({i : v})
                                        resultHeader = resultList["column"]
                                        resultData = list(resultList.values())[1:]

                #Prints the table of records matching the user input
                print(tbt.tabulate(resultData,resultHeader,tablefmt="outline"))

        #Returns user with data that isnt found in the database
        else:
                print(f"\n{dataval} not found in database.")
        



def Find(database):
        print(findPrompt)
        findAsk = pyi.inputInt(prompt="Enter what filter you want to use: \n",
                               min = 1,
                               max = 8
                                )

        if findAsk == 1:
                FindAdvanced(database, dataval =pyi.inputInt(
                        prompt="Enter the index number of the employee record you want to find: "
                ),id = 0)

        if findAsk == 2:
                FindAdvanced(database, dataval =pyi.inputStr(
                        prompt="Enter the name of the project you want to find (with spaces, leave blank if none): ",
                        applyFunc = lambda x: x.title(),
                        default = "N/A",
                        limit = 1
                ),id = 1)

        if findAsk == 3:
                headerFind, dataFind = FindAdvanced(database, dataval =pyi.inputStr(
                        prompt="Enter the name of the job title you want to find (with spaces): ",
                        applyFunc = lambda x: x.title(),
                ),id = 2)

        if findAsk == 4:
                FindAdvanced(database, dataval =pyi.inputStr(
                        prompt="Enter the first name you want to find: ",
                        applyFunc = lambda x: x.title(),
                ),id = 3)
        
        if findAsk == 5:
                FindAdvanced(database, dataval =pyi.inputStr(
                        prompt="Enter the last name you want to find: ",
                        applyFunc = lambda x: x.title(),
                ),id = 4)

        if findAsk == 6:
                FindAdvanced(database, dataval =pyi.inputChoice(
                        prompt="Enter the gender you want to find (m/f): ",
                        applyFunc = lambda x: x.title(),
                        choices=["M","F"]
                ),id = 5)

        if findAsk == 7:
                FindAdvanced(database, dataval =pyi.inputInt(
                        prompt="Enter the age of the employees you want to find: "
                ),id = 6)

        


def Add(database):
        """

        Args:
            database (Dict): Database to be appended to

        Adds new row to the end of the database with values

        """        

        #Automatically determines index
        Index = len(database)-1

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

        #Adds the data to the dictionary
        database.update(
                {Index: [Index, Project_Name, Job_Title, FirstName, LastName, Sex, Age]}
        )

        #Shows the database
        Show(database)

        #Back to menu
        return database

def Delete(database):
        Show(database)
        targetIndex = pyi.inputInt(prompt="Enter the index of the record you want to remove: ",max=(len(database)-2))
        if targetIndex in database:
                print(database[targetIndex])
                removeCheck = pyi.inputYesNo(prompt="Are you sure you want to remove this record? (yes/no): ")
                if removeCheck == 'yes':
                        for idx, val in list(database.items()):
                                if idx == "column":
                                        continue
                                if targetIndex in val:
                                        del database[idx]
                                elif targetIndex < val[0]:
                                        val[0] = idx-1
                                        print(idx,val)
                                        database.update({f"{idx}": val})
                                        del database[idx]
                        Show(database)
        else:
                print(f"Record with index of {targetIndex} wasn't found.")

def specificUpdate(database):
        print(specificUpdatePrompt)

        specifyUpdate = pyi.inputInt(prompt="Which field do you want to change (number)? ",min=1,max=7)

        if specifyUpdate != 7:
                specifyIndex = pyi.inputInt(prompt="Index of record to be updated: ")
                oldRecord = {}
                newRecord = {}
                for i, v in list(database.items()):
                        if i == 'column':
                                oldRecord.update({"column":v})
                                newRecord.update({"column":v})
                                continue
                        if i == specifyIndex:
                                oldRecord.update({i:v})
                                print(f"Current value: \n")
                                print(tbt.tabulate(list(oldRecord.values())[1:],oldRecord["column"],tablefmt="outline"))
                                specifyField = pyi.inputStr(prompt="Enter new field value: ",
                                                        applyFunc = lambda x: x.title(),
                                                        default = "N/A",
                                                        limit = 1
                                                        )
                                v[specifyUpdate] = specifyField
                                newRecord.update({i:v})
                                print(f"New value: \n")
                                print(tbt.tabulate(list(newRecord.values())[1:],newRecord["column"],tablefmt="outline"))                       

def rowUpdate(database):
        rowUpdateCheck = pyi.inputYesNo(prompt="Are you sure you want to update an entire row? (yes/no) ")
        if rowUpdateCheck == 'yes':
                specifyIndex = pyi.inputInt(prompt="Index of record to be updated: ",max=(len(database)-2))
                oldRecord = {}
                newRecord = {}
                for i, v in list(database.items()):
                        if i == 'column':

                                #Adds headers to records for comparison
                                oldRecord.update({"column":v})
                                newRecord.update({"column":v})

                                #Continues loop
                                continue

                        if i == specifyIndex:

                                #Creates a copy and shows current record before any changes
                                oldRecord.update({i:v})
                                print(f"Current values: \n")
                                print(tbt.tabulate(list(oldRecord.values())[1:],oldRecord["column"],tablefmt="outline"))

                                #Iterates through row
                                for indx, field in enumerate(v):

                                        #Skips index of record
                                        if indx == 0:
                                                continue
                                        else:
                                                specifyField = pyi.inputStr(prompt=f"Enter new field value (currently {field}, leave blank if unchanged): ",
                                                                applyFunc = lambda x: x.title(),
                                                                default = field,
                                                                limit = 1
                                                                        )
                                        
                                                #Actually updates the record
                                                v[indx] = specifyField

                                #Updates comparison record to be up-to-date
                                newRecord.update({i:v})

                                #Prints record after changes
                                print(f"New values: \n")
                                print(tbt.tabulate(list(newRecord.values())[1:],newRecord["column"],tablefmt="outline")) 

def columnUpdate(database):

        uniqueValueList = []
        uniqueValueList.append("nullvalue")

        specifyColumn = pyi.inputYesNo(prompt="Are you sure you want to update multiple projects? (yes/no): ")

        if specifyColumn == 'yes':
                for i, v in list(database.items()):
                        if i == "column":
                                continue
                        if v[1] not in uniqueValueList:
                                uniqueValueList.append(v[1])
                for number, uniqueVal in enumerate(uniqueValueList):
                        if number > 0:
                                print(f"{number}. {uniqueVal}")

                print(f"{len(uniqueValueList)}. Cancel")
                print("==========================================================")

                updateColumnSpecify = pyi.inputInt(prompt="Enter value to be edited (number): ",min=1,max=(len(uniqueValueList)))

                if updateColumnSpecify != (len(uniqueValueList)):
                        columnToBeUpdated = uniqueValueList[updateColumnSpecify]
                        FindAdvanced(database, columnToBeUpdated, id=1)
                        updateColumnCheck = pyi.inputYesNo(prompt=f"Are you sure you want to edit all rows with the project {columnToBeUpdated}? (yes/no) ")
                        if updateColumnCheck == 'yes':
                                resultColumnUpdate = pyi.inputStr(prompt=f"Enter new project for all records with the project {columnToBeUpdated}? (leave blank if none) ",
                                                                applyFunc= lambda x: x.title(),
                                                                default="N/A",
                                                                limit = 1
                                                                )
                                resultTable = {}
                                for indx, val in list(database.items()):
                                        if indx == "column":
                                                resultTable.update({"column": val})
                                                continue
                                        if val[1] == columnToBeUpdated:
                                                val[1] = resultColumnUpdate
                                                resultTable.update({indx: val})
                                print(tbt.tabulate(list(resultTable.values())[1:],resultTable["column"],tablefmt="outline"))

def Update(database):
        Show(database)

        print(updateMenuPrompt)

        updateMenu = pyi.inputInt(prompt="How much do you want to update at once? ",min=1,max=4)
        if updateMenu == 1:
                specificUpdate(database)
        if updateMenu == 2:
                rowUpdate(database)
        if updateMenu == 3:
                columnUpdate(database)
        

