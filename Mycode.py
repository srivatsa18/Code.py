from tkinter import *
window=Tk()
window.title('Bank personal book')

fr1=Frame(window)
fr1.pack()

fr2=Frame(window)
fr2.pack()

l1=Label(fr1,text='Name:')
l1.pack(side='left')

e1=Entry(fr1,width=25)
e1.pack(side='right')

l2=Label(fr2,text='Amount:')
l2.pack(side='left')

e2=Entry(fr2,width=25)
e2.pack(side='right')

def save():
    name=e1.get()
    amount=e2.get()
    name.append(name)
    amount.append(amount)

    e1.delete(0,END)
    e2.delete(0,END)

bu=Button(window,text='save',command='save')
bu.pack()

bu=Button(window,text='check',command='check')
bu.pack()

window.mainloop()
