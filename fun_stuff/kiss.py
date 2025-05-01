import tkinter as tk
from tkinter import messagebox

def persistent_alert():
    root = tk.Tk()
    root.withdraw() 
    
    while True:
        response = messagebox.askyesno("For Sandie :3","You have received a sweet, sweet kiss!\nDo you accept?\n\n(If you say no, I will stab you.)")
        
        if response:  # if sandie love me
            messagebox.showinfo("For Sandie :3","Yayyy! I love you so muchh!! <3")
            break
        else:  # if sandie dum dum
            messagebox.showinfo("For Sandie :3","HEY! I told you not to say no!\n\n One more chance...")
            continue

if __name__ == "__main__":
    persistent_alert()