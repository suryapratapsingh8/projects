from tkinter import *
from tkinter import messagebox

def reset_entry():
    age_tf.delete(0,'end')
    height_tf.delete(0,'end')
    weight_tf.delete(0,'end')
    

def calculate_bmi():
    kg = int(weight_tf.get())
    m = int(height_tf.get())/100
    bmi = kg/(m*m)
    bmi = round(bmi, 2)
    bmi_index(bmi)
    
def bmi_index(bmi):
    m = int(height_tf.get())/100
    kg = int(weight_tf.get())
    if bmi < 18.5:
        messagebox.showinfo('result', f'BMI = {bmi} is Underweight')
        b=(18.5-bmi)
        a=(b*m*m)+kg
        messagebox.showinfo('result', f'kg ={a} should be your weight')
        
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('result', f'BMI = {bmi} is Normal')
       # b=(18.5-bmi)
        #a=(b*m*m)+kg
        messagebox.showinfo('result',  'you are fit and fine. \n MAINTAIN IT!')
        
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('result', f'BMI = {bmi} is Overweight')
        b=(bmi-24.9)
        a=kg-(b*m*m)
        messagebox.showinfo('result', f'kg ={a} should be your weight')
        
    elif (bmi > 29.9):
        messagebox.showinfo('result', f'BMI = {bmi} is Obesity') 
        b=(bmi-24.9)
        a=kg-(b*m*m)
        messagebox.showinfo('result', f'kg ={a} should be your weight')
        messagebox.showinfo('result',  'REDUCE WEIGHT AS SOON AS POSSIBLE!')
    else:
        messagebox.showerror('result', 'something went wrong!')   

ws = Tk()
ws.title('result')
ws.geometry('500x400')
ws.config(bg='black')

var = IntVar()

frame = Frame(
    ws,
    padx=10, 
    pady=10
)
frame.pack(expand=True)
name_lb=Label(frame, text="Enter your name")
name_lb.grid(row=1,column=1)
name_tf=Entry(frame,)
name_tf.grid(row=1, column=2 ,pady=5)

age_lb = Label(
    frame,
    text="Enter Age (2 - 120)"
)
age_lb.grid(row=2, column=1)

age_tf = Entry(
    frame, 
)
age_tf.grid(row=2, column=2, pady=5)

gen_lb = Label(
    frame,
    text='Select Gender'
)
gen_lb.grid(row=3, column=1)

frame2 = Frame(
    frame
)
frame2.grid(row=3, column=2, pady=5)

male_rb = Radiobutton(
    frame2,
    text = 'Male',
    variable = var,
    value = 1
)
male_rb.pack(side=LEFT)

female_rb = Radiobutton(
    frame2,
    text = 'Female',
    variable = var,
    value = 2
)
female_rb.pack(side=RIGHT)

height_lb = Label(
    frame,
    text="Enter Height (cm)  "
)
height_lb.grid(row=4, column=1)

weight_lb = Label(
    frame,
    text="Enter Weight (kg)  ",

)
weight_lb.grid(row=5, column=1)

height_tf = Entry(
    frame,
)
height_tf.grid(row=4, column=2, pady=5)

weight_tf = Entry(
    frame,
)
weight_tf.grid(row=5, column=2, pady=5)

frame3 = Frame(
    frame
)
frame3.grid(row=6, columnspan=3, pady=10)

cal_btn = Button(
    frame3,
    text='Calculate',
    command=calculate_bmi
)
cal_btn.pack(side=LEFT)

reset_btn = Button(
    frame3,
    text='Reset',
    command=reset_entry
)
reset_btn.pack(side=LEFT)

exit_btn = Button(
    frame3,
    text='Exit',
    command=lambda:ws.destroy()
)
exit_btn.pack(side=RIGHT)

ws.mainloop()