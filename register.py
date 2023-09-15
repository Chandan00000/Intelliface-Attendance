from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from database import Database
class registration:
    def __init__(self,root,db):
        self.root=root
        self.root.title("New User Registration")
        self.root.attributes('-fullscreen', True)
        self.admin=Database("admin","admin-data")
        #Variables
        self.v_fname=StringVar()
        self.v_lname=StringVar()
        self.v_contact=StringVar()
        self.v_email=StringVar()
        self.v_securityq=StringVar()
        self.v_securitya=StringVar()
        self.v_pw=StringVar()
        self.v_pwcnf=StringVar()
        self.v_check=IntVar()
        self.v_check.set(0)


        #background image
        self.background=ImageTk.PhotoImage(file=r".\resources\bgb.jpg")
        background_label=Label(self.root,image=self.background)
        background_label.place(x=0,y=0,relwidth=1,relheight=1 )

        
        # #welcome
        # welcome_lbl=Label(root,text="WELCOME TO NEW USER REGISTRATION",font=("times new roman",40,"bold"),fg="#990066",bg="black")
        # welcome_lbl.place(x=225,y=200)

        #left image       
        left_pic=Image.open(r".\resources\left.jpg")
        left_pic=left_pic.resize((450,450),Image.LANCZOS)
        self.photoleft_pic=ImageTk.PhotoImage(left_pic)
        label_lp=Label(self.root,image=self.photoleft_pic,borderwidth=0,bg="black")
        label_lp.place(x=200,y=300,width=350,height=319)


        #main frame
        frame=Frame(self.root,bg="black")
        frame.place(x=550,y=300,width=800,height=320)

        register_label=Label(frame,text="REGISTER NOW",font=("Calibri",20,"bold"),fg="red",bg="black")
        register_label.place(x=20,y=20)

        firstname=Label(frame,text="First Name",font=("times new roman",15),fg="white",bg="black")
        firstname.place(x=30,y=75)
        firstname_entry=ttk.Entry(frame,textvariable=self.v_fname,font="timesnewroman 13")
        firstname_entry.place(x=145,y=80,width=150)

        lastname=Label(frame,text="Last Name",font=("times new roman",15),fg="white",bg="black")
        lastname.place(x=380,y=75)
        lastname_entry=ttk.Entry(frame,textvariable=self.v_lname,font="timesnewroman 13")
        lastname_entry.place(x=495,y=80,width=150)

        contact=Label(frame,text="Contact No.",font=("times new roman",15),fg="white",bg="black")
        contact.place(x=30,y=120)
        contact_entry=ttk.Entry(frame,textvariable=self.v_contact,font="timesnewroman 13")
        contact_entry.place(x=145,y=125,width=150)

        email=Label(frame,text="E-Mail",font=("times new roman",15),fg="white",bg="black")
        email.place(x=380,y=120)
        email_entry=ttk.Entry(frame,textvariable=self.v_email,font="timesnewroman 13")
        email_entry.place(x=495,y=125,width=150)

        securityq=Label(frame,text="Security Question",font=("times new roman",15),fg="white",bg="black")
        securityq.place(x=30,y=210)
        self.combo_securityq=ttk.Combobox(frame,textvariable=self.v_securityq,font=("times new roman",10),state="readonly")
        self.combo_securityq["values"]=("Choose","Your pet","1st school","Best friend","Nickname")
        self.combo_securityq.place(x=195,y=215,width=100)
        self.combo_securityq.current(0)

        securitya=Label(frame,text="Security Key",font=("times new roman",15),fg="white",bg="black")
        securitya.place(x=380,y=210)
        securitya_entry=ttk.Entry(frame,textvariable=self.v_securitya,font="timesnewroman 13")
        securitya_entry.place(x=495,y=215,width=150)

        password=Label(frame,text="Password",font=("times new roman",15),fg="white",bg="black")
        password.place(x=30,y=165)
        password_entry=ttk.Entry(frame,textvariable=self.v_pw,font="timesnewroman 13",show="*")
        password_entry.place(x=145,y=170,width=150)

        passwordcnf=Label(frame,text="Confirm Pass",font=("times new roman",15),fg="white",bg="black")
        passwordcnf.place(x=380,y=165)
        passwordcnf_entry=ttk.Entry(frame,textvariable=self.v_pwcnf,font="timesnewroman 13",show="*")
        passwordcnf_entry.place(x=495,y=170,width=150)

        #agreement button
        agree=Checkbutton(frame,variable=self.v_check,text="I Agree to the T/Cs",font=("times new roman",20),selectcolor='black',onvalue=1,offvalue=0,fg='white',bg='black',activebackground="black",activeforeground="white")
        agree.place(x=30,y=255)

        # Register Button
        img=Image.open(r".\resources\reg1.png")
        img=img.resize((150,70),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register,borderwidth=0,cursor="hand2",bg="black",activebackground="black")
        b1.place(x=440,y=245,width=170)

        #Back Button
        img=Image.open(r'.\resources\back_reg.jpg').resize((50,50),Image.LANCZOS)
        self.back_img=ImageTk.PhotoImage(image=img)
        back_button=Button(self.root,image=self.back_img,bd=0,highlightthickness=0,activebackground="black",command=self.backward).place(x=1440,y=35)

    def register(self):
        if self.v_fname.get()=="" or self.v_lname.get()=="" or self.v_email.get()=="" or self.v_contact.get()=="" or self.v_pw.get()=="" or self.v_pwcnf.get()=="" or self.v_securitya.get()=="" or self.v_securityq.get()=="Choose":
            messagebox.showwarning("Missing fields","All fields are required !",parent=self.root)
        elif len(self.v_pw.get())<6:
            messagebox.showwarning("","Password must contain atleast 6 characters",parent=self.root)
        elif self.v_pw.get()!=self.v_pwcnf.get():
            messagebox.showwarning("","Passwords does not match",parent=self.root)
        elif self.v_check.get()==0:
            messagebox.showwarning("","Please agree to the T/Cs",parent=self.root)
        else:
            ack=self.admin.admin_insert_data(self.v_fname.get().capitalize(),self.v_lname.get().capitalize(),self.v_pw.get(),self.v_contact.get(),self.v_email.get(),self.v_securityq.get(),self.v_securitya.get())
            if ack==True:
                messagebox.showinfo("Database","Admin info Registered !",parent=self.root)
                self.root.destroy()
            else:
                messagebox.showwarning("Database",ack,parent=self.root)

    def backward(self):
        # self.root.withdraw()
        self.root.destroy()

if __name__=="__main__":
    root=Tk()
    db=Database("admin","admin-data")
    ob=registration(root,db)
    root.mainloop()