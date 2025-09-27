import tkinter as tk
from tkinter import messagebox

def persistent_alert():
    root = tk.Tk()
    root.withdraw() 
    
    while True:
        response = messagebox.askyesno("For Ita :>","You have received a sweet, sweet kiss!\nDo you accept?\n\n(If you say no, I will stab you.)")
        
        if response:  # if ita love me
            messagebox.showinfo("For Ita :>","Yayyy! I love you so muchh!! <3")
            break
        else:  # if ita dum dum
            messagebox.showinfo("For Ita :>","HEY! I told you not to say no!\n\n One more chance...")
            continue

if __name__ == "__main__":
    persistent_alert()