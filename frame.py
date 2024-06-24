import tkinter

window = tkinter.Tk()
window.title('Tkinter 연습')
window.geometry('300x200+100+100')


frame1 = tkinter.Frame(window, relief='solid', bd=2)
frame2 = tkinter.Frame(window, relief='solid', bd=2)


frame1.pack(side='left', fill='both', expand='True')
frame2.pack(side='right', fill='both', expand='True')

button = tkinter.Button(frame1, text='버튼')
button.pack(side='right')
button2 = tkinter.Button(frame2, text='버튼2')
button2.pack(side='left')


window.mainloop()