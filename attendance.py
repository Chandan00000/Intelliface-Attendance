from tkinter import *
from tkinter import ttk,filedialog
from PIL import Image,ImageTk
import tkinter.messagebox as tkm
import csv
import os
import copy
import pandas as pd
class Attendance :
    def __init__(self,root):
        self.root=root
        self.root.wm_iconbitmap(r'./resources/icon.ico')
        self.root.title("Attendance System")
        self.back=False
        self.root.attributes('-fullscreen', True)
        height = self.root.winfo_screenheight()
        width = self.root.winfo_screenwidth() 
        
        self.csv_data=[]
        self.headings=[]
        self.dept=StringVar()
        self.year=StringVar()
        self.sem=StringVar()
        self.std_id=StringVar()
        self.std_name=StringVar()
        self.std_roll=StringVar()
        self.time=StringVar()
        self.date=StringVar()
        self.status=StringVar()
        
        ########### bg Image ####################
        bg=Image.open(r'./resources/background.jpg').resize((width,height),Image.LANCZOS)
        self.img1=ImageTk.PhotoImage(bg)
        bg_Label=Label(self.root,image=self.img1).pack()
        title=Label(self.root,text="STUDENT ATTENDANCE SYSTEM",bg='RED',fg='white',font="Roboto 40 bold").place(x=0,y=30,width=1536)
        
        ########### back button #################
        img=Image.open(r'.\resources\back.png').resize((50,50),Image.LANCZOS)
        self.back_img=ImageTk.PhotoImage(image=img)
        back_button=Button(self.root,image=self.back_img,bd=0,bg='red',command=self.backward).place(x=20,y=35)
        
        ############# main_frame: ###############
        main_frame=Frame(self.root,height=735,width=1526)
        main_frame.place(x=5,y=118)
        
         ############## left frame ###############
        left_frame=LabelFrame(main_frame,text="Attendance details:",font="robota 24 bold",fg='red')
        left_frame.place(x=10,y=10,height=715,width=730)
        std_img=Image.open(r"./resources/atd_left.jpg").resize((710,200),Image.LANCZOS)
        self.img2=ImageTk.PhotoImage(image=std_img)
        std_lb=Label(left_frame,image=self.img2).place(x=5,y=3)
        
        ################ current course info ###################
        curent_cframe=LabelFrame(left_frame,text="Current Course Info:",font="robota 20 bold",fg='red')
        curent_cframe.place(x=5,y=205,height=140,width=715)

        depart_lb=Label(curent_cframe,text="Department",font="timesnewroman 14 bold",padx=10).grid(row=0,column=0,sticky=W)
        depart_ent=Entry(curent_cframe,width=15,font="timesnewroman 13",textvariable=self.dept,state=DISABLED)
        depart_ent.grid(row=0,column=1,padx=20,pady=10)

        year_lb=Label(curent_cframe,text="Year",font="timesnewroman 14 bold",padx=10).grid(row=0,column=2,sticky=W)
        year_ent=Entry(curent_cframe,width=15,font="timesnewroman 13",textvariable=self.year,state=DISABLED)
        year_ent.grid(row=0,column=3,padx=20,pady=10)  

        sem_lb=Label(curent_cframe,text="Semester",font="timesnewroman 14 bold",padx=10).grid(row=1,column=0,sticky=W)
        sem_ent=Entry(curent_cframe,width=15,font="timesnewroman 13",textvariable=self.sem,state=DISABLED)
        sem_ent.grid(row=1,column=1,padx=20,pady=10) 
        
        ###############  student attendance info ######################
        student_inf0_frame=LabelFrame(left_frame,text="Student Info:",font="robota 20 bold",fg='red')
        student_inf0_frame.place(x=5,y=345,height=250,width=715)
        
        std_id_lb=Label(student_inf0_frame,text="Student ID",font="timesnewroman 14 bold",padx=10).grid(row=0,column=0,sticky=W)
        std_id_ent=Entry(student_inf0_frame,width=15,font="timesnewroman 13",textvariable=self.std_id,state=DISABLED)
        std_id_ent.grid(row=0,column=1,padx=20,pady=10,sticky=W) 

        std_name_lb=Label(student_inf0_frame,text="Student Name",font="timesnewroman 14 bold",padx=10).grid(row=0,column=2,sticky=W)
        std_name_ent=Entry(student_inf0_frame,width=15,font="timesnewroman 13",textvariable=self.std_name,state=DISABLED)
        std_name_ent.grid(row=0,column=3,padx=20,pady=10,sticky=W) 

        std_regNo_lb=Label(student_inf0_frame,text="Roll No",font="timesnewroman 14 bold",padx=10).grid(row=1,column=0,sticky=W)
        std_regNo_ent=Entry(student_inf0_frame,width=15,font="timesnewroman 13",textvariable=self.std_roll,state=DISABLED)
        std_regNo_ent.grid(row=1,column=1,padx=20,pady=10,sticky=W) 
        
        time_lb=Label(student_inf0_frame,text="Time",font="timesnewroman 14 bold",padx=10).grid(row=1,column=2,sticky=W)
        time_ent=Entry(student_inf0_frame,width=15,font="timesnewroman 13",textvariable=self.time)
        time_ent.grid(row=1,column=3,padx=20,pady=10,sticky=W)
        
        date_lb=Label(student_inf0_frame,text="Date",font="timesnewroman 14 bold",padx=10).grid(row=2,column=0,sticky=W)
        date_ent=Entry(student_inf0_frame,width=15,font="timesnewroman 13",textvariable=self.date,state=DISABLED)
        date_ent.grid(row=2,column=1,padx=20,pady=10,sticky=W)
        
        sts_lb=Label(student_inf0_frame,text="Attendance Status",font="timesnewroman 14 bold",padx=10).grid(row=3,column=0,sticky=W,columnspan=2)
        sts_comb=ttk.Combobox(student_inf0_frame,font="timesnewroman 13 ",width=15,state="readonly",textvariable=self.status)
        sts_comb['values']=("None","Present","Absent")
        sts_comb.current(0)
        sts_comb.grid(row=3,column=1,padx=20,pady=10,columnspan=2) 
        
        ################ Button Frame ##################
        button_fr=Frame(left_frame)
        button_fr.place(x=5,y=615,width=715,height=35)

        import_bt=Button(button_fr,text='IMPORT CSV ',bg='red',fg='white',relief=RIDGE,font="robota 14 bold",command=self.import_csv).grid(row=0,column=0,padx=30)
        export_bt=Button(button_fr,text='EXPORT CSV',bg='red',fg='white',relief=RIDGE,font="robota 14 bold",command=self.export_csv).grid(row=0,column=2,padx=30)
        update_bt=Button(button_fr,text='UPDATE',bg='red',fg='white',relief=RIDGE,font="robota 14 bold",command=self.update_data).grid(row=0,column=1,padx=30)
        reset_bt=Button(button_fr,text='RESET',bg='red',fg='white',relief=RIDGE,font="robota 14 bold",command=self.reset_data).grid(row=0,column=3,padx=30)
        
        ################# right frame ##################
        right_frame=LabelFrame(main_frame,text="Student details:",fg='red',font="robota 24 bold")
        right_frame.place(x=750,y=10,height=715,width=770)
        std_img2=Image.open(r"./resources/atd_right.jpg").resize((750,200),Image.LANCZOS)
        self.img3=ImageTk.PhotoImage(image=std_img2)
        std_lb=Label(right_frame,image=self.img3).place(x=5,y=3)
        
        ########## Table Frame #############
        table_frame=Frame(right_frame,bd=5,relief=RIDGE)
        table_frame.place(x=5,y=220,height=450,width=755)
        self.cols=["std_id","dept","year","sem","reg_no","name","status"]
        y_scroll=Scrollbar(table_frame,orient=VERTICAL)
        y_scroll.pack(side=RIGHT,fill=Y)

        self.std_atd_table=ttk.Treeview(table_frame,columns=self.cols,show='headings',yscrollcommand=y_scroll.set,height=60)
        self.std_atd_table.bind("<ButtonRelease>",self.get_cursor)
        y_scroll.config(command=self.std_atd_table.yview)

        self.std_atd_table.heading("std_id",text="STUDENT-ID")
        self.std_atd_table.heading("dept",text="DEPARTMENT")
        self.std_atd_table.heading("year",text="YEAR")
        self.std_atd_table.heading("sem",text="SEMESTER")
        self.std_atd_table.heading("reg_no",text="REG-NO")
        self.std_atd_table.heading("name",text="NAME")
        self.std_atd_table.heading("status",text="STATUS")

        self.std_atd_table.column('std_id',width=100,anchor=CENTER)
        self.std_atd_table.column('dept',width=100,anchor=CENTER)
        self.std_atd_table.column('year',width=50,anchor=CENTER)
        self.std_atd_table.column('sem',width=100,anchor=CENTER)
        self.std_atd_table.column('reg_no',width=100,anchor=CENTER)
        self.std_atd_table.column('name',width=100,anchor=CENTER)
        self.std_atd_table.column('status',width=100,anchor=CENTER)
        self.std_atd_table.pack(fill=BOTH) 
        
    ############## importing csv file ##############
    def import_csv(self):
        try:
            path=filedialog.askopenfilename(initialdir=".\\atd_files",title="Import CSV",filetypes=(("CSV FILE","*.csv"),("ALL FILE","*.*")),parent=self.root)
            if path =="":
                return
            else:
                self.file_path=path
                self.refresh(self.file_path)
        except FileNotFoundError:
            None
        except Exception as e:
            tkm.showerror("Error",f"Due to: {e}",parent=self.root)
            
    ############## Exporting csv file ##############
    def export_csv(self):
        try:
            if len(self.csv_data)>0:      
                file_path=filedialog.asksaveasfilename(initialdir=".\\atd_files",title="Export CSV",filetypes=(("CSV FILE","*.csv"),("ALL FILE","*.*")),parent=self.root)
                with open(file_path,"w",newline="") as f:
                    csv_writer=csv.writer(f)
                    csv_writer.writerow(self.headings)
                    csv_writer.writerows(self.csv_data)
                tkm.showinfo("Export data",f"Exported to {os.path.basename(file_path)} successfully",parent=self.root)
            else:
                tkm.showwarning("Empty data","No data to export",parent=self.root)
        except FileNotFoundError:
            None
        except Exception as e:
            tkm.showerror("Error",f"Due to: {e}",parent=self.root)
            
    ############ refresh data in Table ####################
    def refresh(self,file_path):
        self.csv_data.clear()
        try:
            with open(file_path) as f:
                csv_reader=csv.reader(f)
                self.headings=next(csv_reader)
                for row in csv_reader:
                    self.csv_data.append(row)
                self.fetch_data(copy.deepcopy(self.csv_data))
        except Exception as e:
            tkm.showerror("Error",f"Due to: {e}",parent=self.root)
            
    ############ fetch data to stdudent frame #################
    def fetch_to_frame(self,data):
            self.std_id.set(data[0])
            self.dept.set(data[1])
            self.year.set(data[2])
            self.sem.set(data[3])
            self.std_roll.set(data[4])
            self.std_name.set(data[5])
            self.date.set(data[6])
            self.status.set(data[7])
            self.time.set(data[8])
            
    ########### Reset ####################
    def reset_data(self):
        self.dept.set("")
        self.year.set("")
        self.sem.set("")
        self.std_id.set("")
        self.std_name.set("")
        self.std_roll.set("")
        self.time.set("")
        self.date.set("")
        self.status.set("None")
    
    ############ Update ###################
    def update_data(self):
        if self.std_id.get()=="":
            tkm.showwarning("Empty","Please select a reecord",parent=self.root)
            return
        if self.date.get()=="":
            tkm.showwarning("Empty","No record found on this date",parent=self.root)
        else:
            if self.status.get()=="Present" and self.time.get()=="" :
                tkm.showwarning("Empty","Please add Timestamp!",parent=self.root)
            else:
                update=tkm.askyesno("Update","Do you want to update the data ?",parent=self.root)
                if update:
                    ack=self.update_csv(self.std_id.get(),self.status.get(),self.date.get(),self.time.get())
                    if ack: 
                        self.refresh(self.file_path)
                        tkm.showinfo("Attendance","Student attendance updated !",parent=self.root)
                    else:
                        tkm.showerror("Attendance",ack,parent=self.root)
                else:
                    return
    
    ############ csv update ###########
    def update_csv(self,std_id,status,date,timestamp):
        try:
            df = pd.read_csv(self.file_path)
            if status=="Present":
                df.loc[int(std_id[-1])-1,date]=f"P-{timestamp}"
            elif status=="Absent":
                self.time.set("")
                df.loc[int(std_id[-1])-1,date]=f"Absent"
            df.to_csv(self.file_path,index=False)
            return True
        except Exception as e:
            return str(e)
    
    ############ fetch data to table view ##########
    def fetch_data(self,data):
        self.std_atd_table.delete(*self.std_atd_table.get_children())
        for row_data in data:
            if str(row_data[-1]).startswith("P"):
                row_data[-1]="Present"
            elif str(row_data[-1])=="":
                row_data[-1]="Absent"
            self.std_atd_table.insert("",END,values=row_data)  
    
    def get_cursor(self,event=""):
        try:
            cursor_focus=self.std_atd_table.focus()
            content=self.std_atd_table.item(cursor_focus)
            std_id=content['values'][0]
            status=content['values'][-1]
            df=pd.read_csv(self.file_path)
            data=list(df.loc[int(std_id[-1])-1].values)
            cols=df.columns.values
            std_data=data[:6]
            if len(cols)>6:
                std_data.append(cols[-1])
                if(status=="Present"):
                    std_data.append("Present")
                    std_data.append(str(data[6]).split("-")[-1])
                elif(status=="Absent"):
                    std_data.append("Absent")
                    std_data.append("")
            else:
                std_data.append("")
                std_data.append("None")
                std_data.append("")
            self.fetch_to_frame(std_data)
            self.refresh(self.file_path)
        except Exception as e:
            # tkm.showwarning("Table","Empty Table !",parent=self.root)
            None
    
    def backward(self):
        self.root.withdraw()
        # self.root.destroy()  
        
if __name__=='__main__':
    root=Tk()
    s1=Attendance(root)
    root.mainloop()