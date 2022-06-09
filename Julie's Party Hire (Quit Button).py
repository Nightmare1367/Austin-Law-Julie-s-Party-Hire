"""
Date Created: 09 / 06 / 2022 (9th June)
Written By: Austin Law
"""
from tkinter import *                       # Import the modules

def quit_button():
    # Quits out of the window
    main_window.destroy()

def setup_buttons():
    global customer_entry, receipt_entry, item_entry, itemnum_entry, row_entry, main_window
    # Labels & Placement
    Label(main_window, text = "Julie's Party Hire", font = "Ariel 20").grid(column = 0, row = 0, columnspan = 3, pady = 5)
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
    Button(main_window, text = "Quit", command = quit_button).grid(column = 5, row = 0, sticky = W+E, pady = 5)
    Button(main_window, text = "Append Details").grid(column = 0, row = 7, pady = 5, sticky = W+E)
    Button(main_window, text = "Print Details").grid(column = 1, row = 7, pady = 5, sticky = W+E)
    Button(main_window, text = "Delete Row").grid(column = 2, row = 6, padx = 5, sticky = W+E)

def main():
    # This function essentially sets up Tkinter, creates a new window and stores information in the list.
    global party_list, customer_entry, receipt_entry, item_entry, itemnum_entry, row_entry, total_entries, frame, main_window
    party_list = []
    total_entries = 0
    main_window = Tk()
    frame = Frame(main_window)
    setup_buttons()
    main_window.geometry("500x700")
    main_window.mainloop()

main()
