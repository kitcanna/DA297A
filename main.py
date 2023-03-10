import admin_functionalities as af
import doctor_functionalitites as df
import patient_functionalities as pf

todaysDay = 'thursday' 

mainloop = True

while mainloop:

    print("\n*******************************************\n")    
    print("Welcome! Are you an admin, doctor or a patient?\n")

    user_input = input("You: ")

    if user_input.lower()=="admin" or user_input.lower()=="doctor" or user_input.lower()=="patient" :
        role = user_input.lower()

    elif user_input.lower()=="back":
        mainloop = False
        break

    else:
        print("\n*******************************************\n")    
        print("--------> ERROR! Please try again and enter a valid role.")
        role=""

############################################################################################

    while(role=="admin"):
            print("\n*******************************************\n")    
            print("Hello, {}.\n".format(user_input.lower()))
            print("Please enter your ID number (4-digit):\n")
            admin_id = input("You: ")

            if "back" in admin_id.lower():
                role=""
                break  
            
            # Check so input is valid
            if len(admin_id) == 4 and admin_id.isdigit():     

                checkAdmin = af.check_admin_id(admin_id)

                # If admin_id exists
                if (checkAdmin == True):
                    admin_id_exists = True

                    while(admin_id_exists):

                        print("\n*******************************************\n")    
                        print("Welcome admin ", admin_id + ".\n")     
                        print("----\n")    
                        print("What would you like to do? Choose a number.")
                        print("1. Handle specialization of the doctors.")
                        print("2. Handle the health center’s doctors.")
                        print("3. See a list of information about the patients registered in the health center.")
                        print("4. See a list of all upcoming appointments.")
                        print("5. See a list of all medical record related to a specific patient.")
                        print("6. See a list of all patients and their visit cost.")
                        admin_event = input("You: ")

                        if "back" in admin_event.lower():
                            role=""
                            admin_id_exists=""
                            break  
                        
                        ################# SPECIALIZATION #################

                        elif admin_event=="1":
                            print("\n*******************************************\n")
                            print("You chose 1.")     

                            print("\n*******************************************\n")     
                            print("What would you like to do? Choose a number.")
                            print("1. List all specializations.")
                            print("2. Add a specialization entry.")

                            spec_event = input("You: ")

                            if "back" in spec_event.lower():
                                admin_event=""
                                break  

                            elif spec_event == "1":
                                af.list_specialization()

                            elif spec_event == "2":
                                print("Input the Specialization name (ex. Cardiologist):")
                                input_spec_name = input("You: ")
                                print("Input the specialization cost (ex. 500):")
                                input_spec_cost = input ("You: ")
                                af.add_specialization(input_spec_name, input_spec_cost)

                        ################# DOCTOR #################

                        elif admin_event=="2":
                            print("\n*******************************************\n")
                            print("You chose 2.")  

                            print("\n*******************************************\n")     
                            print("What would you like to do? Choose a number.")
                            print("1. List all doctors.")
                            print("2. Add a doctor.")
                            print("3. Remove a doctor.")

                            doc_event = input("You: ")

                            if "back" in doc_event.lower():
                                admin_event=""
                                break  

                            elif doc_event == "1":
                                af.list_doctor()
                            
                            elif doc_event == "2":
                                af.add_doctor()

                            elif doc_event == "3":
                                af.delete_doctor()


                        ###################################################
                       
                        elif admin_event=="3":
                            print("\n*******************************************\n")
                            print("You chose 3.")
                            af.list_all_patients_information()

                        ###################################################

                        elif admin_event=="4":
                            print("\n*******************************************\n")
                            print("You chose 4.")  
                            af.see_upcoming_appoints(todaysDay) 

                        ###################################################

                        elif admin_event=="5":
                            print("\n*******************************************\n")
                            print("You chose 5.")   
                            af.see_patient_info()

                        ###################################################

                        elif admin_event=="6":
                            print("\n*******************************************\n")
                            print("You chose 6.")
                            af.list_all_patients_visit_costs()

                        ###################################################

                        else:
                            print("\n*******************************************\n")    
                            print("----> ERROR! Please choose a valid number.")

                # If admin_id DOESN't exist
                elif (checkAdmin  == False):
                    print("\n*******************************************\n")    
                    print("--------> ERROR! You are not registered.")
                    break

            else: 
                print("\n*******************************************\n")    
                print("--------> ERROR! You ID must be a 4-digit integer. Try again.")
                break

############################################################################################

    while(role=="doctor"):
            print("\n*******************************************\n")    
            print("Hello, {}.\n".format(user_input.lower()))
            print("Please enter your ID number (6-digit):\n")
            doctor_id = input("You: ")

            if "back" in doctor_id.lower():
                role=""
                break  

            # Check so input is valid
            if len(doctor_id) == 4 and doctor_id.isdigit():     

                checkDoctor = df.check_doc_id(doctor_id)
                # If doctor_id exists
                if (checkDoctor == True):
            
                    doctor_id_exists = True

                    while(doctor_id_exists):
                        print("\n*******************************************\n")    
                        print("Welcome doctor ", doctor_id + ".\n")     
                        print("----\n")    
                        print("What would you like to do? Choose a number.")
                        print("1. Define your availability.")
                        print("2. See your upcoming appointments.")
                        print("3. Add details to a medical record of your patient.")
                        print("4. Print all time slots related to you.")
                        doctor_event = input("You: ")

                        if "back" in doctor_event.lower():
                            role=""
                            doctor_id_exists = ""
                            break

                        elif doctor_event=="1":
                            print("\n*******************************************\n")
                            print("You chose 1.")
                            df.def_availability(doctor_id)

                        elif doctor_event=="2":
                            print("\n*******************************************\n")
                            print("You chose 2.")
                            df.list_all_upcoming_app(doctor_id, todaysDay)

                        elif doctor_event=="3":
                            print("\n*******************************************\n")
                            print("You chose 3.")
                            df.list_all_your_patients(doctor_id)

                        elif doctor_event=="4":
                            print("\n*******************************************\n")
                            print("You chose 3.")
                            df.print_slots(doctor_id)

                        else:
                            print("\n*******************************************\n")    
                            print("----> ERROR! Please choose a valid number.")

                # If doctor_id DOESN'T exist
                elif (checkDoctor == False):
                    print("\n*******************************************\n")    
                    print("--------> RROR! You are not registered.")
                    break

            else: 
                print("\n*******************************************\n")    
                print("--------> ERROR! You ID must be a 4-digit integer. Try again.")
                break


############################################################################################

    while(role=="patient"):
            print("\n*******************************************\n")    
            print("Hello, {}.\n".format(user_input.lower()))
            print("Please enter your medical number (YYYYMMDD):\n")
            medical_number = input("You: ")
            
            if "back" in medical_number.lower():
                role=""
                break     

            # Check so input is valid
            if len(medical_number) == 8 and medical_number.isdigit():   

                checkPatient = pf.check_patient_id(medical_number)
                if (checkPatient == True):
                    pat_id_exists = True

                    while(pat_id_exists):
                        print("\n*******************************************\n")
                        print("Welcome patient", medical_number + ".\n")     
                        print("----\n")    
                        print("What would you like to do? Choose a number.")
                        print("1. See/edit your basic information.")
                        print("2. Book an appointment to visit a doctor.")
                        print("3. View the diagnosis and prescription inserted by a doctor.")
                        print("4. View your upcoming booked appointments.")
                        patient_event = input("You: ")

                        if "back" in patient_event.lower():
                            role=""
                            pat_id_exists=""
                            break  

                        elif patient_event=="1":
                            print("\n*******************************************\n")
                            print("You chose 1.")
                            pf.see_edit_info(medical_number)

                        elif patient_event=="2":
                            print("\n*******************************************\n")
                            print("You chose 2.")
                            pf.book(medical_number, todaysDay)

                        elif patient_event=="3":
                            print("\n*******************************************\n")
                            print("You chose 3.")
                            pf.view_diagnosis_prescription(medical_number)

                        elif patient_event=="4":
                            print("\n*******************************************\n")
                            print("You chose 4.")
                            pf.view_appoints(medical_number)

                        else:
                            print("\n*******************************************\n")    
                            print("----> ERROR! Please choose a valid number.")


                elif (checkPatient == False):
                    print("\n*******************************************\n")
                    print("You haven't registered, please do so now.")

                    print("Input your first name:")
                    pat_firstname = input("You: ")

                    print("Input your last name:")
                    pat_lastname = input("You: ")

                    print("Input your gender (m/f):")
                    pat_gender = input("You: ")

                    print("Input your address:")
                    pat_address = input("You: ")

                    print("Input your phone number (07XXXXXXXX):")
                    pat_phone = input("You: ")

                    pf.add_patient(pat_firstname, pat_lastname, pat_gender, pat_address, pat_phone, medical_number)

            else: 
                print("*******************************************\n")    
                print("--------> ERROR! You ID must be a 8-digit integer. Try again.")
                break