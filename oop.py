import tkinter
from tkinter import ttk
#means theme tkinter

window = tkinter.Tk()

window.title("Hello World")

def add_to_list(event=None):
    text = entry.get() 
    if text: 
        text_list.insert(tkinter.END, text) 
        entry.delete(0, tkinter.END) 

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

frame = ttk.Frame(window)#just change tkinter.element to ttk.element
frame.grid(row=0, column=0, sticky="nsew", padx=5,pady=5)

frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)


entry = ttk.Entry(frame)
entry.grid(row=0, column=0, sticky="ew")

entry.bind("<Return>", add_to_list)

entry_button = ttk.Button(frame, text="Add", command=add_to_list)
entry_button.grid(row=0, column=1)

text_list = tkinter.Listbox(frame)
text_list.grid(row=1, column=0, columnspan=2, sticky="nsew")

window.mainloop()

