import calendar,sys,time
################################################
# Use: python giveacalender.py year
#
# if no year is given just takes current year
################################################
if __name__ == "__main__":
    try:
        argone = sys.argv[1] 
    except:
        argone = time.localtime().tm_year
    result = calendar.calendar(int(argone))
    print(result)
