from tkinter import *
window = Tk()

# add widgets here

window.title('BMI Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')

#function for button

def calculate_bmi():
    weigth = int(weigth_entry.get())
    heigth = int(heigth_entry.get())/100
    bmi = weigth/(heigth*heigth)
    bmi = round(bmi, 1)
    name = username.get()

    result_label.destroy()

    msg=""

    if bmi < 18.5:
        msg="you are Underweight"
    elif bmi > 18.5 and bmi <=24.9:
        msg="is in Normal Range"
    elif bmi > 25 and bmi <=29.9:
        msg="you are Overweight"
    elif bmi > 30:
        msg="you are Obese"
    else:
        msg="Something Went Wrong"

    output__message=Label(result_frame,text=name+", your BMI is"+str(bmi)+" and "+msg, bg = "lightcyan", font=("Calibri",12),width=42)
    output__message.place(x=20, y=40)
    output__message.pack()                

app_label=Label(window, text="BMI CALCULATOR", fg = "black", bg = "lightcyan", font=("Calibri",20),bd=5) 
app_label.place(x=50, y=20)

name_label=Label(window, text="Your Name", fg = "black", bg = "lightcyan", font=("Calibri", 12), bd=1)
name_label.place(x=20, y=90)

username=Entry(window, text="", bd=2, width=22)
username.place(x=150, y=92)

heigth_label=Label(window, text="Enter Height (cm)", fg = "black", bg = "lightcyan", font=("Calibri", 12))
heigth_label.place(x=20, y=140)

heigth_entry=Entry(window, text="", bd=2, width=15)
heigth_entry.place(x=150, y=142)

weigth_label=Label(window, text="Enter weight(Kg)", fg = "black", bg = "lightcyan", font=("Calibri",12))
weigth_label.place(x=20 ,y=185)

weigth_entry=Entry(window, text="", bd=2, width=15)
weigth_entry.place(x=150, y=187)

calculate_button=Button(window,text="CALCULATE", fg="black", bg="cyan", bd=4, command=calculate_bmi)
calculate_button.place(x=20, y=250)

result_frame = LabelFrame(window,text="Result", bg="lightcyan", font=("Calibri",12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20, y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Caligri", 12), width=33)
result_frame.place(x=20, y=20)
result_frame.pack()

window.mainloop()