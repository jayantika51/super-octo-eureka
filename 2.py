from tkinter import*
root= Tk()

root.title("My First Python")
root.geometry("600x500")

show_result=Label(root)

def add():
    result=259657+356721
    show_result["text"]=result

btn = Button(root, text="Add", command=add)
btn.pack()

show_result.pack()

root.mainloop()
