from database import sql 
mydata = sql.data
mycursor = sql.cursor


# View all books
def view_books():
    query = "SELECT id, book_name, author, available FROM books"
    mycursor.execute(query)
    books = mycursor.fetchall()
        
# Check if there are any books to display
    if books:
        for book in books:
                print( f"ID: {book[0]}, book_name: {book[1]}, Author: {book[2]}")
    else:
            print("No books found ")

# show all books id and name when we want to borrow book
def view_books_name():
      query = "select id, book_name from books"
      mycursor.execute(query)
      borrowbooks = mycursor.fetchall()
      for book in borrowbooks:
           print(f" ID: {book[0]},book_name: {book[1]}")




    