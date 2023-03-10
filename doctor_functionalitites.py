from database import Database 
database = Database() 

# A function to check if the entered id exists.
def check_doc_id(doctor_id):
    records = database.execute_retrieve(("SELECT doctor_id FROM doctor"))

    for row in records: 
        if int(doctor_id) == row[0]:
            return True
    return False

# Prints all the doctor's slots: both booked and available ones.
def print_slots(doctor_id): 
    # Query the Appointment table to retrieve the appointments
        query = "SELECT * FROM doctor_availability WHERE avail_doctor_id = '" + doctor_id + "' order by avail_id ASC;"
        records = database.execute_retrieve(query)
                                            
        print("\n*******************************************\n")
        print("ROW. ID | DOCTOR ID | DAY | START TIME | END TIME | BOOKING")
        for row in records:
            print(row)


# Define his/her availabilities for each day of the week.
def def_availability(doctor_id): 
    # Query the Appointment table to retrieve the appointments
        query = "SELECT * FROM doctor_availability WHERE avail_doctor_id = '" + doctor_id + "' AND booking = 'AVAILABLE'"
        records = database.execute_retrieve(query)
                                            
        print("\n*******************************************\n")
        print("ROW. ID | DOCTOR ID | DAY | START TIME | END TIME | BOOKING")
        for row in records:
            print(row)

        print("\n*******************************************\n")
        print("Input ROW. ID of the slot you want to change to 'BUSY': ")
        input_slot = input("You: ")

        sql = """UPDATE doctor_availability SET booking = %s WHERE avail_id = %s"""
        values = ("BUSY", int(input_slot))
        database.execute_edit(sql, values)


# See a list of all his/her upcoming appointments.
def list_all_upcoming_app(doctor_id, todaysDay): 
    daysOfWeek = ["monday", "tuesday", "wednesday", "thursday", "friday"]
    todayIndex = daysOfWeek.index(todaysDay)

    # Slice the list to include only the days from today until Friday
    daysToLoop = daysOfWeek[todayIndex:daysOfWeek.index('friday')+1]

    # Loop over the remaining days of the week
    for i in daysToLoop:
        # Query the Appointment table to retrieve the appointments for the current day
        query = "SELECT * FROM booked_appointments WHERE appointment_day = '" + i + "' AND appt_doctor_id = " + str(doctor_id)
        records = database.execute_retrieve(query)
                                            
        if len(records) == 0:
            print("\nNo appointments scheduled for", i)

        else:
            print("\n*******************************************\n")
            print("APPT. ID | DAY | START TOIME | COST | DATE CREATED | DOCTOR ID | PATIENT ID")
            for appt in records:
                print(appt)


# See a list of his/her patients and add a medical record for each of them. 
def list_all_your_patients(doctor_id): 
    query = "SELECT a.appointment_id, p.patient_id, p.firstname, p.lastname, p.gender, p.birthdate FROM patient p JOIN appointment a ON p.patient_id = a.appt_patient_id WHERE a.appt_doctor_id = "+ doctor_id
    records = database.execute_retrieve(query)
    
    print("\n*******************************************\n")
    print("APPOINTMENT ID | PATIENT ID | P. FIRST NAME | P. LAST NAME | P. GENDER | P. BIRTHDATE")
    for row in records:
        print(row)
    
    print("You can edit the diagnosis and presciption.")
    print("Enter the 4-digit appointment ID of the medical record you want to update: ")
    input_id = input("You: ")

    print("Enter diagnosis: ")
    input_diagnosis = input("You: ")

    print("Enter prescription: ")
    input_prescription = input("You: ")

    sql = """UPDATE medical_record SET diagnosis = %s, prescription = %s WHERE med_appointment_id = %s"""
    values = (input_diagnosis, input_prescription, input_id)
    database.execute_edit(sql, values)