import tkinter as tk
import XmlPy

def btn1_Click_command(sender):
    print('按钮被点击了。',sender.cget('text'))
def chk1_Click_command(sender):
    print('按钮被选择了。',sender.var.get())

if __name__ == "__main__":
    root = tk.Tk()
    XmlPy.XmlInit(root, "main.ui.xml", globals())
    root.mainloop()
