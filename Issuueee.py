from database import sql
mydata = sql.data
mycursor = sql.cursor

def get_borrow_details(book_id):
    mycursor.execute("select * from borrow_records where book_id = %s and status = TRUE",(book_id,))
    result = mycursor.fetchall()

    if result and result[0]:
        mycursor.execute("select member_id from borrow_records where book_id = %s and status = TRUE",(book_id,))
        member_id = mycursor.fetchall()

        for member in member_id:
            mycursor.execute("select name,phone from members where id = %s",(member[0],))
            member_details = mycursor.fetchall()
            
            for data in member_details:
                print(f"Name --> {data[0]}, \nMob.Number ---> {data[1]}")

    else:
        print("Book are Not Issued")
        