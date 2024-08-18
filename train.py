from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
import numpy as np
import cv2




class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="orange")
        title_lbl.place(x=0,y=0,width=1360,height=45)


        image_top=Image.open(r"D:\Face Recognition System\Images\6295132d7bc0a.jpg")
        image_top=image_top.resize((1500,325),Image.BILINEAR)
        self.photoimg_top=ImageTk.PhotoImage(image_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=46,width=1500,height=325)


        #button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="black",fg="green")
        b1_1.place(x=0,y=330,width=1360,height=40)


        image_bottom=Image.open(r"D:\Face Recognition System\Images\629512b9e28ba.jpg")
        image_bottom=image_bottom.resize((1500,325),Image.BILINEAR)
        self.photoimg_bottom=ImageTk.PhotoImage(image_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=370,width=1500,height=325)

    def train_classifier(self):

        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:

            img=Image.open(image).convert('L')  #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #train classifier
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("train/classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")
   

        
if __name__== "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()




if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()