from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter.messagebox as tkm
import os
from database import Database
from dataset import DataSet
import shutil
class Student :
    def __init__(self,root):
        self.Student=Database("Student","data")
        self.ds=DataSet()
        self.root=root
        self.root.wm_iconbitmap(r'./resources/icon.ico')
        self.root.title("Attendance System")
        self.root.attributes('-fullscreen', True)
        height = self.root.winfo_screenheight()
        width = self.root.winfo_screenwidth() 
        self.std_details=None
        self.photo_file_path=f".\\faceData\\"
        
        self.dept=StringVar()
        self.year=StringVar()
        self.sem=StringVar()
        self.std_id=StringVar()
        self.std_name=StringVar()
        self.std_roll=StringVar()
        self.std_grp=StringVar()
        self.std_gender=StringVar()
        self.std_dob=StringVar()
        self.std_email=StringVar()
        self.std_ph=StringVar()
        self.std_address=StringVar()
        self.photoSam=StringVar()

        self.photoSam.set("NO")
        self.std_gender.set(None)


        bg=Image.open(r'./resources/background.jpg').resize((width,height),Image.LANCZOS)
        self.img1=ImageTk.PhotoImage(bg)
        bg_Label=Label(self.root,image=self.img1).pack()
        title=Label(self.root,text="STUDENT MANAGEMENT SYSTEM",bg='RED',fg='white',font="Roboto 40 bold").place(x=0,y=30,width=1536)

        img=Image.open(r'.\resources\back.png').resize((50,50),Image.LANCZOS)
        self.back_img=ImageTk.PhotoImage(image=img)
        back_button=Button(self.root,image=self.back_img,bd=0,bg='red',command=self.backward).place(x=20,y=35)

        ############# main_frame: ###############
        main_frame=Frame(self.root,height=735,width=1526)
        main_frame.place(x=5,y=118)

        ############## left frame ###############
        left_frame=LabelFrame(main_frame,text="Student details:",font="robota 24 bold",fg='red')
        left_frame.place(x=10,y=10,height=715,width=730)
        std_img=Image.open(r"./resources/students.png").resize((710,200),Image.LANCZOS)
        self.img2=ImageTk.PhotoImage(image=std_img)
        std_lb=Label(left_frame,image=self.img2).place(x=5,y=3)

        ################ current course info ###################
        curent_cframe=LabelFrame(left_frame,text="Current Course Info:",font="robota 20 bold",fg='red')
        curent_cframe.place(x=5,y=205,height=140,width=715)

        depart_lb=Label(curent_cframe,text="Department*",font="timesnewroman 14 bold",padx=10).grid(row=0,column=0,sticky=W)
        depart_comb=ttk.Combobox(curent_cframe,font="timesnewroman 13 ",width=15,state="readonly",textvariable=self.dept)
        depart_comb['values']=("Select Dept","CSE","ME","EE","CIVIL","MINING")
        depart_comb.current(0)
        depart_comb.grid(row=0,column=1,padx=20,pady=10)

        year_lb=Label(curent_cframe,text="Year",font="timesnewroman 14 bold",padx=10).grid(row=0,column=2,sticky=W)
        year_comb=ttk.Combobox(curent_cframe,font="timesnewroman 13 ",width=15,state="readonly",textvariable=self.year)
        year_comb['values']=("Select Year","1st","2nd","3rd","4th")
        year_comb.current(0)
        year_comb.grid(row=0,column=3,padx=20,pady=10)  

        sem_lb=Label(curent_cframe,text="Semester",font="timesnewroman 14 bold",padx=10).grid(row=1,column=0,sticky=W)
        sem_comb=ttk.Combobox(curent_cframe,font="timesnewroman 13 ",width=15,state="readonly",textvariable=self.sem)
        sem_comb['values']=("Select Sem","1st","2nd","3rd","4th","5th","6th","7th","8th")
        sem_comb.current(0)
        sem_comb.grid(row=1,column=1,padx=20,pady=10) 

        ############### class student info ######################
        student_inf0_frame=LabelFrame(left_frame,text="Student Info:",font="robota 20 bold",fg='red')
        student_inf0_frame.place(x=5,y=345,height=290,width=715)

        std_id_lb=Label(student_inf0_frame,text="Student ID*",font="timesnewroman 14 bold",padx=10).grid(row=0,column=0,sticky=W)
        std_id_ent=Entry(student_inf0_frame,width=15,font="timesnewroman 13",textvariable=self.std_id)
        std_id_ent.grid(row=0,column=1,padx=20,pady=10,sticky=W) 

        std_name_lb=Label(student_inf0_frame,text="Student Name*",font="timesnewroman 14 bold",padx=10).grid(row=0,column=2,sticky=W)
        std_name_ent=Entry(student_inf0_frame,width=15,font="timesnewroman 13",textvariable=self.std_name)
        std_name_ent.grid(row=0,column=3,padx=20,pady=10,sticky=W) 

        std_rollNo_lb=Label(student_inf0_frame,text="Roll No",font="timesnewroman 14 bold",padx=10).grid(row=1,column=0,sticky=W)
        std_rollNo_ent=Entry(student_inf0_frame,width=15,font="timesnewroman 13",textvariable=self.std_roll)
        std_rollNo_ent.grid(row=1,column=1,padx=20,pady=10,sticky=W) 

        std_grp_lb=Label(student_inf0_frame,text="Group",font="timesnewroman 14 bold",padx=10).grid(row=1,column=2,sticky=W)
        std_grp_ent=Entry(student_inf0_frame,width=15,font="timesnewroman 13",textvariable=self.std_grp)
        std_grp_ent.grid(row=1,column=3,padx=20,pady=10,sticky=W) 
        
        gender_rb_frame=Frame(student_inf0_frame)
        std_gender_lb=Label(gender_rb_frame,text="Gender",font="timesnewroman 14 bold").pack(padx=10,side=LEFT)
        std_gender_male=Radiobutton(gender_rb_frame,text="Male",font="timesnewroman 13 bold",variable=self.std_gender,value="Male").pack(padx=15,side=LEFT)
        std_gender_female=Radiobutton(gender_rb_frame,text="Female",font="timesnewroman 13 bold",variable=self.std_gender,value="Female").pack(side=LEFT)
        gender_rb_frame.grid(row=2,column=0,sticky=W,columnspan=2) 

        std_dob_lb=Label(student_inf0_frame,text="DOB",font="timesnewroman 14 bold",padx=10).grid(row=2,column=2,sticky=W)
        std_dob_ent=Entry(student_inf0_frame,width=15,font="timesnewroman 13",textvariable=self.std_dob)
        std_dob_ent.grid(row=2,column=3,padx=20,pady=10,sticky=W) 

        std_email_lb=Label(student_inf0_frame,text="E-mail",font="timesnewroman 14 bold",padx=10).grid(row=3,column=0,sticky=W)
        std_email_ent=Entry(student_inf0_frame,width=15,font="timesnewroman 13",textvariable=self.std_email)
        std_email_ent.grid(row=3,column=1,padx=20,pady=10,sticky=W) 

        std_ph_lb=Label(student_inf0_frame,text="Phone No",font="timesnewroman 14 bold",padx=10).grid(row=3,column=2,sticky=W)
        std_ph_ent=Entry(student_inf0_frame,width=15,font="timesnewroman 13",textvariable=self.std_ph)
        std_ph_ent.grid(row=3,column=3,padx=20,pady=10,sticky=W) 

        std_add_lb=Label(student_inf0_frame,text="Address",font="timesnewroman 14 bold",padx=10).grid(row=4,column=0,sticky=W)
        std_add_ent=Entry(student_inf0_frame,width=30,font="timesnewroman 13",textvariable=self.std_address)
        std_add_ent.grid(row=4,column=1,padx=20,pady=10,columnspan=2,sticky=W) 

        photosample_fr=Frame(student_inf0_frame)
        photosample=Radiobutton(photosample_fr,text="Has Photo Sample",font="timesnewroman 13 bold",variable=self.photoSam,value="YES").grid(padx=20,row=0,column=0)
        photosample=Radiobutton(photosample_fr,text="No Photo Sample",font="timesnewroman 13 bold",variable=self.photoSam,value="NO").grid(padx=40,row=0,column=1)
        photosample_fr.grid(row=5,column=0,columnspan=4,sticky=W)

        button_fr=Frame(left_frame)
        button_fr.place(x=5,y=640,width=715,height=30)

        save_bt=Button(button_fr,text='SAVE',bg='red',fg='white',font="robota 10 bold",relief=RIDGE,command=self.add_data).grid(row=0,column=0,padx=30)
        update_bt=Button(button_fr,text='UPDATE',bg='red',fg='white',font="robota 10 bold",relief=RIDGE,command=self.update_data).grid(row=0,column=1,padx=30)
        del_bt=Button(button_fr,text='DELETE',bg='red',fg='white',font="robota 10 bold",relief=RIDGE,command=self.delete_data).grid(row=0,column=2,padx=30)
        reset_bt=Button(button_fr,text='RESET',bg='red',fg='white',font="robota 10 bold",relief=RIDGE,command=self.reset_data).grid(row=0,column=3,padx=30)
        photosample_bt=Button(button_fr,text='Take Photo Sample',bg='red',fg='white',font="robota 10 bold",relief=RIDGE,command=self.take_photosample).grid(row=0,column=4,padx=30)

        ################# right frame ##################
        right_frame=LabelFrame(main_frame,text="Student details:",fg='red',font="robota 24 bold")
        right_frame.place(x=750,y=10,height=715,width=770)
        std_img2=Image.open(r"./resources/std_image2.jpg").resize((750,200),Image.LANCZOS)
        self.img3=ImageTk.PhotoImage(image=std_img2)
        std_lb=Label(right_frame,image=self.img3).place(x=5,y=3)

        ############# search_frame ################
        self.search_by=StringVar()
        self.search_ent_var=StringVar()
        search_frame=LabelFrame(right_frame,text="Search System:",fg='red',font="robota 20 bold")
        search_frame.place(x=5,y=205,height=80,width=755)
        search_by_lb=Label(search_frame,text="Search By:",font="timesnewroman 14 bold",padx=10,pady=8).grid(row=0,column=0)

        search_comb=ttk.Combobox(search_frame,font="timesnewroman 13 ",width=15,state="readonly",textvariable=self.search_by)
        search_comb['values']=("Select","Student ID","Name")
        search_comb.current(0)
        search_comb.grid(row=0,column=1,padx=10)

        search_ent=Entry(search_frame,width=15,font="timesnewroman 13",textvariable=self.search_ent_var)
        search_ent.grid(row=0,column=2,padx=10) 

        search_bt=Button(search_frame,text='SEARCH',bg='red',fg='white',font="robota 10 bold",command=self.search_data).grid(row=0,column=3,padx=30)

        showAll_bt=Button(search_frame,text='SHOW ALL',bg='red',fg='white',font="robota 10 bold",command=self.show_all).grid(row=0,column=4,padx=30)

        ########## Table Frame #############
        table_frame=Frame(right_frame,bd=5,relief=RIDGE)
        table_frame.place(x=5,y=290,height=375,width=755)
        self.cols=["std_id","dept","year","sem","name","roll_no","photoSam"]
        y_scroll=Scrollbar(table_frame,orient=VERTICAL)
        y_scroll.pack(side=RIGHT,fill=Y)

        self.std_table=ttk.Treeview(table_frame,columns=self.cols,show='headings',yscrollcommand=y_scroll.set,height=60)
        self.std_table.bind("<ButtonRelease>",self.get_cursor)
        y_scroll.config(command=self.std_table.yview)

        self.std_table.heading("std_id",text="STUDENT-ID")
        self.std_table.heading("dept",text="DEPARTMENT")
        self.std_table.heading("year",text="YEAR")
        self.std_table.heading("sem",text="SEMESTER")
        self.std_table.heading("name",text="NAME")
        self.std_table.heading("roll_no",text="ROLL-NO")
        self.std_table.heading("photoSam",text="PhotoSample")

        self.std_table.column('std_id',width=100,anchor=CENTER)
        self.std_table.column('dept',width=100,anchor=CENTER)
        self.std_table.column('year',width=50,anchor=CENTER)
        self.std_table.column('sem',width=100,anchor=CENTER)
        self.std_table.column('name',width=100,anchor=CENTER)
        self.std_table.column('roll_no',width=100,anchor=CENTER)
        self.std_table.column('photoSam',width=100,anchor=CENTER)
        self.std_table.pack(fill=BOTH) 
        
        ################### Search Data ################## 
    def search_data(self):
        if self.search_by.get()=="Select" or self.search_ent_var.get()=="" or self.search_by.get()=="all":
            tkm.showwarning("Empty","Please enter all required fields!",parent=self.root)
        else:
            self.std_details=self.Student.show_data(self.search_by.get(),self.search_ent_var.get())
            self.show_data(self.std_details)
            
        ################ Select all button ###############
    def show_all(self):
        self.search_by.set("all")
        self.std_details=self.Student.show_data(self.search_by.get(),self.search_ent_var.get())
        self.show_data(self.std_details)
        
        ################ Show data ####################
    def show_data(self,std_det):
        self.std_table.delete(*self.std_table.get_children())
        for i in std_det:
            std_set=list(i.values())
            self.std_table.insert("",END,values=std_set)    
            
        ############# Add data to database #############
    def add_data(self):
        if self.std_name.get()=="" or self.std_id.get()=="" or self.dept.get=="Select Dept":
            tkm.showwarning("Empty","Please enter all required fields!",parent=self.root)
        else:
            self.pathCheck(self.std_id.get())
            ack=self.Student.insert_data(self.dept.get(),self.year.get(),self.sem.get(),self.std_id.get(),self.std_name.get(),self.std_roll.get(),
                                    self.std_grp.get(),self.std_gender.get(),self.std_dob.get(),self.std_email.get(),self.std_ph.get(),
                                    self.std_address.get(),self.photoSam.get())
            if ack==True:
                self.show_all()
                tkm.showinfo("Database","Student info Registered !",parent=self.root)
            else:
                tkm.showerror("Database",ack,parent=self.root)

    
    ################# get data from table ##############
    def get_cursor(self,event=""):
        try:
            cursor_focus=self.std_table.focus()
            content=self.std_table.item(cursor_focus)
            std_id=content['values'][0]
            data=self.Student.show_data("cursor",std_id)
            data_list=list(data.values())
            
            self.std_id.set(data_list[0])
            self.dept.set(data_list[1])
            self.year.set(data_list[2])
            self.sem.set(data_list[3])
            self.std_name.set(data_list[4])
            self.std_roll.set(data_list[5])
            self.std_grp.set(data_list[6])
            self.std_gender.set(data_list[7])
            self.std_dob.set(data_list[8])
            self.std_email.set(data_list[9])
            self.std_ph.set(data_list[10])
            self.std_address.set(data_list[11])
            self.pathCheck(self.std_id.get())
        except Exception as e:
            print(str(e))
            
    ########### update data ##############
    def update_data(self):
        if self.std_name.get()=="" or self.std_id.get()=="" or self.dept.get=="Select Dept":
            tkm.showwarning("Empty","Please enter all required fields!",parent=self.root)
        else:
            update=tkm.askyesno("Update","Do you want to update the data ?",parent=self.root)
            if update:
                self.pathCheck(self.std_id.get())
                ack=self.Student.update_data(self.dept.get(),self.year.get(),self.sem.get(),self.std_id.get(),self.std_name.get(),self.std_roll.get(),
                                        self.std_grp.get(),self.std_gender.get(),self.std_dob.get(),self.std_email.get(),self.std_ph.get(),
                                        self.std_address.get(),self.photoSam.get())
                if ack==True:
                    self.show_all()
                    tkm.showinfo("Database","Student info updated !",parent=self.root)
                else:
                    tkm.showerror("Database",ack,parent=self.root)
            else:
                return
            
    ########### delete data #################
    def delete_data(self):
        if self.std_name.get()=="" or self.std_id.get()=="" or self.dept.get=="Select Dept":
            tkm.showwarning("Empty","Please enter all required fields!",parent=self.root)
        else:
            delete=tkm.askyesno("Delete","Do you want to delete the data ?",parent=self.root)
            if delete:
                ack=self.Student.delete_data(self.std_id.get())
                if ack==True:
                    self.pathCheck(self.std_id.get())
                    if self.photoSam.get()=="YES":
                        shutil.rmtree(f".\\faceData\\{self.std_id.get()}", ignore_errors=False, onerror=None)
                    self.reset_data()
                    self.show_all()
                    tkm.showinfo("Database","Student deleted !",parent=self.root)
                else:
                    tkm.showerror("Database",ack,parent=self.root)
            else:
                return
    
    ########### Reset ####################
    def reset_data(self):
        self.dept.set("Select Dept")
        self.year.set("Select Year")
        self.sem.set("Select Sem")
        self.std_id.set("")
        self.std_name.set("")
        self.std_roll.set("")
        self.std_grp.set("")
        self.std_gender.set(None)
        self.std_dob.set("")
        self.std_email.set("")
        self.std_ph.set("")
        self.std_address.set("")
        self.photoSam.set("NO")
        
    ############### Take photo sample ############
    def take_photosample(self):
        self.pathCheck(self.std_id.get())
        if self.std_name.get()=="" or self.std_id.get()=="" or self.dept.get=="Select Dept":
            tkm.showwarning("Empty","Please enter all required fields!",parent=self.root)
        elif self.photoSam.get()=="YES":
            updt=tkm.askyesno("warning","Photo Sample already exist !\nDo you want to update ?",parent=self.root)
            if updt:
                err_msg=self.ds.takePhotoSample(self.std_id.get(),True)
                if err_msg!=None:
                    tkm.showerror("Error",err_msg,parent=self.root)
                else:
                    self.photoSam.set("YES")
                    tkm.showinfo("Done","Photo Sample Updated",parent=self.root)
        else:
            err_msg=self.ds.takePhotoSample(self.std_id.get(),False)
            if err_msg!=None:
                tkm.showerror("Error",err_msg,parent=self.root)
            else:
                self.photoSam.set("YES")
                tkm.showinfo("Done","Photo Sample collected",parent=self.root)
                
    def pathCheck(self,std_id):
        if std_id=="":
            return
        if os.path.exists(f"{self.photo_file_path}{std_id}"):
            self.photoSam.set("YES")
        else:
            self.photoSam.set("NO")
            
    def backward(self):
        self.root.withdraw()
        # self.root.destroy()     
       

if __name__=='__main__':
    root=Tk()
    s1=Student(root)
    root.mainloop()