from datetime import date
from database import sql 
mydata = sql.data
mycursor = sql.cursor


def borrow_records(book_id, member_id):
# Check there is an active borrow record (indicated by status = 1) for this book and member.    
    mycursor.execute("select * from borrow_records where book_id = %s and member_id = %s and status = 1",
                     (book_id,member_id))
    record = mycursor.fetchone()
    
    if record is None:
        mycursor.execute("select available from books where id = %s", (book_id,))   # Check book availability
        result = mycursor.fetchone()

        if (result[0] != 0):   # Check if the book is available for borrowing
            mycursor.execute("Insert into borrow_records (book_id, member_id, borrow_date) values (%s, %s, %s)",
                          (book_id, member_id , date.today()))
        
 # update the book availability
            mycursor.execute("select available from books where id = %s",(book_id,))
            availability = mycursor.fetchone()
            remaining = availability[0] - 1

            mycursor.execute("update books set available = %s where id = %s ", (remaining,book_id,))
            mydata.commit()
            print("Book borrowed successfully")
            
        else:
            print("Book is not available")
    else:
        print("You have already issued this book")
 



 