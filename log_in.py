from tkinter import* 
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from register import registration
from database import Database

class login:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN PAGE")
        self.root.attributes('-fullscreen', True)
        
        # Database instance created 
        self.admin=Database("admin","admin-data")

        self.new_win=None

        self.background=ImageTk.PhotoImage(file=r".\resources\bgb.jpg")
        label_bg =Label(self.root, image=self.background)
        label_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root, bg="black")
        frame.place(x=820,y=190,width=450,height=550)

        picture=Image.open(r".\resources\mainpage.png")
        picture=picture.resize((600,600),Image.LANCZOS)
        self.photopicture=ImageTk.PhotoImage(picture)
        label_welcome=Label(self.root,image=self.photopicture,bg="#4e0553")
        label_welcome.place(x=220,y=190,width=600,height=550)

        welcome_to=Label(root,text="WELCOME TO INTELLIFACE ATTENDANCE SYSTEM",font=("brown sugar",31,"bold"),fg="white",bg="black")
        welcome_to.place(x=230,y=130)

        start=Label(root,text="ADMIN LOGIN",font=("Calibri",22,"bold"),fg="white",bg="black")
        start.place(x=950,y=320)

        icon1=Image.open(r".\resources\attendance.png")
        icon1=icon1.resize((100,100),Image.LANCZOS)
        self.photowelcome=ImageTk.PhotoImage(icon1)
        label_icon1=Label(image=self.photowelcome,borderwidth=0,bg="black")
        label_icon1.place(x=990,y=210,width=100,height=100)


        username=Label(root,text="Username\E-mail",font=("Times New Roman",15,"bold"),fg="white",bg="black")
        username.place(x=930,y=390)

        self.username=ttk.Entry(root,font=("Times New Roman",15,"bold"))
        self.username.place(x=930,y=420,width=250,height=30)

        password=Label(root,text="Password",font=("Times New Roman",15,"bold"),fg="white",bg="black")
        password.place(x=930,y=470)

        self.password=ttk.Entry(root,font=("Times New Roman",15,"bold"),show="*")
        self.password.place(x=930,y=500,width=250,height=30)

        login=Button(root,text="LOGIN",command=self.user_login,font=("Times New Roman",15,"bold"),fg="white",bg="red")
        login.place(x=1000,y=560,width=100)

        register=Button(root,text="Sign Up",font=("Times New Roman",12),command=self.reg,fg="white",bg="black",borderwidth=0,activebackground="black",activeforeground="white")
        register.place(x=930,y=620)

        Exit=Button(root,text="Exit",font=("Times New Roman",12),command=quit,fg="white",bg="black",borderwidth=0,activebackground="black",activeforeground="white")
        Exit.place(x=930,y=690)

        fp=Button(root,text="Forgot password?",font=("Times New Roman",12),command=self.forgotpw,fg="white",bg="black",borderwidth=0,activebackground="black",activeforeground="white")
        fp.place(x=930,y=660)
        

    def user_login(self):
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showwarning("Log In","All fields are required",parent=self.root)
        elif self.admin.check_credentials(self.username.get(),self.password.get())==1:
            self.root.destroy()
        elif self.admin.check_credentials(self.username.get(),self.password.get())==0:
            messagebox.showwarning("Invalid Credentials","Please enter correct Password",parent=self.root)
        elif self.admin.check_credentials(self.username.get(),self.password.get())==-1:
            messagebox.showwarning("Invalid Credentials","Username not found !",parent=self.root)
            
    #RESET PASSWORD
    def reset_password(self):
        if self.combo_securityq.get()=="Choose":
            messagebox.showwarning("Empty Fields","Select security question",parent=self.root1)
        elif self.securityAns.get()=="":
            messagebox.showwarning("Empty Fields","Enter security answer",parent=self.root1)
        elif self.admin.check_securityKey(self.username.get(),self.combo_securityq.get(),self.securityAns.get()):
            messagebox.showwarning("Invalid Credentials","Wrong security question/answer !",parent=self.root1)
        else:
            if self.btn.cget('text')=='Next':
                self.combo_securityq.place_forget()
                self.securityAns.place_forget()
                self.label_1.config(text="New Password")
                self.label_2.config(text="Confirm Password")
                self.entry_1.place(x=150,y=140,width=150)
                self.entry_2.place(x=150,y=250,width=150)
                self.btn.config(text='Submit')
            else:
                if self.entry_1.get()=="":
                    messagebox.showwarning("Empty Fields","Enter New Password",parent=self.root1)
                elif len(self.entry_1.get()) < 6:
                    messagebox.showwarning("","Password must contain atleast 6 characters",parent=self.root1)
                elif self.entry_2.get()=="":
                    messagebox.showwarning("Empty Fields","Confirm Password",parent=self.root1)
                elif self.entry_1.get()!=self.entry_2.get():
                    messagebox.showwarning("","Passwords does not match. Try Again",parent=self.root1)
                else:
                    ack=self.admin.change_pass(self.username.get(),self.passVar.get())
                    if ack==True:
                        messagebox.showinfo("Success","Password succesfully reset",parent=self.root1)
                        self.root1.destroy()
                    else:
                        messagebox.showwarning("database",ack,parent=self.root1)   
                    
        
   
    #FOGOT PASSWORD TERMINAL
    def forgotpw(self):
        self.passVar=StringVar()
        self.confirmVar=StringVar()
        if self.username.get()=="":
            messagebox.showwarning("","Please enter username to reset password",parent=self.root)
        elif self.admin.check_credentials(self.username.get(),self.password.get())==-1:
            messagebox.showwarning("Invalid Credentials","Username not found !",parent=self.root)
        else:
            data=self.admin.check_credentials(self.username.get(),self.password.get())
            if data==None:
                messagebox.showwarning("","Enter security answer",parent=self.root1)
                return
            else:
                self.root1=Toplevel()
                self.root1.title("Password Reset")
                self.root1.geometry("450x400+550+170")
                self.root1.resizable(width=False,height=False)
                frame1=Frame(self.root1, bg="black")
                frame1.place(x=0,y=0,width=450,height=550)
                fpw=Label(self.root1,text="FORGOTTEN PASSWORD?",font=("times new roman",20,"bold"),fg="red",bg="black")
                fpw.place(x=0,y=30,relwidth=1)

                self.label_1=Label(self.root1,text="Select Security Question",font=("times new roman",15),fg="white",bg="black")
                self.label_1.place(x=0,y=100,relwidth=1)
                self.combo_securityq=ttk.Combobox(self.root1,font=("times new roman",13),state="readonly")
                self.combo_securityq["values"]=("Choose","Your pet","1st school","Best friend","Nickname")
                self.combo_securityq.current(0)  
                self.combo_securityq.place(x=150,y=140,width=150)
                self.entry_1=ttk.Entry(self.root1,font=("times new roman",13),textvariable=self.passVar,show='*')
                self.entry_2=ttk.Entry(self.root1,font=("times new roman",13),textvariable=self.confirmVar,show='*')

                self.label_2=Label(self.root1,text="Security Key",font=("times new roman",15),fg="white",bg="black")
                self.label_2.place(x=0,y=210,relwidth=1)
                self.securityAns=ttk.Entry(self.root1,font=("times new roman",13))
                self.securityAns.place(x=150,y=250,width=150)
                
                self.btn=Button(self.root1,text="Next",command=self.reset_password,font=("Times New Roman",15,"bold"),fg="white",bg="red",activebackground="red",activeforeground="white",width=10)
                self.btn.place(x=155,y=310)



    def reg(self):
        if not self.new_win:
            self.new_win=Toplevel(self.root)
            self.reg=registration(self.new_win,self.admin)
        else:
            self.reg.root.deiconify()

if __name__=="__main__":
    window=Tk()
    app=login(window)
    window.mainloop()