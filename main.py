from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as tkm
import os
from threading import Thread
from student import Student
from train_data import TrainingData
from recognition import Recognition
from attendance import Attendance
import csv
class Face_rec():
    def __init__(self,root):
        self.root=root
        self.root.wm_iconbitmap(r'./resources/icon.ico')
        self.root.title("Attendance System")
        self.root.attributes('-fullscreen', True)
        self.training_data=TrainingData()
        height = self.root.winfo_screenheight()
        width = self.root.winfo_screenwidth()
        
        self.new_window1=None
        self.new_window2=None
        self.new_window3=None
        
        # self.root.geometry("1536x864+0+0")
        # print(height,width)
        # background image

        bg=Image.open(r'.\resources\background.jpg').resize((width,height),Image.LANCZOS)
        self.img1=ImageTk.PhotoImage(bg)
        bg_Label=Label(self.root,image=self.img1).pack()

        title=Label(self.root,text="INTELLIFACE   ATTENDANCE   SYSTEM",bg='#1c1d1f',fg='#ff99ff',font="Roboto 35 bold").place(x=0,y=42,width=1536)
        faceX=Image.open(r'.\resources\face_x.jpg').resize((450,600),Image.LANCZOS)
        self.img8=ImageTk.PhotoImage(image=faceX)
        facex_lb=Label(self.root,image=self.img8,bd=0,bg='#1c1d1f').place(x=60,y=180)

        # student details button
        f1=Frame(self.root)
        std_img=Image.open(r'.\resources\student-details.png').resize((200,250),Image.LANCZOS)
        self.img2=ImageTk.PhotoImage(std_img)
        self.student_details=Button(f1,activebackground='#1c1d1f',bd=0,bg='#1c1d1f',image=self.img2,cursor='hand2',command=self.student_info).pack()
        self.student_det_lb=Label(f1,text="Personal details",bg='#1c1d1f',fg='#ff3399',font="Roboto 15 bold").pack(fill=X)
        f1.place(x=600,y=150)

        # detect face button
        f2=Frame(self.root)
        det_img=Image.open(r'./resources/face-det.png').resize((200,250),Image.LANCZOS)
        self.img3=ImageTk.PhotoImage(det_img)
        self.detect=Button(f2,activebackground='#1c1d1f',bd=0,bg='#1c1d1f',image=self.img3,cursor='hand2',command=self.face_recognition).pack()
        self.detect_lb=Label(f2,text="Detect Face",bg='#1c1d1f',fg='#ff3399',font="Roboto 15 bold").pack(fill=X)
        f2.place(x=900,y=150)

        # Train face button
        f4=Frame(self.root)
        train_img=Image.open(r'.\resources\train-face.png').resize((200,250),Image.LANCZOS)
        self.img5=ImageTk.PhotoImage(train_img)
        self.train=Button(f4,activebackground='#1c1d1f',bd=0,bg='#1c1d1f',image=self.img5,cursor='hand2',command=self.thread_start).pack()
        self.train_lb=Label(f4,text="Train Face",bg='#1c1d1f',fg='#ff3399',font="Roboto 15 bold").pack(fill=X)
        f4.place(x=1200,y=150)

        # Attendance button
        f3=Frame(self.root)
        atten_img=Image.open(r'./resources/attendance.png').resize((200,250),Image.LANCZOS)
        self.img4=ImageTk.PhotoImage(atten_img)
        self.atten=Button(f3,activebackground='#1c1d1f',bd=0,bg='#1c1d1f',image=self.img4,cursor='hand2',command=self.attendance).pack()
        self.atten_lb=Label(f3,text="Attendance",bg='#1c1d1f',fg='#ff3399',font="Roboto 15 bold").pack(fill=X)
        f3.place(x=600,y=520)

        # Photo_file button
        f5=Frame(self.root)
        photo_file=Image.open(r'./resources/photo_file.png').resize((200,250),Image.LANCZOS)
        self.img6=ImageTk.PhotoImage(photo_file)
        self.ph_file=Button(f5,activebackground='#1c1d1f',bd=0,bg='#1c1d1f',image=self.img6,cursor='hand2',command=self.openFile).pack()
        self.ph_file_lb=Label(f5,text="Photo File",bg='#1c1d1f',fg='#ff3399',font="Roboto 15 bold").pack(fill=X)
        f5.place(x=900,y=520)

        # Exit button
        f6=Frame(self.root)
        exit_img=Image.open(r'./resources/exit.png').resize((200,250),Image.LANCZOS)
        self.img7=ImageTk.PhotoImage(exit_img)
        self.exit=Button(f6,activebackground='#1c1d1f',bd=0,bg='#1c1d1f',image=self.img7,cursor='hand2',command=self.exit_window).pack()
        self.exit_lb=Label(f6,text="Exit",bg='#1c1d1f',fg='#ff3399',font="Roboto 15 bold").pack(fill=X)
        f6.place(x=1200,y=520)
        
    def train_model(self):
        msg=self.training_data.train_faces()
        tkm.showinfo("Training Data",msg,parent=self.root)
        
    def thread_start(self):
        t1=Thread(target=self.train_model)
        t1.start()
        
    def student_info(self):
        if not self.new_window1:
            self.new_window1=Toplevel(self.root)
            self.app1=Student(self.new_window1)
        else:
            self.app1.root.deiconify()
            
    def face_recognition(self):
        if not self.new_window2:
            self.new_window2=Toplevel(self.root)
            self.app2=Recognition(self.new_window2)
        else:
            self.app2.root.deiconify()
    
    def attendance(self):
        if not self.new_window3:
            self.new_window3=Toplevel(self.root)
            self.app3=Attendance(self.new_window3)
        else:
            self.app3.root.deiconify()
            
    def openFile(self):
        os.startfile(".\\faceData")
        
    ############# Exit App ######################
    def exit_window(self):
        ########### marking remaining students as absent ##################   
        ack=tkm.askyesno("IntelliFace","Are you sure you want to Exit ?",parent=self.root)
        if ack:
            direc=os.listdir(r".\atd_files")
            if len(direc)>0 :
                csvfile_name=direc[0]
                file_name=f".\\atd_files\\{csvfile_name}"
                data=[]
                fields=[]
                with open(file_name) as csv_file:
                    csv_reader=csv.reader(csv_file)
                    fields=next(csv_reader)
                    for i in csv_reader:
                        try :
                            if i[-1]=="":
                                row=i[:-1]
                                row.append("Absent")
                                data.append(row)
                            else:
                                data.append(i)
                        except:
                            None
                with open(file_name,'w',newline="") as csv_file:
                    csv_writer=csv.writer(csv_file)
                    csv_writer.writerow(fields)
                    csv_writer.writerows(data)
            quit()
        else:
            None

if __name__=='__main__':
    root=Tk()
    mainscreen=Face_rec(root)
    root.mainloop()