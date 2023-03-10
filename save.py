import psycopg2
import sensitive

# A function to check if the entered id exists.
def reg_admin_ids(admin_id):

    ############################ 
    try:
        connection = psycopg2.connect(user = sensitive.user,
                                    password = sensitive.password,
                                    host='pgserver.mau.se',
                                    port=5432,
                                    database="am3963")
        cursor = connection.cursor()
        cursor.execute("SELECT admin_id FROM administrators WHERE admin_id = %s;", (str(admin_id),))        
        records = cursor.fetchone()
        
        bool = False
        for row in records: 
            if int(admin_id) == row:
                bool = True 
            break
        
        cursor.close()
        return bool
            # reg_ids.append(row)
        
    except(Exception) as error:
        print("\n*******************************************\n")    
        print("--------> ERROR: ", error)

    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("\n*******************************************\n")    
            print("--------> Connection closed!")

    ############################ 