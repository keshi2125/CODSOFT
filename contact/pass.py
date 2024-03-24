import tkinter as tk
from tkinter import messagebox

class ContactBookGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        
        # Set background color to blue
        self.root.configure(bg='pink')

        self.contacts = {}

        self.create_widgets()

    def create_widgets(self):
        self.name_label = tk.Label(self.root, text="Name:", bg='lightblue', fg='black')
        self.name_label.grid(row=0, column=0, padx=5, pady=5)

        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.phone_label = tk.Label(self.root, text="Phone Number:", bg='lightblue', fg='black')
        self.phone_label.grid(row=1, column=0, padx=5, pady=5)

        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        self.email_label = tk.Label(self.root, text="Email:", bg='lightblue', fg='black')
        self.email_label.grid(row=2, column=0, padx=5, pady=5)

        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact, bg='yellow', fg='black')
        self.add_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact, bg='grey', fg='white')
        self.delete_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        self.display_button = tk.Button(self.root, text="Display Contacts", command=self.display_contacts, bg='lightgreen', fg='black')
        self.display_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    def add_contact(self):
        name = self.name_entry.get()
        phone_number = self.phone_entry.get()
        email = self.email_entry.get()

        if name.strip() == '' or phone_number.strip() == '' or email.strip() == '':
            messagebox.showerror("Error", "Please enter all fields.")
        elif name in self.contacts:
            messagebox.showerror("Error", f"Contact '{name}' already exists.")
        else:
            self.contacts[name] = {'phone_number': phone_number, 'email': email}
            messagebox.showinfo("Success", f"Contact '{name}' added successfully.")
            self.clear_entries()

    def delete_contact(self):
        name = self.name_entry.get()

        if name.strip() == '':
            messagebox.showerror("Error", "Please enter a name.")
        elif name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", f"Contact '{name}' deleted successfully.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", f"Contact '{name}' not found in the contact book.")

    def display_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts found.")
        else:
            contacts_info = "Contacts in the Contact Book:\n\n"
            for name, info in self.contacts.items():
                contacts_info += f"Name: {name}\n"
                contacts_info += f"Phone Number: {info['phone_number']}\n"
                contacts_info += f"Email: {info['email']}\n\n"

            messagebox.showinfo("Contacts", contacts_info)

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
app = ContactBookGUI(root)
root.mainloop()
