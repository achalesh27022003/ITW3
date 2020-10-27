import numpy as np

import matplotlib.pyplot as plot
from tkinter import *

 
root=Tk()
root.title("Addition of two number")


root.configure(bg='red')
root.geometry('700x500')



Label1=Label(root,text="Enter  frequency for  Sine wave")
Label1.grid(column=0,row=0,pady=(10,0))#if we give only we argument than it take both argumnets as same

Label2=Label(root,text="Enter  Amplitude for  Sine wave")
Label2.grid(column=0,row=1,pady=(10,0))

Label3=Label(root,text="Enter frequency for Cosine Wave")
Label3.grid(column=0,row=2,pady=(10,0))

Label4=Label(root,text="Enter Amplitude for Cosine wave")
Label4.grid(column=0,row=3,pady=(10,0))

txt1=Entry(root,width=10)
txt1.grid(column=1,row=0,padx=(20,0),pady=(10,0))

txt2=Entry(root,width=10)
txt2.grid(column=1,row=1,padx=(20,0),pady=(10,0))

txt3=Entry(root,width=10)
txt3.grid(column=1,row=2,padx=(20,0),pady=(10,0))

txt4=Entry(root,width=10)
txt4.grid(column=1,row=3,padx=(20,0),pady=(10,0))





def show():
      f1=int(txt1.get())
      A1=int(txt2.get())
      f2=int(txt3.get())
      A2=int(txt4.get())
      time=2*np.pi

      ampltude =np.array([time,f1,f2,A1,A2])
      c=np.savetxt('mycsv.csv',ampltude)#saving data into csv file

      def readData():#fetching data from csv file
 
          q=np.loadtxt('mycsv.csv');
          return q

      a=readData() 



      timep=np.arange(0,a[0],0.00001)
      amp1=np.sin(timep*a[1])
      
      plot.subplot(4,2,1)#plot one Sine wave
      plot.plot(timep, a[3]*amp1,color='darkorange')
      plot.title('Sine wave')
      plot.xlabel('Time')
      plot.ylabel('Amplitude')
      plot.grid(True, which='both',color='darkblue')
      plot.axhline(y=0,color='darkblue' )



      amp2=np.cos(timep*a[2])

      plot.subplot(4,2,2)#plot second Cosine Wave
      plot.plot(timep,a[4]*amp2,color='crimson')
      plot.title('Cosine wave')
      plot.xlabel('Time')
      plot.ylabel('Amplitude')
      plot.grid(True, which='both',color='darkblue')
      plot.axhline(y=0, color='darkblue')



    #  plot.savefig('graph.png')
      plot.show()

def save():

      plot.savefig('graph.png')

button=Button(root,text="Plot",command=show)
button.grid(column=0,row=5,pady=(10,0))

button1=Button(root,text="save",command=save)
button1.grid(column=1,row=5,pady=(12,0),padx=(20,0))
root.mainloop()