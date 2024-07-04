from tkinter import *

window=Tk()
window.title("BMI Calculator")
window.minsize(width=200,height=200)
def click_button():
    user_input_1 = entry_1.get()
    user_input_2 = entry_2.get()

    if user_input_1=="" or user_input_2=="":
        label_3.config(text="Enter both weight and height!")

    else:
        try:
           heigh_m = float(user_input_2) / 10000
           bmi = float(user_input_1) / (float(user_input_2) * heigh_m)
           label_3_s=bmi_calculator(bmi)
           label_3.config(text=label_3_s)
        except:
           label_3.config(text="Enter a valid number!")

def bmi_calculator(bmi):
    label_3_s= f"Your BMI is {round(bmi, 2)}. You are "
    if bmi < 18.5:
        label_3_s+="Underweight"
    elif 18.5 <= bmi <= 24.9:
        label_3_s +="Normal"
    elif 25 <= bmi <= 29.9:
        label_3_s +="Overweight"
    elif 30 <= bmi <= 34.9:
        label_3_s +="Obese"
    else:
        label_3_s += "Extremly Obese"
    return label_3_s




label_1=Label(text="Enter Your Weight(kg)")
label_1.pack()

entry_1=Entry(width=10)
entry_1.pack()

label_2=Label(text="Enter Your High(cm)")
label_2.pack()

entry_2=Entry(width=10)
entry_2.pack()

button=Button(text="Calculate",command=click_button)
button.pack()

label_3=Label()
label_3.pack()



window.mainloop()