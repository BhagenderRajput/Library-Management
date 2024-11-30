from database import sql

mydata = sql.data
mycursor = sql.cursor
 
# function for adding books
def add_book(book, author,copies):
    mycursor.execute("Insert into books (book_name,author,total_books,available) values (%s,%s,%s,%s)", 
                     (book,author,copies,copies))
    mydata.commit()
    print(mycursor.rowcount, "record inserted")

def add_more_copies(id, copies):
    mycursor.execute("select total_books, available from books where id = %s", (id,))
    output = mycursor.fetchone()
    totalbooks = output[0]
    available = output[1]
    
    new_total = totalbooks + int(copies)
    new_available = available + int(copies)

    mycursor.execute("update books set total_books = %s , available = %s where id = %s", (new_total,new_available,id))

    mydata.commit()
    print("updated successfully") 


