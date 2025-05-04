import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("For Sandie <3", "Will you marry me?")

def persistent_alert():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    while True:
        response = messagebox.askyesno("For Sandie <3", "Will you marry me?")
        
        if response:  # if she says yes
            messagebox.showinfo("For Sandie <3", "Yayyy! I love you so muchh!! <3")
            break
        else:  # if she says no
            messagebox.showinfo("For Sandie <3", "HEY! I told you not to say no!\n\n One more chance...")
            continue
    root.destroy()  # Close the root window after the loop

if __name__ == "__main__":
    persistent_alert()