import random
from tkinter import *
from PIL import ImageTk, Image

people = []

people = [['Invalid'], ['Nishant', 'Mehul', 'Priyanshu', 'Sarthak'], ['Achalesh', 'Vishvas', 'Shalin', 'Bhavesh'], ['Pavnesh', 'Vikash', 'Lakshit', 'Prashant', 'Tushar'], ['Abhishek(2004)', 'Aseem', 'Abhishek(2030)', 'Parvinder'], ['Himanshu', 'Ayush', 'Krishnakant', 'Deepak'], ['Gauri Shankar', 'Sawant Raj', 'Tanmay', 'Vishal'], ['Akash(2011)', 'Pratul', 'Utkarsh', 'Neha', 'Balkishan'], ['Akash(2026)', 'Iresha', 'Janvi', 'Nipur', 'Priyanshi'], ['Aadesh', 'Harsh', 'Harshit', 'Anand', 'Lokesh'], ['Diwakar', 'Vinita', 'Dharmveer', 'Khushwant'], ['Abhishek Bairwa', 'Manish', 'Korada Akash'], ['Ishank', 'Deepak', 'Saumya Kumari', 'Kapil Kumar']]

root = Tk()
root.title("Ramdom Name Selector")

root.geometry('700x700')

labelGroup=Label(root,text="Enter Group No")
labelGroup.grid(column=0,row=0,pady=(10,0))
entryGroup=Entry(root,width=10)
entryGroup.grid(column=1,row=0,padx=(20,0),pady=(10,0))

def luckyPerson():
    global people
    group = int(entryGroup.get())
    upperLimit = len(people[group])
    index = random.randint(0, upperLimit-1)
    lucky = people[group][index]
    luckyLabel = Label(root, text="Person Selected in Lucky Draw is: " + lucky)
    luckyLabel.grid(row = 3, padx=(0,0), pady=(0,0))
    img  = ImageTk.PhotoImage(Image.open("image.jpg"))
    labelImage = Label(root, image=img)
    labelImage.image = img
    labelImage.place(x=200, y=200)



button=Button(root,text="Generate",command=luckyPerson)
button.grid(column=0,row=2,pady=(10,0))
root.mainloop()