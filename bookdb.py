from tkinter import Tk, Button, Label, Scrollbar, Listbox, StringVar, Entry, W, E, N, S, END
from tkinter import ttk
from tkinter import messagebox
from mysqlserver_config_git import dbConfig
import pymysql

# create connection
con = pymysql.Connect(**dbConfig)

# creating cursor object to execute sql commands in db session
cursor = con.cursor()

# creating/connecting database object
class Bookdb:
    def __init__(self, dbConfig):
        self.con = None
        self.cursor = None

        # connecting database
        try:
            self.con = pymysql.connect(**dbConfig)
            self.cursor = self.con.cursor()
            print('You have connected to database')
            print(self.con)
        
        # if a problem occour while connecting database
        except Exception as e:
            print('A problem has occurred while connecting to the database:', e)

    # losing connection with database
    def deleter(self):
        if self.con:
            self.con.close()
            print('Database connection closed')
            del self.cursor
        else:
            print('No active connection to close')

    # viewing function, fetches all records from db and returns them as rows
    def view(self):
        self.cursor.execute('SELECT * FROM books')
        rows = self.cursor.fetchall()
        return rows
    
    # inserting records function
    def insert(self, title, author, isbn):
        ins_sql = "INSERT INTO books (Title, Author, ISBN) VALUES (%s, %s, %s)"
        values = (title, author, isbn)
        self.cursor.execute(ins_sql, values)
        self.con.commit()




    # updating records function
    def update(self, id, title, author, isbn):
        upd_sql = 'UPDATE books SET title=%s, author=%s, isbn=%s WHERE ID=%s'
        self.cursor.execute(upd_sql, (title, author, isbn, id))
        self.con.commit()
        messagebox.showinfo(title="Book Database", message="Book Updated")


    def delete(self, id):
        delquerry = 'DELETE FROM books WHERE ID=%s'
        self.cursor.execute(delquerry, (id,))
        self.con.commit()
        messagebox.showinfo(title='Book Database', message='Book Deleted')



# instance of Bookdb class
book_db = Bookdb(dbConfig)

# function to select books from listbox
def get_selected_row(event):
    global selected_tuple
    if list_bx.curselection():  # Check if the selection is not empty
        index = list_bx.curselection()[0]
        selected_tuple = list_bx.get(index)

        # when a book click from listbox, anything on entry will be deleted
        title_entry.delete(0, 'end')
        # selected books title shown on entry
        title_entry.insert('end', selected_tuple[1])

        author_entry.delete(0, 'end')
        author_entry.insert('end', selected_tuple[2])

        isbn_entry.delete(0, 'end')
        isbn_entry.insert('end', selected_tuple[3])


# viewing records on listbox
def view_recods():
    # clearing records from listbox
    list_bx.delete(0, 'end')

    # fetching records from db and viewing them on listbox
    for row in book_db.view():
        list_bx.insert('end', row)


# adding new book to db
def add_book():
    # Check for empty fields
    if not title_text.get() or not author_text.get() or not isbn_text.get():
        messagebox.showerror(title='Book Database', message="All fields must be filled.")
        return

    try:
        # Check if the ISBN input is an integer
        int(isbn_text.get())
    except ValueError:
        messagebox.showerror(title='Book Database', message="Invalid ISBN. Please enter an integer value.")
        return

    # Call the insert method without the unique_id
    book_db.insert(title_text.get(), author_text.get(), isbn_text.get())
    list_bx.delete(0, 'end')
    list_bx.insert('end', (title_text.get(), author_text.get(), isbn_text.get()))
    title_entry.delete(0, "end") # Clears input after inserting
    author_entry.delete(0, "end")
    isbn_entry.delete(0, "end")
    con.commit()


# deleting selected record from db
def delete_records():
    book_db.delete(selected_tuple[0])
    con.commit()


# clearing listbox and all entries from records
def clear_screen():
    list_bx.delete(0, 'end')
    title_entry.delete(0, 'end')
    author_entry.delete(0, 'end')
    isbn_entry.delete(0, 'end')


# updating records
def update_records():
    # updates db with inputed record
    book_db.update(selected_tuple[0], title_text.get(), author_text.get(), isbn_text.get())
    
    # clears entry
    title_entry.delete(0, 'end') # clears input after inserting
    author_entry.delete(0, 'end')
    isbn_entry.delete(0, 'end')
    con.commit()

# closing function
def on_closing():
    temp = book_db
    if messagebox.askokcancel('Quit', 'Do you want to quit?'):
        root.destroy()
        del temp


# Windows of app
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
add_btn = Button(root, text="Add Book", bg="blue", fg="white", font="helvetica 10 bold", command=add_book)
add_btn.grid(row=0, column=6, sticky=W)

# adding listbox to display items
list_bx = Listbox(root, height=16, width=40, font="helvetica 13", bg="light blue")
list_bx.grid(row=3, column=1, columnspan=6, sticky=W+E, pady=40, padx=15)

# enables to select any book record which shown on listbox
list_bx.bind('<<ListboxSelect>>', get_selected_row)

# adding scrollbar
scroll_bar = Scrollbar(root)
scroll_bar.grid(row=3, column=7, rowspan=1, sticky=N+S+W)

# attaching scrollbar to listbox
list_bx.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list_bx.yview)

# adding view button
view_btn = Button(root, text="View all records", bg="black", fg="white",
                  font="helvetica 10 bold", command=view_recods)
view_btn.grid(row=4, column=1)

# adding modify button
modify_btn = Button(root, text="Modify Record", bg="purple", fg="white", font="helvetica 10 bold", command=update_records)
modify_btn.grid(row=4, column=2)

# adding clear button
clear_btn = Button(root, text="Clear Screen", bg="maroon", fg="white",
                   font="helvetica 10 bold", command=clear_screen)
clear_btn.grid(row=4, column=3)

# adding exit button
exit_btn = Button(root, text="Exit Application", bg="blue", fg="white",
                  font="helvetica 10 bold", command=root.destroy)
exit_btn.grid(row=4, column=4)

# adding delete button
delete_btn = Button(root, text="Delete Record", bg="red", fg="white", 
                    font="helvetica 10 bold", command=delete_records)
delete_btn.grid(row=4, column=5)

# making windows
root.mainloop()
