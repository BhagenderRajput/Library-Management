import AddBook
import AddMember
import BorrowRecords
import ViewBooks
import BookReturn
import IssueDetails
from database import sql
mydata = sql.data   
mycursor = sql.cursor

while(True):

    email = input("Enter your email --> ")
    password = input("Enter Your Password --> ")
    mycursor.execute("select email,password,type from users where email = %s and password = %s and status = True",(email,password))
    record = mycursor.fetchone()

    if record and record[0] == email and record[1] == password:
        if record[2] == "Admin":
            while True: 
                print("\nLibrary Management System")
                print("1. Register Book")
                print("2. Register Member")
                print("3. Add More Books")
                print("4. Borrow Book")
                print("5. Return Book")
                print("6. View Books")
                print("7. Issue Book Details")
                print("8. Logout")

                choice = input("Enter your choice: ")

                if choice == '1':
                    book_name = input("Enter book name: ")
                    mycursor.execute("select book_name from books where book_name = %s",(book_name,))
                    record = mycursor.fetchone()
                    if record and record[0] == book_name:
                        print("Book is already Exist..")
                        
                    author = input("Enter author name: ")
                    copies = input("Number of copies: ")
                    AddBook.add_book(book_name, author,copies)
                    
                elif choice == '2':
                    name = input("Enter the name: ")
                    phone_no = input("Enter the phone no.: ")
                    AddMember.add_member(name,phone_no)

                elif choice == '3':
                    id = input("Enter Book Id: ")
                    copies = input("Number of Copies: ")
                    AddBook.add_more_copies(id,copies)

                elif choice == '4':
                    ViewBooks.view_books_name()
                    book_id = int(input("Enter book ID to borrow: "))
                    member_id = int(input("Enter member ID: "))
                    BorrowRecords.borrow_records(book_id, member_id)

                elif choice == '5':
                    book_id = int(input("Enter book ID to return: "))
                    m_id = int(input("Enter member ID to return: "))
                    BookReturn.return_book(book_id,m_id)

                elif choice == '6':
                    ViewBooks.view_books()

                elif choice == '7':
                    book_id = input("Enter Book ID : ")
                    IssueDetails.get_borrow_details(book_id)

                elif choice == '8':
                        print("Successfully Logout...")
                        break

                else:
                        print("Invalid choice , please try again")

                run_again = input("Do you want to execute the Library Management System again? (yes/no): ").lower()
                if run_again != "yes":
                    print("Exiting...")
                    break

        elif record[2] == "Librarian":
                while True:
                    print("\nLibrary Management System")
                    print("1. Borrow Book")
                    print("2. Return Book")
                    print("3. View Books")
                    print("4. Issue Book Details")
                    print("5. Logout")

                    choice = input("Enter your choice: ")

                    if choice == '1':
                        ViewBooks.view_books_name()
                        book_id = int(input("Enter book ID to borrow: "))
                        member_id = int(input("Enter member ID: "))
                        BorrowRecords.borrow_records(book_id, member_id)

                    elif choice == '2':
                        book_id = int(input("Enter book ID to return: "))
                        m_id = int(input("Enter member ID to return: "))
                        BookReturn.return_book(book_id,m_id)

                    elif choice == '3':
                        ViewBooks.view_books()

                    elif choice == '4':
                        book_id = input("Enter Book ID : ")
                        IssueDetails.get_borrow_details(book_id)

                    elif choice == '5':
                            print("Successfully Logout...")
                            break

                    else:
                            print("Invalid choice , please try again")

                    run_again = input("Do you want to execute the Library Management System again? (yes/no): ").lower()
                    if run_again != "yes":
                        print("Exiting...")
                        break
    else:
        print("Invalid User")

    run_again = input("Do you want to Continue? (y/n): ").lower()
    if run_again != "y":
        print("Exiting...")
        break 
    
    
