from tkinter import *
import sqlite3
import addpeople
from tkinter import messagebox


con=sqlite3.connect('database.db')
cur = con.cursor()

class MyPoeple(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650+620+200")
        self.title("My Poeple")
        self.resizable(False,False)

        # Frames
        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottomFrame = Frame(self, height=500, bg='#fcc324')
        self.bottomFrame.pack(fill=X)

        # Heading, image and date
        self.top_image = PhotoImage(file='icons/person_icon.png')
        self.top_image_lbl = Label(self.top, image=self.top_image, bg='white')
        self.top_image_lbl.place(x=120, y=10)
        self.heading = Label(self.top, text='My Persons', font='arial 15 bold',
                             fg='#003f8a', bg='white')
        self.heading.place(x=260, y=60)
        #ScrollBar
        self.sb=Scrollbar(self.bottomFrame,orient=VERTICAL)
        #listbox
        self.listBox=Listbox(self.bottomFrame,width=60,height=31)
        self.listBox.grid(row=0, column=0,padx=(40,0))
        self.sb.config(command= self.listBox.yview)
        self.listBox.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0,column=1,sticky=N+S)

        persons=cur.execute("SELECT * FROM persons").fetchall()
        print(persons)
        count=0
        for person in persons:
            self.listBox.insert(count,str(person[0])+"-"+person[1]+" "+person[2])
            count +=1

        #Buttons
        btnadd=Button(self.bottomFrame,text='Add',width=12,font='Sans 12 bold',command=self.funcaddPeople)
        btnadd.grid(row=0,column=2,sticky=N,padx=10,pady=10)

        btnupdate = Button(self.bottomFrame, text='Update', width=12, font='Sans 12 bold',
                           command=self.funcUpdatePerson)
        btnupdate.grid(row=0, column=2, sticky=N, padx=10, pady=50)

        btndisplay = Button(self.bottomFrame, text='Display', width=12, font='Sans 12 bold',
                            command=self.funcDisplayPerson)
        btndisplay.grid(row=0, column=2, sticky=N, padx=10, pady=90)

        btndelete = Button(self.bottomFrame, text='Delete', width=12, font='Sans 12 bold',
                           command=self.funcDeletePerson)
        btndelete.grid(row=0, column=2, sticky=N, padx=10, pady=130)


    def funcaddPeople(self):
        addpage=addpeople.AddPeople()
        self.destroy()

    def funcUpdatePerson(self):
        global person_id
        selected_item=self.listBox.curselection()
        person=self.listBox.get(selected_item)
        person_id=person.split("-")[0]
        updatepage=Update()
    def funcDisplayPerson(self):
        global person_id
        selected_item = self.listBox.curselection()
        person= self.listBox.get(selected_item)
        person_id=person.split("-")[0]
        displaypage=Display()
        self.destroy()

    def funcDeletePerson(self):
        selected_item=self.listBox.curselection()
        person=self.listBox.get(selected_item)
        person_id=person.split("-")[0]

        mbox= messagebox.askquestion("Warning","Are you sure to delete this person",icon='warning')

        if mbox == 'yes':
            try:
                cur.execute("DELETE FROM persons WHERE person_id=?", (person_id,))
                con.commit()
                messagebox.showinfo("Success","Person has been deleted!")
                self.destroy()


            except:
                messagebox.showinfo("Info","Person has not been deleted!")

class Update(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Update Person")
        self.resizable(False,False)

        #get person from database
        global person_id

        person=cur.execute("SELECT * FROM persons WHERE person_id =?",(person_id,))
        person_info = person.fetchall()
        print(person_info)
        self.person_id=person_info[0][0]
        self.person_name=person_info[0][1]
        self.person_surname=person_info[0][2]
        self.person_email=person_info[0][3]
        self.person_phone=person_info[0][4]
        self.person_address=person_info[0][5]

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

        # labels and entries
        # name
        self.lbl_name = Label(self.bottomFrame, text='Name', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_name.place(x=40, y=40)
        self.ent_name = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_name.insert(0, self.person_name)
        self.ent_name.place(x=150, y=45)

        # Surname
        self.lbl_surname = Label(self.bottomFrame, text='Surname', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_surname.place(x=40, y=80)
        self.ent_surname = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_surname.insert(0, self.person_surname)
        self.ent_surname.place(x=150, y=85)

        # email
        self.lbl_email = Label(self.bottomFrame, text='Email', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_email.place(x=40, y=120)
        self.ent_email = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_email.insert(0, self.person_email)
        self.ent_email.place(x=150, y=125)

        # Phone Number
        self.lbl_phone = Label(self.bottomFrame, text='Phone', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_phone.place(x=40, y=160)
        self.ent_phone = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_phone.insert(0, self.person_phone)
        self.ent_phone.place(x=150, y=165)

        # Address

        self.lbl_address = Label(self.bottomFrame, text='Address', font='arial 15 bold',
                                 fg='white', bg='#fcc324')
        self.lbl_address.place(x=40, y=300)
        self.address = Text(self.bottomFrame, width=23, height=15, wrap=WORD)
        self.address.insert('1.0',self.person_address)
        self.address.place(x=150, y=200)

        # Button
        button = Button(self.bottomFrame, text='Update Person',command=self.updatePerson)
        button.place(x=270, y=460)
        self.lift()


    def updatePerson(self):
        person_id=self.person_id
        person_name=self.ent_name.get()
        person_surname=self.ent_surname.get()
        person_email = self.ent_email.get()
        person_phone = self.ent_phone.get()
        person_address = self.address.get(1.0,'end-1c')


        try:
            query= "UPDATE persons set person_name =?, person_surname=?, person_email=?, person_phone=?, person_address =? WHERE person_id=?"
            cur.execute(query,(person_name,person_surname,person_email,person_phone,person_address,person_id))
            con.commit()
            messagebox.showinfo("Success","Person has been updated")
            self.destroy()
        except:
            messagebox.showinfo("Warning", "Person has not been updated",icon='warning')

class Display(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Display Person")
        self.resizable(False,False)

        # get person from database
        global person_id

        person = cur.execute("SELECT * FROM persons WHERE person_id =?", (person_id,))
        person_info = person.fetchall()
        print(person_info)
        self.person_id = person_info[0][0]
        self.person_name = person_info[0][1]
        self.person_surname = person_info[0][2]
        self.person_email = person_info[0][3]
        self.person_phone = person_info[0][4]
        self.person_address = person_info[0][5]

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

        # labels and entries
        # name
        self.lbl_name = Label(self.bottomFrame, text='Name', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_name.place(x=40, y=40)
        self.ent_name = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_name.insert(0, self.person_name)
        self.ent_name.config(state='disabled')
        self.ent_name.place(x=150, y=45)

        # Surname
        self.lbl_surname = Label(self.bottomFrame, text='Surname', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_surname.place(x=40, y=80)
        self.ent_surname = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_surname.insert(0, self.person_surname)
        self.ent_surname.config(state='disabled')
        self.ent_surname.place(x=150, y=85)

        # email
        self.lbl_email = Label(self.bottomFrame, text='Email', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_email.place(x=40, y=120)
        self.ent_email = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_email.insert(0, self.person_email)
        self.ent_email.config(state='disabled')
        self.ent_email.place(x=150, y=125)

        # Phone Number
        self.lbl_phone = Label(self.bottomFrame, text='Phone', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_phone.place(x=40, y=160)
        self.ent_phone = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_phone.insert(0, self.person_phone)
        self.ent_phone.config(state='disabled')
        self.ent_phone.place(x=150, y=165)

        # Address

        self.lbl_address = Label(self.bottomFrame, text='Address', font='arial 15 bold',
                                 fg='white', bg='#fcc324')
        self.lbl_address.place(x=40, y=300)
        self.address = Text(self.bottomFrame, width=23, height=15, wrap=WORD)
        self.address.insert('1.0', self.person_address)
        self.address.config(state='disabled')
        self.address.place(x=150, y=200)
