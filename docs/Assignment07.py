# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Use Pickle to convert data to binary and store in file
#              Use error handling for data validation/troubleshooting
#              Display event based on date for user
# ChangeLog (Who,When,What):
# LShmait,08.20.2022,Started script
# ---------------------------------------------------------------------------- #


import pickle

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
file_name_original_str = "EventsTable.txt" #an initial input of data
file_name_pickle_str = "EventsbyDate.dat" #binary file of data
file_obj = None #object to represent file
file_obj_pickle = None #object to represent binary file
day_dict = {} #dictionary row of data
table_lst = [] #table of data
month_str = "" #month integer for lookup
day_str = "" #day integer for lookup
hist_event_str = "" #event to display
choice = "" #menu choice

file_obj = open("EventsTable.txt", "a")
file_obj.close()


# Processing  --------------------------------------------------------------- #
class Processor:
    """ Performs processing tasks"""

    @staticmethod
    def save_data_to_file(file_name, list_of_rows):
        """Writes the data from list_of_rows into a binary file
        :param file_name- the file being written to
        :param list_of_rows- the data table being written to the file
        """

        file = open(file_name, "ab")
        pickle.dump(list_of_rows, file)
        file.close()

    @staticmethod
    def read_data_from_binary_file(file_name):
        """Reads data from file_name - a binary file- and writes it to a table
        :param file name- the file being read
        :return table of data unpickled"""
        file = open(file_name, "rb")
        table = pickle.load(file)
        file.close()
        return table

    @staticmethod
    def display_event_by_date(month, day, list_of_rows):
        """Takes user input for month and day to return the event
        :param month- the month of the event based on user input
        :param day- the day of the event based on user input
        :param list_of_rows- the table of dictionary rows that has the date and event data
        :return event """
        for row in list_of_rows:
            if row["Month"] == month.strip() and row["Day"] == day.strip():
                return row["Event"]

    @staticmethod
    def add_event_to_date(month, day, new_event, list_of_rows):
        """Writes new event for a month and day based on user input
        :param month- month of event based on user input
        :param day- the day of the event based on user input
        :param new_event string holding new event
        :param list_of_rows table to write the new line to
        :return list_of_rows with updated event"""
        for row in list_of_rows:
            if row["Month"] == month.strip() and row["Day"] == day.strip():
                list_of_rows.remove(row)  #Remove old line
                day_dict = {"Month": month, "Day": day.strip(), "Event": new_event} #create new line
                list_of_rows.append(day_dict) #append new line
            else:
                print("Did not work") #just for testing
                continue



# Input/Output  --------------------------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        This program shares a historical tidbit by day, sourced primarily from "A Leap Year of Great Stories, 
        366 from History for Every Day of the Year" by WB Marsh & Bruce Carrick, as well as some general classics!
        
        Menu of Options
    
        1) View all the Data
        2) Input your month and day to get a fact!
        3) Input and save your own fact of the day!       
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def input_month():
        """function to capture month from user and ensure it is in the right format
        :return: month_str"""
        month_str = input("Please input the numeric month number of the date: ")
        if month_str.isalpha():
            print("Please enter only the number of the month, no need to spell it out!")
        elif int(month_str) < 1 or int(month_str) > 12:
            print("Please input the numeric month of year, 1-12- no leading 0s!")
        else:
            print("I'm not sure what you've entered, but please input a month number 1-12!")
        return month_str

    def input_day():
        """function to capture day number from user and ensure it is in the right format
        :return:day_str"""
        day_str = input("Please input the numeric day of the month: ")
        if day_str.isalpha():
            print("Please enter only the number of the day, no need to spell it out!")
        elif int(day_str) < 1 or int(day_str) >31:
            print("Is this a real day? Please only enter a valid day date,"
                  "and remember the rhyme:"
                  "'Thirty days has September, April, June, and November. "
                   "All the rest have 31'...except Feb. You're on your own.)")
        else:
            print("I'm not sure what you've entered, but please input an existing day number of the month.")
        return day_str

    @staticmethod
    def print_the_year(list_of_rows):
        """ Shows the entire list of dates adn events

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The Events so Far: *******")
        print(["Month"], ["Day"], ["Event"])
        file = open()
        print("*******************************************")
        print()  # Add an extra line for looks

    # @staticmethod
    # def input_new_event(month,day,list_of_rows):
    #     """ Input a new event into a month/date line
    #     :param month- the month of the event
    #     :param day- the day of the event
    #     :return: list_of_rows table updated with month/day/event
    #     """
    #     try:
    #         hist_event_str = input("Enter the event information: ").strip()
    #         day_dict = {"Month": month, "Day": day, "Event": hist_event_str}
    #         list_of_rows.append(day_dict)
    #         if len(hist_event_str)>150:
    #             raise Exception("Please be brief, we didn't sign up for a novel")
    #         elif len(hist_event_str)<25:
    #             raise Exception("A bit more verbose please!")

# Main  --------------------------------------------------------------- #

table_lst = Processor.read_data_from_binary_file(file_name_pickle_str)

while(True):
    IO.output_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option
    if choice_str.strip() == '1':  #TODO
        IO.print_the_year(table_lst)
        continue  # to show the menu

    elif choice_str == '2':
        month_str = IO.input_month()
        day_str = IO.input_day()
        Processor.display_event_by_date(month=month_str, day=day_str, list_of_rows=table_lst)
        continue  # to show the menu

    elif choice_str == '3':  # Save Data to File
        Processor.save_data_to_file(file_name=file_name_pickle_str, list_of_rows=table_lst)
        print("Data Saved!")
        continue  # to show the menu

    elif choice_str == '4':  # Exit Program
        print("Goodbye!")
        break  # by exiting loop

