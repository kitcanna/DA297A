import psycopg2
import sensitive

# CLASS WRITTEN AS A CONTEXT MANAGER

class Database:

    def __init__(self, port = 5432, host = 'pgserver.mau.se', database = "project_healthcenter", user = sensitive.user, password = sensitive.password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.conn = self.connect_to_db()

    try:  
        def connect_to_db(self):
            conn = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            #print("\n*******************************************\n") 
            #print("Connection to database opened.")
            conn.autocommit = True
            return conn

    except(Exception) as error:
        print("\n*******************************************\n")    
        print("--------> ERROR: ", error)

################################################ 

    def execute_retrieve(self, command):
        try: 
            cur = self.connect_to_db().cursor()
            cur.execute(command)
            records = cur.fetchall()
            return records

        except(Exception) as error:
            print("\n*******************************************\n")    
            print("--------> ERROR: ", error)

        finally:
            cur.close()
            self.close_connection()

################################################

    def execute_edit(self, command, values):
        try:
            cur = self.connect_to_db().cursor()
            cur.execute(command, values)
            print("Statement was successful.")

        except(Exception) as error:
            print("\n*******************************************\n")    
            print("--------> ERROR: ", error)

        finally:
            cur.close()
            self.close_connection()

################################################
    
    def close_connection(self):
        if self.conn:
            self.conn.close()

        #print("Connection to database closed.")
        #print("\n*******************************************\n") 
    
################################################

    # The __del__ method is a special method in Python that is
    # automatically called when an object is garbage collected. 
    # When an instance of a class is no longer referenced by any 
    # other part of the program, Python's garbage collector 
    # will delete the object and call its __del__ method, if it exists.
    def __del__(self):
        self.close_connection()