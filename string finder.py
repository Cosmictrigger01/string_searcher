import os

def find_files_and_folders():
    
    #Get the files and folders in choosen directory
    tree = os.walk(start_directory)
    
    for roots, folders, files in tree:
        
        #Adds together the full filepath (folderpath + filename)
        for file in files:
            file_path = os.path.join(roots, file)

            #Opens file and reads its data, then searches for specified string index
            try:
                with open(file_path, 'r') as data:
                    opened_file = (data.read())
                    index = (opened_file.find(search_string))

                    #If the string was found (-1 means not found) print out the index of the string and the path
                    #Then print out the search_string at index position and however much "length" after it
                    while index != -1:
                        print("Found at index: " + str(index) + " | At path: " + file_path + " | String: " + opened_file[index:index + len(search_string) + length])
                        index = opened_file.find(search_string, index + 1)
            
            #If a file cannot be opend it puts out an error message
            except Exception as error:
                print("Error when opening file: " + file_path + " :" + error)


#Input
start_directory = input("Please input your start directory: ")
search_string = input("Please input the string you want to search: ")
length = int(input("Please choose how many characters to print after the string: "))

#Function call
find_files_and_folders()