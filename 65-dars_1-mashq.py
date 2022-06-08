from tkinter import *
window = Tk()
window.title('My App')
window.geometry('250x150')
window.configure(background='yellow')
my_label=Label(window, width=40, height=5, bg='yellow', text='')
my_label.grid(row=0, column=0)
def change_text():
    my_label.config(text='Hello!')
my_button=Button(window, text="Press me!", width=10, command=change_text)
my_button.grid(row=1, column=0)
window.mainloop()
