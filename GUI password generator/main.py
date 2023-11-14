import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    #pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data =  json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email:{email}\n Password:{password}")
        else:
            messagebox.showinfo(title="No results", message=f"Sorry, there is no {website} in the database")



def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password,
        }
    }
    if len(website) ==0 or len(password) == 0:
        messagebox.showinfo(title="Opps", message="Please make sure you haven't left any fields empty")
    else:
        try:
            with open ("data.json", mode="r") as data_file:
            # Reading old data
                data = json.load(data_file)
            #updating old data with new data

        except:
            with open("data.json", "w") as data_file:
            #Saving updated data
                json.dump(new_data,data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
            #Saving updated data
                json.dump(data,data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="#F0F0F0")  # Set background color to a light gray

# Logo
canvas = Canvas(height=200, width=200, bg="#F0F0F0")  # Match canvas background with window background
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, pady=20)  # Add some padding

# Labels
labels_font = ("Courier", 12, "bold")
website_label = Label(text="Website:", font=labels_font, bg="#F0F0F0")  # Adjust font and background color
website_label.grid(row=1, column=0, pady=5)  # Add some padding
email_label = Label(text="Email/Username:", font=labels_font, bg="#F0F0F0")
email_label.grid(row=2, column=0, pady=5)
password_label = Label(text="Password:", font=labels_font, bg="#F0F0F0")
password_label.grid(row=3, column=0, pady=5)

# Entries
entries_font = ("Courier", 12)
website_entry = Entry(width=21, font=entries_font)  # Adjust font
website_entry.grid(row=1, column=1, pady=5)
website_entry.focus()
email_entry = Entry(width=36, font=entries_font)  # Adjust font and width
email_entry.grid(column=1,row=2, columnspan=2)
email_entry.insert(0, "eltaiuly1205@gmail.com")
password_entry = Entry(width=21, font=entries_font)  # Adjust font
password_entry.grid(row=3, column=1, pady=5)

# Buttons
buttons_font = ("Courier", 10, "bold")
generate_password_button = Button(text="Generate Password",width=18, command=generate_password, font=buttons_font, bg="#4CAF50", fg="white")  # Adjust font, background, and text color
generate_password_button.grid(row=3, column=2, pady=5)
add_button = Button(text="Add", width=35, command=save, font=buttons_font, bg="#1E90FF", fg="white")
add_button.grid(row=4, column=1, columnspan=2, pady=5)
search_button = Button(text="Search", width=18, command=find_password, font=buttons_font, bg="#FFD700", fg="black")
search_button.grid(row=1, column=2, pady=5)

window.mainloop()
