# XmlPy
## Implementing a Python UI with XML
The entire project re - encapsulates Tkinter. In the future, you can directly write XML files to create interfaces, which is simple and convenient.
The entire project only generates one XmlPy.pyd file, which is easy to call. It only takes a few lines of code:
```
if __name__ == "__main__":
    root = tk.Tk()
    XmlPy.XmlInit(root, "main.ui.xml", globals())
    root.mainloop()
```
In the main.ui.xml file, write your UI interface:
```
<root>
    <window
        title="Tkinter 窗口示例"
        bg="lightgray"
        geometry="600x500+100+100"
        maxsize="800x600"
        minsize="200x150"
        resizable="True,False"/>
    <button text="按钮 1" id="btn1" bg="lightblue" fg="red" x="50" y="50" 
            anchor="center" activebackground="yellow" activeforeground="black" bd="2" 
            font="Arial 10" highlightcolor="green" justify="center" padx="5" pady="5" 
            ipadx="2" ipady="2" state="normal" image="play.png">
        <Click_command>btn1_Click_command</Click_command>
    </button>
    <checkbutton text="复选框1" fg="black" id="chk1" bg="lightgray" x="100" y="200"
                    anchor="center" bd="1" font="Arial 10" state="normal" 
                    variable="chk_var" onvalue="1" offvalue="0" 
                    indicatoron="True" selectcolor="red" 
                    wraplength="100">
        <Click_command>chk1_Click_command</Click_command>
    </checkbutton>
</root>
```
Currently, only the button and checkbutton have been implemented. Other controls are still being added continuously.

Hurry up and download the example to run it!
