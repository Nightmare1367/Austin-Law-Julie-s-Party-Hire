"""
Date Created: 10 / 06 / 2022 (10th June)
Written By: Austin Law
"""
from tkinter import *                       # Import the modules
from tkinter import ttk

def checking_validity():
    global party_listt, customer_entry, receipt_entry, item_entry, itemnum_entry, total_entries, valid_count
    valid_count = 0
    Label(main_window, text = "                      ").grid(column = 2, row =2, sticky = W+E)
    Label(main_window, text = "                      ").grid(column = 2, row =3, sticky = W+E)
    Label(main_window, text = "                      ").grid(column = 2, row =4, sticky = W+E)
    Label(main_window, text = "                      ").grid(column = 2, row =5, sticky = W+E)

    # Checks if the customer entry box is empty 
    if customer_entry.get().strip() == "":
        valid_count = 1
        Label(main_window, text = "Required", fg = "red").grid(column = 2, row = 2)

    # Checks if the receipt entry box is empty 
    if receipt_entry.get().strip() == "":
        valid_count = 1
        Label(main_window, text = "Required", fg = "red").grid(column = 2, row = 3)

    # Checks if the item hired entry box is empty 
    if item_entry.get().strip() == "":
        valid_count = 1
        Label(main_window, text = "Required", fg = "red").grid(column = 2, row = 4)

    # Checks if the customer entry box has numbers
    if customer_entry.get().isdigit():
        valid_count = 1
        Label(main_window, text = "Can't have number", fg = "red").grid(column = 2, row = 2)

    # Checks if the receipt entry has letters
    if receipt_entry.get().isalpha():
        valid_count = 1
        Label(main_window, text = "Can't have letters", fg = "red").grid(column = 2, row = 3)

    # This function is acts like an else function, if valid_count = 0 then the program will append their details
    if valid_count == 0:
        appending_details()
    
        
def delete_row():
    global party_list, row_entry, total_entries, details_count
    Button(main_window, text = "Delete Row", command = delete_row).grid(column = 2, row = 6, padx = 5, sticky = W)
    try:
        del party_list[int(row_entry.get())]
        total_entries = total_entries - 1
        row_entry.delete(0,"end")

        for widget in frame.winfo_children():
            widget.destroy()
        frame.pack_forget()
        printing_details()
    except:
        # Delete row button will turn red if there is no input or number is out of range
        Button(main_window, text = "Delete Row", command = delete_row, fg = "red").grid(column = 2, row = 6, padx = 5, sticky = W+E)

def appending_details():
    # Appends the users detail into the list created in the 'main' function
    global party_list, customer_entry, receipt_entry, item_entry, itemnum_entry, row_entry, total_entries, frame, main_window
    party_list.append([customer_entry.get(), receipt_entry.get(), item_entry.get(), itemnum_entry.get()])
    customer_entry.delete(0,"end")
    receipt_entry.delete(0,"end")
    item_entry.set("")
    itemnum_entry.set("1")
    total_entries += 1

def printing_details():
    # After the user appends their details, they will be able to print out their details.
    # The information will print under the section where setup_buttons is located in
    global party_list, details_count, total_entries, frame
    details_count = 0
    Label(frame, text = "Row").grid(column = 0, row = 9)
    Label(frame, text = "Customer Name").grid(column = 1, row = 9)
    Label(frame, text = "Receipt Number").grid(column = 2, row = 9)
    Label(frame, text = "Item Hired").grid(column = 3, row = 9)
    Label(frame, text = "Amount Hired").grid(column = 4, row = 9)
    frame.grid(column = 0, row = 9, columnspan = 5, rowspan = 10, sticky = N)
    while details_count < total_entries:
        Label(frame, text=(details_count)).grid(column=0, row=details_count + 10)
        Label(frame, text=(party_list[details_count][0])).grid(column=1, row=details_count + 10)
        Label(frame, text=(party_list[details_count][1])).grid(column=2, row=details_count + 10)
        Label(frame, text=(party_list[details_count][2])).grid(column=3, row=details_count + 10)
        Label(frame, text=(party_list[details_count][3])).grid(column=4, row=details_count + 10)
        details_count += 1

def quit_button():
    # Quits out of the window
    main_window.destroy()

def setup_buttons():
    global customer_entry, receipt_entry, item_entry, itemnum_entry, row_entry, main_window
    # Labels & Placement
    Label(main_window, text = "Julie's Party Hire", font = "Ariel 20").grid(column = 0, row = 0, columnspan = 2, pady = 5)
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
    item_entry = StringVar()
    ComboBox = ttk.Combobox(main_window, textvariable = item_entry, state = "readonly", value = ("Plates", "Chairs", "Foldable Tables", "Silverware", "Glassware", "Balloons", "Table Cloths")).grid(column = 1, row = 4, sticky = W+E)
    itemnum_entry = StringVar()
    spinbox = Spinbox(main_window, from_=1, to=500, textvariable=itemnum_entry, wrap=True, state="readonly").grid(column = 1, row = 5, sticky = W+E)
    
    row_entry = Entry(main_window)                              # Entry for the row number they want to remove
    row_entry.grid(column = 1, row = 6, sticky = W+E)

    # Buttons & Placement
    Button(main_window, text = "Quit", command = quit_button).grid(column = 2, row = 0, sticky = W, pady = 5)
    Button(main_window, text = "Append Details", command = checking_validity).grid(column = 0, row = 7, pady = 5)
    Button(main_window, text = "Print Details", command = printing_details).grid(column = 1, row = 7, pady = 5)
    Button(main_window, text = "Delete Row", command = delete_row).grid(column = 2, row = 6, padx = 5, sticky = W)

def main():
    # This function essentially sets up Tkinter, creates a new window and stores information in the list.
    global party_list, customer_entry, receipt_entry, item_entry, itemnum_entry, row_entry, total_entries, frame, main_window
    party_list = []
    total_entries = 0
    main_window = Tk()
    frame = Frame(main_window)
    setup_buttons()
    main_window.geometry("700x700")
    main_window.mainloop()

main()
