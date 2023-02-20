from mysql_connector import connection

def findAll():
    cursor = connection.cursor()
    query = "select * from bookmanager.Book"
    cursor.execute(query)
    results = cursor.fetchall()
    #connection.close()
    return results
    
#Searches by title
def findByTitle(title):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where title like '%" + title +"%';"
    cursor.execute(query)
    results = cursor.fetchall()
    #connection.close()
    return results

#Searches bu ISBN
def findByISBN(isbn):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where ISBN = '" + isbn +"';"
    cursor.execute(query)
    results = cursor.fetchall()
    #connection.close()
    return results

#searches by publisher
def findByPublisher(publisher):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book b, bookmanager.Publisher p where p.name like '%" + publisher +"%' and p.name = b.published_by;"
    cursor.execute(query)
    results = cursor.fetchall()
    #connection.close()
    return results

#searches by price range
def findByPriceRange(price1, price2):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where price >= " + price1 + " and price <= "+ price2 +";"
    cursor.execute(query)
    results = cursor.fetchall()
    #connection.close()
    return results

#searches by year
def findByYear(year):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where year = " + year + ";"
    cursor.execute(query)
    results = cursor.fetchall()
    #connection.close()
    return results

#searches by title and publisher
def findByTitlePublisher(title, publisher):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where title like '%" + title + "%' and published_by like '%" + publisher + "%';"
    cursor.execute(query)
    results = cursor.fetchall()
    #connection.close()
    return results

#adds publisher to database
def addPublisher(name, phone, city):
    cursor = connection.cursor()
    query = "insert into bookmanager.Publisher values('" + name + "', '"+ phone +"', '"+ city +"');"
    cursor.execute(query)
    results = cursor.fetchall()
    #connection.close()
    return results

#gets all publisher information
def showPublishers():
    cursor = connection.cursor()
    query = "select * from bookmanager.Publisher;"
    cursor.execute(query)
    results = cursor.fetchall()
    #connection.close()
    return results

#adds new book to database
def addBook(bookInfo):
    cursor = connection.cursor()
    query = "insert into bookmanager.Book values(" + bookInfo + ");"
    cursor.execute(query)
    results = cursor.fetchall()
    #connection.close()
    return results

#edits existing book in the database
def editBook(isbn1, isbn2, title, year, publisher, previous_edition, price):
    cursor = connection.cursor()
    query = "update bookmanager.Book set isbn = '" + isbn2 + "', title = '" + title + "', year = " + year + ", published_by = '" + publisher + "', previous_edition = " + previous_edition + ", price = " + price + " where isbn = '" + isbn1 +"';"
    cursor.execute(query)
    results = cursor.fetchall()
    #connection.close()
    return results

#deletes existing book from the database
def deleteBook(isbn):
    cursor = connection.cursor()
    query = "delete from bookmanager.Book where isbn = '" + isbn + "';"
    cursor.execute(query)
    results = cursor.fetchall()
    #connection.close()
    return results