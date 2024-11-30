from database import sql
mydata = sql.data
mycursor = sql.cursor


def add_member(name,phone_no):
    mycursor.execute("Insert into members (name, phone) values (%s,%s)", (name, phone_no))
    mydata.commit()

    print(mycursor.rowcount, "record inserted")
    
    