
import mysql.connector
import re
def add_user(cur,cnx):
    print("###WELCOME TO ADD USER FUNCTION###")
    while True:
        try:
            permission = int(input("please choose permission type:\n1-> admin\n2->data_entry\n3->guest\n0-> exit\n->"))
            if permission == 1:
                user = str(input("please enter username to add:"))
                ans = (input(f"Are you sure you want to add the user {user} (Y/N) ?")).lower()
                if ans == "y":
                    password = input("please enter password:")
                    ans = (input(f"Are you sure about this password -> {password} (Y/N) ?")).lower()
                    if ans =="y":
                        cur.execute(f"CREATE USER IF NOT EXISTS '{user}'@'localhost' IDENTIFIED BY '{password}'") 
                        cur.execute(f"GRANT ALL PRIVILEGES ON art_museum.* TO '{user}'@'localhost';") 
                        cnx.commit()
                        break
            elif permission == 2:
                user = str(input("please enter username to add:"))
                ans = (input(f"Are you sure you want to add the user {user} (Y/N) ?")).lower()
                if ans == "y":
                    password = input("please enter password:")
                    ans = (input(f"Are you sure about this password -> {password} (Y/N) ?")).lower()
                    if ans =="y":
                        cur.execute(f"CREATE USER IF NOT EXISTS '{user}'@'localhost' IDENTIFIED BY '{password}'") 
                        cur.execute(f"GRANT SELECT, INSERT,ALTER ON art_museum.* TO {user}@'localhost';")
                        cnx.commit()
                        break
            elif permission == 3:
                user = str(input("please enter username to add:"))
                ans = (input(f"Are you sure you want to add the user {user} (Y/N) ?")).lower()
                password = ''
                if ans == "y":
                    cur.execute(f"CREATE USER IF NOT EXISTS '{user}'@'localhost' IDENTIFIED BY '{password}'")
                    cur.execute(f"GRANT SELECT ON art_museum.* TO {user}@'localhost';")
                    cnx.commit()
                    
                    break 
            elif permission == 0:
                break
        except Exception:
            print("invalid, please try to enter valid username and password")
def edit_user(cur,cnx):
    print("###WELCOME TO EDIT USER FUNCTION###")
    while True:
        try:
            inp = int(input("please enter 1 to edit user\nenter 2 to revoke permission\nenter 0 to exit\n->"))
            if inp == 1:
                user = str(input("please enter username to edit:"))
                ans = (input(f"Are you sure you want to edit the user {user} (Y/N) ?")).lower()
                if ans == "y":
                    password = input("please enter the new password:")
                    ans = (input(f"Are you sure about this password -> {password} (Y/N) ?")).lower()
                    if ans =="y":
                        cur.execute(f"ALTER USER IF EXISTS '{user}'@'localhost' IDENTIFIED BY '{password}';'",multi = True) 
                        cnx.commit()
                        break
            if inp == 2:
                user = str(input("please enter username to edit:"))
                ans = (input(f"Are you sure you want to edit the user {user} (Y/N) ?")).lower()
                if ans == "y":
                    cur.execute(f"REVOKE ALL, GRANT OPTION FROM {user}@localhost;")
                    cnx.commit()
                    break
            if inp == 0:
                break
        except Exception:
            print("invalid, please try to enter valid password")
                
            
def print_users_priv(cur,cnx):
    admin_query("select host, user from mysql.user;",cur,cnx)
    admin_query("SHOW GRANTS;",cur,cnx)
    tables = cur.fetchall()
    print(tables)
def print_user(cur,cnx):
    inp = input("please enter username you want to view privallage ->")
    cur.execute(f"SHOW GRANTS FOR '{inp}'@'localhost';")
    cnx.commit()
    tables = cur.fetchall()
    print(tables)
def block_users(cur,cnx):
    print("###WELCOME TO BLOCK USER FUNCTION###")
    while True:
        try:
            inp = int(input("please enter 1 to block user\nenter 0 to exit\n->"))
            if inp == 1:
                user = str(input("please enter username to edit:"))
                ans = (input(f"Are you sure you want to edit the user {user} (Y/N) ?")).lower()
                if ans == "y":
                    cur.execute(f"ALTER USER IF EXISTS {user}@localhost ACCOUNT LOCK;")
                    cur.execute(f"SELECT user, host, account_locked FROM mysql.user WHERE user = '{user}' AND host='localhost'")
                    tables = cur.fetchall()
                    print(tables)
                    cnx.commit()
            if inp == 0:
                break
        except Exception:
            print("invalid, please try to block the user again")
def admin_query(command,cur, cnx):
    '''
    This is a function for letting an admin run a query.
    Admin enters their query exactly as they would in a command prompt all as a single line. There are no restrictions on query input. Then, the function outputs the 
    results of their query with no formatting.
    '''
    cur.execute(command)
    cnx.commit()
    tables = cur.fetchall()
    print(tables)
def executeScriptsFromFile(filename,cur,cnx):
    fd = open(f"{filename}", 'r')
    sqlFile = fd.read() 
    fd.close()
    sqlCommands = sqlFile.split(';')
    for command in sqlCommands:
        try:
            admin_query(command,cur,cnx) 
        except Exception:
            print("command skipped!")       
def end_user(cnx,cur):
    browse_data(cnx,cur)
def admin(cur,cnx):
    while True:
        try:
            print("--please enter 1 to enter your sql query--")
            print("--please enter 2 to run sql through sql script filename and path--")
            print("--please enter 3 to add users--")
            print("--please enter 4 to edit users--")
            print("--please enter 5 to block users--")
            print("--please enter 6 to modify database--")
            print("--please enter 7 to print all the users and their privallages--")
            print("--please enter 8 to print a user and it's privallages--")
            print("--please enter 0 to exit--")
            select = int(input("\nYour input->"))
            if select == 1:
                command = input("Enter your query: ")
                admin_query(command,cur,cnx)
            if select == 2:
                file_path = input("please enter file name and path here ->")
                executeScriptsFromFile(file_path,cur,cnx)
            if select == 3:
                add_user(cur,cnx)
            if select == 4:
                edit_user(cur,cnx)
            if select == 5:
                block_users(cur,cnx)
            if select == 6:
                data_entry(cnx,cur)
            if select == 7:
                print_users_priv(cur,cnx)
            if select == 8:
                print_user(cur,cnx)
            if select == 0:
                print("Bye <3")
                exit()
        except Exception:
            print("please try again")
        
def data_entry(cnx,cur):
    while True:
        try:
            selection = menu()
            if selection == 1:
                insert_data(cnx,cur)
            if selection == 2:
                delete_data(cnx,cur)
            if selection == 3:
                update_data(cnx,cur)
            if selection == 4:
                browse_data(cnx,cur)
            if selection == 5:
                print("Bye <3")
                exit()
        except ValueError:
            print("please make sure you enter a number!")
        
def login_credentials():    # asks the user for the connection type
    Selection = input("Please enter 1, 2 or 3 to select your role: ")
    if Selection in ["1","2"]:
        username = input("username: ")
        password = input("password: ")
    else:
        username = input("username: ")
        password = None
    return username, password, Selection
def menu():     # prints menu for the user to manipulate the table
    print("\n1} INSERT")
    print("2} DELETE")
    print("3} UPDATE")
    print("4} BROWSE DATABASE")
    print("5} EXIT PROGRAM")
    selection = int(input("Please enter a menu option number: "))
    return selection

def executor(a,b,cur,cnx):
    cur.execute(a,b)
    cnx.commit()

def get_columns(table_name,cnx,cur):
    '''
    Returns a list of the columns for the inputted table.

        Parameters:
                table_name (str): The name of the table to get the list of column names.
                cnx: mysql connector
                cur: mysql cursor
        Returns:
                columns (list): A list of each column name for the specified table.
    '''

    query = """select `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='art_museum' AND `TABLE_NAME`= %s ORDER BY ORDINAL_POSITION"""
    cur.execute(query, (table_name,))

    columns = cur.fetchall()

    for i in range(0, len(columns)):
        columns[i] = re.sub(r'\W+', '', str(columns[i]))
        i+=1

    return(columns)

def insert_data(cnx,cur):

    user_input = input("Insert data into Art Object (1), Artist (2), Exhibiton (3), or Collection (4)? ")
    while True:
        try:
            if (user_input == '1'):
                
                table_name = "art_object"
                table_columns = get_columns(table_name,cnx,cur) #Retrieves a list of the columns for the art_object table via the get_columns function

                child_table = input("Is this Art object a Statue, Sculpture, Painting or Other? ").lower()
                child_table_columns = get_columns(child_table,cnx,cur) #Retrieves a list of the columns for the child table (Statue, painting etc..) via the get_columns function
                
                user_values = [] #Create empty list to use for inserting values
                for i in range(0, len(table_columns)): #For loop used to populate list with user values. EG. "Enter <id_no> for Statue Art object: (user_input)"
                    if(i == 0 or i == 2): #If primary key then can't be or none
                        user_values.append(input("Enter <" + table_columns[i].replace("_", " ").capitalize() + "> for " + child_table.capitalize() + " " + table_name.replace("_", " ").capitalize() + ": "))
                    else:
                        user_values.append(input("Enter <" + table_columns[i].replace("_", " ").capitalize() + "> for " + child_table.capitalize() + " " + table_name.replace("_", " ").capitalize() + ": ")) or None
                art_obj_id = user_values[0] #Saves the id_no for later
                user_child_table_values = [] #Create empty list for child table values
                user_child_table_values.append(art_obj_id) #Add the id_no to child table values so don't have to ask user to input it again
                

                for i in range(1, len(child_table_columns)): #Populates the list of child table values similar to before.
                    user_child_table_values.append(input("Enter <" + child_table_columns[i].replace("_", " ").capitalize() + "> for " + child_table.capitalize() + " " + table_name.replace("_", " ").capitalize() + ": "))

                placeholders = ', '.join(['%s'] * len(table_columns)) #Creates string based on how many columns there are. Eg. 3 columns would be: '%s, %s, %s'
                query = (f'INSERT INTO {table_name} VALUES ({placeholders})') #Query template for insert
                if user_values[7] == '':                                            #
                    placeholders = ','.join(['%s'] * (len(table_columns)-1))        ##
                    placeholders +=',Null'                                          ### All this to replace '' with Null for exhibition name if it is unknown / none.
                    user_values.pop(7)                                              ##
                    query = (f'INSERT INTO {table_name} VALUES ({placeholders})')   #

                cur.execute(query, user_values) #Executes the insert command for art_object table
                cnx.commit()

                for i in range(1,len(table_columns)-1): #Replaces all '' values with Null to be more consistant Since Null(Unknow) != ''(empty)
                    if i != 2:
                        cur.execute("UPDATE " + table_name + " SET " + table_columns[i] + " = Null WHERE " + table_columns[i] + " =''")
                        cnx.commit()

                placeholders = ', '.join(['%s'] * len(child_table_columns)) #Creates string based on how many columns there are. Eg. 3 columns would be: '%s, %s, %s
                query = (f'INSERT INTO {child_table} VALUES ({placeholders})') #Query template for insert into child table
                cur.execute(query, user_child_table_values) #Executes the insert command for art_object table
                cnx.commit()

                which_collection = input("Is this Art object part of the (1) permanent or a (2) borrowed collection?") #Next step is to determine if the art_object is part of permanent collection or borrowed from another collection..
                if (which_collection == '1'): #Permanent collection
                    table_name = "permanent_collection"
                    table_columns = get_columns(table_name,cnx,cur)

                    user_values = [] #Another empty list to store user values
                    user_values.append(art_obj_id) #Add obj id_no from before
                    for i in range(1,len(table_columns)): #Populate list with user values
                        user_values.append(input("Enter <" + table_columns[i].replace("_", " ").capitalize() + "> for " + table_name.replace("_", " ").capitalize() + ": "))

                    placeholders = ', '.join(['%s'] * len(table_columns))  #Creates string based on how many columns there are. Eg. 3 columns would be: '%s, %s, %s
                    query = (f'INSERT INTO {table_name} VALUES ({placeholders})') #Query template for this table
            
                    cur.execute(query, user_values) #Execute
                    cnx.commit()

                elif (which_collection == '2'): #Borrowed from a collection <><>Most of the following code is similar so no need for comments<><>
                    table_name = "borrowed"
                    table_columns = get_columns(table_name,cnx,cur)

                    user_values = []
                    user_values.append(art_obj_id)
                    for i in range(1,len(table_columns)):
                        user_values.append(input("Enter <" + table_columns[i].replace("_", " ").capitalize() + "> for " + table_name.replace("_", " ").capitalize() + ": "))

                    placeholders = ', '.join(['%s'] * len(table_columns))
                    query = (f'INSERT INTO {table_name} VALUES ({placeholders})')
            
                    cur.execute(query, user_values)
                    cnx.commit()

                    collection_borrowed_from = input("Enter the collection this Art object was borrowed from: ")
                    table_name = "borrowed_from"
                    table_columns = get_columns(table_name,cnx,cur)

                    values = [art_obj_id,collection_borrowed_from]

                    placeholders = ', '.join(['%s'] * len(table_columns))
                    query = (f'INSERT INTO {table_name} VALUES ({placeholders})')

                    cur.execute(query, values)
                    cnx.commit()

            elif (user_input == '2'):
                table_name = "artist"
                table_columns = get_columns(table_name,cnx,cur)

                user_values = []
                for i in range(0, len(table_columns)):
                    if(i == 0):
                        user_values.append(input("Enter <" + table_columns[i].replace("_", " ").capitalize() + "> for " + table_name.replace("_", " ").capitalize() + ": "))
                    else:
                        user_values.append(input("Enter <" + table_columns[i].replace("_", " ").capitalize() + "> for " + table_name.replace("_", " ").capitalize() + ": ")) or None
                
                placeholders = ', '.join(['%s'] * len(table_columns))
                query = (f'INSERT INTO {table_name} VALUES ({placeholders})')
            
                cur.execute(query, user_values)
                cnx.commit()

                for i in range(1,len(table_columns)):
                    cur.execute("UPDATE " + table_name + " SET " + table_columns[i] + " = Null WHERE " + table_columns[i] + " =''")
                    cnx.commit()
            
            elif (user_input == '3'):
                table_name = "exhibition"
                table_columns = get_columns(table_name,cnx,cur)

                user_values = []
                for i in range(0, len(table_columns)):
                    user_values.append(input("Enter <" + table_columns[i].replace("_", " ").capitalize() + "> for " + table_name.replace("_", " ").capitalize() + ": "))   

                placeholders = ', '.join(['%s'] * len(table_columns))
                query = (f'INSERT INTO {table_name} VALUES ({placeholders})')
            
                cur.execute(query, user_values)
                cnx.commit()

            elif (user_input == '4'):
                table_name = "collection"
                table_columns = get_columns(table_name,cnx,cur)

                user_values = []
                for i in range(0, len(table_columns)):
                    user_values.append(input("Enter <" + table_columns[i].replace("_", " ").capitalize() + "> for " + table_name.replace("_", " ").capitalize() + ": "))   

                placeholders = ', '.join(['%s'] * len(table_columns))
                query = (f'INSERT INTO {table_name} VALUES ({placeholders})')
            
                cur.execute(query, user_values)
                cnx.commit()
            
            else:
                print("Invalid Input")
                insert_data(cnx,cur)
        
        except Exception:
            print("There was an error with at least one of your entered values. Please double check your input and try again.")
            continue
        else:
            return

def delete_data(cnx,cur):
    user_input = input("Would you like to delete data from Art object (1), Artist (2), Exhibiton (3) or Collection (4)? ")

    if (user_input == '1'):
        while True:
            try:
                user_delete_input = input("Enter the Id_no of the Art Object you would like to delete: ")

                cur.execute("SELECT id_no FROM art_object")
                id_no_in_art_object = cur.fetchall()
                for i in range(0, len(id_no_in_art_object)):
                    id_no_in_art_object[i] = re.sub(r'\W+', '', str(id_no_in_art_object[i]))
                    i+=1

                cur.execute("SELECT id_no FROM borrowed")
                id_no_in_borrowed = cur.fetchall()
                for i in range(0, len(id_no_in_borrowed)):
                    id_no_in_borrowed[i] = re.sub(r'\W+', '', str(id_no_in_borrowed[i]))
                    i+=1

                cur.execute("SELECT id_no FROM borrowed_from")
                id_no_in_borrowed_from = cur.fetchall()
                for i in range(0, len(id_no_in_borrowed_from)):
                    id_no_in_borrowed_from[i] = re.sub(r'\W+', '', str(id_no_in_borrowed_from[i]))
                    i+=1

                if(user_delete_input in id_no_in_borrowed_from):
                    cur.execute(f"DELETE FROM borrowed_from WHERE id_no = " + user_delete_input)
                    cnx.commit()
                if(user_delete_input in id_no_in_borrowed):
                    cur.execute(f"DELETE FROM borrowed WHERE id_no = " + user_delete_input)
                    cnx.commit()
                if(user_delete_input in id_no_in_art_object):
                    cur.execute(f"DELETE FROM art_object WHERE id_no = " + user_delete_input)
                    cnx.commit()
            except Exception:
                print("There was an error with your input. Please double check and try again.")
                continue
            else:
                return

    elif(user_input == '2'):
        while True:
            try:
                user_delete_input = input("Enter the name of the Artist you would like to delete: ")
                cur.execute(f"DELETE FROM artist WHERE artist_name = '{user_delete_input}'")
            except Exception:
                print("There was an error with your input, please try again.")
                continue
            else:
                return

    elif(user_input == '3'):
        while True:
            try:
                user_delete_input = input("Enter the name of the Exhibition you would like to delete: ")
                cur.execute(f"DELETE FROM exhibition WHERE exhibition_name = '{user_delete_input}'")
            except Exception:
                print("There was an error with your input, please try again.")
                continue
            else:
                return

    elif(user_input == '4'):
        while True:
            try:
                user_delete_input = input("Enter the name of the Collection you would like to delete: ")
                cur.execute(f"DELETE FROM collection WHERE collection_name = '{user_delete_input}'")
            except Exception:
                print("There was an error with your input, please try again.")
                continue
            else:
                return   
    else:
        print("Invalid input.")
        delete_data(cnx,cur)
def update_data(cnx,cur):
    user_input = input("Would you like to update data in Art object (1), Artist (2), Exhibiton (3) or Collection (4)? ")
    
    if (user_input == '1'):
        while True:
            try:
                id_no = str(input("Enter the Id_no of the Art Object you would like to update: "))
                create_num = input("Enter the year the Art Object was created: ")
                title = str(input("Enter the title of the Art Object: "))
                description = str(input("Enter a description for the Art Object: "))
                cname = str(input("Enter the Country name or culture of origin for the Art Object: "))
                epoch = str(input("Enter the epoch of the Art Object: "))
                artist = str(input("Enter the full name of the Artist who made this Art Object: "))
                ex = str(input("Enter the exhibition name of the Art Object (press enter and leave blank if unknown): ")) or None
                update_template = "update art_object set year_of_creation=%s, object_title=%s, object_description=%s, country_or_culture_of_origin=%s, epoch=%s, artist_name=%s, exhibition=%s where id_no=%s"
                update_art_object = (create_num,title,description,cname,epoch,artist,ex,id_no)
                executor(update_template,update_art_object,cur,cnx)
            except Exception:
                print("There was an error with your input. Please double check and try again.")
                continue
            else:
                while True:
                    try:
                        art_table1 = str(input("Is this Art object a Statue, Sculpture, Painting or Other? ")).lower()
                        if (art_table1 == ('statue' or 'sculpture')):
                            weight = str(input("Enter the weight of the Art Object: "))
                            height = str(input("Enter the height of the Art Object: "))
                            material = str(input("Enter the material of the Art Object: "))
                            style = str(input("Enter the style of the Art Object: "))
                            if (art_table1 == 'statue'):
                                update_template = "update statue set weight=%s, height=%s, material=%s, style=%s where id_no=%s"
                            elif (art_table1 == 'sculpture'):
                                update_template = "update sculpture set weight=%s, height=%s, material=%s, style=%s where id_no=%s"
                                update_st_sc = (weight,height,material,style,id_no)
                            executor(update_template,update_st_sc,cur,cnx)
                        if (art_table1 == 'painting'):
                            style = str(input("Enter the style of the Painting Art Object: "))
                            paint_type = str(input("Enter the paint type of the Painting Art Object: "))
                            drawn_on = str(input("Enter what the Painting was drawn on: "))
                            update_template = "update painting set style=%s, paint_type=%s, drawn_on=%s where id_no=%s"
                            update_painting = (style,paint_type,drawn_on,id_no)
                            executor(update_template,update_painting,cur,cnx)
                        if (art_table1 == 'other'):
                            type = str(input("Enter the type of Other Art Object: "))
                            style = str(input("Enter the style of the Other Art Object: "))
                            update_template = "update other set type_of_other=%s, style=%s where id_no=%s"
                            update_other = (type,style,id_no)
                            executor(update_template,update_other,cur,cnx)
                    except Exception:
                        print("There was an error with your input. Please double check and try again.")
                        continue
                    else:
                        while True:
                            try:
                                category = input("Is this Art object part of the (1) permanent or a (2) borrowed collection? ")
                                if(category == '1'):
                                    date = str(input("Enter the date the Art Object was aquired: "))
                                    status = str(input("Enter the Art Object's status: "))
                                    cost = str(input("Enter the cost of the Art Object: "))
                                    update_template = "update permanent_collection set date_aquired=%s, object_status=%s, cost=%s where id_no=%s"
                                    update_perm_collection = (date,status,cost,id_no)
                                    executor(update_template,update_perm_collection,cur,cnx)
                                if(category == '2'):
                                    bdate = str(input("Enter the date the Art Object was borrowed: "))
                                    rdate = str(input("Enter the date the Art Object was returned: "))
                                    update_template = "update borrowed set date_borrowed=%s, date_returned=%s where id_no=%s"
                                    update_borrowed = (bdate,rdate,id_no)
                                    executor(update_template,update_borrowed,cur,cnx)
                                    bfrom = str(input("Enter the collection this Art Object was borrowed from: "))
                                    update_template = "update borrowed_from set borrowed_from=%s where id_no=%s"
                                    update_bfrom = (bfrom,id_no)
                                    executor(update_template,update_bfrom,cur,cnx)
                            except Exception:
                                print("There was an error with your input. Please double check and try again.")
                                continue
                            else:
                                return                  

    elif (user_input == '2'):
        while True:
            try:
                artist = input("Enter the full name of the Artist you would like to update: ")
                bdate = str(input("Enter the date the Artist was born (press enter and leave blank if unknown): "))
                ddate = str(input("Enter the date the Artist died (press enter and leave blank if unknown): "))
                epoch = str(input("Enter the epoch of the Artist: "))
                style = str(input("Enter the main style of the Artist: "))
                description = str(input("Enter a description for the Artist: "))
                update_template = "update artist set date_born=%s, date_died=%s, epoch=%s, main_style=%s, artist_description=%s where artist_name=%s"
                update_artist = (bdate,ddate,epoch,style,description,artist)
                executor(update_template,update_artist,cur,cnx)
            except Exception:
                print("There was an error with your input. Please double check and try again.")
                continue
            else:
                return

    elif (user_input == '3'):
        while True:
            try:
                ex = input("Enter the name of the Exhibition you would like to update: ")
                sdate = str(input("Enter the Exhibition start date: "))
                edate = str(input("Enter the Exhibition end date: "))
                update_template = "update exhibition set start_date=%s, end_date=%s where exhibition_name=%s"
                update_ex = (sdate,edate,ex)
                executor(update_template,update_ex,cur,cnx)
            except Exception:
                print("There was an error with your input. Please double check and try again.")
                continue
            else:
                return

    elif (user_input == '4'):
        while True:
            try:
                collection = input("Enter the name of the Collection you would like to update: ")
                type = str(input("Enter the Collection type: "))
                description = str(input("Enter a description for the Collection: "))
                address = str(input("Enter the address of the Collection: "))
                phone = str(input("Enter the phone number for the Collection: "))
                contact = str(input("Enter the contact person for the Collection: "))
                update_template = "update collection set collection_type=%s, collection_description=%s, address=%s, phone=%s, contact_person=%s where collection_name=%s"
                update_collection = (type,description,address,phone,contact,collection)
                executor(update_template,update_collection,cur,cnx)
            except Exception:
                print("There was an error with your input. Please double check and try again.")
                continue
            else:
                return    
    else:
        print("Invalid input.")
        update_data(cnx,cur)

def b_menu():     # prints menu for the guest user to browse the database
    print("\n1} ART OBJECT")
    print("2} ARTIST")
    print("3} OUR BORROWED COLLECTION")
    print("4} OUR PERMANENT COLLECTION")
    print("5} EXIT PROGRAM")
    b_select = input("Please enter the corresponding number of the data you would like to view: ")
    print()
    return b_select

def create_view(statement,num,cur):
    cur.execute(statement)
    col_names = cur.column_names
    search_result = cur.fetchall()
    header_size=len(col_names)
    print()
    for i in range(header_size):
        print("{:<70s}".format(col_names[i]),end="")
    print()
    print(num*header_size*'-')
    for row in search_result:
        for val in row:
            print("{:<70s}".format(str(val)), end="")
        print() 

def browse_data(cnx,cur):
    b_select = b_menu()

    if b_select == '1':
        while True:
            try:
                statement = ("select id_no, object_title, epoch from art_object")
                num = 55
                create_view(statement,num,cur)
                print("Data for the art pieces at the muesuem is shown above. Below are specific types of art objects.")
                while True:
                    try:
                        print("\n1} PAINTINGS ")
                        print("2} SCULPTURES")  
                        print("3} STATUES")
                        print("4} OTHER TYPES")
                        print("5} BACK TO MAIN BROWSING MENU")
                        o_select = input("Please enter your menu option number: ")
                        if o_select == '1':
                            statement = ("select id_no, style, paint_type from painting")
                            num = 55
                            create_view(statement,num,cur)          
                        if o_select == '2':
                            statement = ("select id_no, material, style from sculpture")
                            num = 55
                            create_view(statement,num,cur)  
                        if o_select == '3':
                            statement = ("select id_no, material, style from statue")
                            num = 55
                            create_view(statement,num,cur)  
                        if o_select == '4':                                
                            statement = ("select* from other")
                            num = 50
                            create_view(statement,num,cur)  
                        if o_select == '5': 
                            print()                               
                            browse_data(cnx,cur)
                    except Exception:
                        print("There was an error with your input. Please double check and try again.")
                        continue
            except Exception:
                print("There was an error with your input. Please double check and try again.")
                continue
    if b_select == '2':
        while True:
            try:
                statement = ("select artist_name, epoch, main_style from artist")
                num = 55
                create_view(statement,num,cur)
                print("Data for the artists is shown above. If you would like to see art objects for an artist select 1 below.")
                while True:
                    try:
                        print("\n1} ART OBJECTS OF SPECIFIC ARTIST")
                        print("2} BACK TO MAIN BROWSING MENU")
                        o_select = input("Please enter your menu option number: ")
                        if o_select == '1':
                            artist = str(input("Enter an artist name: "))
                            statement = ("select id_no, object_title, epoch from art_object where artist_name='") + artist + "'"
                            num = 55
                            print(f"\nArt Objects for {artist}:")
                            create_view(statement,num,cur)          
                        if o_select == '2': 
                            print()                               
                            browse_data(cnx,cur)
                    except Exception:
                        print("There was an error with your input. Please double check and try again.")
                        continue
            except Exception:
                print("There was an error with your input. Please double check and try again.")
                continue
    if b_select == '3':
        while True:
            try:
                statement = ("select* from borrowed")
                num = 55
                create_view(statement,num,cur)
                print("Data for the borrowed collection is shown above. If you would like to see where an art object is borrowed from select 1 below.")
                while True:
                    try:
                        print("\n1} ART OBJECTS BORROWED FROM")
                        print("2} BACK TO MAIN BROWSING MENU")
                        o_select = input("Please enter your menu option number: ")
                        if o_select == '1':
                            id_no = str(input("Enter an Id_no of a borrowed art object: "))
                            statement = ("select* from borrowed_from where id_no='") + id_no + "'"
                            num = 55
                            print(f"\nArt Object {id_no} borrowed from:")
                            create_view(statement,num,cur)          
                        if o_select == '2': 
                            print()                               
                            browse_data(cnx,cur)
                    except Exception:
                        print("There was an error with your input. Please double check and try again.")
                        continue
            except Exception:
                print("There was an error with your input. Please double check and try again.")
                continue
    if b_select == '4':
        while True:
            try:
                statement = ("select id_no, date_aquired, object_status from permanent_collection")
                num = 55
                create_view(statement,num,cur)
                print("Data for the permanent collection is shown above.")
            except Exception:
                print("There was an error with your input. Please double check and try again.")
                continue
            else:
                browse_data(cnx,cur)
    if b_select == '5':
        print("Bye <3")
        exit()
    else:
        print("Invalid input.")
        browse_data(cnx,cur)

def main():
    print("###WELCOME TO OUR ART MUSEUM DATABASE!###\n")
    print("Please choose the type of credential to log in:\n")
    print("1) DB Admin\n")
    print("2) Data Entry\n")
    print("3) Guest\n")

    username, password , Select= login_credentials()
    cnx = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = username,
    password = password)
    cur = cnx.cursor(buffered=True)
    cur.execute("use art_museum")
    if Select == "1":
        admin(cur,cnx)
    if Select == "2":
        data_entry(cnx,cur)
    if Select == "3":
        end_user(cnx,cur)
if __name__ == "__main__":
  main()
