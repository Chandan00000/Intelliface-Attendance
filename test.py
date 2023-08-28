# from tkinter import *
# import tkinter.messagebox as tkm
# root=Tk()
# root.geometry("500x500")
# update=tkm.askyesno("gehf","fewfew")
# print(update)
# root.mainloop()
# import cv2 as cv
# vdo=cv.VideoCapture(0)
# while vdo.isOpened():
#     x,frame=vdo.read()
#     cv.imshow("help",frame)
#     if cv.waitKey(20)==27:
#         break  
# vdo.release()
# cv.destroyAllWindows()
# err=False
# if True:
#     try:
#         print(10/0)
        
#     except:
#         err=True
#         print(err)
#         print("err")
# import os
# import pandas as pd
# csvfile_name=os.listdir(r".\atd_files")[0]
# file_name=f".\\atd_files\\{csvfile_name}"
# df=pd.read_csv(file_name)
# print(df.columns.values)
# df.loc[len(df)]=["s1","2001104076","Chandan","CSE","3rd"]
# df.loc[len(df)]=["s2","2001104077","rutu","CSE","3rd"]
# df.loc[len(df)]=["s3","2001104078","avanti","CSE","3rd"]
# df.loc[len(df)]=["s4","2001104079","bubu","CSE","3rd"]
# df.loc[len(df)]=["s5","2001104080","sahoo","CSE","3rd"]
# df.loc[1,"22/07/2023"]="prese"
# df.loc[3,"22/07/2023"]=("prese")
# # df.to_csv(file_name,index=False)
# print(df)
# try: 
#     print(10/2)
# except:
#     print(10/0)
# else:
#     print("else")
# import datetime
# today=datetime.date.today().strftime("%b/%d/%Y")
# print(today)
# import os

# csvfile_name=os.listdir(r".\atd_files")[0]
# file_name=f".\\atd_files\\{csvfile_name}"
# csv_file=pd.read_csv(file_name)
# print(csv_file)
# csv_file=csv_file.drop(["s1"],axis=0)
# print(csv_file)
# std_id="s1"
# csv_file.loc[0,"22/2/3"]="Present"
# csv_file.loc[0,"22/2/3"]="Present"
# csv_file.loc[0,"22/2/3"]="Present"
# csv_file.loc[0,"22/2/3"]="Present"
# csv_file.loc[0,"22/2/3"]="Present"
# csv_file.loc[0,"22/2/3"]="Present"
# csv_file.loc[0,"22/2/3"]="Present"
# csv_file.to_csv(file_name,index=False)
# print("\033[1;37m"+"hello")
# from tkinter import filedialog
# import csv
# file_path=filedialog.askopenfilename(initialdir=".\\atd_files",title="Import CSV",filetypes=(("CSV FILE","*.csv"),("ALL FILE","*.*")))
# with open(file_path) as f:
#     csv_reaader=csv.reader(f)
#     fields=next(csv_reaader)
#     for i in csv_reaader:
#         print(i)
# csv_data=["chandan","rutu"]
# class x:
#     def __init__(self):
#         self.z()
#     def z(self):
#         global csv_data
#         self.y(csv_data)
#     def y(self,data):
#         for i in data:
#             i="name"
        
# if __name__=="__main__":
#     a=x()
# s=2
# ="hello"
d={}
s="s1"
d[s]=10
s="s2"
d[s]=12
print(d)
print(d["s1"])
