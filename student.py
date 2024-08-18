from tkinter import *
from tkinter import messagebox, ttk
import cv2
import mysql.connector
import numpy
#from turtle import width
from PIL import Image, ImageTk
import os


class student_management_system:
    def __init__(self,root):

         self.root=root
         self.root.geometry("1530x790+0+0")
         self.root.title("student manegment system")

         #====variables=====
         self.var_dept=StringVar()
         self.var_course=StringVar()
         self.var_year=StringVar()
         self.var_semester=StringVar()
         self.var_std_id=StringVar()
         self.var_name=StringVar()
         self.var_div=StringVar()
         self.var_roll=StringVar()
         self.var_gender=StringVar()
         self.var_dob=StringVar()
         self.var_email=StringVar()
         self.var_phone=StringVar()
         self.var_address=StringVar()
         self.var_teacher=StringVar()


         img=Image.open(r"D:\Face Recognition System\Images\629511a5d621c.jpg")
         img=img.resize((500,150),Image.BILINEAR)
         self.photoimg=ImageTk.PhotoImage(img)

         f_lbl=Label(self.root,image=self.photoimg)
         f_lbl.place(x=0,y=0,width=500,height=150)


         #second image

         img1=Image.open(r"D:\Face Recognition System\Images\629511a5d621c.jpg")
         img1=img1.resize((500,150),Image.BILINEAR)
         self.photoimg1=ImageTk.PhotoImage(img1)

         f_lbl=Label(self.root,image=self.photoimg1)
         f_lbl.place(x=500,y=0,width=500,height=150)

         #thirde image
         img2=Image.open(r"D:\Face Recognition System\Images\629511a5d621c.jpg")
         img2=img2.resize((500,150),Image.BILINEAR)
         self.photoimg2=ImageTk.PhotoImage(img2)

         f_lbl=Label(self.root,image=self.photoimg2)
         f_lbl.place(x=1000,y=0,width=550,height=150)

         #background image
         img3=Image.open(r"D:\Face Recognition System\Images\628e5e859a976.jpg")
         img3=img3.resize((1530,660),Image.BILINEAR)
         self.photoimg3=ImageTk.PhotoImage(img3)

         bg_img=Label(self.root,image=self.photoimg3)
         bg_img.place(x=0,y=130,width=1530,height=660)
         title_lbl=Label(bg_img,text="Student Manegment system", font=("times new roman", 35,"bold"),bg="white",fg="green")
         title_lbl.place(x=0,y=0,width=1530,height=45)

         #creating frame
         main_frame=Frame(bg_img,bd=4)
         main_frame.place(x=20,y=48,width=1480,height=600)

         #left label frame
         Left_frame=LabelFrame(main_frame,bd=5,relief=RIDGE,text="Student Details",font=("times new roman", 15,"italic"))
         Left_frame.place(x=10,y=10,width=720,height=580)

         image_left=Image.open(r"D:\Face Recognition System\Images\628e5e859a976.jpg")
         image_left=img2.resize((820,130),Image.BILINEAR)
         self.photoimg_left=ImageTk.PhotoImage(image_left)

         f_lbl=Label(Left_frame,image=self.photoimg_left)
         f_lbl.place(x=5,y=0,width=700,height=130)

         #current course
         current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman", 15,"italic"))
         current_course_frame.place(x=5,y=135,width=700,height=150)
         dept_label=Label(current_course_frame,text="Department",font=("times new roman", 10,"bold"))
         dept_label.grid(row=0,column=0,padx=10)

         dept_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dept,font=("times new roman", 10,"bold"),state="readonly")
         dept_combo["values"]=("select Department","Cse","It","Mechanical","civil","Ece")
         dept_combo.current(0)
         dept_combo.grid(row=0,column=1,padx=10,pady=10)
         
         #course
       
         course_label=Label(current_course_frame,text="Course",font=("times new roman", 10,"bold"))
         course_label.grid(row=0,column=2,padx=10,sticky=W)

         course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman", 10,"bold"),state="readonly")
         course_combo["values"]=("select course","Btech","bca","Hons")
         course_combo.current(0)
         course_combo.grid(row=0,column=3,padx=10,pady=10,sticky=W)

         #year

         
         year_label=Label(current_course_frame,text="Year",font=("times new roman", 10,"bold"))
         year_label.grid(row=1,column=0,padx=10,sticky=W)

         year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman", 10,"bold"),state="readonly")
         year_combo["values"]=("2019-20","2020-21","2021-22","2012-23")
         year_combo.current(0)
         year_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)

         #semester

         semester_label=Label(current_course_frame,text="Semester",font=("times new roman", 10,"bold"))
         semester_label.grid(row=1,column=2,padx=10,sticky=W)

         semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman", 10,"bold"),state="readonly")
         semester_combo["values"]=("1ST","2ND","3RD","4TH","5TH","6TH","7TH","8TH")
         semester_combo.current(0)
         semester_combo.grid(row=1,column=3,padx=10,pady=10,sticky=W)

         #class student information
         student_information__frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class student information",font=("times new roman", 15,"italic"))
         student_information__frame.place(x=5,y=260,width=700,height=300)

         #student id
         studentid_label=Label(student_information__frame,text="StudentID:",font=("times new roman", 12,"italic"),bg="white",fg="#00ffff")
         studentid_label.grid(row=0,column=0,padx=10,pady=2,sticky=W)

         studentid_entry=ttk.Entry(student_information__frame,textvariable=self.var_std_id,width=20,font=("times new roman", 12,"italic"))
         studentid_entry.grid(row=0,column=1,padx=10,sticky=W)

         #student name
         studentid_label=Label(student_information__frame,text="Student Name:",font=("times new roman", 12,"italic"),fg="#3b3c36")
         studentid_label.grid(row=0,column=2,padx=10,sticky=W)

         studentid_entry=ttk.Entry(student_information__frame,textvariable=self.var_name,width=20,font=("times new roman", 12,"italic"))
         studentid_entry.grid(row=0,column=3,padx=10,sticky=W)

         #class division
         studentid_label=Label(student_information__frame,text="Class Division:",font=("times new roman", 12,"italic"),fg="#3b3c36")
         studentid_label.grid(row=1,column=0,padx=5,sticky=W)

         studentid_entry=ttk.Entry(student_information__frame,textvariable=self.var_div,width=20,font=("times new roman", 12,"italic"))
         studentid_entry.grid(row=1,column=1,padx=10,pady=2,sticky=W)

         #roll no
         studentid_label=Label(student_information__frame,text="Roll No:",font=("times new roman", 12,"italic"),fg="#3b3c36")
         studentid_label.grid(row=1,column=2,padx=10,sticky=W)

         studentid_entry=ttk.Entry(student_information__frame,textvariable=self.var_roll,width=20,font=("times new roman", 12,"italic"))
         studentid_entry.grid(row=1,column=3,padx=10,sticky=W)

         #gender

         studentid_label=Label(student_information__frame,text="Gender",font=("times new roman", 12,"italic"),fg="#3b3c36")
         studentid_label.grid(row=2,column=0,padx=10,sticky=W)

       
         gender_combo=ttk.Combobox(student_information__frame,textvariable=self.var_gender,font=("times new roman", 10,"bold"),state="readonly")
         gender_combo["values"]=("MALE","FEMALE","OTHER")
         gender_combo.current(0)
         gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)


         #date of birth

         studentid_label=Label(student_information__frame,text="DOB",font=("times new roman", 12,"italic"),fg="#3b3c36")
         studentid_label.grid(row=2,column=2,padx=10,pady=2,sticky=W)

         studentid_entry=ttk.Entry(student_information__frame,textvariable=self.var_dob,width=20,font=("times new roman", 12,"italic"))
         studentid_entry.grid(row=2,column=3,padx=10,pady=2,sticky=W)

         #email
         studentid_label=Label(student_information__frame,text="Email:",font=("times new roman", 12,"italic"),fg="#3b3c36")
         studentid_label.grid(row=3,column=0,padx=10,pady=2,sticky=W)

         studentid_entry=ttk.Entry(student_information__frame,textvariable=self.var_email,width=20,font=("times new roman", 12,"italic"))
         studentid_entry.grid(row=3,column=1,padx=10,pady=2,sticky=W)

         #phone no
         studentid_label=Label(student_information__frame,text="Phone No:",font=("times new roman", 12,"italic"),fg="#3b3c36")
         studentid_label.grid(row=3,column=2,padx=10,pady=2,sticky=W)

         studentid_entry=ttk.Entry(student_information__frame,textvariable=self.var_phone,width=20,font=("times new roman", 12,"italic"))
         studentid_entry.grid(row=3,column=3,padx=10,pady=2,sticky=W)

         #address
         studentid_label=Label(student_information__frame,text="Address",font=("times new roman", 12,"italic"),fg="#3b3c36")
         studentid_label.grid(row=4,column=0,padx=10,pady=3,sticky=W)
         studentid_entry=ttk.Entry(student_information__frame,textvariable=self.var_address,width=20,font=("times new roman", 12,"italic"))
         studentid_entry.grid(row=4,column=1,padx=10,pady=2,sticky=W)

         #teacher

         studentid_label=Label(student_information__frame,text="Teacher Name",font=("times new roman", 12,"italic"),fg="#3b3c36")
         studentid_label.grid(row=4,column=2,padx=10,pady=3,sticky=W)

         studentid_entry=ttk.Entry(student_information__frame,textvariable=self.var_teacher,width=20,font=("times new roman", 12,"italic"))
         studentid_entry.grid(row=4,column=3,padx=10,pady=2,sticky=W)

         #radio button
         self.var_radio1=StringVar()
         radiobtn1=ttk.Radiobutton(student_information__frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
         radiobtn1.grid(row=6,column=0)
         



         radiobtn2=ttk.Radiobutton(student_information__frame,variable=self.var_radio1,text="No Photo Sample",value="no")
         radiobtn2.grid(row=6,column=1)

         #button frame
         btn_frame=Frame(student_information__frame,bd=2,relief=RIDGE,bg="white")
         btn_frame.place(x=0,y=180,width=715,height=36)

         save_btn=Button(btn_frame,text="Save", command=self.add_data,width=19,font=("times new roman",12,"bold"),bg="#89cff0")
         save_btn.grid(row=0,column=0)

         update_btn=Button(btn_frame,text="Update",command=self.update_data,width=19,font=("times new roman",12,"bold"),bg="#89cff0")
         update_btn.grid(row=0,column=1)

         delete_btn=Button(btn_frame,text="Delete", command=self.delete_data,width=19,font=("times new roman",12,"bold"),bg="#89cff0")
         delete_btn.grid(row=0,column=2)

         reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("times new roman",12,"bold"),bg="#89cff0")
         reset_btn.grid(row=0,column=3)

         btn_frame1=Frame(student_information__frame,bd=2,relief=RIDGE,bg="white")
         btn_frame1.place(x=0,y=220,width=715,height=70)

         take_photo_btn=Button(btn_frame1,text="Take Photo Sample",width=40,font=("times new roman",12,"bold"),bg="#89cff0")
         take_photo_btn.grid(row=0,column=0)

         update_photo_btn=Button(btn_frame1,text="update Photo Sample",width=40,font=("times new roman",12,"bold"),bg="#89cff0")
         update_photo_btn.grid(row=0,column=1)





         



         

         #rightft label frame

         right_frame=LabelFrame(main_frame,bd=5,relief=RIDGE,text="Student Details",font=("times new roman", 10,"bold"))
         right_frame.place(x=730,y=10,width=730,height=580)

         right_img=Image.open(r"D:\Face Recognition System\Images\629511a5d621c.jpg")
         right_img=img.resize((820,130),Image.BILINEAR)
         self.rphotoimg=ImageTk.PhotoImage(right_img)

         f_lbl=Label(right_frame,image=self.rphotoimg)
         f_lbl.place(x=0,y=0,width=720,height=130)

         #search system
         search_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="search details",font=("times new roman", 15,"italic"))
         search_frame.place(x=5,y=135,width=700,height=70)

         search_label=Label(search_frame,text="Search by:",font=("times new roman", 12,"italic"),fg="#3b3c36")
         search_label.grid(row=0,column=0,padx=10,pady=2,sticky=W)

         search_combo=ttk.Combobox(search_frame,font=("times new roman", 10,"bold"),state="readonly")
         search_combo["values"]=("select","roll","Name","Dept")
         search_combo.current(0)
         search_combo.grid(row=0,column=1,padx=10,pady=10,sticky=W)

         search_entry=ttk.Entry(search_frame,width=20,font=("times new roman", 12,"italic"))
         search_entry.grid(row=0,column=2,padx=10,pady=2,sticky=W)

         
         search_btn=Button(search_frame,text="Search",width=10,font=("times new roman", 12,"italic"))
         search_btn.grid(row=0,column=3)

         ShowAll_btn=Button(search_frame,text="Show All",width=10,font=("times new roman", 12,"italic"))
         ShowAll_btn.grid(row=0,column=4)

         #======table framwe=======

         table_frame=Frame(right_frame,bd=2,relief=RIDGE)
         table_frame.place(x=5,y=210,width=700,height=350)

         scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
         scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

         self.student_table=ttk.Treeview(table_frame,column=("dept","course","year","sem","std_id","name","div","roll","gender","dob","email","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
         scroll_x.pack(side=BOTTOM,fill=X)
         scroll_y.pack(side=RIGHT,fill=Y)
         scroll_x.config(command=self.student_table.xview)
         scroll_y.config(command=self.student_table.yview)

         self.student_table.heading("dept",text="department")
         self.student_table.heading("course",text="Course")
         self.student_table.heading("year",text="Year")
         self.student_table.heading("sem",text="Semester")
         self.student_table.heading("std_id",text="Student Id")
         self.student_table.heading("name",text="Name")
         self.student_table.heading("div",text="division")
         self.student_table.heading("roll",text="Roll")
         self.student_table.heading("gender",text="Gender")
         self.student_table.heading("dob",text="Date of Birth")
         self.student_table.heading("email",text="Email")
         self.student_table.heading("address",text="Address")
         self.student_table.heading("teacher",text="Teacher")
         self.student_table.heading("photo",text="Photo sample status")
         self.student_table["show"]="headings"

         self.student_table.pack(fill=BOTH,expand=1)
         self.student_table.bind("<ButtonRelease>",self.get_cursor)
         self.fetch_data()

         ####function declaration############
    def add_data(self):
        if self.var_dept.get()=="Select Department" or self.var_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("error","All Fields required",parent=self.root)
        else:
            
                
       
          
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='root',database='face_recognizer')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                    self.var_dept.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    
                    self.var_teacher.get(),
                    
                                  
                    self.var_radio1.get(),
                   
                ))
                conn.commit()
                self.fetch_data()
                
                conn.close()
                messagebox.showinfo("Success","Student details has been added succcessfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)

     
     
     
      ######################################### Fetch data #########################################
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='root',database='face_recognizer')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

        #===============get cursor======
    def get_cursor(self,event=""):
        cuursor_focus=self.student_table.focus()  #this is for focusing the cursor
        content=self.student_table.item(cuursor_focus)  #this for geeting the value from the table
        
        data=content["values"]
        
        self.var_dept.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14]),
    
    ### update details#######
    def update_data(self):
        if self.var_dept.get()=="Select Department" or self.var_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("error","All Fields required",parent=self.root)
      
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update",parent=self.root)
                if(update>0):
                    conn=mysql.connector.connect(host='localhost',username='root',password='root',database='face_recognizer')
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set dept=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where std_id=%s",(

                    self.var_dept.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    
                    self.var_teacher.get(),
                    
                                  
                    self.var_radio1.get(),
                   
                     

                    self.var_std_id.get()
                    


                    ))
                    
                    

                

                    
                else:
                    if not update:
                        return 

                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","student detail successfully updated",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)

                #========delete the dat=========
                
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete",parent=self.root)
                if(delete>0):
                    conn=mysql.connector.connect(host='localhost',username='root',password='root',database='face_recognizer')
                    my_cursor=conn.cursor()
                    sql='delete from student where std_id=%s'
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)

                else:
                    if not delete:
                        return 

                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","student detail successfully deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)




     ##=====================reset all========  
    def reset_data(self):
          self.var_dept.set("select Department"),
          self.var_course.set("select course"),
          self.var_year.set("2019-20"),
          self.var_semester.set("1ST"),
          self.var_std_id.set("")
            
          self.var_name.set(""),
          self.var_div.set(""),
          self.var_roll.set(""),
        
          self.var_gender.set(""),
          self.var_dob.set(""),
          self.var_email.set(""),
          self.var_phone.set(""),
          self.var_address.set(""),
        
          self.var_teacher.set(""),
        
                        
          self.var_radio1.set(""),
    #from cgitb import text



import csv
from tkinter import *
from tkinter import messagebox, ttk

import cv2
import mysql.connector
import numpy
#from turtle import width
from PIL import Image, ImageTk


class student_management_system:
    def __init__(self,root):

         self.root=root
         self.root.geometry("1530x790+0+0")
         self.root.title("student manegment system")

         #====variables=====
         self.var_dept=StringVar()
         self.var_course=StringVar()
         self.var_year=StringVar()
         self.var_semester=StringVar()
         self.var_std_id=StringVar()
         self.var_name=StringVar()
         self.var_div=StringVar()
         self.var_roll=StringVar()
         self.var_gender=StringVar()
         self.var_dob=StringVar()
         self.var_email=StringVar()
         self.var_phone=StringVar()
         self.var_address=StringVar()
         self.var_teacher=StringVar()


         img=Image.open(r"D:\Face Recognition System\Images\628e5df65b50f.jpg")
         img=img.resize((500,150),Image.BILINEAR)
         self.photoimg=ImageTk.PhotoImage(img)

         f_lbl=Label(self.root,image=self.photoimg)
         f_lbl.place(x=0,y=0,width=500,height=150)


         #second image

         img1=Image.open(r"D:\Face Recognition System\Images\628e5df65b50f.jpg")
         img1=img1.resize((500,150),Image.BILINEAR)
         self.photoimg1=ImageTk.PhotoImage(img1)

         f_lbl=Label(self.root,image=self.photoimg1)
         f_lbl.place(x=500,y=0,width=500,height=150)

         #thirde image
         img2=Image.open(r"D:\Face Recognition System\Images\628e5df65b50f.jpg")
         img2=img2.resize((500,150),Image.BILINEAR)
         self.photoimg2=ImageTk.PhotoImage(img2)

         f_lbl=Label(self.root,image=self.photoimg2)
         f_lbl.place(x=1000,y=0,width=550,height=150)

         #background image
         img3=Image.open(r"D:\Face Recognition System\Images\628e5df65b50f.jpg")
         img3=img3.resize((1530,660),Image.BILINEAR)
         self.photoimg3=ImageTk.PhotoImage(img3)

         bg_img=Label(self.root,image=self.photoimg3)
         bg_img.place(x=0,y=130,width=1530,height=660)
         title_lbl=Label(bg_img,text="Student Manegment system", font=("times new roman", 35,"bold"),bg="white",fg="green")
         title_lbl.place(x=0,y=0,width=1530,height=45)

         #creating frame
         main_frame=Frame(bg_img,bd=4)
         main_frame.place(x=20,y=48,width=1480,height=600)

         #left label frame
         Left_frame=LabelFrame(main_frame,bd=5,relief=RIDGE,text="Student Details",font=("times new roman", 15,"italic"))
         Left_frame.place(x=10,y=10,width=720,height=580)

         image_left=Image.open(r"D:\Face Recognition System\Images\628e5df65b50f.jpg")
         image_left=img2.resize((820,130),Image.BILINEAR)
         self.photoimg_left=ImageTk.PhotoImage(image_left)

         f_lbl=Label(Left_frame,image=self.photoimg_left)
         f_lbl.place(x=5,y=0,width=700,height=130)

         #current course
         current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman", 15,"italic"))
         current_course_frame.place(x=5,y=135,width=700,height=150)
         dept_label=Label(current_course_frame,text="Department",font=("times new roman", 10,"bold"))
         dept_label.grid(row=0,column=0,padx=10)

         dept_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dept,font=("times new roman", 10,"bold"),state="readonly")
         dept_combo["values"]=("select Department","Cse","It","Mechanical","civil","Ece")
         dept_combo.current(0)
         dept_combo.grid(row=0,column=1,padx=10,pady=10)
         
         #course
       
         course_label=Label(current_course_frame,text="Course",font=("times new roman", 10,"bold"))
         course_label.grid(row=0,column=2,padx=10,sticky=W)

         course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman", 10,"bold"),state="readonly")
         course_combo["values"]=("select course","Btech","bca","Hons")
         course_combo.current(0)
         course_combo.grid(row=0,column=3,padx=10,pady=10,sticky=W)

         #year

         
         year_label=Label(current_course_frame,text="Year",font=("times new roman", 10,"bold"))
         year_label.grid(row=1,column=0,padx=10,sticky=W)

         year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman", 10,"bold"),state="readonly")
         year_combo["values"]=("2019-20","2020-21","2021-22","2012-23")
         year_combo.current(0)
         year_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)

         #semester

         semester_label=Label(current_course_frame,text="Semester",font=("times new roman", 10,"bold"))
         semester_label.grid(row=1,column=2,padx=10,sticky=W)

         semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman", 10,"bold"),state="readonly")
         semester_combo["values"]=("1ST","2ND","3RD","4TH","5TH","6TH","7TH","8TH")
         semester_combo.current(0)
         semester_combo.grid(row=1,column=3,padx=10,pady=10,sticky=W)

         #class student information
         student_information__frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class student information",font=("times new roman", 15,"italic"))
         student_information__frame.place(x=5,y=260,width=700,height=300)

         #student id
         studentid_label=Label(student_information__frame,text="StudentID:",font=("times new roman", 12,"italic"),bg="white",fg="#00ffff")
         studentid_label.grid(row=0,column=0,padx=10,pady=2,sticky=W)

         studentid_entry=ttk.Entry(student_information__frame,textvariable=self.var_std_id,width=20,font=("times new roman", 12,"italic"))
         studentid_entry.grid(row=0,column=1,padx=10,sticky=W)

         #student name
         studentid_label=Label(student_information__frame,text="Student Name:",font=("times new roman", 12,"italic"),fg="#3b3c36")
         studentid_label.grid(row=0,column=2,padx=10,sticky=W)

         studentid_entry=ttk.Entry(student_information__frame,textvariable=self.var_name,width=20,font=("times new roman", 12,"italic"))
         studentid_entry.grid(row=0,column=3,padx=10,sticky=W)

         #class division
         studentid_label=Label(student_information__frame,text="Class Division:",font=("times new roman", 12,"italic"),fg="#3b3c36")
         studentid_label.grid(row=1,column=0,padx=5,sticky=W)

         studentid_entry=ttk.Entry(student_information__frame,textvariable=self.var_div,width=20,font=("times new roman", 12,"italic"))
         studentid_entry.grid(row=1,column=1,padx=10,pady=2,sticky=W)

         #roll no
         studentid_label=Label(student_information__frame,text="Roll No:",font=("times new roman", 12,"italic"),fg="#3b3c36")
         studentid_label.grid(row=1,column=2,padx=10,sticky=W)

         studentid_entry=ttk.Entry(student_information__frame,textvariable=self.var_roll,width=20,font=("times new roman", 12,"italic"))
         studentid_entry.grid(row=1,column=3,padx=10,sticky=W)

         #gender

         studentid_label=Label(student_information__frame,text="Gender",font=("times new roman", 12,"italic"),fg="#3b3c36")
         studentid_label.grid(row=2,column=0,padx=10,sticky=W)

       
         gender_combo=ttk.Combobox(student_information__frame,textvariable=self.var_gender,font=("times new roman", 10,"bold"),state="readonly")
         gender_combo["values"]=("MALE","FEMALE","OTHER")
         gender_combo.current(0)
         gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)


         #date of birth

         studentid_label=Label(student_information__frame,text="DOB",font=("times new roman", 12,"italic"),fg="#3b3c36")
         studentid_label.grid(row=2,column=2,padx=10,pady=2,sticky=W)

         studentid_entry=ttk.Entry(student_information__frame,textvariable=self.var_dob,width=20,font=("times new roman", 12,"italic"))
         studentid_entry.grid(row=2,column=3,padx=10,pady=2,sticky=W)

         #email
         studentid_label=Label(student_information__frame,text="Email:",font=("times new roman", 12,"italic"),fg="#3b3c36")
         studentid_label.grid(row=3,column=0,padx=10,pady=2,sticky=W)

         studentid_entry=ttk.Entry(student_information__frame,textvariable=self.var_email,width=20,font=("times new roman", 12,"italic"))
         studentid_entry.grid(row=3,column=1,padx=10,pady=2,sticky=W)

         #phone no
         studentid_label=Label(student_information__frame,text="Phone No:",font=("times new roman", 12,"italic"),fg="#3b3c36")
         studentid_label.grid(row=3,column=2,padx=10,pady=2,sticky=W)

         studentid_entry=ttk.Entry(student_information__frame,textvariable=self.var_phone,width=20,font=("times new roman", 12,"italic"))
         studentid_entry.grid(row=3,column=3,padx=10,pady=2,sticky=W)

         #address
         studentid_label=Label(student_information__frame,text="Address",font=("times new roman", 12,"italic"),fg="#3b3c36")
         studentid_label.grid(row=4,column=0,padx=10,pady=3,sticky=W)
         studentid_entry=ttk.Entry(student_information__frame,textvariable=self.var_address,width=20,font=("times new roman", 12,"italic"))
         studentid_entry.grid(row=4,column=1,padx=10,pady=2,sticky=W)

         #teacher

         studentid_label=Label(student_information__frame,text="Teacher Name",font=("times new roman", 12,"italic"),fg="#3b3c36")
         studentid_label.grid(row=4,column=2,padx=10,pady=3,sticky=W)

         studentid_entry=ttk.Entry(student_information__frame,textvariable=self.var_teacher,width=20,font=("times new roman", 12,"italic"))
         studentid_entry.grid(row=4,column=3,padx=10,pady=2,sticky=W)

         #radio button
         self.var_radio1=StringVar()
         radiobtn1=ttk.Radiobutton(student_information__frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
         radiobtn1.grid(row=6,column=0)
         



         radiobtn2=ttk.Radiobutton(student_information__frame,variable=self.var_radio1,text="No Photo Sample",value="no")
         radiobtn2.grid(row=6,column=1)

         #button frame
         btn_frame=Frame(student_information__frame,bd=2,relief=RIDGE,bg="white")
         btn_frame.place(x=0,y=180,width=715,height=36)

         save_btn=Button(btn_frame,text="Save", command=self.add_data,width=19,font=("times new roman",12,"bold"),bg="#89cff0")
         save_btn.grid(row=0,column=0)

         update_btn=Button(btn_frame,text="Update",command=self.update_data,width=19,font=("times new roman",12,"bold"),bg="#89cff0")
         update_btn.grid(row=0,column=1)

         delete_btn=Button(btn_frame,text="Delete", command=self.delete_data,width=19,font=("times new roman",12,"bold"),bg="#89cff0")
         delete_btn.grid(row=0,column=2)

         reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("times new roman",12,"bold"),bg="#89cff0")
         reset_btn.grid(row=0,column=3)

         btn_frame1=Frame(student_information__frame,bd=2,relief=RIDGE,bg="white")
         btn_frame1.place(x=0,y=220,width=715,height=70)

         take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=40,font=("times new roman",12,"bold"),bg="#89cff0")
         take_photo_btn.grid(row=0,column=0)

         update_photo_btn=Button(btn_frame1,text="update Photo Sample",width=40,font=("times new roman",12,"bold"),bg="#89cff0")
         update_photo_btn.grid(row=0,column=1)





         



         

         #rightft label frame

         right_frame=LabelFrame(main_frame,bd=5,relief=RIDGE,text="Student Details",font=("times new roman", 10,"bold"))
         right_frame.place(x=730,y=10,width=730,height=580)

         right_img=Image.open(r"D:\Face Recognition System\Images\628e5df65b50f.jpg")
         right_img=img.resize((820,130),Image.BILINEAR)
         self.rphotoimg=ImageTk.PhotoImage(right_img)

         f_lbl=Label(right_frame,image=self.rphotoimg)
         f_lbl.place(x=0,y=0,width=720,height=130)

         #search system
         search_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="search details",font=("times new roman", 15,"italic"))
         search_frame.place(x=5,y=135,width=700,height=70)

         search_label=Label(search_frame,text="Search by:",font=("times new roman", 12,"italic"),fg="#3b3c36")
         search_label.grid(row=0,column=0,padx=10,pady=2,sticky=W)

         search_combo=ttk.Combobox(search_frame,font=("times new roman", 10,"bold"),state="readonly")
         search_combo["values"]=("select","roll","Name","Dept")
         search_combo.current(0)
         search_combo.grid(row=0,column=1,padx=10,pady=10,sticky=W)

         search_entry=ttk.Entry(search_frame,width=20,font=("times new roman", 12,"italic"))
         search_entry.grid(row=0,column=2,padx=10,pady=2,sticky=W)

         
         search_btn=Button(search_frame,text="Search",width=10,font=("times new roman", 12,"italic"))
         search_btn.grid(row=0,column=3)

         ShowAll_btn=Button(search_frame,text="Show All",width=10,font=("times new roman", 12,"italic"))
         ShowAll_btn.grid(row=0,column=4)

         #======table framwe=======

         table_frame=Frame(right_frame,bd=2,relief=RIDGE)
         table_frame.place(x=5,y=210,width=700,height=350)

         scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
         scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

         self.student_table=ttk.Treeview(table_frame,column=("dept","course","year","sem","std_id","name","div","roll","gender","dob","email","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
         scroll_x.pack(side=BOTTOM,fill=X)
         scroll_y.pack(side=RIGHT,fill=Y)
         scroll_x.config(command=self.student_table.xview)
         scroll_y.config(command=self.student_table.yview)

         self.student_table.heading("dept",text="department")
         self.student_table.heading("course",text="Course")
         self.student_table.heading("year",text="Year")
         self.student_table.heading("sem",text="Semester")
         self.student_table.heading("std_id",text="Student Id")
         self.student_table.heading("name",text="Name")
         self.student_table.heading("div",text="division")
         self.student_table.heading("roll",text="Roll")
         self.student_table.heading("gender",text="Gender")
         self.student_table.heading("dob",text="Date of Birth")
         self.student_table.heading("email",text="Email")
         self.student_table.heading("address",text="Address")
         self.student_table.heading("teacher",text="Teacher")
         self.student_table.heading("photo",text="Photo sample status")
         self.student_table["show"]="headings"

         self.student_table.pack(fill=BOTH,expand=1)
         self.student_table.bind("<ButtonRelease>",self.get_cursor)
         self.fetch_data()

         ####function declaration############
    def add_data(self):
        if self.var_dept.get()=="Select Department" or self.var_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("error","All Fields required",parent=self.root)
        else:
            
                
       
          
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='root',database='face_recognizer')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                    self.var_dept.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    
                    self.var_teacher.get(),
                    
                                  
                    self.var_radio1.get(),
                   
                ))
                conn.commit()
                self.fetch_data()
                
                conn.close()
                messagebox.showinfo("Success","Student details has been added succcessfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)

     
     
     
      ######################################### Fetch data #########################################
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='root',database='face_recognizer')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

        #===============get cursor======
    def get_cursor(self,event=""):
        cuursor_focus=self.student_table.focus()  #this is for focusing the cursor
        content=self.student_table.item(cuursor_focus)  #this for geeting the value from the table
        
        data=content["values"]
        
        self.var_dept.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14]),
    
    ### update details#######
    def update_data(self):
        if self.var_dept.get()=="Select Department" or self.var_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("error","All Fields required",parent=self.root)
      
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update",parent=self.root)
                if(update>0):
                    conn=mysql.connector.connect(host='localhost',username='root',password='root',database='face_recognizer')
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set dept=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where std_id=%s",(

                    self.var_dept.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    
                    self.var_teacher.get(),
                    
                                  
                    self.var_radio1.get(),
                   
                     

                    self.var_std_id.get()
                    


                    ))
                    
                    

                

                    
                else:
                    if not update:
                        return 

                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","student detail successfully updated",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)

                #========delete the dat=========
                
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete",parent=self.root)
                if(delete>0):
                    conn=mysql.connector.connect(host='localhost',username='root',password='root',database='face_recognizer')
                    my_cursor=conn.cursor()
                    sql='delete from student where std_id=%s'
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)

                else:
                    if not delete:
                        return 

                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","student detail successfully deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)




     ##=====================reset all========  
    def reset_data(self):
          self.var_dept.set("select Department"),
          self.var_course.set("select course"),
          self.var_year.set("2019-20"),
          self.var_semester.set("1ST"),
          self.var_std_id.set("")
            
          self.var_name.set(""),
          self.var_div.set(""),
          self.var_roll.set(""),
        
          self.var_gender.set(""),
          self.var_dob.set(""),
          self.var_email.set(""),
          self.var_phone.set(""),
          self.var_address.set(""),
        
          self.var_teacher.set(""),
        
                        
          self.var_radio1.set(""),
    #from cgitb import text



import csv
from tkinter import *
from tkinter import messagebox, ttk

import cv2
import mysql.connector
import numpy
#from turtle import width
from PIL import Image, ImageTk


class student_management_system:
    def __init__(self,root):

         self.root=root
         self.root.geometry("1530x790+0+0")
         self.root.title("student manegment system")

         #====variables=====
         self.var_dept=StringVar()
         self.var_course=StringVar()
         self.var_year=StringVar()
         self.var_semester=StringVar()
         self.var_std_id=StringVar()
         self.var_name=StringVar()
         self.var_div=StringVar()
         self.var_roll=StringVar()
         self.var_gender=StringVar()
         self.var_dob=StringVar()
         self.var_email=StringVar()
         self.var_phone=StringVar()
         self.var_address=StringVar()
         self.var_teacher=StringVar()


         img=Image.open(r"D:\Face Recognition System\Images\628e5df65b50f.jpg")
         img=img.resize((500,150),Image.BILINEAR)
         self.photoimg=ImageTk.PhotoImage(img)

         f_lbl=Label(self.root,image=self.photoimg)
         f_lbl.place(x=0,y=0,width=500,height=150)


         #second image

         img1=Image.open(r"D:\Face Recognition System\Images\628e5df65b50f.jpg")
         img1=img1.resize((500,150),Image.BILINEAR)
         self.photoimg1=ImageTk.PhotoImage(img1)

         f_lbl=Label(self.root,image=self.photoimg1)
         f_lbl.place(x=500,y=0,width=500,height=150)

         #thirde image
         img2=Image.open(r"D:\Face Recognition System\Images\628e5df65b50f.jpg")
         img2=img2.resize((500,150),Image.BILINEAR)
         self.photoimg2=ImageTk.PhotoImage(img2)

         f_lbl=Label(self.root,image=self.photoimg2)
         f_lbl.place(x=1000,y=0,width=550,height=150)

         #background image
         img3=Image.open(r"D:\Face Recognition System\Images\628e5df65b50f.jpg")
         img3=img3.resize((1530,660),Image.BILINEAR)
         self.photoimg3=ImageTk.PhotoImage(img3)

         bg_img=Label(self.root,image=self.photoimg3)
         bg_img.place(x=0,y=130,width=1530,height=660)
         title_lbl=Label(bg_img,text="Student Manegment system", font=("times new roman", 35,"bold"),bg="white",fg="green")
         title_lbl.place(x=0,y=0,width=1530,height=45)

         #creating frame
         main_frame=Frame(bg_img,bd=4)
         main_frame.place(x=20,y=48,width=1480,height=600)

         #left label frame
         Left_frame=LabelFrame(main_frame,bd=5,relief=RIDGE,text="Student Details",font=("times new roman", 15,"italic"))
         Left_frame.place(x=10,y=10,width=720,height=580)

         image_left=Image.open(r"D:\Face Recognition System\Images\628e5df65b50f.jpg")
         image_left=img2.resize((820,130),Image.BILINEAR)
         self.photoimg_left=ImageTk.PhotoImage(image_left)

         f_lbl=Label(Left_frame,image=self.photoimg_left)
         f_lbl.place(x=5,y=0,width=700,height=130)

         #current course
         current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman", 15,"italic"))
         current_course_frame.place(x=5,y=135,width=700,height=150)
         dept_label=Label(current_course_frame,text="Department",font=("times new roman", 10,"bold"))
         dept_label.grid(row=0,column=0,padx=10)

         dept_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dept,font=("times new roman", 10,"bold"),state="readonly")
         dept_combo["values"]=("select Department","Cse","It","Mechanical","civil","Ece")
         dept_combo.current(0)
         dept_combo.grid(row=0,column=1,padx=10,pady=10)
         
         #course
       
         course_label=Label(current_course_frame,text="Course",font=("times new roman", 10,"bold"))
         course_label.grid(row=0,column=2,padx=10,sticky=W)

         course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman", 10,"bold"),state="readonly")
         course_combo["values"]=("select course","Btech","bca","Hons")
         course_combo.current(0)
         course_combo.grid(row=0,column=3,padx=10,pady=10,sticky=W)

         #year

         
         year_label=Label(current_course_frame,text="Year",font=("times new roman", 10,"bold"))
         year_label.grid(row=1,column=0,padx=10,sticky=W)

         year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman", 10,"bold"),state="readonly")
         year_combo["values"]=("2019-20","2020-21","2021-22","2012-23")
         year_combo.current(0)
         year_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)

         #semester

         semester_label=Label(current_course_frame,text="Semester",font=("times new roman", 10,"bold"))
         semester_label.grid(row=1,column=2,padx=10,sticky=W)

         semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman", 10,"bold"),state="readonly")
         semester_combo["values"]=("1ST","2ND","3RD","4TH","5TH","6TH","7TH","8TH")
         semester_combo.current(0)
         semester_combo.grid(row=1,column=3,padx=10,pady=10,sticky=W)

         #class student information
         student_information__frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class student information",font=("times new roman", 15,"italic"))
         student_information__frame.place(x=5,y=200,width=700,height=300)

         #student id
         studentid_label=Label(student_information__frame,text="StudentID:",font=("times new roman", 12,"italic"),bg="white",fg="#00ffff")
         studentid_label.grid(row=0,column=0,padx=10,pady=2,sticky=W)

         studentid_entry=ttk.Entry(student_information__frame,textvariable=self.var_std_id,width=20,font=("times new roman", 12,"italic"))
         studentid_entry.grid(row=0,column=1,padx=10,sticky=W)

         #student name
         studentid_label=Label(student_information__frame,text="Student Name:",font=("times new roman", 12,"italic"),fg="#3b3c36")
         studentid_label.grid(row=0,column=2,padx=10,sticky=W)

         studentid_entry=ttk.Entry(student_information__frame,textvariable=self.var_name,width=20,font=("times new roman", 12,"italic"))
         studentid_entry.grid(row=0,column=3,padx=10,sticky=W)

         #class division
         studentid_label=Label(student_information__frame,text="Class Division:",font=("times new roman", 12,"italic"),fg="#3b3c36")
         studentid_label.grid(row=1,column=0,padx=5,sticky=W)

         studentid_entry=ttk.Entry(student_information__frame,textvariable=self.var_div,width=20,font=("times new roman", 12,"italic"))
         studentid_entry.grid(row=1,column=1,padx=10,pady=2,sticky=W)

         #roll no
         studentid_label=Label(student_information__frame,text="Roll No:",font=("times new roman", 12,"italic"),fg="#3b3c36")
         studentid_label.grid(row=1,column=2,padx=10,sticky=W)

         studentid_entry=ttk.Entry(student_information__frame,textvariable=self.var_roll,width=20,font=("times new roman", 12,"italic"))
         studentid_entry.grid(row=1,column=3,padx=10,sticky=W)

         #gender

         studentid_label=Label(student_information__frame,text="Gender",font=("times new roman", 12,"italic"),fg="#3b3c36")
         studentid_label.grid(row=2,column=0,padx=10,sticky=W)

       
         gender_combo=ttk.Combobox(student_information__frame,textvariable=self.var_gender,font=("times new roman", 10,"bold"),state="readonly")
         gender_combo["values"]=("MALE","FEMALE","OTHER")
         gender_combo.current(0)
         gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)


         #date of birth

         studentid_label=Label(student_information__frame,text="DOB",font=("times new roman", 12,"italic"),fg="#3b3c36")
         studentid_label.grid(row=2,column=2,padx=10,pady=2,sticky=W)

         studentid_entry=ttk.Entry(student_information__frame,textvariable=self.var_dob,width=20,font=("times new roman", 12,"italic"))
         studentid_entry.grid(row=2,column=3,padx=10,pady=2,sticky=W)

         #email
         studentid_label=Label(student_information__frame,text="Email:",font=("times new roman", 12,"italic"),fg="#3b3c36")
         studentid_label.grid(row=3,column=0,padx=10,pady=2,sticky=W)

         studentid_entry=ttk.Entry(student_information__frame,textvariable=self.var_email,width=20,font=("times new roman", 12,"italic"))
         studentid_entry.grid(row=3,column=1,padx=10,pady=2,sticky=W)

         #phone no
         studentid_label=Label(student_information__frame,text="Phone No:",font=("times new roman", 12,"italic"),fg="#3b3c36")
         studentid_label.grid(row=3,column=2,padx=10,pady=2,sticky=W)

         studentid_entry=ttk.Entry(student_information__frame,textvariable=self.var_phone,width=20,font=("times new roman", 12,"italic"))
         studentid_entry.grid(row=3,column=3,padx=10,pady=2,sticky=W)

         #address
         studentid_label=Label(student_information__frame,text="Address",font=("times new roman", 12,"italic"),fg="#3b3c36")
         studentid_label.grid(row=4,column=0,padx=10,pady=3,sticky=W)
         studentid_entry=ttk.Entry(student_information__frame,textvariable=self.var_address,width=20,font=("times new roman", 12,"italic"))
         studentid_entry.grid(row=4,column=1,padx=10,pady=2,sticky=W)

         #teacher

         studentid_label=Label(student_information__frame,text="Teacher Name",font=("times new roman", 12,"italic"),fg="#3b3c36")
         studentid_label.grid(row=4,column=2,padx=10,pady=3,sticky=W)

         studentid_entry=ttk.Entry(student_information__frame,textvariable=self.var_teacher,width=20,font=("times new roman", 12,"italic"))
         studentid_entry.grid(row=4,column=3,padx=10,pady=2,sticky=W)

         #radio button
         self.var_radio1=StringVar()
         radiobtn1=ttk.Radiobutton(student_information__frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
         radiobtn1.grid(row=6,column=0)
         



         radiobtn2=ttk.Radiobutton(student_information__frame,variable=self.var_radio1,text="No Photo Sample",value="no")
         radiobtn2.grid(row=6,column=1)

         #button frame
         btn_frame=Frame(student_information__frame,bd=2,relief=RIDGE,bg="white")
         btn_frame.place(x=0,y=180,width=715,height=36)

         save_btn=Button(btn_frame,text="Save", command=self.add_data,width=19,font=("times new roman",12,"bold"),bg="#89cff0")
         save_btn.grid(row=0,column=0)

         update_btn=Button(btn_frame,text="Update",command=self.update_data,width=19,font=("times new roman",12,"bold"),bg="#89cff0")
         update_btn.grid(row=0,column=1)

         delete_btn=Button(btn_frame,text="Delete", command=self.delete_data,width=19,font=("times new roman",12,"bold"),bg="#89cff0")
         delete_btn.grid(row=0,column=2)

         reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("times new roman",12,"bold"),bg="#89cff0")
         reset_btn.grid(row=0,column=3)

         btn_frame1=Frame(student_information__frame,bd=2,relief=RIDGE,bg="white")
         btn_frame1.place(x=0,y=220,width=715,height=70)

         take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=40,font=("times new roman",12,"bold"),bg="#89cff0")
         take_photo_btn.grid(row=0,column=0)

         update_photo_btn=Button(btn_frame1,text="update Photo Sample",width=40,font=("times new roman",12,"bold"),bg="#89cff0")
         update_photo_btn.grid(row=0,column=1)





         



         

         #rightft label frame

         right_frame=LabelFrame(main_frame,bd=5,relief=RIDGE,text="Student Details",font=("times new roman", 10,"bold"))
         right_frame.place(x=730,y=10,width=730,height=580)

         right_img=Image.open(r"D:\Face Recognition System\Images\628e5df65b50f.jpg")
         right_img=img.resize((820,130),Image.BILINEAR)
         self.rphotoimg=ImageTk.PhotoImage(right_img)

         f_lbl=Label(right_frame,image=self.rphotoimg)
         f_lbl.place(x=0,y=0,width=720,height=130)

         #search system
         search_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="search details",font=("times new roman", 15,"italic"))
         search_frame.place(x=5,y=135,width=700,height=70)

         search_label=Label(search_frame,text="Search by:",font=("times new roman", 12,"italic"),fg="#3b3c36")
         search_label.grid(row=0,column=0,padx=10,pady=2,sticky=W)

         search_combo=ttk.Combobox(search_frame,font=("times new roman", 10,"bold"),state="readonly")
         search_combo["values"]=("select","roll","Name","Dept")
         search_combo.current(0)
         search_combo.grid(row=0,column=1,padx=10,pady=10,sticky=W)

         search_entry=ttk.Entry(search_frame,width=20,font=("times new roman", 12,"italic"))
         search_entry.grid(row=0,column=2,padx=10,pady=2,sticky=W)

         
         search_btn=Button(search_frame,text="Search",width=10,font=("times new roman", 12,"italic"))
         search_btn.grid(row=0,column=3)

         ShowAll_btn=Button(search_frame,text="Show All",width=10,font=("times new roman", 12,"italic"))
         ShowAll_btn.grid(row=0,column=4)

         #======table framwe=======

         table_frame=Frame(right_frame,bd=2,relief=RIDGE)
         table_frame.place(x=5,y=210,width=700,height=350)

         scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
         scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

         self.student_table=ttk.Treeview(table_frame,column=("dept","course","year","sem","std_id","name","div","roll","gender","dob","email","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
         scroll_x.pack(side=BOTTOM,fill=X)
         scroll_y.pack(side=RIGHT,fill=Y)
         scroll_x.config(command=self.student_table.xview)
         scroll_y.config(command=self.student_table.yview)

         self.student_table.heading("dept",text="department")
         self.student_table.heading("course",text="Course")
         self.student_table.heading("year",text="Year")
         self.student_table.heading("sem",text="Semester")
         self.student_table.heading("std_id",text="Student Id")
         self.student_table.heading("name",text="Name")
         self.student_table.heading("div",text="division")
         self.student_table.heading("roll",text="Roll")
         self.student_table.heading("gender",text="Gender")
         self.student_table.heading("dob",text="Date of Birth")
         self.student_table.heading("email",text="Email")
         self.student_table.heading("address",text="Address")
         self.student_table.heading("teacher",text="Teacher")
         self.student_table.heading("photo",text="Photo sample status")
         self.student_table["show"]="headings"

         self.student_table.pack(fill=BOTH,expand=1)
         self.student_table.bind("<ButtonRelease>",self.get_cursor)
         self.fetch_data()

         ####function declaration############
    def add_data(self):
        if self.var_dept.get()=="Select Department" or self.var_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("error","All Fields required",parent=self.root)
        else:
            
                
       
          
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='root',database='face_recognizer')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                    self.var_dept.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    
                    self.var_teacher.get(),
                    
                                  
                    self.var_radio1.get(),
                   
                ))
                conn.commit()
                self.fetch_data()
                
                conn.close()
                messagebox.showinfo("Success","Student details has been added succcessfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)

     
     
     
      ######################################### Fetch data #########################################
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='root',database='face_recognizer')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

        #===============get cursor======
    def get_cursor(self,event=""):
        cuursor_focus=self.student_table.focus()  #this is for focusing the cursor
        content=self.student_table.item(cuursor_focus)  #this for geeting the value from the table
        
        data=content["values"]
        
        self.var_dept.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14]),
    
    ### update details#######
    def update_data(self):
        if self.var_dept.get()=="Select Department" or self.var_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("error","All Fields required",parent=self.root)
      
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update",parent=self.root)
                if(update>0):
                    conn=mysql.connector.connect(host='localhost',username='root',password='root',database='face_recognizer')
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set dept=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where std_id=%s",(

                    self.var_dept.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    
                    self.var_teacher.get(),
                    
                                  
                    self.var_radio1.get(),
                   
                     

                    self.var_std_id.get()
                    


                    ))
                    
                    

                

                    
                else:
                    if not update:
                        return 

                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","student detail successfully updated",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)

                #========delete the dat=========
                
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete",parent=self.root)
                if(delete>0):
                    conn=mysql.connector.connect(host='localhost',username='root',password='root',database='face_recognizer')
                    my_cursor=conn.cursor()
                    sql='delete from student where std_id=%s'
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)

                else:
                    if not delete:
                        return 

                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","student detail successfully deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)




     ##=====================reset all========  
    def reset_data(self):
          self.var_dept.set("select Department"),
          self.var_course.set("select course"),
          self.var_year.set("2019-20"),
          self.var_semester.set("1ST"),
          self.var_std_id.set("")
            
          self.var_name.set(""),
          self.var_div.set(""),
          self.var_roll.set(""),
        
          self.var_gender.set(""),
          self.var_dob.set(""),
          self.var_email.set(""),
          self.var_phone.set(""),
          self.var_address.set(""),
        
          self.var_teacher.set(""),
          self.var_radio1.set(""),
        
                        
    def generate_dataset(self):
         if self.var_dept.get()=="Select Department" or self.var_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("error","All Fields required",parent=self.root)
      
         else:

              try:
                    conn=mysql.connector.connect(host='localhost',username='root',password='root',database='face_recognizer')
                    my_cursor=conn.cursor()
                    my_cursor.execute("select * from student")
                    myresult=my_cursor.fetchall()
                    id=0
                    for x in myresult:
                           id+=1
                    my_cursor.execute("update student set dept=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where std_id=%s",(

                    self.var_dept.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    
                    self.var_teacher.get(),
                    
                                  
                    self.var_radio1.get(),
                   
                     

                    self.var_std_id.get()
                    


                    )) 

                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close() 
                    cam = cv2.VideoCapture(0)
                    harcascadePath = ("haarcascade_frontalface_default.xml")
                    face_classifier = detector = cv2.CascadeClassifier(harcascadePath)
                    sampleNum = 0

                    while(True):
                        ret, img = cam.read()
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = detector.detectMultiScale(gray, 1.3, 5, minSize=(30,30),flags = cv2.CASCADE_SCALE_IMAGE)
                        for(x,y,w,h) in faces:
                            cv2.rectangle(img, (x, y), (x+w, y+h), (10, 159, 255), 2)
                            sampleNum = sampleNum+1
                            #saving the captured face in the dataset folder TrainingImage
                            cv2.imwrite("data/image." + str(id) + '.' +
                                        str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])
                            cv2.imshow('frame', img)
                        if cv2.waitKey(30) & 0xFF == ord('q'):
                            break
                        elif sampleNum > 30:
                            break
                    cam.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generating data set successfully")

              except Exception as es:

                
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
 

              
                








  
      


        


            

        
           
                
            


         



         





if __name__== "__main__":

    root=Tk()
    obj=student_management_system(root)
    root.mainloop()
        

            

        
           
                
            


         



         





              
        
            

          
        





   
                       

                       
                            
                                
                                
                            
                        
              

                        


                    
                     

                    
                 

           
               
                   


               
                








  
      


        


            

        
           
                
            


         



         





