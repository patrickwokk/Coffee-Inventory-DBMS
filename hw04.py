from random import choice
import mysql.connector
import random
from tabulate import DataRow, tabulate

def open_database (hostname,user_name,mysql_pw,database_name):
      global conn
      conn= mysql.connector.connect(host= hostname, 
      user= user_name,  
      password= mysql_pw, 
      database= database_name 
    ) 
      global cursor
      cursor = conn.cursor() 

def printFormat(result):
    header=[]
    for cd in cursor.description:# get headers
        header.append(cd[0])
    print('')
    print('Query Result:')
    print('')
    print(tabulate(result, headers=header))# print results in table format

# select and display query
def executeSelect (query):
    cursor.execute(query)
    printFormat(cursor.fetchall())

def  insert(table,values):
     query ="INSERT into " + table + " values (" + values + ")" +';'
     cursor.execute(query)
     conn.commit()

def executeUpdate(query): # use this function for delete and update
    cursor.execute(query)
    conn.commit()

def close_db ():  # use this function to close db
    cursor.close()
    conn.close()

def userChoice():  # user Choice Menu
    print('Please Choose the following option: ')
    print('1. Find all suppliers and coffee names')
    print('2. Add new supplier')
    print('3. List item sold by a specific employee')
    print('4. Update item')
    print('5. Cancel Sales')
    print('6. Exit')

    try:
        num = int (input(">>> "))
    except ValueError:
        print('integer only...')
        num = int (input(">>> "))

    return num

def menu1():  #1
    print(' ')
    print('Option 1: ')
    CountryName = input('Name of the Country: \n') #input country
    print(' ')
    print('=================================================================') #query sql
    executeSelect('SELECT s.ID, s.NAME AS SUPPLIER_NAME, s.PHONE_NUMBER, i.NAME AS COFFEE_NAME, i.ROASTING_TYPE FROM SUPPLIER s, INVENTORY_MGMT m, ITEM i WHERE i.ID = m.ITEM_ID AND s.ID = m.SUPPLIER_ID AND s.COUNTRY = "%s";' %CountryName)
    print(' ')
    if cursor.rowcount == 0: #if pointer is blank to sql (no data in sql)
        print('No Supplier')
        print(' ')
    print('=================================================================')
    print(' ')


def menu2():  #2
    print(' ')
    print('Option 2: ')
    #input
    randomID = random.randint(11,100) #generating random number for supplier ID
    print('this is the ID for new supplier: ',randomID)
    print(' ')
    newSupplier = input('Enter a new supplier name: \n')
    print(' ')
    newPhone = input('Enter the supplier phone number: \n')
    print(' ')
    newCountry = input('Enter the supplier country: \n')
    print(' ')

    print('=================================================================') #query
    insert('SUPPLIER', "%s, '%s', %s, '%s'" % (randomID, newSupplier, newPhone, newCountry))
    executeSelect('SELECT * FROM SUPPLIER WHERE SUPPLIER.NAME = "%s";' %newSupplier) #print record
    print(' ')
    
    #NEED TO ADD INFO TO INVENTORY_MGMT (e.g. supplier id) TOO, look at the below code how i would do it
    #i also add random integer for the id, please make sure we are using the same random id when inserting info to inventory mgmt

    print('what coffee can you provide: ')
    print('1. ANTIGUA')
    print('2. HAMBELA KIRITE')
    print('3. KHAWLANI')
    print('4. MOGIANA')
    print('5. ALWADI')
    print('6. VOLCANICA SUPREMO')
    print('7. PNG')
    print('8. SUMATRA GAYO')
    print('9. ARABICA')
    print('10. GENERAL MERCHANDISE')
    print('11. SIDAMO')
    print('12. GHIMBI')
    print('13. ALDURRAR')

    try:
        num = int (input(">>> "))
    except ValueError:
        print('integer only...')
        num = int (input(">>> "))

    if num == 1:
        insert('INVENTORY_MGMT', " 1, '%s', 0, 0" % randomID)
        executeSelect('SELECT s.NAME AS SUPPLIERS_WHO_SELL_ANTIGUA FROM SUPPLIER s, INVENTORY_MGMT m WHERE m.ITEM_ID = 1 and s.ID = m.SUPPLIER_ID;')
        print('\n')
        print('Data added to Inventory_mgmt')
    elif num == 2:
        insert('INVENTORY_MGMT', " 2, '%s', 0, 0" % randomID)
        executeSelect('SELECT s.NAME AS SUPPLIERS_WHO_SELL_HAMBELA_KIRITE FROM SUPPLIER s, INVENTORY_MGMT m WHERE m.ITEM_ID = 2 and s.ID = m.SUPPLIER_ID;')
        print('\n')
        print('Data added to Inventory_mgmt')
    elif num == 3:
        insert('INVENTORY_MGMT', " 3, '%s', 0, 0" % randomID)
        executeSelect('SELECT s.NAME AS SUPPLIERS_WHO_SELL_KHAWLANI FROM SUPPLIER s, INVENTORY_MGMT m WHERE m.ITEM_ID = 3 and s.ID = m.SUPPLIER_ID;')
        print('\n')
        print('Data added to Inventory_mgmt')
    elif num == 4:
        insert('INVENTORY_MGMT', " 4, '%s', 0, 0" % randomID)
        executeSelect('SELECT s.NAME AS SUPPLIERS_WHO_SELL_MOGIANA  FROM SUPPLIER s, INVENTORY_MGMT m WHERE m.ITEM_ID = 4 and s.ID = m.SUPPLIER_ID;')
        print('\n')
        print('Data added to Inventory_mgmt')
    elif num == 5:
        insert('INVENTORY_MGMT', " 5, '%s', 0, 0" % randomID)
        executeSelect('SELECT s.NAME AS SUPPLIERS_WHO_SELL_ALWADI FROM SUPPLIER s, INVENTORY_MGMT m WHERE m.ITEM_ID = 5 and s.ID = m.SUPPLIER_ID;')
        print('\n')
        print('Data added to Inventory_mgmt')
    elif num == 6:
        insert('INVENTORY_MGMT', " 6, '%s', 0, 0" % randomID)
        executeSelect('SELECT s.NAME AS SUPPLIERS_WHO_SELL_VOLCANICA_SUPREMO FROM SUPPLIER s, INVENTORY_MGMT m WHERE m.ITEM_ID = 6 and s.ID = m.SUPPLIER_ID;')
        print('\n')
        print('Data added to Inventory_mgmt')
    elif num == 7:
        insert('INVENTORY_MGMT', " 7, '%s', 0, 0" % randomID)
        executeSelect('SELECT s.NAME AS SUPPLIERS_WHO_SELL_PNG FROM SUPPLIER s, INVENTORY_MGMT m WHERE m.ITEM_ID = 7 and s.ID = m.SUPPLIER_ID;')
        print('\n')
        print('Data added to Inventory_mgmt')
    elif num == 8:
        insert('INVENTORY_MGMT', " 8, '%s', 0, 0" % randomID)
        executeSelect('SELECT s.NAME AS SUPPLIERS_WHO_SELL_SUMATRA-GAYO FROM SUPPLIER s, INVENTORY_MGMT m WHERE m.ITEM_ID = 8 and s.ID = m.SUPPLIER_ID;')
        print('\n')
        print('Data added to Inventory_mgmt')
    elif num == 9:
        insert('INVENTORY_MGMT', " 9, '%s', 0, 0" % randomID)
        executeSelect('SELECT s.NAME AS SUPPLIERS_WHO_SELL_ARABICA FROM SUPPLIER s, INVENTORY_MGMT m WHERE m.ITEM_ID = 9 and s.ID = m.SUPPLIER_ID;')
        print('\n')
        print('Data added to Inventory_mgmt')
    elif num == 10:
        insert('INVENTORY_MGMT', " 10, '%s', 0, 0" % randomID)
        executeSelect('SELECT s.NAME AS SUPPLIERS_WHO_SELL_GENERAL_MERCHANDISE FROM SUPPLIER s, INVENTORY_MGMT m WHERE m.ITEM_ID = 10 and s.ID = m.SUPPLIER_ID;')
        print('\n')
        print('Data added to Inventory_mgmt')
    elif num == 11:
        insert('INVENTORY_MGMT', " 11, '%s', 0, 0" % randomID)
        executeSelect('SELECT s.NAME AS SUPPLIERS_WHO_SELL_SIDAMO FROM SUPPLIER s, INVENTORY_MGMT m WHERE m.ITEM_ID = 11 and s.ID = m.SUPPLIER_ID;')
        print('\n')
        print('Data added to Inventory_mgmt')
    elif num == 12:
        insert('INVENTORY_MGMT', " 12, '%s', 0, 0" % randomID)
        executeSelect('SELECT s.NAME AS SUPPLIERS_WHO_SELL_GHIMBI FROM SUPPLIER s, INVENTORY_MGMT m WHERE m.ITEM_ID = 12 and s.ID = m.SUPPLIER_ID;')
        print('\n')
        print('Data added to Inventory_mgmt')
    elif num == 13:
        insert('INVENTORY_MGMT', " 13, '%s', 0, 0" % randomID)
        executeSelect('SELECT s.NAME AS SUPPLIERS_WHO_SELL_ALDURRAR FROM SUPPLIER s, INVENTORY_MGMT m WHERE m.ITEM_ID = 13 and s.ID = m.SUPPLIER_ID;')
        print('\n')
        print('Data added to Inventory_mgmt')
    else:
        print('\n')
        print('selection not found, please try again')
    print(' ')
    print('=================================================================')
    print(' ')


def menu3():  #3
    print(' ')
    print('Option 3: ')
    #input
    employeeName = input('Name of the employee: \n')
    print(' ')
    print('=================================================================') #query sql
    executeSelect('SELECT i.NAME AS COFFEE_NAME, i.ROASTING_TYPE, COUNT(a.ITEM_ID) AS TOTAL_SALES FROM INVENTORY_MGMT m, ITEM i, EMPLOYEE e, SALES a WHERE a.ITEM_ID = i.ID AND i.ID = m.ITEM_ID AND a.EMPLOYEE_ID = e.ID AND e.NAME = "%s" GROUP BY i.ID;' %employeeName)
    print(' ')
    if cursor.rowcount == 0: #if there is no data in sql
        print('No items sold by this employee')
        print(' ')
    print('=================================================================')
    print(' ')


def menu4():  #4
    print(' ')
    print('Option 4: ')
    #input
    nameItem = input('Enter the name of the item: \n')
    print(' ')
    print('=================================================================')
    #query for initial available
    executeSelect('SELECT i.NAME, m.TOTAL_AVAILABLE FROM ITEM i, INVENTORY_MGMT m WHERE i.NAME = "%s" AND m.ITEM_ID = i.ID;' %nameItem)
    print(' ')
    if cursor.rowcount == 0: #if item is not listed, move on
        print('No item listed')
        print(' ')
    else:
        choice = input('Type "sale" if you made a sale, or type "shipment" if you recieved a shipment: ') #ask for sale or shipment
        print('')
        #query for sale or shipment
        if choice == 'sale':
            numSold = input('Enter the quantity of items sold: ')
            print(' ')
            executeUpdate('UPDATE INVENTORY_MGMT m, ITEM i SET m.TOTAL_AVAILABLE = (m.TOTAL_AVAILABLE - "%s") WHERE i.NAME = "%s" AND m.ITEM_ID = i.ID;' % (numSold, nameItem))
            executeSelect('SELECT i.NAME, m.TOTAL_AVAILABLE FROM ITEM i, INVENTORY_MGMT m WHERE i.NAME = "%s" AND m.ITEM_ID = i.ID;' %nameItem)
        elif choice == 'shipment':
            numBought = input('Enter the quantity of items bought:')
            executeUpdate('UPDATE INVENTORY_MGMT m, ITEM i SET m.TOTAL_AVAILABLE = (m.TOTAL_AVAILABLE + "%s") WHERE i.NAME = "%s" AND m.ITEM_ID = i.ID;' % (numBought, nameItem))
            executeSelect('SELECT i.NAME, m.TOTAL_AVAILABLE FROM ITEM i, INVENTORY_MGMT m WHERE i.NAME = "%s" AND m.ITEM_ID = i.ID;' %nameItem)
        else:
            print('choice is invalid, please try again')
    print(' ')
    print('=================================================================')
    print(' ')


def menu5():  #5
    print(' ')
    print('Option 5: ')
    #input
    print(' ')
    print('=================================================================\n')
    #QUERY
    print('NOT BUILD YET (IN PROGRESS)')
    print(' ')
    print('=================================================================')
    print(' ')


def menu6():  #6
    print('Goodbye')
    close_db()# close database


##### Test #######
mysql_username = '' # please change to your username
mysql_password = ''  # please change to your MySQL password

open_database('localhost',mysql_username,mysql_password,mysql_username) # open database   

MenuFlag = False;
choice = userChoice()

while MenuFlag == False:
    if choice == 1:
        menu1()
        choice = userChoice()

    elif choice == 2:
        menu2()
        choice = userChoice()

    elif choice == 3:
        menu3()
        choice = userChoice()

    elif choice == 4:
        menu4()
        choice = userChoice()
    
    elif choice == 5:
        menu5()
        choice = userChoice()

    elif choice == 6:
        menu6()
        MenuFlag = True

    else:
        print('Invalid Choice\n')