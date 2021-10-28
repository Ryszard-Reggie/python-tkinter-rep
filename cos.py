import tkinter

window = tkinter.Tk()
window.title('Ramki')

data_labelframe = tkinter.LabelFrame(window, text='Coś:')
data_labelframe.grid()

data = tkinter.Text(data_labelframe, width=128, height=8)
data.grid()

window.mainloop()