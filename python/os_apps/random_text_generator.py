# random generátor hesel

import random
import string
import os
import time
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import colorchooser

# text gen

def generate_random_text(length):
    characters = string.ascii_letters + string.digits + string.punctuation + ' '
    return ''.join(random.choice(characters) for _ in range(length))
def save_text_to_file(text, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
def load_text_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()
# ui
class RandomTextGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password Generator")
        self.root.geometry("600x400")
        self.create_widgets()
    def create_widgets(self):
        # Style
        btn_bg = "#4CAF50"
        btn_fg = "#FFFFFF"
        btn_active_bg = "#45a049"
        btn_active_fg = "#FFFFFF"
        text_bg = "#f0f0f0"
        text_fg = "#000000"

        # text area
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=70, height=15,
                                                   bg=text_bg, fg=text_fg, font=("Arial", 12))
        self.text_area.pack(pady=10)

        # button frame
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=10)

        # gen
        self.generate_button = tk.Button(self.buttons_frame, text="Generate Random Text", bg=btn_bg, fg=btn_fg,
                                         activebackground=btn_active_bg, activeforeground=btn_active_fg,
                                         command=self.generate_text)
        self.generate_button.grid(row=0, column=0, padx=5)

        # save
        self.save_button = tk.Button(self.buttons_frame, text="Save to File", bg=btn_bg, fg=btn_fg,
                                     activebackground=btn_active_bg, activeforeground=btn_active_fg,
                                     command=self.save_to_file)
        self.save_button.grid(row=0, column=1, padx=5)

        # load
        self.load_button = tk.Button(self.buttons_frame, text="Load from File", bg=btn_bg, fg=btn_fg,
                                     activebackground=btn_active_bg, activeforeground=btn_active_fg,
                                     command=self.load_from_file)
        self.load_button.grid(row=0, column=2, padx=5)
    def generate_text(self):
        length = simpledialog.askinteger("Input", "Enter the length of the random text:", minvalue=1, maxvalue=10000)
        if length:
            random_text = generate_random_text(length)
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, random_text)
    def save_to_file(self):
        text = self.text_area.get(1.0, tk.END).strip()
        if text:
            filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                                    filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
            if filename:
                save_text_to_file(text, filename)
                messagebox.showinfo("Success", f"Text saved to {filename}")
        else:
            messagebox.showwarning("Warning", "Text area is empty!")
    def load_from_file(self):
        filename = filedialog.askopenfilename(defaultextension=".txt",
                                              filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if filename:
            try:
                text = load_text_from_file(filename)
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, text)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load file: {e}")
if __name__ == "__main__":
    root = tk.Tk()
    app = RandomTextGeneratorApp(root)
    root.mainloop()

    