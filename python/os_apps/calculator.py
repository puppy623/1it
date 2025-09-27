# funkce

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y
def power(x, y):
    return x ** y
def modulus(x, y):
    return x % y
def floor_divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x // y
def square_root(x):
    if x < 0:
        return "Error! Cannot compute square root of a negative number."
    return x ** 0.5
def percentage(x, y):
    return (x / 100) * y
def factorial(x):
    if x < 0:
        return "Error! Factorial of a negative number doesn't exist."
    if x == 0 or x == 1:
        return 1
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result
def logarithm(x, base=10):
    import math
    if x <= 0:
        return "Error! Logarithm of non-positive numbers is undefined."
    return math.log(x, base)
def sine(x):
    import math
    return math.sin(math.radians(x))
def cosine(x):
    import math
    return math.cos(math.radians(x))
def tangent(x):
    import math
    return math.tan(math.radians(x))
def cotangent(x):
    import math
    if x % 180 == 0:
        return "Error! Cotangent is undefined for this angle."
    return 1 / math.tan(math.radians(x))
def secant(x):
    import math
    if x % 180 == 90:
        return "Error! Secant is undefined for this angle."
    return 1 / math.cos(math.radians(x))
def cosecant(x):
    import math
    if x % 180 == 0:
        return "Error! Cosecant is undefined for this angle."
    return 1 / math.sin(math.radians(x))
def absolute(x):
    return abs(x)
def round_number(x):
    return round(x)
def negate(x):
    return -x
def reciprocal(x):
    if x == 0:
        return "Error! Division by zero."
    return 1 / x
def to_binary(x):
    return bin(x).replace("0b", "")
def to_octal(x):
    return oct(x).replace("0o", "")
def to_hexadecimal(x):
    return hex(x).replace("0x", "").upper()
def from_binary(x):
    return int(x, 2)
def from_octal(x):
    return int(x, 8)
def from_hexadecimal(x):
    return int(x, 16)
def gcd(x, y):
    import math
    return math.gcd(x, y)
def lcm(x, y):
    import math
    return abs(x * y) // math.gcd(x, y)
def mean(numbers):
    return sum(numbers) / len(numbers) if numbers else 0
def median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n == 0:
        return 0
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]
def mode(numbers):
    from collections import Counter
    if not numbers:
        return None
    count = Counter(numbers)
    max_count = max(count.values())
    modes = [k for k, v in count.items() if v == max_count]
    return modes if len(modes) > 1 else modes[0]
def variance(numbers):
    if len(numbers) == 0:
        return 0
    mean_value = mean(numbers)
    return sum((x - mean_value) ** 2 for x in numbers) / len(numbers)
def standard_deviation(numbers):
    import math
    return math.sqrt(variance(numbers))
def permutation(n, r):
    import math
    if r > n or n < 0 or r < 0:
        return "Error! Invalid values for permutation."
    return math.factorial(n) // math.factorial(n - r)
def combination(n, r):
    import math
    if r > n or n < 0 or r < 0:
        return "Error! Invalid values for combination."
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
def fahrenheit_to_celsius(f):
    return (f - 32) * 5.0/9.0
def celsius_to_fahrenheit(c):
    return (c * 9.0/5.0) + 32
def kilometers_to_miles(km):
    return km * 0.621371
def miles_to_kilometers(miles):
    return miles / 0.621371

# ui

import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
import math
import sys
import os
import json
import re
import ast
import random
import time
import threading
import datetime
import platform
import subprocess

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Negr Kalkulačka")
        self.root.configure(bg="#232946")
        self.history = []
        self.create_widgets()

    def create_widgets(self):
        # barvy
        entry_bg = "#803943"
        entry_fg = "#232946"
        btn_bg = "#393e46"
        btn_fg = "#803943"
        btn_active_bg = "#803943"
        btn_active_fg = "#232946"
        hist_bg = "#121629"
        hist_fg = "#803943"

        # entry
        self.entry = tk.Entry(self.root, width=28, borderwidth=3, font=("Segoe UI", 18),
                              bg=entry_bg, fg=entry_fg, relief=tk.FLAT, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=(20, 5), pady=20, sticky="ew")

        # historie
        self.history_box = tk.Listbox(self.root, width=22, height=10, font=("Segoe UI", 12),
                                      bg=hist_bg, fg=hist_fg, borderwidth=0, highlightthickness=0)
        self.history_box.grid(row=0, column=4, rowspan=6, padx=(5, 20), pady=20, sticky="ns")
        self.history_box.insert(tk.END, "Historie:")

        # layout tlačítek (2D grid)
        buttons = [
            ["7", "8", "9", "/", "sqrt"],
            ["4", "5", "6", "*", "^"],
            ["1", "2", "3", "-", "%"],
            ["0", ".", "=", "+", "C"],
            ["sin", "cos", "tan", "log", "!"]
        ]

        for r, row in enumerate(buttons, 1):
            for c, text in enumerate(row):
                button = tk.Button(
                    self.root, text=text, font=("Segoe UI", 14, "bold"), width=5, height=2,
                    bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg, activeforeground=btn_active_fg,
                    relief=tk.RAISED, bd=0, highlightthickness=0,
                    command=lambda t=text: self.on_button_click(t)
                )
                button.grid(row=r, column=c, padx=3, pady=3, sticky="nsew")

        # Make grid cells expand
        for i in range(5):
            self.root.grid_columnconfigure(i, weight=1)
        for i in range(1, 6):
            self.root.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.entry.delete(0, tk.END)
        elif char == '=':
            try:
                expression = self.entry.get()
                result = self.evaluate_expression(expression)
                self.add_to_history(expression, result)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif char == 'sqrt':
            try:
                value = float(self.entry.get())
                result = square_root(value)
                self.add_to_history(f"sqrt({value})", result)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif char == 'sin':
            try:
                value = float(self.entry.get())
                result = sine(value)
                self.add_to_history(f"sin({value})", result)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif char == 'cos':
            try:
                value = float(self.entry.get())
                result = cosine(value)
                self.add_to_history(f"cos({value})", result)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif char == 'tan':
            try:
                value = float(self.entry.get())
                result = tangent(value)
                self.add_to_history(f"tan({value})", result)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif char == 'log':
            try:
                value = float(self.entry.get())
                result = logarithm(value)
                self.add_to_history(f"log({value})", result)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif char == '!':
            try:
                value = int(self.entry.get())
                result = factorial(value)
                self.add_to_history(f"{value}!", result)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            self.entry.insert(tk.END, char)

    def add_to_history(self, expr, result):
        entry = f"{expr} = {result}"
        self.history.append(entry)
        if len(self.history) > 20:
            self.history = self.history[-20:]
        self.history_box.delete(1, tk.END)
        for item in self.history:
            self.history_box.insert(tk.END, item)
    def evaluate_expression(self, expression):
        # Replace '^' with '**' for power operation
        expression = expression.replace('^', '**')
        # Evaluate the expression safely
        allowed_names = {
            'add': add, 'subtract': subtract, 'multiply': multiply,
            'divide': divide, 'power': power, 'modulus': modulus,
            'floor_divide': floor_divide, 'square_root': square_root,
            'percentage': percentage, 'factorial': factorial,
            'logarithm': logarithm, 'sine': sine, 'cosine': cosine,
            'tangent': tangent, 'cotangent': cotangent, 'secant': secant,
            'cosecant': cosecant, 'absolute': absolute, 'round_number': round_number,
            'negate': negate, 'reciprocal': reciprocal, 'to_binary': to_binary,
            'to_octal': to_octal, 'to_hexadecimal': to_hexadecimal,
            'from_binary': from_binary, 'from_octal': from_octal,
            'from_hexadecimal': from_hexadecimal, 'gcd': gcd, 'lcm': lcm,
            'mean': mean, 'median': median, 'mode': mode,
            'variance': variance, 'standard_deviation': standard_deviation,
            'permutation': permutation, 'combination': combination,
            'fahrenheit_to_celsius': fahrenheit_to_celsius,
            'celsius_to_fahrenheit': celsius_to_fahrenheit,
            'kilometers_to_miles': kilometers_to_miles,
            'miles_to_kilometers': miles_to_kilometers,
            '__builtins__': {}
        }
        code = compile(expression, "<string>", "eval")
        for name in code.co_names:
            if name not in allowed_names:
                raise NameError(f"The use of '{name}' is not allowed")
        return eval(code, {"__builtins__": {}}, allowed_names)
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
text = "Ahoj"
i = 0
for letter in text:
    print(letter, end= "-" if i < len(text) - 1 else "")
    i += 1
print()
