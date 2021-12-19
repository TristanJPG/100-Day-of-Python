from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    passwordLetters = [choice(letters) for _ in range(randint(8, 10))]
    passwordNumbers = [choice(numbers) for _ in range(randint(2, 4))]
    passwordSymbol = [choice(symbols) for _ in range (randint(2, 4))]

    passwordList = passwordLetters + passwordNumbers + passwordSymbol
    shuffle(passwordList)

    password = "".join(passwordList)
    passwordEntry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = websiteEntry.get()
    email = usernameEntry.get()
    password = passwordEntry.get()

    if len(website) == 0 or len(password) == 0 or len(email) ==0:
        messagebox.showwarning(title="Oops?", message="Please do not leave any field empty!")
    else:
        askok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \n "
                                                          f"Password: {password} \n is this ok to save? ")
        if askok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email} | {password}\n")
                websiteEntry.delete(0, END)
                passwordEntry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, )
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(column=1, row=0)
# Labels
websiteText = Label(text="Website:")
websiteText.grid(column=0, row=1)

usernameText = Label(text="Username/Email:")
usernameText.grid(column=0, row=2)

passwordText = Label(text="Password:")
passwordText.grid(column=0, row=3)
# Entries
websiteEntry = Entry(width=35)
websiteEntry.grid(column=1, row=1, columnspan=2)
websiteEntry.focus()

usernameEntry = Entry(width=35)
usernameEntry.grid(column=1, row=2, columnspan=2)
usernameEntry.insert(0, "Tristanscholar05@gmail.com")

passwordEntry = Entry(width=22)
passwordEntry.grid(column=1, row=3)
# Buttons
generatePass = Button(text="Generate Button!", command=gen_pass)
generatePass.grid(column=2, row=3)

add = Button(text="Add!", width=36, command=save)
add.grid(column=1, row=4, columnspan=2)
window.mainloop()
