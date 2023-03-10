from database import Database 
database = Database() 

# Check so that the admin is registered
def check_admin_id(admin_id):
    records = database.execute_retrieve(("SELECT admin_id FROM admin"))

    for row in records: 
        if int(admin_id) == row[0]:
            return True
    return False

###################################### 

# Lists all specializations
def list_specialization(): 
    records = database.execute_retrieve(("SELECT * FROM specialization"))
    
    print("\n*******************************************\n")
    print("SPEC. ID | SPEC. NAME | COST")
    
    for row in records: 
        print (row)

# Adds a specialization
def add_specialization(name, cost):
    sql = """INSERT INTO specialization (specialization_name, visit_cost) VALUES (%s, %s)"""
    values = (name, int(cost))

    database.execute_edit(sql, values)
    
######################################

# Lists all doctors in the health center.
def list_doctor(): 
    records = database.execute_retrieve(("SELECT*FROM admin_lists_doctors"))
    
    print("\n*******************************************\n")
    print("DOC. ID | FIRST NAME | LAST NAME | PHONE | ADDRESS | PHONE | SPECIALIZATION | VISIT COST")
    
    for row in records: 
        print (row)    

# Add a new doctor to the health center. 
def add_doctor(): 
    print("\n*******************************************\n")
    print("Doctor first name:")
    input_firstname = input("You: ")
    print("Doctor last name:")
    input_lastname = input("You: ")
    print("Doctor phone numeber:")
    input_phone = input("You: ")

    records = database.execute_retrieve(("SELECT specialization_id, specialization_name FROM specialization"))
    print("\n*******************************************\n")
    print("SPEC. ID | SPEC. NAME")
    for row in records: 
        print (row)    

    print("\nDoctor specialization number:")
    input_spec_id = input("You: ")

    sql = """INSERT INTO doctor (firstname, lastname, phone, doctor_specialization_id) VALUES (%s, %s, %s, %s)"""
    values = (input_firstname, input_lastname, int(input_phone), int(input_spec_id))
    database.execute_edit(sql, values)

# Deletes a doctor from the health center.
def delete_doctor(): 
    records = database.execute_retrieve(("SELECT*from admin_lists_doctors"))
    
    print("\n*******************************************\n")
    print("DOC. ID | FIRST NAME | LAST NAME | PHONE | ADDRESS | PHONE | SPECIALIZATION | VISIT COST")
    
    for row in records: 
        print (row)

    print("\nInput the 4-digit doctor_id of the doctor you want to delete:")
    doc_id_input = input("You: ")
    sql = """call delete_doctor(%s)"""
    values = (int(doc_id_input))

    database.execute_edit(sql, [values])

######################################

# Lists all patients and their information.
def list_all_patients_information(): 
    records = database.execute_retrieve(("SELECT * FROM patient"))
    
    print("\n*******************************************\n")
    print("PAT. ID | FIRST NAME | LAST NAME | GENDER | ADDRESS | PHONE | BIRTHDAY | REG. DATE | TOTAL VISIT COST")
    
    for row in records: 
        print (row)

######################################

# See a list of all medical record related to a specific patient.
def see_patient_info(): 
    records = database.execute_retrieve(("SELECT patient_id, firstname, lastname, birthdate FROM patient"))
    
    print("\n*******************************************\n")
    print("PAT. ID | FIRST NAME | LAST NAME | BIRTHDAY")
    
    for row in records: 
        print (row)

    print("\nInput the 9-digit PAT. ID of the patient you want to see medical records of: ")
    input_chosen = input("You: ")

    query = "SELECT m.* FROM medical_record m JOIN appointment a ON m.med_appointment_id = a.appointment_id WHERE a.appt_patient_id =" + input_chosen
    med_recs = database.execute_retrieve(query)

    print("\n*******************************************\n")
    print("MED.REC. ID | DIAGNOSIS | PRESCRIPTION | DATE CREATED | APPOINTMEN ID")
    for row in med_recs: 
        print (row)

######################################

# See a list of all patients and their total visit costs. 
# Visit cost is here updated by a trigger and procedure/transaction.
def list_all_patients_visit_costs(): 
    records = database.execute_retrieve(("SELECT patient_id, firstname, lastname, total_visit_cost FROM patient"))
    
    print("\n*******************************************\n")
    print("PAT. ID | FIRST NAME | LAST NAME | TOTAL VISIT COST")
    
    for row in records: 
        print (row)
    
######################################

# See a list of all upcoming appointments from today until Friday.
def see_upcoming_appoints(todaysDay):
    daysOfWeek = ["monday", "tuesday", "wednesday", "thursday", "friday"]
    todayIndex = daysOfWeek.index(todaysDay)

    # Slice the list to include only the days from today until Friday
    daysToLoop = daysOfWeek[todayIndex:daysOfWeek.index('friday')+1]

    # Loop over the remaining days of the week
    for i in daysToLoop:
        # Query the Appointment table to retrieve the appointments for the current day
        query = "SELECT * FROM booked_appointments WHERE appointment_day = '" + i + "'"
        records = database.execute_retrieve(query)
                                            
        if len(records) == 0:
            print("\nNo appointments scheduled for", i)

        else:
            print("\n*******************************************\n")
            print("APPT. ID | DAY | START TOIME | COST | DATE CREATED | DOCTOR ID | PATIENT ID")
            for appt in records:
                print(appt)
        
