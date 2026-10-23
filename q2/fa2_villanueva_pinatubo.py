class Patient:
    name:str
    bill_amount:float
    def __init__(self,name,bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount
    
    def get_name(self):
        return self.__name
        
    def get_bill_amount(self):
        return self.__bill_amount
        
    def set_name(self,name):
        self.__name = name
    
    def set_bill_amount(self,bill_amount):
        if bill_amount >= 0:
            self.__bill_amount = bill_amount
        else:
            print("Bill amount can not be negative.")
            
    def calculate_bill(self):
        return self.get_bill_amount()
        
class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80
        
class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85
        
regular_patient = Patient("Francesca Raymundo", 15000.00)
senior_patient = SeniorPatient("Zakiyyah Muneer Munnilakath", 15000.00)
philhealth_patient = PhilHealthPatient("Luisa Entac", 15000.00)

print("Hospital Billing System\n-------------------")

patients = [
    regular_patient,
    senior_patient,
    philhealth_patient,
]

for patient in patients:
    print("Patient Name: ", patient.get_name())
    print("Original Bill: ₱{:,.2f}".format(patient.get_bill_amount()))
    print("Final Bill: ₱{:,.2f}".format(patient.calculate_bill()))
    print()
