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
file_name_pickle_str = "EventsbyDate.dat" #binary file of data
file_obj_pickle = None #object to represent binary file
table_lst = {} #table of dictionary rows
month_str = "" #month integer for lookup
day_str = "" #day integer for lookup
hist_event_str = "" #event to display
choice = "" #menu choice


# Processing  --------------------------------------------------------------- #
class Processor:
    """ Performs processing tasks"""

    @staticmethod
    def save_data_to_file(file_name, list_of_rows):
        """Writes the data from list_of_rows into a binary file
        :param file_name- the file being written to
        :param list_of_rows- the data table being written to the file
        """

        file_obj_pickle = open(file_name, "wb")
        pickle.dump(list_of_rows, file_obj_pickle)
        file_obj_pickle.close()

    @staticmethod
    def read_data_from_binary_file(file_name):
        """Reads data from file_name - a binary file- and writes it to a table
        :param file name- the file being read
        :return table of data unpickled"""
        try:
            file = open(file_name, "rb")
            table = pickle.load(file)
            file.close()
        except (FileNotFoundError):
            print("File issue, did you save your pickle file in the same location as the code?")
        return table

    @staticmethod
    def event_by_date(month, day, list_of_rows):
        """Takes user input for month and day to return the event
        :param month- the month of the event based on user input
        :param day- the day of the event based on user input
        :param list_of_rows- the table of dictionary rows that has the date and event data
        :return event """
        try:
            for row in list_of_rows:
                if row["Month"] == month.strip() and row["Day"] == day.strip():
                    return row["Event"]
        except KeyError as e:
            print(e, e.__doc__, type(e), sep='\n')
        except LookupError as e:
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print(e, e.__doc__, type(e), sep='\n')

    @staticmethod
    def add_event_to_date(month, day, new_event, list_of_rows):
        """Writes new event for a month and day based on user input
        :param month- month of event based on user input
        :param day- the day of the event based on user input
        :param new_event string holding new event
        :param list_of_rows table to write the new line to
        :return list_of_rows with updated event"""
        found = False
        for row in list(list_of_rows): #casting- iterating over same size list but removing from original
            if row["Month"] == month.strip() and row["Day"] == day.strip():
                list_of_rows.remove(row)
                found = True
        if not found:
            print("Date not found")
        #print(month,type(month))
        #print(day,type(day))
        #print(new_event,type(event))
        day_dict = {"Month": month, "Day": day.strip(), "Event": new_event} #create new line
        list_of_rows.append(day_dict) #append new line (learn to order)

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
        4) Save your data
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice_int = 0
        while (choice_int<1) or (choice_int>5):
            try:
                choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
                choice_int = int(choice)
            except ValueError:
                print("Please only enter 1-5")
        return choice

    @staticmethod
    def input_month():
        """function to capture month from user and ensure it is in the right format
        :return: month_str"""
        month_int = 0
        while not 1<=month_int<=12: #(month_int<1) or (month_int>12):
            try:
                month_input_str = input("Please input the numeric month number of the date: ")
                month_int = int(month_input_str)
                month_str = str(month_int) #get rid of leading 0s
                if(1<=month_int<=12):
                    print("Got it! Great month.")
                else:
                    print("Are you sure that's a month number? 1-12 please!")
            except ValueError:
                print("Please type a number between 1 and 12, no leading 0s!")
        return month_str

    def input_day():
        """function to capture day number from user and ensure it is in the right format
        :return:day_str"""
        day_int = 0
        while (day_int<1) or (day_int>31):
            try:
                day_input_str = input("Please input the numeric day of the month: ")
                day_int = int(day_input_str)
                day_str = str(day_int) #ensure no leading 0s
                if(1<=day_int<=31):
                    print("Got it! Let's see if that date exists..."
                          "You will be routed to the menu if you're close but no cigar")
                else:
                    print("Is this a real day? Please only enter a valid day date,"
                          "and remember the rhyme:"
                          "'Thirty days has September, April, June, and November. "
                          "All the rest have 31'...except Feb. You're on your own.)")
            except ValueError:
                print("Is this a real day? Please only enter a valid day date for your selected month.")
        return day_str

    @staticmethod
    def print_the_year(list_of_rows):
        """ Shows the entire list of dates and events

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The Events so Far: *******")
        print("Month/Day- Event")
        for row in list_of_rows:
            print(row["Month"] + "/" + row["Day"] + " - " + row["Event"])
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def new_event_request():
        new_event_response = ""
        try:
            while (new_event_response == ""):
                new_event_response = input("Would you like to input or replace the event of the day? y/n ").strip().lower()
        except ValueError:
            print("Please type only y or n")
        return new_event_response

    @staticmethod
    def input_new_event(month,day,list_of_rows, new_event_response):
        """ Input a new event into a month/date line
        :param month- the month of the event
        :param day- the day of the event
        :return: list_of_rows table updated with month/day/event
        """
        if new_event_response == 'y':
            try:
                new_event_entry = input("Enter the event information: ").strip()
            except ValueError:
                print("Please type a quick message")
                return new_event_entry
        else:
            print("Back to main menu!")


# Main  --------------------------------------------------------------- #

table_lst = Processor.read_data_from_binary_file(file_name_pickle_str) #unpickles data to table_lst

while(True):
    IO.output_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    if choice_str.strip() == '1':#prints the table of data
        IO.print_the_year(table_lst)
        continue  # to show the menu

    elif choice_str == '2': #input day and get some info, option to add data if none exists
        month_str = IO.input_month()
        day_str = IO.input_day()
        hist_event_str = str(Processor.event_by_date(month=month_str, day=day_str, list_of_rows=table_lst))

        if len(hist_event_str)<3:
            print("No event input for this day.")
            response_event_req = IO.new_event_request()
            event = IO.input_new_event(month=month_str, day=day_str,list_of_rows=table_lst,new_event_response=response_event_req)
            Processor.add_event_to_date(month=month_str, day=day_str,new_event=event, list_of_rows=table_lst)
        else:
            print(hist_event_str)
        continue  # to show the menu

    elif choice_str == '3':  # Input new event to table
        month_str = IO.input_month()
        day_str = IO.input_day()
        print("Current entry:")
        hist_event_str = Processor.event_by_date(month=month_str, day=day_str, list_of_rows=table_lst)
        print(hist_event_str)
        response_event_req = IO.new_event_request()
        event = IO.input_new_event(month=month_str, day=day_str, list_of_rows=table_lst,new_event_response=response_event_req)
        Processor.add_event_to_date(month=month_str, day=day_str, new_event=event, list_of_rows=table_lst)
        print("Ok!")
        continue  # to show the menu

    elif choice_str == '4':  # Exit Program
        Processor.save_data_to_file(file_name=file_name_pickle_str, list_of_rows=table_lst)
        print("Data saved!")
        continue  # to show the menu

    elif choice_str == '5':  # Exit Program
        print("Goodbye!")
        break  # by exiting loop

