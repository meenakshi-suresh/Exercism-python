def leap_year(year):
    """Function to check if a given year is leap year or not"""
    if year % 4 ==0 and year % 100 != 0:
        return True
    if year % 400 == 0 and year % 100 == 0:
        return True
    return False