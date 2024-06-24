import tkinter
import tkinter.font

window = tkinter.Tk()
window.title('음식계산기')
window.geometry('600x400+100+100')

def func1():
    price = 0
    if cv1.get() == 1:
        price+=10000
    if cv2.get() == 1:
        price+=9000
    if cv3.get() == 1:
        price+=8000
    if cv4.get() == 1:
        price+=11000        
    #배달비 추가
    if 0 < price < 20000:
        price+=3000
        text.config(text = '(배달비 : 3000원)')
    else:
        text.config(text='')


    result.config(text='가격 : '+str(price)+'원')

title_font = tkinter.font.Font(family='궁서체',size=25)

text_font = tkinter.font.Font(family='궁서체', size=15)
text = tkinter.Label(window, text='(배달비 : 3000원)', fg='green')
text.grid(row = 4, column=0, columnspan=4)


title = tkinter.Label(window, text='음식 계산기', font=title_font)
title.grid(row = 0, column = 0, columnspan=4)


image1 = tkinter.PhotoImage(file = '볶음밥.png')
image2 = tkinter.PhotoImage(file = '짬뽕.png')
image3 = tkinter.PhotoImage(file = '짜장면.png')
image4 = tkinter.PhotoImage(file = '탕수육.png')


label1 = tkinter.Label(window, image=image1)
label2 = tkinter.Label(window, image=image2)
label3 = tkinter.Label(window, image=image3)
label4 = tkinter.Label(window, image=image4)


cv1 = tkinter.IntVar()
ckb1 = tkinter.Checkbutton(window, text='10000원', variable=cv1, command=func1)

cv2 = tkinter.IntVar()
ckb2 = tkinter.Checkbutton(window, text='9000원', variable=cv2, command=func1)

cv3 = tkinter.IntVar()
ckb3 = tkinter.Checkbutton(window, text='8000원', variable=cv3, command=func1)

cv4 = tkinter.IntVar()
ckb4 = tkinter.Checkbutton(window, text='11000원', variable=cv4, command=func1)


label1.grid(row = 1, column = 0)
label2.grid(row = 1, column = 1)
label3.grid(row = 1, column = 2)
label4.grid(row = 1, column = 3)
ckb1.grid(row=2, column=0)
ckb2.grid(row=2, column=1)
ckb3.grid(row=2, column=2)
ckb4.grid(row=2, column=3)


result = tkinter.Label(window, text='가격 : 0원', font=title_font)
result.grid(row = 3, column = 0, columnspan=4)


window.mainloop()

