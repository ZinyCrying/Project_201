from tkinter import *
window = Tk()

window.title("SI Calculator")
window.geometry("400x400")
window.configure(bg="lightblue")

def calculate_si():
    p = float(principal.get())
    r = float(rate.get())
    t = float(time.get())
    i= (p*r*t)/100
    interest = round(i,2)
    
    output_message=Label(result_frame,text=str(interest), bg = "white", font=("Calibri", 12), width=42)
    output_message.place(x=20,y=40)
    output_message.pack()

app_label = Label(window, text="Simple Interest Calculator", fg="black", bg="orange",font=("Playfair Display", 15), bd=10)
app_label.place(x=80, y=20)

principal_label = Label(window, text="Principal: ", fg="black", bg="lightgreen", font=("Open Sans", 12), bd=5)
principal_label.place(x=20, y=90)

principal = Entry(window, text="", bd=5,width=20)
principal.place(x=120, y=92)

rate_label = Label(window, text="Rate%: ", fg="black", bg="lightgreen", font=("Open Sans", 12), bd=5)
rate_label.place(x=20, y=130)

rate = Entry(window, text="", bd=5,width=20)
rate.place(x=117, y=132)

time_label = Label(window, text="Time(days)", fg="black", bg="lightgreen", font=("Open Sans", 12), bd=5)
time_label.place(x=20, y=170)

time = Entry(window, text="", bd=5,width=20)
time.place(x=120, y=172)

calculate_button=Button(window,text="Calculate",fg = "white", bg = "blue",bd=4, command=calculate_si)
calculate_button.place(x=170,y=230)

result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()


window.mainloop()