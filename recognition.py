from tkinter import *
from PIL import Image,ImageTk
import cv2 as cv
import numpy as np
import os
import pandas as pd
import datetime
from database import Database
class Recognition():
    def __init__(self,root):
        self.today=datetime.date.today().strftime("%d/%m/%Y")
        self.root=root
        self.root.wm_iconbitmap(r'./resources/icon.ico')
        self.root.title("Attendance System")
        self.back=False
        self.root.attributes('-fullscreen', True)
        height = self.root.winfo_screenheight()
        width = self.root.winfo_screenwidth()
        
        self.Student=Database("Student","data")
        self.harr_cascade=cv.CascadeClassifier(r'.\resources\harr_face.xml')
        self.attendee=[]
        self.scanned=[]
        
        ########### Background img setting #########
        bg=Image.open(r'./resources/background.jpg').resize((width,height),Image.LANCZOS)
        self.img1=ImageTk.PhotoImage(bg)
        bg_Label=Label(self.root,image=self.img1).pack()
        title=Label(self.root,text="FACE RECOGNITION",bg='RED',fg='white',font="Roboto 40 bold").place(x=0,y=30,width=1536)
        
        ################## Back Button ###############
        img2=Image.open(r'.\resources\back.png').resize((50,50),Image.LANCZOS)
        self.back_img=ImageTk.PhotoImage(image=img2)
        back_button=Button(self.root,image=self.back_img,bd=0,bg='red',command=self.backward).place(x=20,y=35)

        ########### left photo ###############
        img3=Image.open(r".\resources\face_rec1.png").resize((860,740),Image.LANCZOS)
        self.left_img=ImageTk.PhotoImage(image=img3)
        left_fr=Label(self.root,image=self.left_img,bd=0).place(x=10,y=110)
        
        ############ right photo ###################
        img4=Image.open(r".\resources\face_rec2.jpg").resize((650,740),Image.LANCZOS)
        self.right_img=ImageTk.PhotoImage(image=img4)
        right_fr=Label(self.root,image=self.right_img,bd=0).place(x=870,y=110)

        ############### redognition button ################
        recognise_button=Button(self.root,text="SCAN FACE",bg="#0459e6",fg="#ffffff",font="Roboto 10 bold",width=20,bd=0,command=self.face_rec).place(x=1110,y=780)
    
    ################ retrieve data from database ##############
    def std_det(self,std_id):
        data=self.Student.show_data("cursor",std_id)
        data_list=list(data.values())
        return data_list
    
    ############### recognition work ################
    def face_rec(self):
        self.people=os.listdir(r".\faceData")
        self.labels=np.load(r'.\resources\labels.npy')
        self.face_recognizer=cv.face.LBPHFaceRecognizer_create()
        self.face_recognizer.read(r'.\resources\faces_trained.yml')
        std_dict={}
        std_lb=""
        self.occ=0
        vdo=cv.VideoCapture(0)
        while True:
            flag,frame=vdo.read()
            if flag:
                x=0.8
                frame=cv.resize(frame,(0,0),None,x,x,interpolation=cv.INTER_AREA)
                gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
                face_list=self.harr_cascade.detectMultiScale(gray,1.2,5)
                if len(face_list)==0:
                    cv.putText(frame,'NO FACE DETECTED !',(10,30),cv.FONT_HERSHEY_TRIPLEX,0.7,(180,105,255),2)
                elif len(face_list)>=2:
                    cv.putText(frame,'MULTI FACE DETECTED !',(10,30),cv.FONT_HERSHEY_TRIPLEX,0.7,(180,105,255),2)
                else:
                    (x,y,w,h)=face_list[0]
                    img_roi=gray[y:y+h,x:x+w]
                    cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)
                    label,confi=self.face_recognizer.predict(img_roi)
                    # confi=int(100*(1-confi/300))
                    if confi>80:
                        cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)
                        cv.putText(frame,"Unknown !",(x,y-10),cv.FONT_HERSHEY_DUPLEX,0.5,(180,105,255),2)
                        self.occ=0
                    else:
                        std_id=self.people[label]
                        std_info=self.std_det(std_id)
                        std_lb=std_id
                        self.occ+=1
                        std_dict[std_lb]=self.occ
                        if std_id in self.scanned:   
                            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)
                            cv.putText(frame,f"Dept: {std_info[1]}",(x,y-10),cv.FONT_HERSHEY_DUPLEX,0.5,(180,105,255),2)
                            cv.putText(frame,f"Name: {std_info[4]}",(x,y-25),cv.FONT_HERSHEY_DUPLEX,0.5,(180,105,255),2)
                            cv.putText(frame,f"Sem: {std_info[2]}",(x,y-40),cv.FONT_HERSHEY_DUPLEX,0.5,(180,105,255),2)
                            if std_id not in self.attendee:
                                self.attendee.append(std_id)
                                self.markAttendance(std_id) 
                        else:
                            if std_dict[std_id] < 100:
                                cv.putText(frame,"Scanning",(x,y-10),cv.FONT_HERSHEY_DUPLEX,0.5,(180,105,255),2)
                                cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)
                            else:
                                self.scanned.append(std_id)
                                
                    # cv.putText(frame,str(confi),(x,y-50),cv.FONT_HERSHEY_DUPLEX,1,(0,0,255),1)
                cv.imshow('faces',frame)
                
            else:
                break
            if cv.waitKey(1)==27 or cv.getWindowProperty("faces", cv.WND_PROP_VISIBLE) <1:
                break
        vdo.release()
        cv.destroyAllWindows()
    
    ############## opening csv file and marking as attendance ###############
    def markAttendance(self,std_id):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        self.attendee.append(std_id)
        csvfile_name=os.listdir(r".\atd_files")[0]
        file_name=f".\\atd_files\\{csvfile_name}"
        csv_file=pd.read_csv(file_name)
        csv_file.loc[int(std_id[-1])-1,self.today]=f"P-{now}"
        csv_file.to_csv(file_name,index=FALSE)
        
    def backward(self):
        self.root.withdraw()
        # self.root.destroy()   
if __name__=="__main__":
    root=Tk()
    td=Recognition(root)
    root.mainloop()