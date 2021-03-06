try:
    class Cinema:

        global nr_of_tickets
        nr_of_tickets = []

        def __init__(self):

            print("------------Welcome to  MRUNAl's Cinema--------------")
            print("Hi, Before we begin, please define the size of the cinema!")
            self.rows = 0
            self.columns = 0
            a = True
            
            while(a):
                self.rows = input("Enter the number of rows: ")
                self.columns = input("Enter the number of seats in each row: ")
            
                if (self.rows  == '08') or (self.columns == '08'):
                    print("Please don't enter zero rows or columns!")

                elif self.rows.isdigit() == False or self.columns.isdigit() == False:
                    print("Please Enter Integer values only!")
                
                else:
                    a = False
                
            self.rows = int(self.rows)
            self.columns = int(self.columns)
            print("")
            
            self.row_nr = []
            self.column_nr = []
            self.current_income = 0
            self.total_income = 0
            self.menu()
            self.details_list = []

        #We will keep calling this method in the main file until 0 is entered
        def menu(self):
            try:
                print("\n\nChoose one of the following options: ")
                print("1. Show the seats")
                print("2. Buy a ticket")
                print("3. Statistics")
                print("4. Show booked tickets user info")
                print("0. Exit")
                self.choice = int(input())
            except:
                print("Must have entered wrong value!")

        #This method will be called whenever we need to display the seats(we'll mostly use this in other methods)
        # Ive used this protected method as it does the job of showing vacant seats as well as pre booked scenes, this
        # helps save us time in the rest of the program
        def _seat_matrix(self):
            print("\tMRUNAL's Cinema: \n")
            print('   ' + '  '.join(map(str,list(range(1,self.columns+1)))))
            print()
            for i in range(0, self.rows):
                    print(i+1, end = ' ')
                    for j in range(self.columns):
                        if ((i+1,j+1) in list(zip(self.row_nr,self.column_nr))):
                            print(" B ", end = '')
                        else:
                            print(" S ", end = '')
                    print("\n")
            print("-----------SCREEN THIS SIDE-----------")

        
        #this is the protected function which books the tickets for the user
        #nr_of_tickets is a list, in order to use recursion if ticket details which have been entered, already exist
        def _book_tickets(self, nr_of_tickets): 
            try:
                for i in nr_of_tickets: 
                          
                    
                    row = input("Please enter row number for Ticket No." + str(i) + ": ")
                    column = input("Please enter column number for Ticket No." + str(i) + ": ")
                    x = True
                    while x:
                        if (row.isdigit() == False or column.isdigit() == False):
                            print("Please enter integer values only!")
                            row = input("Please enter row number for Ticket No." + str(i) + ": ")
                            column = input("Please enter column number for Ticket No." + str(i) + ": ")
                        # Here we are checking to make sure enter row number is b/w 1 and the max rows of the cinema and same 
                    	# for column

                        elif (int(row) > self.rows) or (int(row) < 1):
                            print("Row number does not exist!")
                            row = input("Please enter a row number between {} and {}: ".format(1, self.rows))

                        elif (int(column) > self.columns) or (int(column) < 1):
                            print("Column number does not exist!")
                            column = input("Please enter a column number between {} and {}: ".format(1, self.columns))
                        else:
                            x = False
                            
                    row = int(row)
                    column = int(column)

                    #check if the entered row and column already exist, if yes then call the function again!
                    if (row, column) in list(zip(self.row_nr, self.column_nr)):         
                        print("Seems like this ticket is already booked!Please try again!")
                        self._book_tickets([i])
                    else:
                        print("Price for ticket no {} is: ${}".format(i, self.ticket_price(row)))
                        if (input("Please enter 'Y' if you would like to proceed to book the ticket!") in ['Y','y']):
                            self.row_nr.append(row)
                            self.column_nr.append(column) 
                            print("Great! Please enter your details for the ticket no. ", i)
                            self._get_details()
                            print("Ticket No. {} has been booked!".format(str(i)))
                            print("-"*15)
                        else:
                            print("Thanks for visiting!")

            except:
                print("Please try again as an incorrect value has been entered!")



        # This method will take the details while booking the tickets
        #We can change the function a bit to make it show an actual ticket! That would be pretty cool!
        def _get_details(self):
            details = {}
            for i in ["Name", "Gender", "Age", "Phone Number"]:
                details[i] = input("Please enter your {}: ".format(i))

            for i in range(len(self.row_nr)):
                details["Row Number"] =self.row_nr[i]
                details["Column Number"] =self.column_nr[i]
                details["Ticket Price"] = "$" + str(self.ticket_price(self.row_nr[i]))

            
            self.details_list.append(details)

            print("Please check the details of your tickets!")
            for i,j in details.items():
                print("{}: {}".format(i,j))

        
             #returns the ticket price based on the rules set of the cinema
        def ticket_price(self, row_nr):
            if (self.columns * self.rows) < 60:
                return 10
            else:
                if (self.rows%2 != 0) and (row_nr <= self.rows//2):
                    return 10
                elif (self.rows % 2 != 0) and (row_nr > self.rows//2):
                    return 8
                elif (self.rows % 2 == 0) and (row_nr <= self.rows//2):
                    return 10
                elif (self.rows % 2 == 0) and (row_nr > self.rows//2):
                    return 8

        def _total_income(self):
            if (self.rows*self.columns) < 60:
                return self.rows*self.columns*10
            else:
                return (self.columns)*((self.rows-self.rows//2)*8 + ((self.rows//2)*10))
            
        # Method which will display the seat matrix
        def ShowSeats(self):      
            try:
                if len(self.row_nr) > 0:
                    print("Seems like you've already purchased some tickets! We'll show you the booked seats as well!\n\n")
                    self._seat_matrix()           
                else:
                    print("\n\n\n")
                    self._seat_matrix()
            except ValueError:
                print("You have to enter an integer value!")    
            
        def Tickets(self):   
            try:
                
                nr_of_tickets = [i+1 for i in range(int(input("Okay Great! How many tickets would you like to book?")))]
                if len(nr_of_tickets) > (self.columns * self.rows):
                	print("There aren't those many seats in the cinema!")
                	raise Exception()

                print("Awesome! Please enter the row and column numbers for {} tickets below!".format(max(nr_of_tickets)))

                self._book_tickets(nr_of_tickets)
                print("Your tickets are booked successfully!")
                print("-"*15)
                                  
                self._seat_matrix()
            except ValueError:
                print("Please enter a valid integer value between 1 and {} seats!".format(self.rows*self.columns))

        def Statistics(self):
            try:
                perc_of_tickets = round((len(self.row_nr)*100/(self.columns * self.rows)),2)

                for i in self.row_nr:
                    self.current_income += self.ticket_price(i)

                print("Number of purchased tickets: ",len(self.row_nr))
                print("Percentage of tickets booked: {}%".format(str(perc_of_tickets)))
                print("Current Income is: $", self.current_income)
                print("Total Income: $", self._total_income())
                print("-"*15)
            except ZeroDivisionError:
                print("\n\nSeems like you've not yet defined the theater and seats!")

        def User_info(self):
            try:
                if len(self.details_list) > 0:
                    
                    print("Okay great please enter the row and column number below, and we will fetch your details!\n\n")
                    row = int(input("Please enter Row Number: "))
                    column = int(input("Please enter Column Number: "))

                    for i in self.details_list:
                        if (i["Row Number"] == row) and (i["Column Number"] == column):
                            print("Great we have found your seats! Here are your details!")
                            for (j,k) in i.items():
                                print("{}: {}".format(j,k))
                            break
                        else:
                            continue
                    else:
                        print("Seems like you haven't booked these tickets!")
                else:
                    print("It seems no tickets have been booked yet!")
            except ValueError:
                print("Please enter a valid integer value!")
except:
    print("I'm sorry, something seems to be wrong!")
    
try:
    obj = Cinema()

    while obj.choice != 0:
        if obj.choice == 1:
            obj.ShowSeats()
            obj.menu() 
        elif obj.choice == 2:
            obj.Tickets()
            obj.menu()
        elif obj.choice == 3:
            obj.Statistics()
            obj.menu()
        elif obj.choice == 4:
            obj.User_info()
            obj.menu()
        else:
            raise Exception()
except:
    print("Please make sure you've entered a correct option!")
    obj.menu()
    