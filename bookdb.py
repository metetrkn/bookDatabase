from tkinter import Tk, Button, Label, Scrollbar, Listbox, StringVar, Entry, W, E, N, S, END
from tkinter import ttk
from tkinter import messagebox
from mysqlserver_config_orig import dbConfig
import pymysql

# create connection
con = pymysql.Connect(**dbConfig)
print(con)

# creating cursor object to execute sql commands in db session
cursor = con.cursor()
class Bookdb:
    def __init__(self):
        self.con = pymysql.connect(**dbConfig)
        self.cursor = con.cursor()
        print('You have connected to database')
        print(con)
 

root = Tk()
root.title("My Books Database Application")
root.configure(background="light green")
root.geometry("990x500")
root.resizable(width=False, height=False)

# title widget
title_label = ttk.Label(root, text="Title", background="light green", font=("TkDefaultFont", 16))
title_label.grid(row=0, column=0, sticky=W)
title_text = StringVar()
title_entry = ttk.Entry(root, width=24, textvariable=title_text)
title_entry.grid(row=0, column=1, sticky=W)

# author widget
author_label = ttk.Label(root, text="Author", background="light green", font=("TkDefaultFont", 16))
author_label.grid(row=0, column=2, sticky=W)
author_text = StringVar()
author_entry = ttk.Entry(root, width=24, textvariable=author_text)
author_entry.grid(row=0, column=3, sticky=W)

# ISBN widget
isbn_label = ttk.Label(root, text="ISBN", background="light green", font=("TkDefaultFont", 14))
isbn_label.grid(row=0, column=4, sticky=W)
isbn_text = StringVar()
isbn_entry = ttk.Entry(root, width=24, textvariable=isbn_text)
isbn_entry.grid(row=0, column=5, sticky=W)

# adding "Add Book" Button
add_btn = Button(root, text="Add Book", bg="blue", fg="white", font="helvetica 10 bold", command="")
add_btn.grid(row=0, column=6, sticky=W)

# adding listbox to display items
list_bx = Listbox(root, height=16, width=40, font="helvetica 13", bg="light blue")
list_bx.grid(row=3, column=1, columnspan=6, sticky=W+E, pady=40, padx=15)

# adding scrollbar
scroll_bar = Scrollbar(root)
scroll_bar.grid(row=3, column=7, rowspan=1, sticky=N+S+W)

# attaching scrollbar to listbox
list_bx.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list_bx.yview)

# adding view button
view_btn = Button(root, text="View all records", bg="black", fg="white",
                  font="helvetica 10 bold", command="")
view_btn.grid(row=4, column=1)

# adding modify button
modify_btn = Button(root, text="Modify Record", bg="purple", fg="white", font="helvetica 10 bold", command="")
modify_btn.grid(row=4, column=2)

# adding clear button
clear_btn = Button(root, text="Clear Screen", bg="maroon", fg="white",
                   font="helvetica 10 bold", command="")
clear_btn.grid(row=4, column=3)

# adding exit button
exit_btn = Button(root, text="Exit Application", bg="blue", fg="white",
                  font="helvetica 10 bold", command="")
exit_btn.grid(row=4, column=4)

# adding delete button
delete_btn = Button(root, text="Delete Record", bg="red", fg="white", 
                    font="helvetica 10 bold", command="")
delete_btn.grid(row=4, column=5)

# making windows
root.mainloop()
