import sqlite3
import subprocess as sp


class Database():

    conn = sqlite3.connect('stdb.sqlite3')
    cursor = conn.cursor()

    def create_table(self):

        query = '''
			CREATE TABLE IF NOT EXISTS student(
				id INTEGER PRIMARY KEY, 
				roll INTEGER, 
				name TEXT,
				phone TEXT,
				address TEXT
			)
		'''
        self.cursor.execute(query)
        self.conn.commit()


    def add_student(self, roll, name, phone, address):

        query = '''
			INSERT INTO student( roll, name, phone, address )
						VALUES ( ?,?,?,? )
		'''

        self.cursor.execute(query, (roll, name, phone, address))

        self.conn.commit()
        

    def get_students(self):
        

        query = '''
			SELECT roll, name, phone, address
			FROM student
		'''

        self.cursor.execute(query)
        all_rows = self.cursor.fetchall()

        self.conn.commit()
        

        return all_rows




    def get_student_by_roll(self, roll):
        

        query = '''
			SELECT roll, name, phone, address
			FROM student
			WHERE roll = {}
		'''.format(roll)

        self.cursor.execute(query)
        all_rows = self.cursor.fetchall()

        self.conn.commit()
        

        return all_rows

    def update_student(self, roll, name, phone, address):
        

        query = '''
			UPDATE student
			SET name = ?, phone = ?, address = ?
			WHERE roll = ?
		'''

        self.cursor.execute(query, (name, phone, address, roll))

        self.conn.commit()
        

    def delete_student(self, roll):
        

        query = '''
			DELETE
			FROM student
			WHERE roll = {}
		'''.format(roll)

        self.cursor.execute(query)
        all_rows = self.cursor.fetchall()

        self.conn.commit()
        

        return all_rows

class Division(Database):


    def get_students_of_Rangpur(self):


            query = '''
                SELECT roll, name, phone, address
                FROM student
                WHERE address LIKE "Din%"
                OR address LIKE "Kuri%"
                OR address LIKE "Pan%"
                OR address LIKE "Thak%"
                OR address LIKE "Ran%"
                OR address LIKE "Nil%"
                OR address LIKE "Lal%"
                OR address LIKE "Gai%"
            '''

            self.cursor.execute(query)
            all_rows = self.cursor.fetchall()

            self.conn.commit()


            return all_rows

    def get_students_of_Rajshahi(self):


            query = '''
                SELECT roll, name, phone, address
                FROM student
                WHERE address LIKE "Raj%"
                OR address LIKE "Bog%"
                OR address LIKE "Chap%"
                OR address LIKE "Nao%"
                OR address LIKE "Pab%"
                OR address LIKE "Joy%"
                OR address LIKE "Sira%"
                OR address LIKE "Nat%"
            '''

            self.cursor.execute(query)
            all_rows = self.cursor.fetchall()

            self.conn.commit()


            return all_rows

class Operator(Database):

    def get_students_of_GP_User(self):
         query = '''
                SELECT roll, name, phone, address
                FROM student
                WHERE phone LIKE "017%"
         '''

         self.cursor.execute(query)
         all_rows = self.cursor.fetchall()

         self.conn.commit()


         return all_rows



    def get_students_of_Robi_User(self):

        query = '''
                SELECT roll, name, phone, address
                FROM student
                WHERE phone LIKE "018%"
        '''

        self.cursor.execute(query)
        all_rows = self.cursor.fetchall()

        self.conn.commit()

        return all_rows




class MainClass(Division,Operator):

    def __init__(self):

        self.create_table()

        while self.select():
            pass

    def __del__(self):

        self.conn.close()
        print("\n>>> Good Bye <<<")


    def add_data(self, id_, name, phone, address):
        self.add_student(id_, name, phone, address)
        print("\nThe student has been added.\n")

    def get_data(self):
        return self.get_students()

    def show_data(self):
        students = self.get_data()
        for student in students:
            print(student)

    def show_data_of_Rangpur(self):
        students = self.get_students_of_Rangpur()
        for student in students:
            print(student)

    def show_data_of_Rajshahi(self):
        students = self.get_students_of_Rajshahi()
        for student in students:
            print(student)

    def show_data_of_GP_user(self):
        students = self.get_students_of_GP_User()
        for student in students:
            print(student)

    def show_data_of_Robi_user(self):
        students = self.get_students_of_Robi_User()
        for student in students:
            print(student)

    def show_data_by_id(self, id_):
        students = self.get_student_by_roll(id_)
        if not students:
            print("No data found at roll", id_)
        else:
            print(students)

    def select(self):
        sp.call('clear', shell=True)
        sel = input("1.Add data\n2.Show Data\n3.Search\n4.Update\n5.Delete\n6.Exit\n\n")

        if sel == '1':
            sp.call('clear', shell=True)
            id_ = int(input('id: '))
            name = input('Name: ')
            phone = input('phone: ')
            address = input('address: ')
            self.add_data(id_, name, phone, address)

        elif sel == '2':
            sp.call('clear', shell=True)
            sel = input("1.All Students\n2.Show by Division\n3.Show by Operator\n\n")

            if sel == '1':
                sp.call('clear', shell=True)
                self.show_data()
                input("\n\npress enter to back:")

            elif sel == '2':
                sp.call('clear', shell=True)
                sel = input("1.Students of Rangpur Division\n2.Students of Rajshahi Division\n\n")
                if sel == '1':
                    sp.call('clear', shell=True)
                    self.show_data_of_Rangpur()
                    input("\n\npress enter to back:")

                elif sel == '2':
                    sp.call('clear', shell=True)
                    self.show_data_of_Rajshahi()

            elif sel == '3':
                sp.call('clear', shell=True)
                sel = input("1.Gp\n2.Robi\n3.BL\n4.Airtel\n5.Teletalk\n\n")

                if sel == '1':
                    sp.call('clear', shell=True)
                    self.show_data_of_GP_user()

                elif sel == '2':
                    sp.call('clear', shell=True)
                    self.show_data_of_Robi_user()

            input("\n\npress enter to back:")


        elif sel == '3':
            sp.call('clear', shell=True)
            id__ = int(input('Enter Id: '))
            self.show_data_by_id(id__)
            input("\n\npress enter to back:")

        elif sel == '4':
            sp.call('clear', shell=True)
            id__ = int(input('Enter Id: '))
            self.show_data_by_id(id__)
            print()
            name = input('Name: ')
            phone = input('Phone: ')
            address = input('Address: ')
            self.update_student(id__, name, phone, address)
            input("\nYour data has been updated \n\npress enter to back:")

        elif sel == '5':
            sp.call('clear', shell=True)
            id__ = int(input('Enter Id: '))
            self.show_data_by_id(id__)
            self.delete_student(id__)
            input("\nYour data has been deleted \npress enter to back:")
        else:
            return 0
        return 1






Output = MainClass()

