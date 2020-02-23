import mysql.connector
from Book_Database import mydb
from Book_Database import mycursor
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

font = ("Segoe UI", 10)
bg = '#939393'
rel = 'flat'
List_choices = ["All", "Fiction", "Progamming", "Literature"]

class MyBooks:
    def __init__(self, master): #App
        frame = Frame(root, width=400, height=170, bg= '#939393').pack()
        self.BookLabel_Books = Label(frame, text="Book:", font=("Segoe UI", 14), rel=rel, bg=bg)
        self.BookLabel_Category = Label(frame, text="Category:", font=("Segoe UI", 14), rel=rel, bg=bg)
        self.BookEntry = Entry(frame, font=("Segoe UI", 14), textvariable="")
        self.BookCategory = Entry(frame, font=("Segoe UI", 14), textvariable="")
        self.BookRegister = Button(frame, text="Register", font=("Segoe UI", 12), relief=rel, command=self.register)
        self.BookDatabase = Button(frame, text="Database", font=("Segoe UI", 12), relief=rel, command=self.database)
        self.BookClear = Button(frame, text="Clear", font=("Segoe UI", 12), relief=rel, command=self.clear)

        self.BookLabel_Books.place(x=60, y=25)
        self.BookLabel_Category.place(x=25, y=60)
        self.BookEntry.place(x=120, y=27, width=250, height=25)
        self.BookCategory.place(x=120, y=63, width=250, height=25)
        self.BookRegister.place(x=25, y=110, width=110)
        self.BookDatabase.place(x=143, y=110, width=110)
        self.BookClear.place(x=260, y=110, width=110)

    def register(self):
        mycursor = mydb.cursor()
        sqlformula = "INSERT INTO books (name, category) VALUES (%s, %s)"
        data = (self.BookEntry.get(), self.BookCategory.get())
        mycursor.execute(sqlformula, data)
        mydb.commit()
        messagebox.showinfo("Book Registration", "Book is registered!")

    def clear(self):
        self.BookEntry.delete(0, 'end')
        self.BookCategory.delete(0, 'end')
        self.List.set('')
        self.Lb.delete(0, 'end')

    def database(self):
        
        top = Toplevel(width=393, height=396, bg= '#939393')
        self.BookList = Label(top, text="Books", font=("Segoe UI", 10), bg='#939393')
        self.List = ttk.Combobox(top, values=List_choices, font=font)
        self.Lb = Listbox(top, font=font, bd=0, highlightthickness=0, relief=rel)
        self.Clear = Button(top, text="Clear", font=font, relief=rel, command=self.clear)
        self.SearchBook = Button(top, text="Search", font=font, relief=rel, command=self.search)

        self.BookList.place(x=65, y=50)
        self.List.place(x=110 , y=53, width=210, height=20)
        self.Lb.place(x=65, y=83, width=253, height=220)
        self.Clear.place(x=65, y=310, width=123.5, height=25)
        self.SearchBook.place(x=193, y=310, width=123.5, height=25)

        top.title("Book Database")
        top.mainloop()

    def search(self):
        if self.List.get() == List_choices[0]:
            for Book in Books:
                self.Lb.insert(END, Book)
        elif self.List.get() == List_choices[1]:
            self.Lb.delete(0, 'end')
            sql = "SELECT * FROM books WHERE category LIKE 'Fiction'"
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            for result in myresult:
                self.Lb.insert(1, result[0])
        
        elif self.List.get() == List_choices[2]:
            self.Lb.delete(0, 'end')
            self.Lb.insert(1, Books[2])
        elif self.List.get() == List_choices[3]:
            self.Lb.delete(0, 'end')
            self.Lb.insert(1, Books[1])
            self.Lb.insert(2, Books[3])

root = Tk()
root.title("Book Registration")
app = MyBooks(root)
root.mainloop()
        