from tkinter import *
import tkinter.messagebox
import mysql.connector
from tkinter import ttk
import random
import time
import datetime

class window1:
    def __init__(self,user1):
        self.user1 = user1
        self.user1.title("ITClub Management System")
        self.user1.geometry("1000x600+0+0")
        self.frame = Frame(self.user1,bg="indigo")
        self.frame.pack()
        
        #### creating variables for each #####
        self.Username = StringVar()
        self.password = StringVar()
        
        self.LabelTitle = Label(self.frame, text="ITClub Management System", font=("Arial bold", 50), bd=20)
        self.LabelTitle.grid(row=0, column=0, columnspan=2, pady=20)
        
        self.Loginframe1 = Frame(self.frame, width=1010, height=300, bd=20, relief="ridge", bg="brown")
        self.Loginframe1.grid(row=1, column=0,)
        
        self.Loginframe2 = Frame(self.frame, width=1000, height=100, bd=20, relief="ridge", bg="purple")
        self.Loginframe2.grid(row=2, column=0)

        self.Loginframe3 = Frame(self.frame, width=1000, height=200, bd=20, relief="ridge", bg="black")
        self.Loginframe3.grid(row=3, column=0, pady=2)
        
        #---------------------------------------------------
        self.lblUsername = Label(self.Loginframe1, text="Username", font=("Arial bold", 30), bd=22, fg="gray", bg="brown")
        self.lblUsername.grid(row=0, column=0)
        self.txtUsername = Entry(self.Loginframe1, font=("Arial bold", 30), bd=22, textvariable=self.Username, fg="blue", bg="gray")
        self.txtUsername.grid(row=0, column=1)
        
        self.lblPassword = Label(self.Loginframe1, text="Password", font=("Arial bold", 30), bd=22, fg="gray", bg="brown")
        self.lblPassword.grid(row=1, column=0)
        self.txtpassword = Entry(self.Loginframe1, font=("Arial bold", 30), bd=22, textvariable=self.password, fg="blue", bg="gray")
        self.txtpassword.grid(row=1, column=1, padx=85)
        #---------------------------------------------------
        
        self.btnLogin = Button(self.Loginframe2, text="Login", width=17, bg="blue", fg="white", font=("arial bold", 20), command=self.LoginSystem)
        self.btnLogin.grid(row=0, column=0)
        
        self.btnReset = Button(self.Loginframe2, text="Reset", font=("arial bold", 20), width=17, bg="green", command=self.Reset)
        self.btnReset.grid(row=0, column=1)
        
        self.btnExit = Button(self.Loginframe2, text="Exit", font=("arial bold", 20), width=17, bg="red", command=self.Exit)
        self.btnExit.grid(row=0, column=2)
        
        ### btn takes u to student registration form ###
        self.btnRegistration = Button(self.Loginframe3, text="Student Registration System", font=("arial bold", 20), state=DISABLED, command=self.Registration_window, bg="orange")
        self.btnRegistration.grid(row=0, column=0)
        
        ### btn takes u to IT department form ###
        self.btnDepartment = Button(self.Loginframe3, text="IT Department Management System", font=("arial bold", 20), state=DISABLED, command=self.department_window, bg="violet")
        self.btnDepartment.grid(row=0, column=1, pady=8, padx=22)
    
    #------------------------------------------------------------
    def LoginSystem(self):
        user = (self.Username.get())
        pas = (self.password.get())
        if (user == str(1234)) and (pas == str(123)):
            self.btnRegistration.config(state=NORMAL)
            self.btnDepartment.config(state=NORMAL)
        else:
            tkinter.messagebox.askyesno("ITClub Management System","You have entered and invalid login details")
            self.btnRegistration.config(state=DISABLED)
            self.btnDepartment.config(state=DISABLED)
            self.Username.set("")
            self.password.set("")
            self.txtUsername.focus()
            
    def Reset(self):
        self.btnRegistration.config(state=DISABLED)
        self.btnDepartment.config(state=DISABLED)
        self.Username.set("")
        self.password.set("")
        self.txtUsername.focus()
        
    def Exit(self):
        self.Exit = tkinter.messagebox.askyesno("ITClub Management System","Confirm if you want to exit")
        if self.Exit > 0:
            self.user1.destroy()
            return
    #------------------------------------------------------------
    def Registration_window(self):
        self.new_window = Toplevel(self.user1)
        self.app = window2(self.new_window)
        
    def department_window(self):
        self.new_window = Toplevel(self.user1)
        self.app = window3(self.new_window)
        
        
class window2:
    def __init__(self, user1):
        self.user1 = user1
        self.user1.title("ITStudent Registration System")
        self.user1.geometry("1350x750+0+0")
        # self.frame = Frame(self.user1)
        #self.frame.pack()
        
        #-------------------------------------------------------------------------
        DateofOrder = StringVar()
        DateofOrder.set(time.strftime("%d,%m,%Y"))
        
        var1=StringVar()
        var2=StringVar()
        var3=StringVar()
        var4=IntVar()
        
        firstname = StringVar()
        surname = StringVar()
        Address = StringVar()
        Email = StringVar()
        Telephone = StringVar()
        Ref = StringVar()
        
        Subscription = StringVar()
        Subscription.set("0")
        ####### functions declared ####
        
        def iExit():
            iExit = tkinter.messagebox.askyesno("ITClub Registration System", "Confirm if you want to exit")
            if iExit > 0:
                user1.destroy()
                return
            
        def iReset():
            firstname.set("")
            surname.set("")
            Address.set("")
            Email.set("")
            Telephone.set("")
            Ref.set("")
            Subscription.set("0")
            
            var1.set("")
            var2.set("")
            var3.set("")
            var4.set(0)
            
            self.cmboProve.current(0)
            self.cmboTypeOfMember.current(0)
            self.cmboMethodOfPayment.current(0)
            
        def iResetRecord():
            iResetRecord = tkinter.messagebox.askokcancel("ITClub Member Registration System","Confirm that you want to reset record")
            if iResetRecord >0:
                iReset()
            elif iResetRecord<= 0:
                iReset()
                #self.btnDelete.delete("1.0",END)
                return
            
        def Ref_No():
            #Member_Ref=StringVar
            x = random.randint(10903,600873)
            randomRef = str(x)
            Ref.set(randomRef)
            
        def delete_student_details():
            selected_item = self.tree.selection()
            for item in selected_item:
                self.tree.delete(item)
            
        def add_student_details():
            
            if not (firstname.get() and surname.get() and Address.get() and Email.get() and Telephone.get()) and Subscription.get():
                tkinter.messagebox.showwarning("Warning", "Please fill in all required fields.")
                return
            
            Ref_No()
            # Get values from entry widgets
            reference_no = Ref.get()
            first_name = firstname.get()
            surname_val = surname.get()
            address_val = Address.get()
            email_val = Email.get()
            telephone_val = Telephone.get()
            date_val = DateofOrder.get()
            subscription_val = Subscription.get()
            
            # Insert values into Treeview widget
            self.tree.insert("", "end", values=(reference_no, first_name, surname_val, address_val, date_val, telephone_val, email_val, subscription_val))
            
            # Optionally, clear the entry widgets after adding
            iReset()
            
        # def Receipt():
        #     self.txtReceipt.delete("1.0",END)
        #     self.txtReceipt.insert(END,"\t"+ "IT Club Member Registration System" + "\n\n")
        #     self.txtReceipt.insert(END, "Reference:\t\t\t" + Ref.get() + "\n")
        #     self.txtReceipt.insert(END, "Firstname:\t\t\t" + firstname.get() + "\n")
        #     self.txtReceipt.insert(END, "Surname:\t\t\t" + surname.get() + "\n")
        #     self.txtReceipt.insert(END, "Address:\t\t\t" + Address.get() + "\n")
        #     self.txtReceipt.insert(END, "Telephone:\t\t\t" + Telephone.get() + "\n")
        #     self.txtReceipt.insert(END, "Email:\t\t\t" + Email.get() + "\n")
        #     self.txtReceipt.insert(END, "Subscription:\t\t\t" + Subscription.get() + "\n")
        #     self.txtReceipt.insert(END, "Date:\t\t\t" + DateofOrder.get() + "\n")
            
        def Subscription_Fees():
            if (var4.get() == 1):
                self.txtSubscription.configure(state=NORMAL)
                Item1 = float(50)
                Subscription.set("Ugx" + str(Item1))
            elif (var4.get() == 0):
                self.txtSubscription.configure(state=DISABLED)
                Subscription.set("0")
                
        #------------------- FRAME ----------------------------------------------------------------#
        Mainframe = Frame(self.user1)
        Mainframe.pack(fill=BOTH, expand=True)
        
        TitleFrame = Frame(Mainframe,bd=20,width=1350,padx=26,relief="ridge")
        TitleFrame.pack(side=TOP)
        
        self.lblTitle=Label(TitleFrame,font=("arial bold",59),text="Member Registration System",padx=3,justify=CENTER)
        self.lblTitle.pack()
        
        MemberDetailsFrame = LabelFrame(Mainframe, text="Students' Details", bd=10, padx=20, pady=20, relief=RIDGE)
        MemberDetailsFrame.pack(side=LEFT, fill=BOTH, expand=True)
        
        FrameDetails = LabelFrame(MemberDetailsFrame,bd=10,width=880,height=400,relief=RIDGE)
        FrameDetails.pack(side=LEFT)
        
        MemberName_F = LabelFrame(FrameDetails,bd=10,width=350,height=400,font=("arial bold",12),text="Students' Details",relief=RIDGE)
        MemberName_F.grid(row=0,column=0)
        
        Receipt_BtnFrame = LabelFrame(MemberDetailsFrame,bd=10,width=1000,height=400,relief=RIDGE)
        Receipt_BtnFrame.pack(side=BOTTOM,expand=True)
        
        ###################### labels, entries, and comboboxes #################################
        
        self.lblReference = Label(MemberName_F, font=("arial bold",15),text="Reference No:",bd=7)
        self.lblReference.grid(row=0,column=0,sticky=W)    
        self.txtReference = Entry(MemberName_F,textvariable=Ref,font=("arial bold",15),bd=7,state=DISABLED,insertwidth=2)
        # self.entry_email = tk.Entry(user)
        #self.entryReference = tkinter.Entry(user1)
        self.txtReference.grid(row=0,column=1)    
        
        self.lblFirstName = Label(MemberName_F, font=("arial bold",15),text="FirstName:",bd=7)
        self.lblFirstName.grid(row=1,column=0,sticky=W)  
        #self.name=tkinter.Entry(user1)
        self.txtFirstName = Entry(MemberName_F,textvariable=firstname,font=("arial bold",15),bd=7,insertwidth=2)
        self.txtFirstName.grid(row=1,column=1)    
        
        self.lblUsername = Label(MemberName_F, font=("arial bold",15),text="Surname:",bd=7)
        self.lblUsername.grid(row=2,column=0,sticky=W)    
        self.txtUsername = Entry(MemberName_F,textvariable=surname,font=("arial bold",15),bd=7,insertwidth=2)
        self.txtUsername.grid(row=2,column=1)    
        
        self.lblEmail = Label(MemberName_F, font=("arial bold",15),text="Email:",bd=7)
        self.lblEmail.grid(row=3,column=0,sticky=W)    
        self.txtEmail = Entry(MemberName_F,textvariable=Email,font=("arial bold",15),bd=7,insertwidth=2)
        self.txtEmail.grid(row=3,column=1)
        
        self.lblAddress = Label(MemberName_F, font=("arial bold",15),text="Address:",bd=7)
        self.lblAddress.grid(row=4,column=0,sticky=W)    
        self.txtAddress = Entry(MemberName_F,textvariable=Address,font=("arial bold",15),bd=7,insertwidth=2)
        self.txtAddress.grid(row=4,column=1) 
        
        self.lblTelephone = Label(MemberName_F, font=("arial bold",15),text="Telephone No:",bd=7)
        self.lblTelephone.grid(row=5,column=0,sticky=W)    
        self.txtTelephone = Entry(MemberName_F,textvariable=Telephone,font=("arial bold",15),bd=7,insertwidth=2)
        self.txtTelephone.grid(row=5,column=1) 
        
        self.lblDate = Label(MemberName_F, font=("arial bold",15),text="Date:",bd=7)
        self.lblDate.grid(row=6,column=0,sticky=W)    
        self.txtDate = Entry(MemberName_F,textvariable=DateofOrder,font=("arial bold",15),bd=7,insertwidth=2)
        self.txtDate.grid(row=6,column=1) 
        
        self.lblProve = Label(MemberName_F, font=("arial bold",15),text="Prove of ID:",bd=7)
        self.lblProve.grid(row=7,column=0,sticky=W)
        self.cmboProve = ttk.Combobox(MemberName_F, font=("arial bold",15),state="readonly",width=19,textvariable=var1)
        self.cmboProve["value"]=("",'National ID','Student ID','Passport','Driving Licence','Pilot Licence')
        self.cmboProve.current(0)
        #self.txtProve = Entry(MemberName_F,font=("arial bold",15),bd=7,insertwidth=2)
        self.cmboProve.grid(row=7,column=1) 
        
        self.lblTypeOfMember = Label(MemberName_F, font=("arial bold",15),text="Type of Member:",bd=7)
        self.lblTypeOfMember.grid(row=8,column=0,sticky=W) 
        self.cmboTypeOfMember= ttk.Combobox(MemberName_F, font=("arial bold",15),state="readonly",width=19,textvariable=var2)
        self.cmboTypeOfMember["value"]=("",'Full Member','Annual Member','Monthly Member','Pay As You Go','Honorary Member')
        self.cmboTypeOfMember.current(0)   
        #self.txtTypeOfMember = Entry(MemberName_F,font=("arial bold",15),bd=7,insertwidth=2)
        self.cmboTypeOfMember.grid(row=8,column=1) 
        
        self.lblMethodOfPayment = Label(MemberName_F, font=("arial bold",15),text="Method Payment:",bd=7)
        self.lblMethodOfPayment.grid(row=9,column=0,sticky=W)    
        self.cmboMethodOfPayment= ttk.Combobox(MemberName_F, font=("arial bold",15),state="readonly",width=19,textvariable=var3)
        self.cmboMethodOfPayment["value"]=("",'Cash','Master Card','Debit Card','Visa Card','Banking')
        self.cmboMethodOfPayment.current(0)
        #self.txtMethodOfPayment = Entry(MemberName_F,font=("arial bold",15),bd=7,insertwidth=2)
        self.cmboMethodOfPayment.grid(row=9,column=1) 
        
        self.chkSubscription = Checkbutton(MemberName_F,text="Subscription Fee",variable=var4,onvalue=1,offvalue=0,command=Subscription_Fees,font=("arial bold",16))
        self.chkSubscription.grid(row=10,column=0,sticky=W)
        self.txtSubscription = Entry(MemberName_F,font=("arial bold",15),textvariable=Subscription,bd=7, insertwidth=2,state=DISABLED,justify=RIGHT)
        self.txtSubscription.grid(row=10,column=1)
        
    
        
        # self.chkConfirm = Checkbutton(MemberName_F, text="I hereby confirm that the details above are true",
        #                                 variable=var4, onvalue=1, offvalue=0, font=('arial', 12, 'bold'),
        #                                 command=Subscription_Fees)
        # self.chkConfirm.grid(row=11, column=1, sticky=W)
        
        ###################### Treeview Widget #################################
        
        self.tree = ttk.Treeview(MemberDetailsFrame, columns=("Reference No", "First Name", "Surname", "Address", "Date", "Telephone", "Email", "Subscription Fee"), show="headings")
        self.tree.pack(side=BOTTOM, fill=BOTH, expand=True)
        
        # Define column headings
        self.tree.heading("Reference No", text="Reference No")
        self.tree.heading("First Name", text="First Name")
        self.tree.heading("Surname", text="Surname")
        self.tree.heading("Address", text="Address")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Telephone", text="Telephone")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Subscription Fee", text="Subscription Fee")
        
        # Add scrollbars
        scrollbar_y = ttk.Scrollbar(MemberDetailsFrame, orient="vertical", command=self.tree.yview)
        scrollbar_y.pack(side=BOTTOM, fill="y")
        self.tree.configure(yscrollcommand=scrollbar_y.set)
        
        scrollbar_x = ttk.Scrollbar(MemberDetailsFrame, orient="horizontal", command=self.tree.xview)
        scrollbar_x.pack(side=BOTTOM, fill="x")
        self.tree.configure(xscrollcommand=scrollbar_x.set)
        
        # Buttons
        self.btnAdd = Button(Receipt_BtnFrame, bd=7, width=13,bg="green",fg="white", text="Add", font=("arial bold", 10), padx=10, command=add_student_details)
        self.btnAdd.grid(row=1, column=0)
        #self.btnAdd.pack(side=RIGHT, padx=1)
        
        self.btnReset = Button(Receipt_BtnFrame, bd=7, width=13,bg="violet",fg="white", text="Reset", font=("arial bold", 10), padx=10, command=iResetRecord)
        self.btnReset.grid(row=1, column=1)
        #self.btnReset.pack(side=RIGHT, padx=1)
        
        self.btnDelete = Button(Receipt_BtnFrame, bd=7, width=13,bg="indigo",fg="white", text="Delete", font=("arial bold", 10), padx=10, command=delete_student_details) # Add the function you want for delete
        self.btnDelete.grid(row=1, column=2)
        #self.btnDelete.pack(side=LEFT, padx=1)
        
        self.btnExit = Button(Receipt_BtnFrame, bd=7, width=13,bg="red",fg="white", text="Exit", font=("arial bold", 10), padx=10, command=iExit)
        self.btnExit.grid(row=1, column=3)
        #self.btnExit.pack(side=LEFT, padx=1)
        
        
        self.lblSearch = Button(Receipt_BtnFrame, font=("arial bold", 15), text="Search:", bd=7,command=self.search_student_details)
        self.lblSearch.grid(row=0, column=0, sticky=W)
        self.txtSearch = Entry(Receipt_BtnFrame, font=("arial bold", 15), bd=7)
        self.txtSearch.grid(row=0, columnspan=3)
        self.txtSearch.bind("<Return>", self.search_student_details)

        # Function to handle search
    def search_student_details(self):
        search_query = self.txtSearch.get()
        if search_query:
            found_items = []
            for child in self.tree.get_children():
                item_values = self.tree.item(child)["values"]
                if any(search_query.lower() in str(value).lower() for value in item_values):
                    found_items.append(child)
            # Clear current selection
            self.tree.selection_remove(self.tree.selection())
            # Highlight found items
            for item in found_items:
                self.tree.selection_add(item)
                self.tree.focus(item)
                self.tree.see(item)
        
class window3:
    def __init__(self,user1):
        self.user1 = user1
        self.user1.title("ITDepartment Management System")
        self.user1.geometry("1350x750+0+0")
        self.frame = Frame(self.user1)
        self.frame.pack()
        self.LabelTitle = Label(self.frame, text = "ITDepartment Management System", font=("Arial bold",50),bd=20)
        self.LabelTitle.grid(row=0, column=0,columnspan=2,pady= 20)
        
if __name__ == "__main__":
    root = Tk()
    application = window1(root)
    root.resizable(1,1)
    root.mainloop()
    