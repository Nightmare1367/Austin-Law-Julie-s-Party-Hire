"""
Date Created: 07 / 06 / 2022 (7th June)
Written By: Austin Law
"""
from tkinter import *                       # Import the modules

def setup_buttons():
    # Labels & Placement
    Label(main_window, text = "Julie's Party Hire", font = "Ariel 20").grid(column = 0, row = 0, column_span = 3, pady = 5)
    Label(main_window, text = "Customer Name:").grid(column = 0, row = 2, sticky = W+E)
    Label(main_window, text = "Receipt Number:").grid(column = 0, row = 3, sticky = W+E)
    Label(main_window, text = "Item Hired:").grid(column = 0, row = 4, sticky = W+E)
    Label(main_window, text = "Amount Hired:").grid(column = 0, row = 5, sticky = W+E)
    Label(main_window, text = "Row Number:").grid(column = 0, row = 6, sticky = W+E)

    # Entry Boxes & Placement
    customer_entry = Entry(main_window)                         # Entry for the customers name
    customer_entry.grid(column = 1, row = 2, sticky = W+E)
    receipt_entry = Entry(main_window)                          # Entry for their receipt number
    receipt_entry.grid(column = 1, row = 3, sticky = W+E)
    item_entry = Entry(main_window)                             # Entry for the item they hired
    item_entry.grid(column = 1, row = 4, sticky = W+E)
    itemnum_entry = Entry(main_window)                          # Entry for the amount of that item they hired
    itemnum_entry.grid(column = 1, row = 5, sticky = W+E)
    row_entry = Entry(main_window)                              # Entry for the row number they want to remove
    row_entry.grid(column = 1, row = 6, sticky = W+E)

    # Buttons & Placement
    Button(main_window, text = "Quit").grid(column = 5, row = 0, sticky = W+E, pady = 5)
    Button(main_window, text = "Append Details").grid(column = 0, row = 7, pady = 5, sticky = W+E)
    Button(main_windoe, text = "Print Details").grid(column = 1, row = 7, pady = 5, sticky = W+E)
    Button(main_window, text = "Delete Row").grid(column = 2, row = 6, padx = 5, sticky = W+E)