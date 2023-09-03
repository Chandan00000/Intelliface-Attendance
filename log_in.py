from tkinter import* 
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from register import registration

class login:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN PAGE")
        self.root.attributes('-fullscreen', True)

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


        username=Label(root,text="Username",font=("Times New Roman",15,"bold"),fg="white",bg="black")
        username.place(x=930,y=390)

        self.textname=ttk.Entry(root,font=("Times New Roman",15,"bold"))
        self.textname.place(x=930,y=420,width=250,height=30)

        password=Label(root,text="Password",font=("Times New Roman",15,"bold"),fg="white",bg="black")
        password.place(x=930,y=470)

        self.textpass=ttk.Entry(root,show="*")
        self.textpass.place(x=930,y=500,width=250,height=30)

        login=Button(root,text="LOGIN",command=self.user_login,font=("Times New Roman",15,"bold"),fg="white",bg="red")
        login.place(x=1000,y=560,width=100)

        register=Button(root,text="Sign Up",font=("Times New Roman",12),command=self.reg,fg="white",bg="black",borderwidth=0,activebackground="black",activeforeground="white")
        register.place(x=930,y=620)

        Exit=Button(root,text="Exit",font=("Times New Roman",12),command=quit,fg="white",bg="black",borderwidth=0,activebackground="black",activeforeground="white")
        Exit.place(x=930,y=690)

        fp=Button(root,text="Forgot password?",font=("Times New Roman",12),command=self.forgotpw,fg="white",bg="black",borderwidth=0,activebackground="black",activeforeground="white")
        fp.place(x=930,y=660)
        

    def user_login(self):
        if self.textname.get()=="" or self.textpass.get()=="":
            messagebox.showerror("Error","All fields required",parent=self.root)
        elif self.textname.get()=="momo" and self.textpass.get()=="momo":
            self.root.destroy()
        else:
            messagebox.showerror("Invalid Credentials","Please enter correct details",parent=self.root)
    
    #RESET PASSWORD
    def reset_password(self):
        if self.combo_securityq.get()=="Choose":
            messagebox.showerror("Empty Fields","Select security question",parent=self.root1)
        elif self.securitya_entry.get()=="":
            messagebox.showerror("Empty Fields","Enter security answer",parent=self.root1)
        elif self.new_pw_entry.get()=="":
            messagebox.showerror("Empty Fields","Enter New Password",parent=self.root1)
        elif self.new_pw_cnf_entry.get()=="":
            messagebox.showerror("Empty Fields","Confirm Password",parent=self.root1)
        elif self.new_pw_entry.get()!=self.new_pw_cnf_entry.get():
            messagebox.showerror("Error","Passwords does not match. Try Again",parent=self.root1)
        else:
            messagebox.showinfo("Success","Password succesfully reset")
            self.root1.destroy()
        
   
    #FOGOT PASSWORD TERMINAL
    def forgotpw(self):
        if self.textname.get()=="":
            messagebox.showerror("Error","Please enter username to reset password")
        else:
            self.root1=Toplevel()
            self.root1.title("Password Reset")
            self.root1.geometry("450x550+550+170")
            frame1=Frame(self.root1, bg="black")
            frame1.place(x=0,y=0,width=450,height=550)
            fpw=Label(self.root1,text="FORGOTTEN PASSWORD?",font=("times new roman",20,"bold"),fg="red",bg="black")
            fpw.place(x=0,y=30,relwidth=1)

            securityq=Label(self.root1,text="Select Security Question",font=("times new roman",15),fg="white",bg="black")
            securityq.place(x=30,y=100)
            self.combo_securityq=ttk.Combobox(self.root1,font=("times new roman",10),state="readonly")
            self.combo_securityq["values"]=("Choose","Your pet","1st school","Best friend","Nickname")
            self.combo_securityq.place(x=30,y=130,width=150)
            self.combo_securityq.current(0)

            securitya=Label(self.root1,text="Security Key",font=("times new roman",15),fg="white",bg="black")
            securitya.place(x=30,y=180)
            self.securitya_entry=ttk.Entry(self.root1,font=("calibri",10))
            self.securitya_entry.place(x=30,y=210,width=150)

            new_pw=Label(self.root1,text="New Password",font=("times new roman",15),fg="white",bg="black")
            new_pw.place(x=30,y=260)
            self.new_pw_entry=ttk.Entry(self.root1,font=("calibri",10))
            self.new_pw_entry.place(x=30,y=290,width=150)

            new_pw_cnf=Label(self.root1,text="Confirm New Password",font=("times new roman",15),fg="white",bg="black")
            new_pw_cnf.place(x=30,y=340)
            self.new_pw_cnf_entry=ttk.Entry(self.root1,show="*")
            self.new_pw_cnf_entry.place(x=30,y=370,width=150)
            
            reset_btn=Button(self.root1,text="RESET PASSWORD",command=self.reset_password,font=("Times New Roman",15,"bold"),fg="white",bg="red",activebackground="red",activeforeground="white")
            reset_btn.place(x=130,y=430)



    def reg(self):
        if not self.new_win:
            self.new_win=Toplevel(self.root)
            self.reg=registration(self.new_win)
        else:
            self.reg.root.deiconify()

if __name__=="__main__":
    window=Tk()
    app=login(window)
    window.mainloop()