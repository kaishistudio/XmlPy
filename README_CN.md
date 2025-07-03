# XmlPy
## 实现用xml来打造python UI
整个项目将Tkinter进行二次封装，未来可以直接编写xml文件来实现界面，简单方便。
整个项目只生成一个XmlPy.pyd文件，调用方便，仅仅几行代码：
```
if __name__ == "__main__":
    root = tk.Tk()
    XmlPy.XmlInit(root, "main.ui.xml", globals())
    root.mainloop()
```
在main.ui.xml文件中，编写你的ui界面：
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
赶紧下载示例来运行一下吧！
