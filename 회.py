import tkinter
import tkinter.font

window = tkinter.Tk()
window.title('음식계산기')
window.geometry('600x400+100+100')

title_font = tkinter.font.Font(family='맑은 고딕',size=20)

title = tkinter.Label(window, text='음식 계산기', font=title_font)


title.grid(row = 0, column = 0)

image1 = tkinter.PhotoImage(file = '볶음밥.png')
#image2 = tkinter.PhotoImage(file = '막창.jpg')
#image3 = tkinter.PhotoImage(file = '파스타.jpg')
#image4 = tkinter.PhotoImage(file = '콩나물 국밥.jpg')

label1 = tkinter.Label(window, image=image1)
#label2 = tkinter.Label(window, image=image2)
#label3 = tkinter.Label(window, image=image3)
#label4 = tkinter.Label(window, image=image4)

label1.grid(row = 1, column = 0)
#label2.grid(row = 1, column = 1)
#label3.grid(row = 1, column = 2)
#label4.grid(row = 1, column = 3)

window.mainloop()

