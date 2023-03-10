from database import Database 
database = Database() 

def check_patient_id(patient_id):
    records = database.execute_retrieve(("SELECT birthdate FROM patient"))

    for row in records: 
        if int(patient_id) == row[0]:
            return True
    return False

def add_patient(firstanme, lastname, gender, address, phone, birthdate):
    sql = """INSERT INTO patient (firstname, lastname, gender, address, phone, birthdate) VALUES (%s, %s, %s, %s, %s, %s)"""
    values = (firstanme,lastname,gender,address,int(phone),int(birthdate))

    database.execute_edit(sql, values)


def see_edit_info(patient_id): 
    records = database.execute_retrieve(("SELECT firstname, lastname, gender, address, phone, birthdate, total_visit_cost FROM patient where birthdate="+patient_id))

    print("\n*******************************************\n")
    print("FIRST NAME | LAST NAME | GENDER | ADDRESS | PHONE NR | BIRTHDATE | TOTAL COST")

    for row in records:     
        print(row)

    print("\nDo you want to edit information? (y/n): ")
    choice = input("You: ")

    if "y" in choice.lower(): 
        print("\nSelect 1 to change your first name.")
        print("\nSelect 2 to change your last name.")
        print("\nSelect 3 to change your gender.")
        print("\nSelect 4 to change your address.")
        print("\nSelect 5 to change your phone number.")
        change_choice = input("You: ")

        if change_choice == "1":
            print("\nEnter new first name: ")
            new_fn = input("You: ")

            sql = """UPDATE patient SET firstname = %s WHERE birthdate = %s"""
            values = (new_fn, patient_id)
            database.execute_edit(sql, values)

        elif change_choice == "2":
            print("\nEnter new last name: ")
            new_ln = input("You: ")

            sql = """UPDATE patient SET lastname = %s WHERE birthdate = %s"""
            values = (new_ln, patient_id)
            database.execute_edit(sql, values)

        elif change_choice == "3":
            print("\nEnter new gender (m/f): ")
            new_ge = input("You: ")

            if new_ge.lower() == "m" or new_ge.lower() == "f":
                sql = """UPDATE patient SET gender = %s WHERE birthdate = %s"""
                values = (new_ge, patient_id)
                database.execute_edit(sql, values)

            else: 
                print("\n------> Incorrect input format.")

        elif change_choice == "4":
            print("\nEnter new address: ")
            new_add = input("You: ")

            sql = """UPDATE patient SET address = %s WHERE birthdate = %s"""
            values = (new_add, patient_id)
            database.execute_edit(sql, values)

        elif change_choice == "5":
            print("\nEnter new phone number: ")
            new_pn = input("You: ")

            sql = """UPDATE patient SET phone = %s WHERE birthdate = %s"""
            values = (new_pn, patient_id)
            database.execute_edit(sql, values)


def view_appoints(patient_id): 
    # Retrieve the medical_number from patient
    query = "SELECT * FROM patient WHERE birthdate = '" + patient_id + "'"
    patrec = database.execute_retrieve(query)
    pat_id = patrec[0][0]

    query2 = "SELECT a.appointment_day, a.appointment_time, a.appointment_cost, d.firstname, d.lastname FROM appointment a JOIN doctor d ON a.appt_doctor_id = d.doctor_id WHERE a.appt_patient_id = "+ str(pat_id)

    records = database.execute_retrieve(query2)

    print("\n*******************************************\n")
    print("DAY | START TIME | COST | DOCTOR FULL NAME")
    for row in records:     
        print(row)


def book(patient_id, todaysDay): 

    print("\n*******************************************\n")
    print("DO YOU WANT TO....")
    print("1. List all doctors and their specification + visit cost?")
    print("2. Seach for doctors with a specific specialization?")
    firstchoice = input ("You: ")

    if firstchoice == "1":
        query = "Select*from patient_view_doctors"
        records = database.execute_retrieve(query)

        print("\n*******************************************\n")
        print("DOCTOR. ID | FIRST NAME | LAST NAME | SPECIALIZATION | VISIT COST")
        for row in records:
            print(row)
        
        inner_function(todaysDay, patient_id)


    elif firstchoice == "2": 
        specrecords = database.execute_retrieve(("SELECT * FROM specialization"))
        
        print("\n*******************************************\n")
        print("SPEC. ID | SPEC. NAME | COST")
        for row in specrecords: 
            print (row)

        print("\nEnter the SPEC. ID to list doctors of that specialization: ")
        spec_id = input("You: ")

        docrecords = database.execute_retrieve("SELECT doctor_id, firstname, lastname FROM Doctor WHERE doctor_specialization_id =" + spec_id)
        print("\n*******************************************\n")
        print("DOC. ID | DOC. FIRST NAME | DOC. LAST NAME | COST")
        for row in docrecords: 
            print (row)

        inner_function(todaysDay, patient_id)
        

def inner_function(todaysDay, patient_id):
    
    if todaysDay == 'friday': 

        print("\nDo you want to continue to book an appointment? (y/n): ")
        sec_choice = input("You: ")

        if "y" in sec_choice.lower(): 

                print("\nEnter the DOCTOR.ID of choice to view availabe dates: ")
                input_doc_id = input("You: ")

                query = "SELECT * FROM doctor_availability WHERE avail_doctor_id = '" + input_doc_id + "' AND booking = 'AVAILABLE' order by avail_id ASC;"
                records = database.execute_retrieve(query)
                                                    
                print("\n*******************************************\n")
                print("ROW. ID | DOCTOR ID | DAY | START TIME | END TIME | BOOKING")
                for row in records:
                    print(row)

                print("\nEnter the ROW.ID of the slot you want to book: ")
                input_row_id = input("You: ")

                print("\nConfirm booking? (y/n): ")
                third_choice = input("You: ")

                if "y" in third_choice.lower(): 

                    # Retrieve the medical_number from patient
                    query = "SELECT * FROM patient WHERE birthdate = '" + patient_id + "'"
                    patrec = database.execute_retrieve(query)
                    pat_id = patrec[0][0]
                
                    # Retrieve the details of the selected availability slot
                    query = "SELECT * FROM doctor_availability WHERE avail_id = '" + input_row_id + "'"
                    records = database.execute_retrieve(query)

                    if len(records) == 0:
                        print("\nInvalid ROW.ID. Please try again.")

                    else:
                        # Extract the relevant details
                        doctor_id = records[0][1]
                        appointment_day = records[0][2]
                        appointment_time = records[0][3]

                        # Insert a new row into the appointment table
                        query = """INSERT INTO appointment (appointment_day, appointment_time, appt_doctor_id, appt_patient_id) VALUES (%s, %s, %s, %s)"""
                        values = (appointment_day, appointment_time, int(doctor_id), int(pat_id))
                        database.execute_edit(query, values)

        else:
            print("\nBooking canceled.")
        
    else: 
        print("\n----> Please come back friday to book your appointment for the upcoming week.")


# View the diagnosis and prescription inserted by a doctor for each previous medical appointment.
def view_diagnosis_prescription(patient_id): 
    query = "SELECT m.* FROM medical_record m JOIN appointment a ON m.med_appointment_id = a.appointment_id JOIN patient p ON a.appt_patient_id = p.patient_id WHERE p.birthdate = " + patient_id
    med_recs = database.execute_retrieve(query)

    if len(med_recs) == 0:
        print("\nNo medical records available.")

    else:
        print("\n*******************************************\n")
        print("MED.REC. ID | DIAGNOSIS | PRESCRIPTION | DATE CREATED | APPOINTMEN ID")
        for row in med_recs: 
            print (row)


