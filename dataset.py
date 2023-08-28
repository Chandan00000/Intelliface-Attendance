import cv2 as cv
import numpy as np
import os
class DataSet():
    def __init__(self) :
        self.harr_cascade=cv.CascadeClassifier(".\\resources\\harr_face.xml")
        
    ######### scanning faces in image and creating photoes with only face area ############ 
    def resize_img(self,img):
        gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        face_rect=self.harr_cascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=6)
        if len(face_rect)==1 :
            for (x,y,w,h) in face_rect:
                face_roi=gray[y:y+h,x:x+w]
                face=cv.resize(face_roi,(450,450),interpolation=cv.INTER_LINEAR)
                return face
        else :
            return None
        
    ########## saving face image in separate directory
    def takePhotoSample(self,std_id,update=False):
        if not update :
            try:
                os.mkdir(f".\\faceData\\{std_id}")
            except os.error as e:
                return str(e) 
        file_path=f".\\faceData\\{std_id}\\"
        i=0
        try:
            vdo=cv.VideoCapture(0)
            while(vdo.isOpened()):
                flag,frame=vdo.read()
                loading_txt=f"Scanning - {int((i+1)/2)}%   "+"."*i
                cv.rectangle(frame,(5,340),(635,355),(179,179,179),-1)
                cv.putText(frame,loading_txt,(10,352),cv.FONT_HERSHEY_TRIPLEX,0.47,(75,0,27),2)
                cv.imshow("Generating dataSet",frame)
                x=0.6
                frame=cv.resize(frame,(0,0),None,x,x,interpolation=cv.INTER_AREA)
                if flag:
                    img=self.resize_img(frame)
                    if img is not None:
                        std_file=f"{file_path}ph{i+1}.jpg"
                        cv.imwrite(std_file,img)
                        i+=1 
                if cv.waitKey(20)==27 or i==300:
                    break
            vdo.release()
            cv.destroyAllWindows()
        except :
            return "Video Error !"
        return None
if __name__=="__main__"  :
    ds=DataSet()
    print(ds.takePhotoSample("s1",False))