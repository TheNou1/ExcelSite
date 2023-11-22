

#call = input("Welcome to the Simple Bookstore Inventory System. Here’s the list of options:\n\tA- Add books to the inventory.\n\tB- Sell books by ISBN.\n\tC- List all books by a given author.\n\tD- List all books to be re-ordered.\n\tE- List the entire inventory.\n\tX- Exit\nSelect an option by entering its letter:")
def isbncheck(x):
    if len(x) == 10 and x.isdigit or (all(x[0:-2]).isdigit and x[-1] == "X"):
        multiply = [10,9,8,7,6,5,4,3,2,1]
        validity = []
        for i in range(len(x)):
            if i != "X":
                validity.append(int(x[i])*multiply[i])
            else:
                validity.append(10)
        if sum(validity) % 11 ==0:
            return True
        else:
            return False


def sell(x):
    for i in inventory:
        if x in i:# removes the quantity sold
            if i[3] > 0:
                i[3] -= 1
            print(i[0],"by",i[1],"$", i[-1])
        elif i[3] == 0: # if the book is out of stock, the book can't be sold
            print("Sorry, we don’t seem to have that book!")
            

choice = input("Welcome to the Simple Bookstore Inventory System. Here’s the list of options:\n\tA- Add books to the inventory.\n\tB- Sell books by ISBN.\n\tC- List all books by a given author.\n\tD- List all books to be re-ordered.\n\tE- List the entire inventory.\n\tX- Exit\nSelect an option by entering its letter:")
inventory = []
while choice != "X" and choice != "x":

    #A
    if choice == "A" or choice == "a":
        add = input("Enter book record or done:")
        while add  != "done":# keeps looping until done is called
            store = add.split(',')
            while add[-1].isdigit() == False:
                print("Record invalid, rejected")
                add = input("Enter book record or done:")
                store = add.split(',')
            while len(store) != 5:#checks length of the string to ensure the record is valid
                print("Record incomplete, rejected")
                add = input("Enter book record or done:")
                store = add.split(',')
            store[-1], store[-2] = float(store[-1]), int(store[-2])
            store[-1] += 0.1
            store[-1] -=0.1# the code above turns the last two strings in the book record into an integer and float
            tempstore = []
            for i in store:
                tempstore.append(i)
            if isbncheck(tempstore[2]) == True: #true if the isbn is valid
                if len(inventory) > 0:
                    for i in inventory:# checks all values in inventory to account for books with the same isbn 
                        if tempstore[2] in i[2]:
                            i[3]+=tempstore[3]
                            print("Quantity for", i[2],"is now", i[3])
                            break# to try to fix the "record accepted"
                        else:
                            inventory.append(tempstore)
                elif tempstore in inventory:# i tried to fix the "record accepted that popped up but i could not figure out how exactly,"
                    break
                else:
                    inventory.append(tempstore)
                print("record accepted")
            else:
                print("Record invalid, rejected")
            add =input("Enter book record or done:")


    #B
    elif choice == "B" or choice =="b":
        #check storage
        isbn = input("Enter the ISBN or done:")
        numbers = []
        for i in inventory:# makes a seperate list full of just the isbn's in the inventory
                numbers.append(i[2])
        while isbn != "done": #keeps looping until done
            if isbn in numbers:# if the isbn is in the inventory, respond accordingly
                sell(isbn)
                isbn = input("Enter the ISBN or done:")
            else:
                print("Sorry, we don't seem to have that book!")
                isbn = input("Enter the ISBN or done")
        print("Thank you for shopping with us.")
                

    #C

    elif choice == "C" or choice == "c":
        name = input("Enter the author's name:")
        name = name.title()# turns the input into a string that accounts for incorrect spelling
        for book in inventory:
            if name in book[1]:# prints the books with the same author name
                print(book[0],"by",book[1],book[3],"on hand, price $",book[4])# properly prints the text
        print("End of list")
    #D
    elif choice == "D" or choice == "d":
        for i in inventory:
            if i[3] > 2:#Only prints the books with less than 2 copies
                print(i[0],"by",i[1],i[3],"on hand, price $",i[4])# properly prints the text
        print("End of re-order list")

    #E
    elif choice == "E" or choice == "e":
        for i in inventory:
            print(i[0],"by",i[1],i[3],"on hand, price $",i[4])# properly prints the text
        total= 0
        for i in inventory:
             total += i[-2]*i[-1] #the total is the price of all copies so multiply the quantity and price to get the correct value
        print(sorted(inventory))
        print("The Total inventory value is $",total)
      
    choice = (input("Welcome to the Simple Bookstore Inventory System. Here’s the list of options:\n\tA- Add books to the inventory.\n\tB- Sell books by ISBN.\n\tC- List all books by a given author.\n\tD- List all books to be re-ordered.\n\tE- List the entire inventory.\n\tX- Exit\nSelect an option by entering its letter:"))

