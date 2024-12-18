import tkinter as tk
from tkinter import ttk, messagebox

# Conversion functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return fahrenheit_to_celsius(fahrenheit) + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))


def convert_temperature():
    try:
        
        temp_value = float(entry_temp.get())
        temp_unit = unit_var.get()

        
        if temp_unit == 'Celsius':
            fahrenheit = celsius_to_fahrenheit(temp_value)
            kelvin = celsius_to_kelvin(temp_value)
            result_label.config(text=f"{temp_value}°C is {fahrenheit:.2f}°F and {kelvin:.2f}K")

        elif temp_unit == 'Fahrenheit':
            celsius = fahrenheit_to_celsius(temp_value)
            kelvin = fahrenheit_to_kelvin(temp_value)
            result_label.config(text=f"{temp_value}°F is {celsius:.2f}°C and {kelvin:.2f}K")

        elif temp_unit == 'Kelvin':
            celsius = kelvin_to_celsius(temp_value)
            fahrenheit = kelvin_to_fahrenheit(temp_value)
            result_label.config(text=f"{temp_value}K is {celsius:.2f}°C and {fahrenheit:.2f}°F")
        
    except ValueError:
        
        messagebox.showerror("Invalid input", "Please enter a valid numerical temperature value.")


root = tk.Tk()
root.title("Temperature Converter")
root.geometry("600x400")


tk.Label(root, text="Enter Temperature:").pack(pady=8)
entry_temp = tk.Entry(root)
entry_temp.pack()


unit_var = tk.StringVar()
unit_var.set("Celsius")  # default value
units_menu = ttk.Combobox(root, textvariable=unit_var, values=["Celsius", "Fahrenheit", "Kelvin"])
units_menu.pack(pady=8)


convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack(pady=15)


result_label = tk.Label(root, text="Converted values will appear here")
result_label.pack(pady=15)


root.mainloop()
