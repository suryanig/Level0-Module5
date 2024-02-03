"""
Create algorithms and use to solve
https://central.jointheleague.org/levels/Level0/Recipes/ForLoopGauntlet.html
"""


if __name__ == '__main__':
    pass

    #1 yes
    for i in range(0,101):
        print(i)

    #2 yes
    for i in range(100,-1,-1):
        print(i)

    #3 yes
    for i in range (2,101,2):
        print(i)

    #4 yes
    for i in range (1,100,2):
        print(i)

    #5 yes
    for i in range (1,501):
        if i % 2==0:
            print (i)
            print ("is even")
        else:
            print (i)
            print ("is odd")

    #6 yes
    for i in range (0,778,7):
        print(i)

    #7 yes
    for i in range (2010, 2025, 1):
        print ("In "+ str(i) + " I was " + str(i - 2010) + " years old.")


    #1 yes
    for i in range (0, 3, 1):
        for s in range (0, 3, 1):
            print (str(i) + " " +str(s))

    #2 yes
    for i in range (0,3,1):
        for s in range (1,4,1):
            print (i*3 + s, end = "  ")
        print (" ")

    #3 still working on


    # end = ""

