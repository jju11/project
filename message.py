import tkinter

window = tkinter.Tk()
window.title('메시지')
window.geometry('300x200+100+100')


m = tkinter.Message(window, text='메시지 입니다', width=100, relief='solid')
m.pack()


window.mainloop()