import tkinter

window = tkinter.Tk()

window.title("Calculator")
window.minsize(width=300, height=300)

def new_window():

    window2 = tkinter.Tk()
    window2.title("New Window")
    window2.minsize(width=200, height=200)

    window2.mainloop()


one_button = tkinter.Button(text="Open new window", command=new_window)
one_button.grid(row=0, column=0)





window.mainloop()

