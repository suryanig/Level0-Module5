"""
Write an algorithm to change a string into a "goofy" version.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    # TODO)
    #  1. Ask the user to enter their name.
    window = Tk()
    window.withdraw()
    name = simpledialog.askstring(None, prompt = "What is your name?")
    #  2. Use a loop to alternately modify each character of the name into
    #     uppercase and lowercase letters until a new "goofy" representation
    #     of their name has been constructed.
    wacky = ""
    for i in range(len(name)):
        if i % 2 == 0:
            wacky += name[i].upper()
        else:
            wacky += name[i].lower()
    #     For example, if they enter their name as Alexander Hamilton
    #     their goofy name will be AlExAnDeR HaMiLtOn
    #  3. Show the user the goofy version of their name in a pop-up.
    messagebox.showinfo(message=wacky)
    pass
