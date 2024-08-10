import tkinter as tk
from tkinter import ttk

class ContactManagerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Contact Manager")

        # Create a frame for the contact list
        self.contact_list_frame = tk.Frame(master)
        self.contact_list_frame.pack()

        # Create a label for the contact list
        self.contact_list_label = tk.Label(self.contact_list_frame, text="Contacts:")
        self.contact_list_label.pack()

        # Create a listbox to display contact nicknames
        self.contact_listbox = tk.Listbox(self.contact_list_frame)
        self.contact_listbox.pack()

        # Example contact data (replace with your actual contacts)
        self.contacts = [
            {"nickname": "alice", "first_name": "Alice", "last_name": "Smith", "phone": "123-456-7890", "email": "asmith@gmail.com"},
            {"nickname": "Bobby", "first_name": "Bob", "last_name": "Johnson", "phone": "987-654-3210", "email": "bobj12345@outlook.com"}
        ]

        # Populate the listbox with nicknames
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, contact["nickname"])

        # Create a frame for the contact details
        self.contact_details_frame = tk.Frame(master)
        self.contact_details_frame.pack()

        # Create labels for contact details
        self.nickname_label = tk.Label(self.contact_details_frame, text="Nickname:")
        self.nickname_label.grid(row=0, column=0)
        self.first_name_label = tk.Label(self.contact_details_frame, text="First Name:")
        self.first_name_label.grid(row=1, column=0)
        self.last_name_label = tk.Label(self.contact_details_frame, text="Last Name:")
        self.last_name_label.grid(row=2, column=0)
        self.phone_label = tk.Label(self.contact_details_frame, text="Phone:")
        self.phone_label.grid(row=3, column=0)
        self.email_label = tk.Label(self.contact_details_frame, text="Email:")
        self.email_label.grid(row=4, column=0)

        # Create labels to display contact details
        self.nickname_value_label = tk.Label(self.contact_details_frame, text="")
        self.nickname_value_label.grid(row=0, column=1)
        self.first_name_value_label = tk.Label(self.contact_details_frame, text="")
        self.first_name_value_label.grid(row=1, column=1)
        self.last_name_value_label = tk.Label(self.contact_details_frame, text="")
        self.last_name_value_label.grid(row=2, column=1)
        self.phone_value_label = tk.Label(self.contact_details_frame, text="")
        self.phone_value_label.grid(row=3, column=1)
        self.email_value_label = tk.Label(self.contact_details_frame, text="")
        self.email_value_label.grid(row=4, column=1)

        # Bind the listbox selection to display contact details
        self.contact_listbox.bind("<<ListboxSelect>>", self.display_contact_details)

    def display_contact_details(self, event):
        selection = self.contact_listbox.curselection()
        if selection:
            index = selection[0]
            contact = self.contacts[index]
            self.nickname_value_label.config(text=contact["nickname"])
            self.first_name_value_label.config(text=contact["first_name"])
            self.last_name_value_label.config(text=contact["last_name"])
            self.phone_value_label.config(text=contact["phone"])
            self.email_value_label.config(text=contact["email"])

# Create the main window
root = tk.Tk()
app = ContactManagerGUI(root)
root.mainloop()