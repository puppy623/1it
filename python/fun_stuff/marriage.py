import tkinter as tk
from tkinter import messagebox

def persistent_alert():
    root = tk.Tk()
    root.withdraw() 

    while True:
        response = messagebox.askyesno("For Sandie <3", "Will you marry me?")
        
        if response: 
            messagebox.showinfo("For Sandie <3", "Yayyy! I love you so muchh!! <3")
            break
        else:
            messagebox.showinfo("For Sandie <3", "HEY! I told you not to say no!\n\n One more chance...")
            continue
    root.destroy() 

if __name__ == "__main__":
    persistent_alert()