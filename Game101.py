import ImproveTech
import sys



class stuff: 
    commands = ["hey","openit","cls","clear", "help"]

    def Hello():
        f = input("Type stuff:")
        print("oh you just typed:",f,"\n")
        ImproveTech.testing.waitsec(2)
        stuff.FrontDesk(f)


    def FrontDesk(getf):
        print("Front Desk")
        
        if  getf == stuff.commands[0]:
            print("Well hey to you too")

        if getf == stuff.commands[1]:
            # for fixing invalid escape sequence '\B' use /
            ImproveTech.testing.OpenBrowser("Img/Bug Fixing.gif")
            print("Opening Something")   
        if getf == stuff.commands[2] or stuff.commands[3]:
            ImproveTech.testing.clearscreen()
        
        if getf == stuff.commands[4]:
            print("List of functions:")
            for x in stuff.commands:
                print(x)
                ImproveTech.testing.waitsec(1)
            print("----------------------")
            ImproveTech.testing.pausetheCMD()
        
        #Ending
        else:
            print("Game Over")


def ProgStart():
    # argv works only if it has this safety line else index error
    first = sys.argv[1] if len(sys.argv) > 1 else '.'

    if first == "world":
        print("Well Hello")
    else:
        ImproveTech.testing.clearscreen()
        print("Game of Hey")
        stuff.Hello()
    
    print("--Program ending--")
ProgStart()
