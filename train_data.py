import cv2 as cv
import numpy as np
from PIL import Image
import os
class TrainingData():
    def __init__(self):
        self.harr_cascade=cv.CascadeClassifier(r'.\resources\harr_face.xml')
    def train_faces(self):
        self.dir=r".\faceData"
        self.people=os.listdir(self.dir)
        features=[]
        labels=[]
        for person in self.people:
            path=os.path.join(self.dir,person)
            label=self.people.index(person)
            for img in os.listdir(path):
                img_path=os.path.join(path,img)
                img=Image.open(img_path).convert('L')
                imgNp=np.array(img,'uint8')
                features.append(imgNp)
                labels.append(label)
        print(len(features),len(labels))
        labels=np.array(labels)
        face_recognizer=cv.face.LBPHFaceRecognizer_create() #Local Binary Pattern Histogram
        face_recognizer.train(features,labels)
        face_recognizer.save(r'.\resources\faces_trained.yml')
        np.save(r'.\resources\labels.npy',labels)
        return 'Training Completed !'
if __name__=="__main__":
    td=TrainingData()
    td.train_faces()