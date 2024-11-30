from datetime import date 
from database import sql 
mydata = sql.data
mycursor = sql.cursor

def return_book(book_id,member_id):
# check if book exist and is available
    mycursor.execute("select available from books where id = %s ",(book_id,))
    record = mycursor.fetchall()
       
    if record is not None:
        # check if there are any active user for book from borrow records
        mycursor.execute("select * from borrow_records where book_id = %s and member_id = %s and status= 1", (book_id,member_id))
        active_record = mycursor.fetchone()

        if active_record is not None:
            # update the borrow_record of user status to 0 (book)
            mycursor.execute("update borrow_records set status = 0 where book_id = %s and member_id = %s",(book_id,member_id))

            # calculate overdue days and late fee 
            borrow_date = active_record[3] # Assuming the fourth column is borrow date 
            return_date = date.today()

            overdue_days = (return_date - borrow_date).days
            late_fee = 0
            # if the book is returend after 5 days , apply a late fee of rupees 10
            if overdue_days > 5:
                late_fee = (overdue_days - 5) * 10   # 10 rupees per day after 5 days 
            # update the borrow records with return date , late fee, and status 
                mycursor.execute("update borrow_records set return_date = %s, late_fee = %s, status = 0 where book_id = %s and member_id = %s and status = true",
                                 (return_date, late_fee, book_id, member_id))
            # update the book availability ( increment the count)
            mycursor.execute("select available from books where id = %s",(book_id,))
            availability = mycursor.fetchone()
            remaining = availability[0] + 1
            mycursor.execute("update books set available = %s where id = %s", (remaining, book_id))
                
            mydata.commit()
            print(f"Book returned successfully. Late fee : {late_fee} rupees")

        else:
            print("No active borrow record found for this book and member.")

    else:
        print("No active borrow records for this book or the book doesn't exist")



