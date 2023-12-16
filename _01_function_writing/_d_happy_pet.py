"""
Write methods to represent the activities that will make the user's pet happy.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO)
    #   1. Ask the user to enter the type of pet they want (give them a few
    #      choices).

    pet = simpledialog.askstring(title="Pet", prompt="Do you want a dog, cat, fish, or bunny?")
    print(pet)
    #   2. Use a loop (maybe a while loop?) to keep offering interactions with
    #      their pet until the desired pet happiness level has been reached.
    #      Examples of activities are: Feed, Walk, Play
    happiness = 0


    #   3. Write a method for each of the pet activities offered.
    #      Each activity should increase (or decrease) the pet's happiness
    #      level by a different amount, depending on the kind of pet they
    #      have. For example, a fish might not enjoy a walk!
    def feed():
        global happiness
        if pet == "dog":
            happiness = happiness+2
        if pet == "cat":
            happiness = happiness+2
        if pet == "fish":
            happiness = happiness+2
        if pet == "bunny":
            happiness = happiness+2

    def walk():
        global happiness
        if pet == "dog":
            happiness = happiness+1
        if pet == "cat":
            happiness = happiness+0
        if pet == "fish":
            happiness = happiness-1
        if pet == "bunny":
            happiness = happiness+1

    def bathe():
        global happiness
        if pet == "dog":
            happiness = happiness+1
        if pet == "cat":
            happiness = happiness+0
        if pet == "fish":
            happiness = happiness+0
        if pet == "bunny":
            happiness = happiness+0

    def play():
        global happiness
        if pet == "dog":
            happiness = happiness+2
        if pet == "cat":
            happiness = happiness+1
        if pet == "fish":
            happiness = happiness+0
        if pet == "bunny":
            happiness = happiness+2

    while happiness < 8:
        activity = simpledialog.askstring(title="Activity", prompt="Do you want to feed, walk, bathe, or play with your pet?")
        print(activity)

        if activity == "feed":
            feed()
        elif activity == "walk":
            walk()
        elif activity == "bathe":
            bathe()
        elif activity == "play":
            play()
        else:
            messagebox.showinfo(None, message="Sorry, I don't know how to "+activity+" your "+pet)




