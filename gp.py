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
        self.appointments = []

    def get_name(self):
        return self.practise_name.upper()

    def add_patient_to_practise(self, new_patient):
        self.patient_list.append(new_patient)

    def get_patients(self):
        return self.patient_list

    def add_doctor_to_practise(self, new_doctor):
        self.doctor_list.append(new_doctor)

    def create_appointment(self, patient, doctor, date, notes=""):
        new_appointment = Appointment(patient, doctor, date, notes)
        self.appointments.append(new_appointment)

    def get_all_appointments(self):
        return self.appointments

class Appointment:

    def __init__(self, patient, doctor, date, notes=""):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.notes = notes

    def get_appointment_info(self):
        return "Patient -> " + self.patient.get_name() + " Doctor -> " + self.doctor.get_name() + "(" + self.doctor.get_specialization() + ")" + "Notes (optional) -> " + self.notes


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

    gp_practice.create_appointment(patient1, doctor1, "30 July 2022", "Federico has headaches in kindergarden")
    gp_practice.create_appointment(patient2, doctor1, "10 August 2022", "Jane's daugher can't stop hiccups")

    for app in gp_practice.get_all_appointments():
        print("APPOINTMENT")
        print(app.get_appointment_info())
