""" 
This Python script provides reusable functions for creating
a series of project folders using looping techniques, 
conditional branching and list comprehension methods.
"""

#IMPORT REQUIRED LIBRARIES 
import math
import statistics
import pathlib
import time
import JayaTries_utils

#Function 1
def create_folders_for_range(start_year, end_year):
    """This function creates folders from a given range"""
    for year in range(start_year, end_year + 1):
        year = str(year)
        pathlib.Path(year).mkdir(exist_ok=True)

#Function 2
def create_folders_from_list(folder_list, to_lowercase=False, remove_spaces=False):
    """This function creates folders from a list of names"""
    for folder_name in folder_list:
        if to_lowercase:
            folder_name = folder_name.lower() # Convert foldername to lowercase
        if remove_spaces:
            folder_name = folder_name.replace(' ', '') #Strip spaces from folder name
        path = pathlib.Path(folder_name)
        path.mkdir(parents=True, exist_ok=True)

#Function 3
def create_prefixed_folders(folder_list, prefix):
    """This function creates prefixed folders by transforming a list of names and combining each with a prefix"""
    for folder_name in folder_list:
        folder = pathlib.Path(prefix + folder_name) #Concat prefix & folder name
        folder.mkdir(parents=True, exist_ok=True)

#Function 4
def create_folders_periodically(duration):
    """This function creates 5 folders periodically based on the duration provided by user"""
    num_folders = 5 
    folder_count = 1

    while folder_count <= num_folders:
        pathlib.Path("folder-" + str(folder_count)).mkdir(exist_ok=True)
        folder_count += 1
        time.sleep(duration)

def main():
    ''' Main function to demonstrate module capabilities. '''

    # Print byline from imported module
    print(f"Byline: {JayaTries_utils.byline}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['old', 'current', 'new']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    # Add options e.g., to force lowercase and remove spaces 
    # to one or more of your functions (e.g. function 2) 
    # Call your function and test these options
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

# Conditional Script Execution
if __name__ == '__main__':
    main()