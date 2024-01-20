"""
Create algorithms and use to solve
https://central.jointheleague.org/levels/Level0/Recipes/ForLoopGauntlet.html
"""


if __name__ == '__main__':
    pass

    #1
    for i in range(0,101):
        print(i)

    #2
    for i in range(100,-1,-1):
        print(i)

    #3
    for i in range (2,101,2):
        print(i)

    #4
    for i in range (1,100,2):
        print(i)

    #5 fix this
    for i in range (1,501):
        if i % 2==0:
            print (i)
        else:
            print
