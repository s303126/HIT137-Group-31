#import 'os' which is a Python module that provides functions for interacting with the native Operating System (OS).
import os
#import 'csv' which is a Python module that provides functions for reading and displaying data in '.csv' file format.
import csv

#define global variables.
total_winter_temp, count_winter = 0, 0
total_spring_temp, count_spring = 0, 0
total_summer_temp, count_summer = 0, 0
total_fall_temp, count_fall = 0, 0

"""This function called 'get_season' has a 'month' index (integer) as parameters and checks if the provided 'month' is one of the values in the list's.
The 'in' keyword is used to check if an entry exists in a collection (list). If no entry is found, the function will return 0."""
def get_season(month):
    if month in [1, 2, 12]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Fall"
    
#'scandir()' is a function provided by the 'os' module that scans the provided directory path and returns an Iterator object.
csv_files = os.scandir("temperature_data")

#loop through all entries inside the scanned directory (stored as 'csv_files' variable)
for file in csv_files:
    
    #'isfile()' is a function provided by the 'os' module that checks if the entry is a file or not.
    if file.is_file():
        
        #Try/Except block where 'try' keyword allows for testing a block of code for errors and 'except' handles the error.
        try:
           
            """'open()' is a function that returns a file object which can used to read, write and modify a file
            (in this case, every file listed in the 'temperature_data' directory). Providing the file path and supported encoding as arguments.""" 
            f = open(file=file.path, encoding='utf-8')
         
            """'reader()' is a function provided by the 'csv' module that reads the given file object 
            provided as arguments and returns an Iterator object."""
            stream = csv.reader(f)

            """To avoid reading in the header that contains the data structure of the file, we use the 'next()' function that 
            returns the next item in the Iterator object (stream)."""
            header = next(stream)

            """'reader()' function above states that 'Each iteration returns a row of the CSV file (which can span multiple input lines)'. So,
            we must iterate each row of the CSV file to get all of the contents."""
            for row in stream:
               
                station_name = row[0]
                station_id = row[1]
                station_months = row[4:15+1]
                month_names = header[4:15+1]

                #station months length = 12
                for i in range(len(station_months)):
                    
                    try:
                        temp = float(station_months[i])
                        month = i + 1

                        season = get_season(month)

                        if season == "Winter":
                            total_winter_temp += temp
                            count_winter += 1
                        elif season == "Spring":
                            total_spring_temp += temp
                            count_spring += 1
                        elif season == "Summer":
                            total_summer_temp += temp
                            count_summer += 1
                        elif season == "Fall":
                            total_fall_temp += temp
                            count_fall += 1
            
                    except ValueError:
                        continue

            f.close()
            
        #handle the Try/Except error with the 'except' keyword, printing the error as 'e'.
        except Exception as e:
            print("could not read file: ", e)


average_winter_temp = total_winter_temp / count_winter
average_spring_temp = total_spring_temp / count_spring
average_summer_temp = total_summer_temp / count_summer
average_fall_temp = total_fall_temp / count_fall

f = open("average_temp.txt", "w")

f.write("Season, Average Temperatures\n")
f.write("Winter: " + str(average_winter_temp) + "\n")
f.write("Spring: " + str(average_spring_temp) + "\n")
f.write("Summer: " + str(average_summer_temp) + "\n")
f.write("Fall: " + str(average_fall_temp) + "\n")

f.close()
