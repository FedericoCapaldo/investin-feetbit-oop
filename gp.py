class Patient:

    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    def get_name(self):
        return self.first_name.capitalize() + " " + self.last_name.capitalize()

class Doctor:

    def __init__(self, fname, lname, s):
        self.first_name = fname
        self.last_name = lname
        self.specialization = s

    def get_name(self):
        return self.first_name.capitalize() + " " + self.last_name.capitalize()

    def get_specialization(self):
        return self.specialization

class GP_Practice:

    def __init__(self, name):
        self.practise_name = name
        self.patient_list = []
        self.doctor_list = []

    def get_name(self):
        return self.practise_name.upper()

    def add_patient_to_practise(self, new_patient):
        self.patient_list.append(new_patient)

    def get_patients(self):
        return self.patient_list

    def add_doctor_to_practise(self, new_doctor):
        self.doctor_list.append(new_doctor)

if __name__ == "__main__":

    patient1 = Patient("federico", "capaldo")
    patient2 = Patient("jane", "smith")
    doctor1 = Doctor("Alan", "Pollock", "Pediatrician")
    doctor2 = Doctor("Jennifer", "Finger", "Hand specialist")

    print(patient1.get_name())
    print(patient2.get_name())
    print(doctor1.get_name(), doctor1.get_specialization())


    gp_practice = GP_Practice("Marylebone Square 1")
    print(gp_practice.get_name())

    gp_practice.add_patient_to_practise(patient1)
    gp_practice.add_patient_to_practise(patient2)

    print("from the practice")
    for single_patient in gp_practice.get_patients():
        print(single_patient.get_name())
