class Doctor:

    def __init__(self, ID = '', name = '', specialization = '', working_time = '', qualification = '', room_number = ''):

        self.ID = ID
        self.Name = name
        self.Specialization = specialization
        self.Working_Time = working_time
        self.Qualification = qualification
        self.Room_number = room_number


    def getdoctor_ID(self): return self.ID
    def getdoctor_name(self): return self.Name
    def getdoctor_specialization(self): return self.Specialization
    def getdoctor_working_time(self): return self.Working_Time
    def getdoctor_qualification(self): return self.Qualification
    def getdoctor_room_number(self): return self.Room_number


    def set_doctor_ID(self, new_ID): self.ID = new_ID
    def set_doctor_name(self, new_name): self.Name = new_name
    def set_doctor_specialization(self, new_specialization): self.Specialization = new_specialization
    def set_doctor_working_time(self, new_working_time): self.Working_Time = new_working_time
    def set_doctor_qualification(self, new_qualification): self.Qualification = new_qualification
    def set_doctor_room_number(self, new_room_number): self.Room_number = new_room_number




    def __str__(self): return '%s_%s_%s_%s_%s_%s' .format(self.ID, self.Name, self.Specialization, self.Working_Time, self.Qualification, self.Room_number)

    


class DoctorManager:

    def __init__(self):
      
        self.doctors = self.read_doctors_file()
    

    def read_doctors_file(self):

        docfile = open("C:/Users/J/Documents/SAIT/PROGRAMMING_WORKSPACE/OOP1/W14/doctors.txt", "r") 

        doctor = []

        doctorclass = ''

        for x in range(0, 6):
            doctorclass = docfile.readline()


            thing = doctorclass.split('_')

            doctor.append(Doctor(thing))

            x = x + 1

        return doctor



    ###def format_dr_info(self, ID, name, Specialization, Working_Time, Qualification, Room_number): return '%s_%s_%s_%s_%s_%s' .format(ID, name, Specialization, Working_Time, Qualification, Room_number)

    def format_dr_info(self): 

        x = 0

        other_doctors = []
        
        for x in self.doctors:

             print (self.doctors[x].getdoctor_ID(),"_", self.doctors[x].getdoctor_name(),"_", self.doctors[x].getdoctor_specialization(),"_", self.doctors[x].getdoctor_working_time(),"_", self.doctors[x].getdoctor_qualification(),"_", self.doctors[x].getdoctor_room_number())

        
        return other_doctors

    def enter_dr_info(self):

        new_ID = input("Enter the doctor’s ID: ")
        new_name = input("Enter the doctor's name: ")
        new_specialization = input("Enter the doctor’s specility: ")
        new_working_time = input("Enter the doctor’s timing (e.g., 7am-10pm): ")
        new_qualification = input("Enter the doctor’s qualification: ")
        new_room_number = input("Enter the doctor’s room number: ")

        return self.doctors.append(new_ID, new_name, new_specialization, new_working_time, new_qualification, new_room_number)

    def search_doctor_by_id(self):

        id = input("Enter the doctor Id: ")

        x = 0

        while x != self.doctors.__len__:

            if self.doctors[x].getdoctor_ID() == id:
                print (self.doctors[x].getdoctor_ID(), self.doctors[x].getdoctor_name(), self.doctors[x].getdoctor_specialization(), self.doctors[x].getdoctor_working_time(), self.doctors[x].getdoctor_qualification())
            x = x + 1

    def search_doctor_by_name(self):

        name = input("Enter the doctor Name: ")

        x = 0

        while x != self.doctors.__len__:

            if self.doctors[x].getdoctor_name() == name:
                print (self.doctors[x].getdoctor_ID(), self.doctors[x].getdoctor_name(), self.doctors[x].getdoctor_specialization(), self.doctors[x].getdoctor_working_time(), self.doctors[x].getdoctor_qualification())
            x = x + 1

    def display_doctor_info(self):

        for i in self.doctors:

            print (self.doctors[x].ID(),"_", self.doctors[x].name(),"_", self.doctors[x].Specialization(),"_", self.doctors[x].Working_Time(),"_", self.doctors[x].Qualification(),"_", self.doctors[x].Room_number())
            x = x + 1

    def edit_doctor_info(self):

        id = input("Enter the doctor ID of the doctor you want to edit: ")

        x = 0

        while x != self.doctor.__len__:

            if self.doctor[x].getdoctor_ID == id:

                self.doctors[x].name = input("Enter the new name: ")
                self.doctors[x].specialization = input("Enter the new specilization: ")
                self.doctors[x].working_time = input("Enter the new working time: ")
                self.doctors[x].qualification = input("Enter the new qualification: ")
                self.doctors[x].room_number = input("Enter the new room number: ")

                print (self.doctors[x].getdoctor_ID(), self.doctors[x].getdoctor_name(), self.doctors[x].getdoctor_specialization(), self.doctors[x].getdoctor_working_time(), self.doctors[x].getdoctor_qualification())
            x = x + 1

            ###else: print ("Cannot find doctor with ID", new_id )
    
    def Write_list_of_doctors_to_file(self):

        list_doctors = []


        for i in self.doctors:

            list_doctors.append(self.doctors[x].ID(),"_", self.doctors[x].getdoctor_name(),"_", self.doctors[x].Specialization(),"_", self.doctors[x].Working_Time(),"_", self.doctors[x].Qualification(),"_", self.doctors[x].Room_number())
            x = x + 1


    def add_dr_to_file(self):

        new_ID = input("Enter the new doctor's ID: ")
        new_Name = input("Enter the new doctor's name: ")
        new_Specialization = input("Enter the new doctor's specialization: ")
        new_Working_Time = input("Enter the new doctor's working time: ")
        new_Qualification = input("Enter the new doctor's qualification: ")
        new_Room_number = input("Enter the new doctor's Room number: ")

        self.doctors.append(Doctor(new_ID,new_Name,new_Qualification,new_Room_number,new_Room_number, new_Specialization,new_Working_Time))


        return self.doctors
            

## pid, name, disease, gender, age 

class Patient:

    def __init__(self, PID, name, disease, gender, age):

        Patient.PID = PID
        Patient.Name = name
        Patient.Disease = disease
        Patient.Gender = gender
        Patient.Age = age

    def getpatient_PID(self): return self.PID
    def getpatient_name(self): return self.Name
    def getpatient_disease(self): return self.Disease
    def getpatient_gender(self): return self.Gender
    def getpatient_age(self): return self.Age


    def set_patient_ID(self, new_PID): self.PID = new_PID
    def set_patient_name(self, new_name): self.Name = new_name
    def set_patient_disease(self, new_disease): self.Disease = new_disease
    def set_patient_gender(self, new_gender): self.Gender = new_gender
    def set_patient_age(self, new_age): self.Age = new_age




    def __str__(self): return '%s_%s_%s_%s_%s_%s' .format(self.PID, self.Name, self.Disease, self.Gender, self.Age)


class PatientManager:

    def __init__(self):
        docfile = open("patients.txt")

        patient = []

        patientclass = ""

        for x in docfile:

            patientclass = docfile.readline()

            PatientManager.patient[x] = Patient(patientclass.split("_"))

        print (patient[1].ID)
        
        return patient[x]

    def format_patient_info_for_file(self, PID, name, Disease, gender, age): return '%s_%s_%s_%s_%s' .format(PID, name,  Disease, gender, age)

    def enter_patient_info(self):

        new_PID = input("Enter the patient’s ID: ")
        new_name = input("Enter the patient's name: ")
        new_disease = input("Enter the patient’s disease: ")
        new_gender = input("Enter the patient's gender: ")
        new_age = input("Enter the patient's age: ")

        return self.patient.__add__(new_PID, new_name, new_disease, new_gender, new_age)

    def search_patient_by_id(self):

        id = input("Enter the patient's ID: ")

        x = 0

        while x != self.patient.__len__:

            if self.patient[x] == id:
                print (patient[x].getpatient_PID, Patient.getpatient_name, Patient.getpatient_disease, Patient.getpatient_gender, Patient.getpatient_age)
            x = x + 1

    def search_patient_by_name(self):

        name = input("Enter the patient's name: ")

        x = 0

        while x != self.patient.__len__:

            if self.patient[x] == name:
                print (patient[x].getpatient_PID, Patient.getpatient_name, Patient.getpatient_disease, Patient.getpatient_gender, Patient.getpatient_age)
            x = x + 1

    def display_patient_info(self):

        for i in patient:

            return '%s_%s_%s_%s_%s_%s' .format(i.getpatient_PID, i.getpatient_name, i.getpatient_disease, i.getpatient_gender, i.getpatient_age)

    def edit_patient_info(self):

        id = input("Enter the patient ID of the patient you want to edit: ")

        x = 0

        while x != self.patient.__len__:

            if patient[x].PID == id:

                patient[x].name = input("Enter the new name: ")
                patient[x].disease = input("Enter the new specilization: ")
                patient[x].gender = input("Enter the new working time: ")
                patient[x].age = input("Enter the new qualification: ")

                print (patient[x].getpatient_PID, Patient.getpatient_name, Patient.getpatient_disease, Patient.getpatient_gender, Patient.getpatient_age)
            x = x + 1

            ###else: print ("Cannot find doctor with ID", new_id )

        return patient
    
    def Write_list_of_patients_to_file():

        list_patients = ''

        list_patients = display_patient_info()


    def add_patient_to_file(self):

        new_PID = input("Enter the new patient's ID: ")
        new_name = input("Enter the new patient's name: ")
        new_disease = input("Enter the new patient's disease: ")
        new_gender = input("Enter the new patient's gender: ")
        new_age = input("Enter the new patient's age: ")

        patient.append(Patient(new_PID,new_name,new_disease,new_gender,new_age))


        return patient
            

## pid, name, disease, gender, age 


option = 0

while option != 3:

    print ("Welcome to Alberat Hospital (AH) Management System.")

    option = int(input('''
    Select from the following options, or select 0 to stop: 
    1 - 	Doctors
    2 - 	Patients
    3 -	Exit Program  

    ''')) 

 

    if option == 2:
        menu = 0
        while menu != 5:
            menu = int(input(''' Patients Menu:
                            1 - display patients list
                            2 - Search for patient by ID
                            3 - Add patient
                            4 - Edit patient info
                            5 - Back to the Main Menu '''))
            print("")
            
           

            if menu == 1: PatientManager.display_patient_info()
            if menu == 2: PatientManager.search_patient_by_
            if menu == 3: None
            if menu == 4: None
            if menu == 5: break
        


    if option == 1:
        menu = 0
        while menu != 6:
            menu = int(input(''' Doctors Menu:
                            1 - Display Doctors list
                            2 - Search for doctor by ID
                            3 - Search for doctor by name
                            4 - Add doctor
                            5 - Edit doctor info
                            6 - Back to the Main Menu'''))
            print("")
            

            if menu == 1: DoctorManager.display_doctor_info()
            if menu == 2: DoctorManager.search_doctor_by_id()
            if menu == 3: DoctorManager.search_doctor_by_name()
            if menu == 4: DoctorManager.enter_dr_info()
            if menu == 5: DoctorManager.edit_doctor_info()
            if menu == 6: DoctorManager.Write_list_of_doctors_to_file(); break

    if option == 3: break
