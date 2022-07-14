class Patient:

    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    def get_name(self):
        return self.first_name + " " + self.last_name


if __name__ == "__main__":

    patient1 = Patient("federico", "capaldo")
    patient2 = Patient("jane", "smith")

    print(patient1.get_name())
    print(patient2.get_name())
