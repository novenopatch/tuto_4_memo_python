import tkinter
#fonction observateur
def update_label(*args):
    var_label.set(var_entry.get())
#definition des parametre

app=tkinter.Tk()
app.geometry("1080x720")
app.title("variables tkinter")

#widget
var_entry = tkinter.StringVar()
var_entry.trace("w",update_label)
entry = tkinter.Entry(app,textvariable=var_entry)

var_label = tkinter.StringVar()
label = tkinter.Label(app,textvariable=var_label)

entry.pack()
label.pack()


app.mainloop()
