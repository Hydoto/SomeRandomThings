import calendar,time

class time_control:
    
    timer = time.time()
    current_year = time.localtime(timer).tm_year
    # Easy
    def giveMeCalendar(year:int):
        return calendar.calendar(year)
    # Just a gest
    def giveMeCalendarZero():
        return calendar.calendar(0)
    # Getting there
    def giveMeCalendarFuture():
        future_year = time_control.current_year + 1
        return calendar.calendar(future_year)


if __name__ == "__main__":
    lm = time_control
    l = lm.giveMeCalendarFuture()
    print(l)
