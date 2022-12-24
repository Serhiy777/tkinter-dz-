
from tkinter import *

def mph_to_km():
    entry4.delete(0, END)
    value = int(entry2.get())
    s = value * 1.6
    entry4.insert(1,f"{int(s)} KM")

def km_to_mph():
    entry4.delete(0, END)
    value = int(entry3.get())
    s = value / 1.6
    entry4.insert(1,f"{int(s)} MPH")


window = Tk()
window.geometry('411x206+100+100')
window.title('MI \N{RIGHTWARDS BLACK ARROW} KM | Converter')
window['bg'] = "#000000"

label1 = Label(text='MI \N{RIGHTWARDS BLACK ARROW} KM', bg='black', fg='white', font='Tahoma')
label1.pack(pady=10)

label2 = Label(text='Input MI:', bg='black', fg='white', font='Tahoma')
label2.place(x=10 ,y=70)

label3 = Label(text='Input KM:', bg='black', fg='white', font='Tahoma')
label3.place(x=10 ,y=110)

label4 = Label(text='Result:', bg='black', fg='white', font='Tahoma')
label4.place(x=10, y=160)

entry2 = Entry()
entry2.place(x=100, y=70)
entry2.insert(0,'0')

entry3 = Entry()
entry3.place(x=100, y=110)
entry3.insert(0,'0')

entry4 = Entry()
entry4.place(x=100, y=160)
entry4.insert(0,'0')

btn1 = Button(text='MPH \N{RIGHTWARDS BLACK ARROW} KM', bg='black',fg='white', command=mph_to_km, font='Tahoma')
btn1.place(x=293,y=80)
btn2 = Button(text='KM \N{RIGHTWARDS BLACK ARROW} MPH', bg='black',fg='white', command=km_to_mph, font='Tahoma')
btn2.place(x=293, y=135)


window.mainloop()
