import tkinter 
from tkinter import messagebox



def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    if name and phone and email:
        contact = f"{name} - {phone} - {email}"
        contact_listbox.insert(tkinter.END, contact)
        name_entry.delete(0, tkinter.END)
        phone_entry.delete(0, tkinter.END)
        email_entry.delete(0, tkinter.END)
    else:
        messagebox.showinfo("주의주의!!", "연락처 칸이 부족해유 ㅠㅠ.")

def delete_contact():
    try:
        selected_contact_index = contact_listbox.curselection()[0]
        contact_listbox.delete(selected_contact_index)
    except IndexError:
        messagebox.showinfo("주의주의!!", "연락처를 골라야 돼요!.")

def edit_contact():
    try:
        selected_contact_index = contact_listbox.curselection()[0]
        contact = contact_listbox.get(selected_contact_index)
        name, phone, email = contact.split(" - ")
        name_entry.delete(0, tkinter.END)
        name_entry.insert(0, name)
        phone_entry.delete(0, tkinter.END)
        phone_entry.insert(0, phone)
        email_entry.delete(0, tkinter.END)
        email_entry.insert(0, email)
        delete_contact()
    except IndexError:
        messagebox.showinfo("주의주의!!", "연락처를 고르라고!!")

window = tkinter.Tk()
window.title("주소록")
window.geometry("500x400")

name_label = tkinter.Label(window, text="이름?")
name_label.pack(ipadx=10)
name_entry = tkinter.Entry(window, width=50)
name_entry.pack(ipadx=5)

phone_label = tkinter.Label(window, text="전화번호?")
phone_label.pack(pady=10)
phone_entry = tkinter.Entry(window, width=50)
phone_entry.pack(pady=5)

email_label = tkinter.Label(window, text="집주소? ")
email_label.pack(pady=10)
email_entry = tkinter.Entry(window, width=50)
email_entry.pack(pady=5)

add_contact_button = tkinter.Button(window, text="연락처 추가", command=add_contact)
add_contact_button.pack(pady=10)

edit_contact_button = tkinter.Button(window, text="연락처 편집", command=edit_contact)
edit_contact_button.pack(pady=10)

delete_contact_button = tkinter.Button(window, text="없어지는 버튼", command=delete_contact)
delete_contact_button.pack(pady=10)


contact_listbox = tkinter.Listbox(window, width=70, height=15)
contact_listbox.pack(pady=10)

window.mainloop()
