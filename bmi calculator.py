#BMI CALCULATOR
import tkinter as tk
from tkinter import *
from tkinter import messagebox
def bmi():   
 
 weight=float(wt.get())
 height=float(ht.get())
 BMI=weight/height**2
 if BMI<18.40:
    
    messagebox.showinfo("",f"You are Underweight and BMI is:{BMI}")
   
 elif BMI<=24.9 and BMI>=18.5:
    messagebox.showinfo("",f"You are Normal and BMI is:{BMI}")
    
 elif BMI<=29.9 and BMI>=25.0:
    messagebox.showinfo("",f"You are Overweight and BMI is:{BMI}")
    
 elif BMI>=30.0:
    messagebox.showinfo("",f"You are Obese and BMI is:{BMI}")
    
 else:
    messagebox.showinfo("","please enter a valid input")
  

root=tk.Tk()
root.title("BMI CALCULATOR")
root.geometry("600x300")
global wt
global ht
global BMI
label1=tk.Label(root,text="Enter the weight in kgs:")
label1.grid(column=1,row=0)
label2=tk.Label(root,text="Enter the height in mts:")
label2.grid(column=1,row=1)

wt=Entry(root,width=50)
wt.grid(column=2,row=0)
ht=Entry(root,width=50)
ht.grid(column=2,row=1)
button=Button(root,text="Calculate",command=bmi,bg="blue",fg="white")
button.grid(column=2,row=2)


root.mainloop()

