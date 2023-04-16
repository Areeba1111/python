from tkinter import *
import tkinter as tk
from tkinter import ttk
import requests

# Function to perform currency conversion
def conv():
    # API url to get latest exchange rates
    url = "https://openexchangerates.org/api/latest.json?app_id=7b8be725cb21402f8c1a6ce19b722424"
    # Send GET request to API and convert response to JSON format
    r = requests.get(url).json()
    # Perform currency conversion calculation based on selected currencies and amount
    ans = r["rates"][example2.get()] / r["rates"][example1.get()] * int(amt.get())
    # Display converted currency amount as a label on the GUI
    currency = Label(text=f"Currency: {ans}").grid(row=6, column=2)

# Function to reset GUI form
def rst():
    example1.delete(0, "end")
    example2.delete(0, "end")
    amt.delete(0, "end")

# Create the root window
root = Tk()
# Set the title of the GUI window
root.title=("currency converter")
# Set the padding for the GUI window
root.config(padx=20, pady=20)

# Create a label for the "Enter amount" field
amount_lbl = Label(root, text="Enter amount:  ", pady=20).grid(row=1, column=1)
# Create an entry field for the amount to be converted
amt = tk.Entry()
amt.grid(row=1, column=2)

# Create a label for the "Select currency" field
comb1 = Label(text="Select currency: ").grid(row=2, column=1)
# Create a drop-down menu for selecting the currency to convert from
example1 = ttk.Combobox(root,
      values=[
        "USD",
        "EUR",
        "JPY",
        "GBP",
        "CHF",
        "CAD",
        "AUD",
        "NZD",
        "CNY",
        "HKD",
        "SGD",
        "KRW",
        "SEK",
        "NOK",
        "DKK",
        "TRY",
        "RUB",
        "BRL",
        "ZAR",
        "SAR",
        "AED",
        "MXN",
        "ILS",
        "EGP",
        "THB",
        "MYR",
        "PHP",
        "PKR",
        "BDT",
        "IDR",
        "INR",
        "KES",
        "EGP",
        "TRY",
        "RUB",
        "UAH",
        "PLN",
        "HUF",
        "CZK",
        "RON",
        "BGN",
        "HRK",
        "DKK",
        "NOK",
        "SEK",
        "CHF",
        "RSD",
        "MKD",
        "BAM",
        "EUR",
    ])
example1.grid(column=2, row=2)

# create label for currency to convert to and place it in the grid
comb2 = Label(text="Currency to convert to: ", pady=20).grid(row=3, column=1)

# create a combobox widget for the currency options and place it in the grid
example2 = ttk.Combobox(root,
                        values=[
                            "USD",
                            "EUR",
                            "JPY",
                            "GBP",
                            "CHF",
                            "CAD",
                            "AUD",
                            "NZD",
                            "CNY",
                            "HKD",
                            "SGD",
                            "KRW",
                            "SEK",
                            "NOK",
                            "DKK",
                            "TRY",
                            "RUB",
                            "BRL",
                            "ZAR",
                            "SAR",
                            "AED",
                            "MXN",
                            "ILS",
                            "EGP",
                            "THB",
                            "MYR",
                            "PHP",
                            "PKR",
                            "BDT",
                            "IDR",
                            "INR",
                            "KES",
                            "EGP",
                            "TRY",
                            "RUB",
                            "UAH",
                            "PLN",
                            "HUF",
                            "CZK",
                            "RON",
                            "BGN",
                            "HRK",
                            "DKK",
                            "NOK",
                            "SEK",
                            "CHF",
                            "RSD",
                            "MKD",
                            "BAM",
                            "EUR",
                        ])
example2.grid(column=2, row=3)

# create a button for converting the amount and place it in the grid
convert = Button(text="Convert", command=conv).grid(row=4, column=2)

# create a button for resetting the input and output fields and place it in the grid
reset = Button(text="Reset", command=rst).grid(row=5, column=2)
root.mainloop()