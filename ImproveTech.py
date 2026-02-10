from random import randint
import os
import time
import webbrowser

NOTE = "TRY to think of a better name than Testing"


class testing:
    one = 1
    two = 2

    def OpenBrowser(Url):
        webbrowser.open(Url)

    def tryit():
        return randint(0,testing.two)


    def whatdo():
        # so what am i going to do
        return 0
    
    def Something(NotRaining):
        if NotRaining == 1:
            return "Its not raining"
        else:
            return "Its Raining"



    def clearscreen():
        os.system('cls||clear') 
    
    def waitsec(floatNum):
        time.sleep(floatNum)


    def pausetheCMD():
            os.system("pause")
