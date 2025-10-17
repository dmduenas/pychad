class User():
    def __init__(self, id_number, fname, lname, age, marital_status, region, job):
        self.id_number = id_number
        self.fname = fname
        self.lname = lname
        self.age = age
        self.marital_status = marital_status
        self.region = region
        self.job = job

    def set_id_number(self, new_id_number):
        self.id_number = new_id_number

    def set_fname(self, new_fname):
        self.fname = new_fname
    
    def set_lname(self, new_lname):
        self.lname = new_lname

    def set_age(self, new_age):
        self.age = new_age

    def set_marital_status(self, new_marital_status):
        self.marital_status = new_marital_status

    def set_region(self, new_region):
        self.region = new_region

    def set_job(self, new_job):
        self.job = new_job

new_id_number = input("Enter ID Number: ")
new_fname = input("Enter First Name: ")
new_lname = input("Enter Last Name: ")
new_age = int(input("Enter Age: "))
new_marital_status = input("Enter Marital Status: ")
new_region = input("Enter Region: ")
new_job = input("Enter Job Description: ")

user = User(new_id_number, new_fname, new_lname, new_age, new_marital_status, new_region, new_job)