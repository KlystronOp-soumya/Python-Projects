# Program to test a date pattern : dd/mm/yyyy is valid or not
import re

def isValidDateWithRegex(date:str) -> bool:
    datePattern = r"^(?:(?:3[01]|[12][0-9]|0?[1-9]))\\(?!0{2})(?:(?:[0][1-9]|[1][0-2]))\\(?:\d{4})$"
    cPattern = re.compile(pattern= datePattern)
    if(re.search( cPattern , date) is None ) :
        return False
    else:
        return True


def isValidDate(date: str) -> bool:
    
    def isLeapYear(year: int) -> int :
        return year % 4
    
    if (len(date) < 10) :
        return False
    #split the fields
    fields = date.split("\\")
    dd = fields[0]
    dayInt = int(dd)
    mm = fields[1]
    monthInt = int(mm)
    yy = fields[2]
    yearInt = int(yy)
    print(fields)
    #check each fields
    if (len(dd) < 2 or dayInt < 0 or ( dayInt > 31) ) :
        return False
    
    #check for the month
    if( len(mm) < 2 or ( not 1 <=  monthInt <= 12 ) or (dayInt > 28 and  isLeapYear(yearInt) != 0 and monthInt == 2) or ( dayInt > 29 and  isLeapYear(yearInt) == 0 and monthInt == 2) ) :
        return False
    
    #check for the year :
    if(len(yy) < 4 or len(yy) > 4):
        return False
        

    return True

if __name__ == "__main__" :
    inputDate = input("Please enter a date: ")
    print("Checking the date validity without using regex pattern")
    print("Date {} valid :  {} ".format(inputDate , isValidDate(inputDate)))
    print("Checking the date validity  using regex pattern")
    print("Date {} valid :  {} ".format(inputDate , isValidDateWithRegex(inputDate)))
