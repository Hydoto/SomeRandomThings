from random import randint

# big list of value
level:list = []
levelmax:int = 100

# For loop of why not
def seed_levels(levelmax):
    for i in range(levelmax):
        level.append(i)
        i =-1

# creating an array of stuff for no reason 
# can't put those on top since it will chaos
seed_levels(levelmax)
levelman:int = randint(0,levelmax)
leveled:int = randint(0,level.__len__() -1)

# adding combat because i could
def combat(levelman):
    if levelman >= leveled:
        print("We lost",levelman)
    else:
        print("We won",levelman)

# a few getters
def level_get():
    return level.__len__()
def leveled_get():
    return leveled

# Sure...
if __name__ == "__main__":
    combat(levelman)
    print("Total levels:",level_get(),"\n"+"Your level:",leveled_get())
