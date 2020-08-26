import sqlite3

connection = sqlite3.connect("myTable.db")

def add_record():
   print();
   print("ADD EMPLOYEE RECORD")
   print()
   empId = int(input(  "Enter employee id                : "))
   EmpNm =   input(    "Enter employee Name              : ")
   EmpSal = int(input( "Enter employee Salary            : "))
   DoJ = input(        "Enter employee Date of Joining   : ")
   Designation = input("Enter employee Designation       : ")
   print()
   try:
      cursor=connection.cursor()
      sql_command = """CREATE TABLE MyTeam (empId INTEGER PRIMARY KEY, 
                                EmpNm VARCHAR(20), 
                                EmpSal INTEGER, 
                                DoJ DATE, 
                                Designation VARCHAR(20));"""
      sql = ("INSERT INTO MyTeam VALUES (?,?,?,?,?);")
      
          
      try:
            cursor.execute(sql, (empId,EmpNm, EmpSal,DoJ,Designation))
            print("Employee added successfully")
            connection.commit()
      except:
          cursor.execute(sql_command)
          sql_command = """INSERT INTO MyTeam (empId,EmpNm,EmpSal,DoJ,Designation) 
          VALUES
          (101,"Sachin",25000,10-08-2010,'Batsman'),
          (102,'Shewag',20000,12-06-2011,'Batsman'),
          (103,'Dravid',15000,15-10-2012,'Batsman'),
          (104,'Laxman',12000,20-11-2013,'Batsman'),
          (105,'Raina',10000,12-11-2012,'Batsman'),
          (106,'Dhoni',10000,15-10-2014,'Keeper'),
          (107,'Pathan',12000,20-12-2013,'Allrounder'),
          (108,'Kumble',12500, 11-02-2014,'Bowler'),
          (109,'Srinath',9000, 01-02-2012,'Bowler'),
          (110,'Bhajji', 9000,10-02-2013,'Bowler'),
          (111,'Prasad',8000,12-12-2011,'Bowler');"""
          cursor.execute(sql_command)
          connection.commit()
   finally:
      print("") #connection.close()

def select_records():
   try:
      cursor=connection.cursor()
      sql = "SELECT * FROM MyTeam"     
      try:
         cursor.execute(sql)
         result = cursor.fetchall()
         print()
         print("VIEW EMPLOYEE RECORDS")
         print()
         print("ID\t\t NAME\t\tSalary\t\tDate of Joining\t\tDesignation")
         print("---------------------------------------------------------------------------")
         for row in result:
            print(str(str(row[0]) + "\t\t" + str(row[1]) + "\t\t" + str(row[2])+"\t\t" + str(row[3])+"\t\t" + str(row[4])))
#         print(result)
      except:
         print("Unable to fetch records")
      connection.commit()
   finally:
      print("") #connection.close()

def delete_input():
   print();
   print("DELETE EMPLOYEE RECORD")
   print();
   id = input("Enter Employee ID  : ")
   print();
   delete_record(id)

def delete_record(empid):
   try:
      cursor=connection.cursor()
      sql = "DELETE FROM MyTeam WHERE empId = ?"  
      try:
         cursor.execute(sql, (empid,))
         print("Successfully Deleted the Record...")
      except:
         print("Unable to delete record")
      connection.commit()
   finally:
      print("") #connection.close()

def update_input():
   print()
   print("UPDATE EMPLOYEE RECORD")
   print();
   empId = int(input("Enter employee id                : "))
   EmpNm =   input("Enter employee Name                : ")
   EmpSal = int(input("Enter employee Salary               : "))
   DoJ = input("Enter employee Date of Joining               : ")
   Designation = input("Enter employee Designation               : ")
   print();
   update_record(empId,EmpNm, EmpSal,DoJ,Designation)

def update_record(empId,EmpNm, EmpSal,DoJ,Designation):
   try:
      cursor=connection.cursor()
      sql = "UPDATE MyTeam SET `EmpNm`=?, `EmpSal`=? ,`DoJ`=?, `Designation`=? WHERE `empId` = ?"         
      try:
         cursor.execute(sql, (EmpNm, EmpSal, DoJ, Designation, empId))
         print("Successfully Updated the Record...")
      except:
         print("Unable to update record")
      connection.commit()
   finally:
      print("") #connection.close()

def exit_app():
   print()
   print("\tThank you for using this software.")
   print()
   connection.close()

def user_def():
   print()
   cmd=input("\tEnter your query : \t")
   try:
       cursor=connection.cursor()
       cursor.execute(cmd)
   except:
       print("\n Error in enterred querry.")
   print()

def menu_option():
   ch = "0"   
   while ch != "6":
      #tmp = sp.call('cls',shell=True)
      print();
      print("===== EMPLOYEE RECORD SYSTEM =====")
      print();
      print("1. Add Employee Record")
      print("2. Update Employee Record")
      print("3. Show Employee List Record")
      print("4. Delete a Employee Record")
      print("5. User Defined Query")
      print("6. Quit Program ")
      print();
      ch = input("Select option : ")
      menu_selection = {
         "1": add_record,
         "2": update_input,
         "3": select_records,
         "4": delete_input,
         "5": user_def,
         "6": exit_app
      }  
      func = menu_selection.get(ch)
      if func is not None:
         func()
      else:
         print("Invalid option selected")
      print();
      input('PRESS THE ENTER KEY TO CONTINUE ')

menu_option()