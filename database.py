import pymongo
from pymongo import errors
import tkinter.messagebox as tkm
import pandas as pd
class Database:
    def __init__(self,db_name,col_name) :
        try:
            self.client=pymongo.MongoClient(host="mongodb://localhost:27017")
        except:
            tkm.showerror("Database","Database Not Connected !")    
        self.db=self.client[db_name]
        self.col=self.db[col_name]
        try:
            self.csv_file=open(f".\\atd_files\\{col_name}.csv","r")
        except OSError:
            self.csv_file=open(f".\\atd_files\\{col_name}.csv","w")
            
        self.file_name=f".\\atd_files\\{col_name}.csv"
        csv_cols=["STUDENT-ID","DEPARTMENT","YEAR","SEMESTER","REG-NO","NAME"]
        try:
            self.df = pd.read_csv(self.csv_file)
        except :
            self.df = pd.DataFrame(columns=csv_cols)
        self.df.to_csv(self.file_name,index=False)
        
    def insert_data(self,dept,year,sem,std_id,std_name,std_roll,std_grp,std_gender,std_dob,std_email,std_ph,std_address,photoSam):
        try:
            if dept=="Select Dept":
                dept="None"
            if year=="Select Year":
                year="None"
            if sem=="Select Sem":
                sem="None"
            data={"_id":std_id,"dept":dept,"year":year,"sem":sem,"std_name":std_name,"std_roll":std_roll,"std_grp":std_grp,"std_gender":std_gender,"std_dob":std_dob,"std_email":std_email,"std_ph":std_ph,"std_address":std_address,"photoSam":photoSam}
            insert=self.col.insert_one(data)
            self.df.loc[len(self.df)]=[std_id,dept,year,sem,std_roll,std_name]
            self.df.to_csv(self.file_name,index=False)
            return True
        except errors.DuplicateKeyError:
            return "Student-ID already exist !"
        except ValueError as e:
            return str(e)
        
    def show_data(self,var,text):
        if var =="Student ID":
            std_details=self.col.find({"_id":text},{"dept":1,"year":1,"sem":1,"std_name":1,"std_roll":1,"photoSam":1})
        elif var =="Name":
            std_details=self.col.find({"std_name":text},{"dept":1,"year":1,"sem":1,"std_name":1,"std_roll":1,"photoSam":1})
        elif var =="all":
            std_details=self.col.find({},{"dept":1,"year":1,"sem":1,"std_name":1,"std_roll":1,"photoSam":1}).sort("_id")  
        elif var =="cursor":
            std_details=self.col.find_one({"_id":text})
        return std_details
    
    def update_data(self,dept,year,sem,std_id,std_name,std_roll,std_grp,std_gender,std_dob,std_email,std_ph,std_address,photoSam):
        try:
            if dept=="Select Dept":
                dept="None"
            if year=="Select Year":
                year="None"
            if sem=="Select Sem":
                sem="None"
            data={"dept":dept,"year":year,"sem":sem,"std_name":std_name,"std_roll":std_roll,"std_grp":std_grp,"std_gender":std_gender,"std_dob":std_dob,"std_email":std_email,"std_ph":std_ph,"std_address":std_address,"photoSam":photoSam}
            update=self.col.update_one({"_id":std_id},{"$set":data},upsert=True)
            self.df.loc[int(std_id[-1])-1,"STUDENT-ID"]=std_id
            self.df.loc[int(std_id[-1])-1,"DEPARTMENT"]=dept
            self.df.loc[int(std_id[-1])-1,"YEAR"]=year
            self.df.loc[int(std_id[-1])-1,"SEMESTER"]=sem
            self.df.loc[int(std_id[-1])-1,"REG-NO"]=std_roll
            self.df.loc[int(std_id[-1])-1,"NAME"]=std_name
            self.df.to_csv(self.file_name,index=False)
            return True
        except Exception as ee: 
            return str(ee)   

    def delete_data(self,std_id):
        try:
            self.df=self.df.drop([int(std_id[-1])-1],axis=0)
            self.df.to_csv(self.file_name,index=False)
            delete=self.col.delete_one({"_id":std_id})
            return True
        except errors.DuplicateKeyError as ee: 
            return str(ee)
        except Exception as e:
            return str(e)
    
if __name__=="__main__":
    Student=Database("Student","data")