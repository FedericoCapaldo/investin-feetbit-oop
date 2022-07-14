class Patient:

    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    def get_name(self):
        return self.first_name + " " + self.last_name

class Doctor:

    def __init__(self, fname, lname, s):
        self.first_name = fname
        self.last_name = lname
        self.specialization = s

    def get_name(self):
        return self.first_name + " " + self.last_name

    def get_specialization(self):
        return self.specialization


if __name__ == "__main__":

    patient1 = Patient("federico", "capaldo")
    patient2 = Patient("jane", "smith")
    doctor1 = Doctor("Alan", "Pollock", "Pediatrician")
    doctor2 = Doctor("Jennifer", "Finger", "Hand specialist")

    print(patient1.get_name())
    print(patient2.get_name())
    print(doctor1.get_name(), doctor1.get_specialization())
