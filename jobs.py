from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import random

root = Tk()
root.title("Jobs")
root.geometry("800x500")
root.configure(background="LightBlue1")

label_title = Label(root, font=("courier", 18, "bold"), text="Connecting Jobs", bg="LightBlue1")
label_title.place(relx=0.5, rely=0.1, anchor=CENTER)

label_selected_doctor = Label(root, bg="LightBlue1")
label_selected_doctor.place(relx=0.01, rely=0.3, anchor=W)

label_selected_IT = Label(root, bg="LightBlue1")
label_selected_IT.place(relx=0.01, rely=0.6, anchor=W)

label_selected_chemical = Label(root, bg="LightBlue1")
label_selected_chemical.place(relx=0.01, rely=0.9, anchor=W)

class parent():
    def __init__(self):
        print("This is the parent class")
    
    def doctor(doctor_name):
        hospital_list = ["ICSS", "City Hospital", "City Care", "Galaxy"]
        random_hospital = random.randint(0,3)
        label_selected_doctor['text'] = doctor_name + " has been alloted to " + hospital_list[random_hospital]
    
    def softwareEngineer(it_professional_name):
        IT_company_list = ["Z code", "Web Access", "Dotcom Services", "ATOS"]
        random_IT_company = random.randint(0,3)
        label_selected_IT["text"] = it_professional_name + " has been alloted to " + IT_company_list[random_IT_company]

    def chemicalEngineer(chemical_engineer_name):
        company_list = ["Som Labs", "B.O.T. chemical services", "Combus"]
        random_company = random.randint(0,2)
        label_selected_chemical['text'] = chemical_engineer_name + " has been alloted to " + company_list[random_company]

class doctor(parent):
    def __init__(self):
        print("This is the doctor class")
    def getDoctor(self):
        name = "Micheal"
        parent.doctor(name)
        
class engineer(parent):
    def __init__(self):
        print("This is the engineer class")
    def getIT(self):
        name = "Jessica"
        parent.softwareEngineer(name) 

class chemical(parent):
    def __init__(self):
        print("This is the chemical class")
    def getChemical(self):
        name = "John"
        parent.chemicalEngineer(name)

obj1 = doctor()
obj2 = engineer()
obj3 = chemical()

btn_doctor = Button(root, text="Show the hospital alloted", command=obj1.getDoctor, bg="light goldenrod")
btn_doctor.place(relx=0.1, rely=0.23,anchor=CENTER)

btn_it = Button(root, text="Show the IT company alloted", command=obj2.getIT, bg="light goldenrod")
btn_it.place(relx=0.11, rely=0.53,anchor=CENTER)

btn_chemical = Button(root, text="Show the chemical company alloted", command=obj3.getChemical, bg="light goldenrod")
btn_chemical.place(relx=0.13, rely=0.83,anchor=CENTER)

root.mainloop()