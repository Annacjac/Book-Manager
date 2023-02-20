import sys
import book_dao

menu_options = {
    1: 'Add a Publisher',
    2: 'Add a Book',
    3: 'Edit a Book',
    4: 'Delete a Book',
    5: 'Search Books',
    6: 'Exit',
}

search_menu_options = {
    1: 'Search All',
    2: 'Search by Title',
    3: 'Search by ISBN',
    4: 'Search by Publisher',
    5: 'Search by Price Range',
    6: 'Search by Year',
    7: 'Search by Title and Publisher'
}

def search_all_books():
    # Use a data access object (DAO) to 
    # abstract the retrieval of data from 
    # a data resource such as a database.
    results = book_dao.findAll()

    # Display results
    print("The following are the ISBNs and titles of all books.")
    for item in results:
        print(item[0], "|", item[1])
    print("The end of books.")


def search_by_title():
    #gets a title from user input
    title = input("Enter a full or incomplete book title: ")

    #stores results from the query
    results = book_dao.findByTitle(title)

    #prints out the results from the query
    print("The following are the ISBNs and titles of books with title similar to: " + title)
    for item in results:
        print(item[0], "|", item[1])
    print("The end of books.")

def search_by_ISBN():
    #gets an isbn from user input
    isbn = input("Enter a full ISBN: ") 

    #stores results from query
    results = book_dao.findByISBN(isbn)

    #prints results from query
    print("The following are the ISBNs and titles of books with ISBN similar to: " + isbn)
    for item in results:
        print(item[0], "|", item[1])
    print("The end of books.")

def search_by_publisher():
    #gets a publisher from user input
    publisher = input("Enter a full or incomplete publisher name: ")

    #stores results from query
    results = book_dao.findByPublisher(publisher)

    #prints results from query
    print("The following are the ISBNs, titles, and publishers of books with Publisher similar to: " + publisher)
    for item in results:
        print(item[0], "|", item[1], "|", item[3])
    print("The end of books.")

def search_by_pricerange():
    #gets a price range from user input and stores each price into a separate variable
    priceRange = input("Enter a minimum and maximum price in the format (excluding brackets) [minPrice, maxPrice]: ")
    price1 = priceRange.split(", ")[0]
    price2 = priceRange.split(", ")[1]

    #checks to make sure the first input price is lower than the second input price
    while(price1 > price2): 
        print()
        priceRange = input("Minimum price cannot be greater than Maximum price. Please try again: ")
        print()
        price1 = priceRange.split(", ")[0]
        price2 = priceRange.split(", ")[1]

    #stores results from query
    results = book_dao.findByPriceRange(price1, price2)

    #prints results from query
    print("The following are the ISBNs, titles, and prices of books within the price range of: " + price1 + " and " + price2)
    for item in results:
        print(item[0], "|", item[1], "|", item[5])
    print("The end of books.")

def search_by_year():
    #gets a year from user input
    year = input("Enter a year: ")
    
    #stores results from query
    results = book_dao.findByYear(year)

    #prints results from query
    print("The following are the ISBNs, titles, and year of books from the year: " + year)
    for item in results:
        print(item[0], "|", item[1], "|", item[2])
    print("The end of books.")

def search_by_title_pub():
    #gets a title and publisher from user input and stores each in a separate variable
    titlePub = input("Enter a full or incomplete book title and publisher in the format (excluding brackets) [title, publisher]: ")
    title = titlePub.split(", ")[0]
    publisher = titlePub.split(", ")[1]

    #stores results from query
    results = book_dao.findByTitlePublisher(title, publisher)

    #prints results from query
    print("The following are the ISBNs, titles, and publishers of books with title: " + title + " and publisher: " + publisher)
    for item in results:
        print(item[0], "|", item[1], "|", item[3])
    print("The end of books.")

def print_menu():
    print()
    print("Please make a selection")
    for key in menu_options.keys():
        print (str(key)+'.', menu_options[key], end = "  ")
    print()
    print("The end of top-level options")
    print()


def option1():
    #gets publisher info from user input
    pubInfo = input("Enter publisher information in the format (excluding brackets) [name, phone number, city]: ")

    #checks to make sure user has input the correct amount of arguments
    while(len(pubInfo.split(", ")) != 3):
        if(len(pubInfo.split(", ")) > 3):
            pubInfo = input("Too many fields entere. Please try again: ")
        elif(len(pubInfo.split(", ")) < 3):
            pubInfo = input("Too few fields entered. Please try again: ")

    #stores each piece of info in a separate variable
    name = pubInfo.split(", ")[0]
    phone = pubInfo.split(", ")[1]
    city = pubInfo.split(", ")[2]

    #stores all information from all publishers in the database
    publishers = book_dao.showPublishers()

    #flag that checks if publisher already exists
    pubExists = False
    for item in publishers:
        if(name == item[0]):
            pubExists = True

    #prompts user to input a different publisher name if publisher already exists        
    while(pubExists == True):
        name = input("Publisher by that name already exists. Please enter a new name: ")
        for item in publishers:
            if(name != item[0]):
                pubExists = False
                break
    
    #adds publisher to database
    book_dao.addPublisher(name, phone, city)

    #prints all publishers so user can see theirs was added
    print("Added publisher with the following information: ('"+ name + "', '" + phone + "', '" + city + "')")
    print("See all publishers below:")
    publishers = book_dao.showPublishers()
    for item in publishers:
        print(item[0], "|", item[1], "|", item[2])
    print("The end of publishers.")


def option2():
    #gets book info from user input
    bookInfo = input("Enter book information in the format (excluding brackets) [isbn, title, year, existing publisher, existing previous edition isbn or NULL, price]: ")
    
    #checks to make sure user has input correct number of arguments
    while(len(bookInfo.split(", ")) != 6):
        if(len(bookInfo.split(", ")) < 6):
            bookInfo = input("Too few fields entered. Please try again: ")
        elif(len(bookInfo.split(", ")) > 6):
            bookInfo = input("Too many fields entered. Please try again: ")

    #stores each piece of info in separate variable
    isbn = bookInfo.split(", ")[0]
    title = bookInfo.split(", ")[1]
    year = bookInfo.split(", ")[2]
    publisher = bookInfo.split(", ")[3]
    #puts single quotations on previous edition if not NULL
    if bookInfo.split(", ")[4] == "NULL":
        prevEdition = bookInfo.split(", ")[4]
    else:
        prevEdition = "'" + bookInfo.split(", ")[4] + "'"
    price = bookInfo.split(", ")[5]
    allInfo = "'"+ isbn + "', '" + title + "', " + year + ", '" + publisher + "', " + prevEdition + ", " + price

    #stores all publisher and book info from database
    publishers = book_dao.showPublishers()  
    books = book_dao.findAll()

    #flags to check if the publisher, previous edition, and isbn already exist
    pubExists = False
    prevEdExists = False
    isbnExists = False   
    for item in books:
        if(isbn == item[0]):
            isbnExists = True
            #print("isbn exists")
            break
    for item in publishers:
        if(publisher == item[0]):
            pubExists = True
            #print("pub exists")
            break
    for item in books:
        if(prevEdition == "'" +item[0]+ "'" or prevEdition == "NULL"):
            prevEdExists = True
            #print("prev edition exists")
            break

    #prompts user to input a different ISBN if it already exists
    while(isbnExists == True):
        isbn = input("Book with that ISBN already exists. Please enter a new one: ")
        isbnExists = False
        allInfo = "'"+ isbn + "', '" + title + "', " + year + ", '" + publisher + "', " + prevEdition + ", " + price
        for item in books:
            if(isbn == item[0]):
                isbnExists = True
                break
    #prompts user to input a different publisher name if it does not exist
    while(pubExists == False):
        publisher = input("Publisher does not exist. Please enter a valid one: ")
        for item in publishers:
            if(publisher == item[0]):
                pubExists = True
                allInfo = "'"+ isbn + "', '" + title + "', " + year + ", '" + publisher + "', " + prevEdition + ", " + price
                #print("pub exists")
                break
    #prompts user to input a different previous edition isbn or NULL if it does not exist
    while(prevEdExists == False):
        prevEdition = input("Previous edition ISBN does not exist. Please enter a valid one or NULL: ")
        if(prevEdition != "NULL"):
            prevEdition = "'" + prevEdition + "'"
        for item in books:
            if(prevEdition == "'" +item[0]+ "'" or prevEdition == "NULL"):
                prevEdExists = True
                allInfo = "'"+ isbn + "', '" + title + "', " + year + ", '" + publisher + "', " + prevEdition + ", " + price
                #print("prev edition exists")
                break

    if(isbnExists == False and pubExists == True and prevEdExists == True):
        #adds book to the database
        book_dao.addBook(allInfo)

        #prints all books so user can see theirs was added
        print("Added book with the following information: ("+ allInfo +")")
        print("See all books below:")
        books = book_dao.findAll()
        for item in books:
            print(item[0], "|", item[1], "|", item[2], "|", item[3], "|", item[4], "|", item[5])
        print("The end of books.")
        
    
    

def option3():
    #gets ISBN of book to edit from user input
    isbn1 = input("Enter the ISBN of the book you'd like to edit: ")

    #stores all book info from database
    books = book_dao.findAll()

    #flag to check if ISBN of book to edit exists
    bookExists = False
    for item in books:
        if(isbn1 == item[0]):
            bookExists = True
            break
    
    #prompts user to input a new ISBN if it does not exist
    while(bookExists == False):
        isbn1 = input("Book with that ISBN does not exist. Please enter a valid ISBN: ")
        for item in books:
            if(isbn1 == item[0]):
                bookExists = True
                break

    #gets book info from user input
    bookInfo = input("Enter the new information for the book in the format (excluding the brackets) [isbn, title, year, existing publisher, existing previous edition isbn or NULL, price]: ")
    
    #checks to make sure user has input correct number of arguments
    while(len(bookInfo.split(", ")) != 6):
        if(len(bookInfo.split(", ")) < 6):
            bookInfo = input("Too few fields entered. Please try again: ")
        elif(len(bookInfo.split(", ")) > 6):
            bookInfo = input("Too many fields entered. Please try again: ")

    #stores each piece of info into separate variables
    isbn2 = bookInfo.split(", ")[0]
    title = bookInfo.split(", ")[1]
    year = bookInfo.split(", ")[2]
    publisher = bookInfo.split(", ")[3]
    if bookInfo.split(", ")[4] == "NULL":
        prevEdition = bookInfo.split(", ")[4]
    else:
        prevEdition = "'" + bookInfo.split(", ")[4] + "'"
    price = bookInfo.split(", ")[5]
    publishers = book_dao.showPublishers()
    
    #flags to check if isbn, publisher, previous edition isbn already exist
    pubExists = False
    prevEdExists = False
    isbnExists = False
    for item in books:
        if(isbn2 == item[0] and isbn1 != isbn2):
            isbnExists = True
            #print("isbn exists")
            break
    for item in publishers:
        if(publisher == item[0]):
            pubExists = True
            #print("pub exists")
            break
    for item in books:
        if(prevEdition == "'" +item[0]+ "'" or prevEdition == "NULL"):
            prevEdExists = True
            #print("prev edition exists")
            break

    #prompts user to input a new isbn if another book with the same isbn already exists
    while(isbnExists == True):
        isbn2 = input("A different book with that ISBN already exists. Please enter a new one: ")
        isbnExists = False
        for item in books:
            if(isbn2 == item[0]):
                isbnExists = True
                break

    #prompts user to input new publisher if it does not exist
    while(pubExists == False):
        publisher = input("Publisher does not exist. Please enter a valid one: ")
        for item in publishers:
            if(publisher == item[0]):
                pubExists = True
                #print("pub exists")
                break

    #prompts user to input new previous edition isbn or NULL if it does not exist
    while(prevEdExists == False):
        prevEdition = input("Previous edition ISBN does not exist. Please enter a valid one or NULL: ")
        if(prevEdition != "NULL"):
            prevEdition = "'" + prevEdition + "'"
        for item in books:
            if(prevEdition == "'" +item[0]+ "'" or prevEdition == "NULL"):
                prevEdExists = True
                #print("prev edition exists")
                break

    if(isbnExists == False and pubExists == True and prevEdExists == True):
        #edits book in database
        book_dao.editBook(isbn1, isbn2, title, year, publisher, prevEdition, price)

        #prints all books so user can see their edit applied
        print("Edited book with the following information: ('" + isbn2 +"', '" + title + "', " + year + ", '" + publisher + "', '" + prevEdition + "', " + price + "')")
        print("See all books below:")
        books = book_dao.findAll()
        for item in books:
            print(item[0], "|", item[1], "|", item[2], "|", item[3], "|", item[4], "|", item[5])
        print("The end of books.")

def option4():
    #gets isbn of book to delete from user input
    isbn = input("Enter the ISBN of the book you'd like to delete: ")

    #stores all book info from database
    books = book_dao.findAll()

    #flag to check if that book exists
    bookExists = False
    for item in books:
        if(isbn == item[0]):
            bookExists = True

            #deleted the book
            book_dao.deleteBook(isbn)

            #updates all book info
            books = book_dao.findAll()

            #prints all books so user can see their deletion was applied
            print("Book deleted. See remaining books:")
            for book in books:
                print(book[0], "|", book[1])
            print("The end of books.")    
            break

    #prompts user to input new isbn if their input isbn doesn't exist
    while(bookExists == False):
        isbn = input("That book does not exist. Please enter an existing ISBN to delete: ")
        for item in books:
            if(isbn == item[0]):
                bookExists = True
                book_dao.deleteBook(isbn)
                books = book_dao.findAll()
                print("Book deleted. See remaining books:")
                for book in books:
                    print(book[0], book[1])
                print("The end of books.")    
                break        
    

def option5():
    # A sub-menu shall be printed
    # and prompt user selection

    # print_search_menu

    # user selection of options and actions

    # Assume the option: search all books was chosen
    while(True):    
        option = ''
        print()
        print("Please make a selection")
        for key in search_menu_options.keys():
            print (str(key)+'.', search_menu_options[key], end = "  ")
        print()
        print("End of search options")
        print()
        try:
            option = int(input('Enter your choice: '))
        except KeyboardInterrupt:
            print('Interrupted')
            sys.exit(0)
        except:
            print('Wrong input. Please enter a number ...')
        if option == 1:
            print("Search Option 1: all books were chosen.")
            search_all_books()
            break
        elif option == 2:
            print("Search Option 2: Search by Title.")
            search_by_title()
            break
        elif option == 3:
            print("Search Option 3: Search by ISBN.")
            search_by_ISBN()
            break
        elif option == 4:
            print("Search Option 4: Search by Publisher.")
            search_by_publisher()
            break
        elif option == 5:
            print("Search Option 5: Search by Price Range.")
            search_by_pricerange()
            break
        elif option == 6:
            print("Search Option 6: Search by Year.")
            search_by_year()
            break
        elif option == 7:
            print("Search Option 7: Search by Title and Publisher")
            search_by_title_pub()
            break



if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except KeyboardInterrupt:
            print('Interrupted')
            sys.exit(0)
        except:
            print('Wrong input. Please enter a number ...')

        # Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            option5()
        elif option == 6:
            print('Thanks your for using our database services! Bye')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 6.')











