import mysql.connector

class DBhelper:
     
    def __init__(self):
        print('class called')
        try: 
            self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="hit-db-demo")
            self.mycursor = self.conn.cursor()
        except:
            print('Some Database connection error occured')

        else:
            print("Conected to Database")


    def register(self, name, email, password):
        try:
            self.mycursor.execute("""
            INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES (NULL, '{}', '{}', '{}');
            """.format(name, email, password))
            self.conn.commit()
        except:
            print('Some registeration error occured')
            return -1
        else:
            print('registerration done successfully')
            return 1