import tkinter

def mtok():
    miles=float(entry.get())
    km=round(miles*1.609)
    label3.config(text=f"{km}")

window=tkinter.Tk()
window.config(width=600,height=600)
window.title("Miles to KM Converter")

entry=tkinter.Entry(width=7)
entry.grid(column=1,row=0)
label=tkinter.Label(text="Miles")
label.grid(column=2,row=0)
label2=tkinter.Label(text="is equal to")
label2.grid(column=0,row=1)
label3=tkinter.Label(text="0")
label3.grid(column=1,row=1)
label4=tkinter.Label(text="Km")
label4.grid(column=2,row=1)
cal=tkinter.Button(text="convert",command=mtok)
cal.grid(column=1,row=3)

window.mainloop()