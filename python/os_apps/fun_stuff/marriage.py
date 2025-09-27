import tkinter as tk
from tkinter import messagebox

def persistent_alert():
    root = tk.Tk()
    root.withdraw() 

    while True:
        response = messagebox.askyesno("For Ita <3", "Will you marry me? (dont say no pls)")
        
        if response: 
            messagebox.showinfo("For Ita <3", "Yayyy! I love you so muchh!! <3")
            break
        else:
            messagebox.showinfo("For Ita <3", "HEY! I told you not to say no!\n\n One more chance...")
            continue
    root.destroy() 

if __name__ == "__main__":
    persistent_alert()

