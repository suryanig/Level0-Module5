"""
Write code that can tell if a number is prime.
A prime number is a number that is only divisible by 1 and itself.
"""
from tkinter import messagebox, simpledialog, Tk



    #  2. Use a for loop, if statement, and modulo to find if the number
    #     is prime.
def prime_or_not(number):
    if number == 1:
        return True
    elif number == 2:
        return True
    else:
        for i in range (2, number):
            if number % i == 0:
                return False
        return True
if __name__ == '__main__':
    # TODO)
    #  1. Ask the user for a number
    window = Tk()
    window.withdraw()
    number = simpledialog.askinteger(title='Number', prompt="What number do you want me to use to check if it is prime or not.")
    if prime_or_not(number) == True:
        messagebox.showinfo (None, message = str(number) + " is prime.")
    else:
        messagebox.showinfo(None, message= str(number) + " is not prime.")


    #  3. If the number is divisible by any number other than 1 or itself,
    #     the number is not prime.
    pass
