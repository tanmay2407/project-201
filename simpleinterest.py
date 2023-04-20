from tkinter import *
window=Tk()
window.title("simple intrest")
window.geometry("400x400")
window.configure(bg="skyblue")
heading_Label=Label(window, text="Simple Intrest" , fg="black" , bg="lightblue" , font=("calibri" ,20) , bd=5)
heading_Label.place(x=50 , y=20)

principal_Label=Label(window , text="principal" , fg="black" , bg="lightblue" , font=("calibri" , 20) , bd=2)
principal_Label.place(x=20 , y=90)
principal_entry=Entry(window , text="" ,  bd=2 , width=22)
principal_entry.place(x=150 ,y=92)

Rate_Label=Label(window , text="rate" , fg="black" , bg="lightblue" , font=("calibri" , 20) , bd=2)
Rate_Label.place(x=20 , y=160)
Rate_entry=Entry(window , text="" ,  bd=2 , width=22)
Rate_entry.place(x=150 ,y=162)

Time_Label=Label(window , text="Time" , fg="black" , bg="lightblue" , font=("calibri" , 20) , bd=2)
Time_Label.place(x=20 , y=220)
Time_entry=Entry(window , text="" ,  bd=2 , width=22)
Time_entry.place(x=150 ,y=222)

def calculate_intrest():
    p=float(principal_entry.get())
    r=float(Rate_entry.get())
    t=float(Time_entry.get())
    i=(p*r*t)/100
    interest = round(i , 2)
    result_Label.destroy()

    output_message=Label(result_frame,text="interest = {interest}  ((- $1000 for using app))".format(interest=interest), bg = "lightcyan", font=("Calibri", 12), width=42)
    output_message.place(x=20,y=40)
    output_message.pack()
    


intreast_button=Button(window , text="Calculate" , fg="black" , bg="blue" , bd=4 , command=calculate_intrest)
intreast_button.place(x=170,y=270)

result_frame= LabelFrame(window , text="Result" , bg="skyblue" ,font=("calibri" , 20))
result_frame.pack(padx=20,pady=20)
result_frame.place(x=20 , y=300)

result_Label = Label(result_frame , text=" " ,bg="lightblue", width=33 , font=("calibri" , 20) )
result_Label.place(x=20 , y=20)
result_Label.pack()

window.mainloop()


