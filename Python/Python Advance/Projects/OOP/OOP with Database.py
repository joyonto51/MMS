class Database():
	import sqlite3

	def create_table():
		conn = sqlite3.connect('stdb.sqlite3')

		cursor = conn.cursor()
		query = '''
		CREATE TABLE IF NOT EXISTS student(
		    id INTEGER PRIMARY KEY, 
	    	roll INTEGER, 
	    	name TEXT,
	        phone TEXT,
	        address TEXT
	    )
	    '''
		cursor.execute(query)
		conn.commit()
		conn.close()


	def add_student(self,roll,name,phone,address):
		conn = sqlite3.connect('stdb.sqlite3')

		cursor = conn.cursor()

		query = '''                                           
	        INSERT INTO student( roll, name, phone, address ) 
	        	        VALUES ( ?,?,?,? )                    
	    '''

		cursor.execute(query,(roll,name,phone, address))

		conn.commit()
		conn.close()

	def get_students():
		conn = sqlite3.connect('stdb.sqlite3')

		cursor = conn.cursor()

		query = '''                                                
    	    SELECT roll, name, phone, address                      
    	    FROM student                                           
    	'''


		cursor.execute(query)
		all_rows = cursor.fetchall()

		conn.commit()
		conn.close()

		return all_rows

	def get_students_of_Rangpur():
		conn = sqlite3.connect('stdb.sqlite3')

		cursor = conn.cursor()

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


		cursor.execute(query)
		all_rows = cursor.fetchall()

		conn.commit()
		conn.close()

		return all_rows

	def get_students_of_Rajshahi():
		conn = sqlite3.connect('stdb.sqlite3')

		cursor = conn.cursor()

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


		cursor.execute(query)
		all_rows = cursor.fetchall()

		conn.commit()
		conn.close()

		return all_rows

	def get_students_of_GP_User():
		conn = sqlite3.connect('stdb.sqlite3')

		cursor = conn.cursor()

		query = '''                                                
    	    SELECT roll, name, phone, address                      
    	    FROM student                                           
            WHERE phone LIKE "017%"                                
    	'''


		cursor.execute(query)
		all_rows = cursor.fetchall()

		conn.commit()
		conn.close()

		return all_rows

	def get_students_of_Robi_User():
		conn = sqlite3.connect('stdb.sqlite3')

		cursor = conn.cursor()

		query = '''                                                
    	    SELECT roll, name, phone, address                      
    	    FROM student                                           
            WHERE phone LIKE "018%"                                
    	'''


		cursor.execute(query)
		all_rows = cursor.fetchall()

		conn.commit()
		conn.close()

		return all_rows

	def get_student_by_roll(roll):
		conn = sqlite3.connect('stdb.sqlite3')

		cursor = conn.cursor()

		query = '''                                                
    	    SELECT roll, name, phone, address                      
    	    FROM student                                           
    	    WHERE roll = {}                                        
    	''' .format(roll)

		cursor.execute(query)
		all_rows = cursor.fetchall()

		conn.commit()
		conn.close()

		return all_rows

	def update_student(roll,name,phone,address):
		conn = sqlite3.connect('stdb.sqlite3')

		cursor = conn.cursor()

		query = '''                                                
    	    UPDATE student                                         
    	    SET name = ?, phone = ?, address = ?                   
    	    WHERE roll = ?                                         
    	'''

		cursor.execute(query,(name,phone,address,roll))

		conn.commit()
		conn.close()


	def delete_student(roll):
		conn = sqlite3.connect('stdb.sqlite3')

		cursor = conn.cursor()

		query = '''                                                
    	    DELETE                                                 
    	    FROM student                                           
    	    WHERE roll = {}                                        
    	''' .format(roll)

		cursor.execute(query)
		all_rows = cursor.fetchall()

		conn.commit()
		conn.close()

		return all_rows



	create_table()





