#report doctor - patient details 
class Person:
    def __init__(self,name,age,gender):
        self.Name=name
        self.Age=age
        self.Gender=gender
    def Details(self):
        print(f"Name of the person: ",{self.Name})
        print(f"Age of the Person: ",{self.Age})
        print(f"Gender of the person : ",{self.Gender})
class Patient(Person):
    def __init__(self,name,age,gender,disease):
        super().__init__(name,age,gender)
        self.Disease=disease
    def Details(self):
        print(f"Name of the Patient: ",{self.Name})
        print(f"Age of the Patient: ",{self.Age})
        print(f"Gender of the Patient: ",{self.Gender})
        print("Disease of the Patient: ",{self.Disease})   
class Doctor(Person):
    def __init__(self, name, age, gender,specialization):
        super().__init__(name, age, gender)
        self.Specialization=specialization
        self._patients = []
    def assign_patient(self,patient):
        self.__patients.append(patient)    
    def Details(self):
        print(f"Name of the Doctor: ",{self.Name})
        print(f"Age of the Doctor: ",{self.Age})
        print(f"Gender of the Doctor: ",{self.Gender})
        print(f"Specialization of the Doctor: ",{self.Specialization})
    def Details_Patients(self):
        if not self._patients:
            return "No patients assigned"
        results = ""
        for p in self._patients:
            result += f"- {p.name}({p.disease})\n"
        return result.strip()
doctors=[]
Patients=[]
def find_doctor_by_name(name):
    for doc in doctors:
        if doc.name.lower()==name.lower():
            return doc 
    return None
 
           

              
