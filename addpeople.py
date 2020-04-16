from tkinter import *
import sqlite3
from tkinter import messagebox


con=sqlite3.connect('database.db')
cur=con.cursor()



class AddPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Add People")
        self.resizable(False,False)

        # Frames
        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottomFrame = Frame(self, height=600, bg='#fcc324')
        self.bottomFrame.pack(fill=X)

        # Heading, image and date
        self.top_image = PhotoImage(file='icons/addperson.png')
        self.top_image_lbl = Label(self.top, image=self.top_image, bg='white')
        self.top_image_lbl.place(x=120, y=10)
        self.heading = Label(self.top, text='My Persons', font='arial 15 bold',
                             fg='#003f8a', bg='white')
        self.heading.place(x=260, y=60)

        ##############################################################################

        #labels and entries
        #name
        self.lbl_name=Label(self.bottomFrame,text='Name',font='arial 15 bold',fg='white',bg='#fcc324')
        self.lbl_name.place(x=40,y=40)
        self.ent_name=Entry(self.bottomFrame,width=30,bd=4)
        self.ent_name.insert(0,'Please enter a name')
        self.ent_name.place(x=150,y=45)

        #Surname
        self.lbl_surname = Label(self.bottomFrame, text='Surname', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_surname.place(x=40, y=80)
        self.ent_surname= Entry(self.bottomFrame, width=30, bd=4)
        self.ent_surname.insert(0, 'Please enter a Surname')
        self.ent_surname.place(x=150, y=85)

        #email
        self.lbl_email = Label(self.bottomFrame, text='Email', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_email.place(x=40, y=120)
        self.ent_email = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_email.insert(0, 'Please enter an Email')
        self.ent_email.place(x=150, y=125)

        #Phone Number
        self.lbl_phone = Label(self.bottomFrame, text='Phone', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_phone.place(x=40, y=160)
        self.ent_phone = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_phone.insert(0, 'Please enter a Phone Number')
        self.ent_phone.place(x=150, y=165)

        #Address

        self.lbl_address = Label(self.bottomFrame, text='Address', font='arial 15 bold',
                                 fg='white', bg='#fcc324')
        self.lbl_address.place(x=40, y=300)
        self.address = Text(self.bottomFrame, width=23, height=15,wrap=WORD)
        self.address.place(x=150, y=200)

        #Button
        button=Button(self.bottomFrame,text='Add Person',command=self.addPerson)
        button.place(x=270,y=460)
        self.lift()
    def addPerson(self):
        name=self.ent_name.get()
        surname=self.ent_surname.get()
        email=self.ent_email.get()
        phone=self.ent_phone.get()
        address=self.address.get(1.0,'end-1c')

        if(name and surname and email and phone and address !=""):
            try:
                query="INSERT INTO 'persons' (person_name,person_surname,person_email,person_phone,person_address) VALUES(?,?,?,?,?)"
                cur.execute(query,(name,surname,email,phone,address))
                con.commit()
                messagebox.showinfo("Success","Successfully added to database!",icon='info')

            except:
                messagebox.showerror("Error", "Cant add to database!", icon='warning')

        else:
            messagebox.showerror("Error","Fields cant be empty!",icon='warning')




