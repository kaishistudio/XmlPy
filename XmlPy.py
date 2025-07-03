import tkinter as tk
import xml.etree.ElementTree as ET

button_id_map = {}
button_images = {}
checkbutton_id_map = {}
checkbutton_vars = {}
checkbutton_images = {}

def create_widgets_from_xml(root_widget, xml_root):
    for child in xml_root:
        if child.tag == 'button':
            text = child.attrib.get('text', 'Button')
            command = None
            bg = child.attrib.get('bg')
            fg = child.attrib.get('fg')
            width = child.attrib.get('width')
            height = child.attrib.get('height')
            button_id = child.attrib.get('id') 
            x = child.attrib.get('x') 
            y = child.attrib.get('y')
            anchor = child.attrib.get('anchor')
            activebackground = child.attrib.get('activebackground')
            activeforeground = child.attrib.get('activeforeground')
            bd = child.attrib.get('bd')
            font = child.attrib.get('font')
            highlightcolor = child.attrib.get('highlightcolor')
            image = child.attrib.get('image')
            justify = child.attrib.get('justify')
            padx = child.attrib.get('padx')
            pady = child.attrib.get('pady')
            ipadx = child.attrib.get('ipadx')
            ipady = child.attrib.get('ipady')
            state = child.attrib.get('state')
            if width:
                width = int(width)
            if height:
                height = int(height)
            if x:
                x = int(x)
            if y:
                y = int(y)
            if bd:
                bd = int(bd)
            if padx:
                padx = int(padx)
            if pady:
                pady = int(pady)
            if ipadx:
                ipadx = int(ipadx)
            if ipady:
                ipady = int(ipady)
            command_name = None
            for sub_child in child:
                if sub_child.tag == 'Click_command':
                    command_name = sub_child.text
            button_args = {
                'text': text
            }
            if bg:
                button_args['bg'] = bg
            if fg:
                button_args['fg'] = fg
            if width:
                button_args['width'] = width
            if height:
                button_args['height'] = height
            if anchor:
                button_args['anchor'] = anchor
            if activebackground:
                button_args['activebackground'] = activebackground
            if activeforeground:
                button_args['activeforeground'] = activeforeground
            if bd:
                button_args['bd'] = bd
            if font:
                button_args['font'] = font
            if highlightcolor:
                button_args['highlightcolor'] = highlightcolor
            if justify:
                button_args['justify'] = justify
            if state:
                button_args['state'] = state
            if image:
                im=tk.PhotoImage(file=image)
                button_images[button_id]=im
                button_args['image'] = im
            button = tk.Button(root_widget, **button_args)
            if command_name and command_name in globals():
                command = lambda btn=button, cmd=command_name: globals()[cmd](btn)
                button.config(command=command)
            if x is not None and y is not None:
                place_args = {'x': x, 'y': y}
                if ipadx:
                    place_args['x'] -= ipadx
                if ipady:
                    place_args['y'] -= ipady
                button.place(**place_args)
            else:
                pack_args = {}
                if padx:
                    pack_args['padx'] = padx
                if pady:
                    pack_args['pady'] = pady
                if ipadx:
                    pack_args['ipadx'] = ipadx
                if ipady:
                    pack_args['ipady'] = ipady
                button.pack(**pack_args)
            if button_id:
                button_id_map[button_id] = button  
        elif child.tag == 'checkbutton':
            text = child.attrib.get('text', 'Checkbutton')
            command = None
            bg = child.attrib.get('bg')
            fg = child.attrib.get('fg')
            width = child.attrib.get('width')
            height = child.attrib.get('height')
            button_id = child.attrib.get('id')  
            x = child.attrib.get('x') 
            y = child.attrib.get('y') 
            anchor = child.attrib.get('anchor')
            activebackground = child.attrib.get('activebackground')
            activeforeground = child.attrib.get('activeforeground')
            bd = child.attrib.get('bd')
            font = child.attrib.get('font')
            highlightcolor = child.attrib.get('highlightcolor')
            image = child.attrib.get('image')
            justify = child.attrib.get('justify')
            padx = child.attrib.get('padx')
            pady = child.attrib.get('pady')
            ipadx = child.attrib.get('ipadx')
            ipady = child.attrib.get('ipady')
            state = child.attrib.get('state')
            variable = child.attrib.get('variable')
            onvalue = child.attrib.get('onvalue')
            offvalue = child.attrib.get('offvalue')
            indicatoron = child.attrib.get('indicatoron')
            wraplength = child.attrib.get('wraplength')
            if width:
                width = int(width)
            if height:
                height = int(height)
            if x:
                x = int(x)
            if y:
                y = int(y)
            if bd:
                bd = int(bd)
            if padx:
                padx = int(padx)
            if pady:
                pady = int(pady)
            if ipadx:
                ipadx = int(ipadx)
            if ipady:
                ipady = int(ipady)
            if wraplength:
                wraplength = int(wraplength)
            if indicatoron:
                indicatoron = indicatoron.lower() == 'true'
            for sub_child in child:
                if sub_child.tag == 'Click_command':
                    command_name = sub_child.text
            checkbutton_args = {
                'text': text
            }
            if bg:
                checkbutton_args['bg'] = bg
            if fg:
                checkbutton_args['fg'] = fg
            if width:
                checkbutton_args['width'] = width
            if height:
                checkbutton_args['height'] = height
            if anchor:
                checkbutton_args['anchor'] = anchor
            if activebackground:
                checkbutton_args['activebackground'] = activebackground
            if activeforeground:
                checkbutton_args['activeforeground'] = activeforeground
            if bd:
                checkbutton_args['bd'] = bd
            if font:
                checkbutton_args['font'] = font
            if highlightcolor:
                checkbutton_args['highlightcolor'] = highlightcolor
            if image:
                im=tk.PhotoImage(file=image)
                checkbutton_images[button_id]=im
                checkbutton_args['image'] = im
            if justify:
                checkbutton_args['justify'] = justify
            if state:
                checkbutton_args['state'] = state
            var = tk.IntVar()
            checkbutton_vars[button_id] = var 
            if onvalue is not None:
                try:
                    onvalue = int(onvalue)
                except ValueError:
                    pass
                checkbutton_args['onvalue'] = onvalue
            if offvalue is not None:
                try:
                    offvalue = int(offvalue)
                except ValueError:
                    pass
                checkbutton_args['offvalue'] = offvalue
            checkbutton_args['variable'] = var
            checkbutton = tk.Checkbutton(root_widget,**checkbutton_args)
            if command_name and command_name in globals():
                command = lambda btn=checkbutton, cmd=command_name: globals()[cmd](btn)
                checkbutton.config(command=command)
            if x is not None and y is not None:
                place_args = {'x': x, 'y': y}
                if ipadx:
                    place_args['x'] -= ipadx
                if ipady:
                    place_args['y'] -= ipady
                checkbutton.place(**place_args)
            else:
                pack_args = {}
                if padx:
                    pack_args['padx'] = padx
                if pady:
                    pack_args['pady'] = pady
                if ipadx:
                    pack_args['ipadx'] = ipadx
                if ipady:
                    pack_args['ipady'] = ipady
                checkbutton.pack(**pack_args)
            if button_id:
                checkbutton_id_map[button_id] = checkbutton  
                if var is not None:
                    checkbutton_id_map[button_id].var = var 


def setup_window_properties(root, xml_root):
    window_node = xml_root.find('window')
    if window_node is not None: 
        if window_node.get('title'):
            root.title(window_node.get('title'))
        if window_node.get('bg'):
            root.configure(bg=window_node.get('bg'))
        if window_node.get('geometry'):
            root.geometry(window_node.get('geometry'))
        if window_node.get('minsize'):
            min_w, min_h = map(int, window_node.get('minsize').split('x'))
            root.minsize(min_w, min_h)
        if window_node.get('maxsize'):
            max_w, max_h = map(int, window_node.get('maxsize').split('x'))
            root.maxsize(max_w, max_h)
        if window_node.get('resizable'):
            resizable_w, resizable_h = window_node.get('resizable').split(',')
            root.resizable(resizable_w.lower() == 'true', resizable_h.lower() == 'true')
        if window_node.get('iconbitmap'):
            root.iconbitmap(window_node.get('iconbitmap'))



def btn1_Click_command(sender):
    print('按钮被点击了',sender.cget('text'))

def chk1_Click_command(sender):
    print('按钮被点击了。',sender.var.get())

if __name__ == "__main__":
    root = tk.Tk()
    xml_data = '''
    <root>
        <window
            title="Tkinter 窗口示例"
            bg="lightgray"
            geometry="600x500+100+100"
            maxsize="800x600"
            minsize="200x150"
            resizable="True,False"
        />
        <button text="按钮 1" id="btn1" bg="lightblue" fg="red" width="200" height="200" x="50" y="50" 
                anchor="center" activebackground="yellow" activeforeground="black" bd="2" 
                font="Arial 10" highlightcolor="green" justify="center" padx="5" pady="5" 
                ipadx="2" ipady="2" state="normal" image="play.png">
            <Click_command>btn1_Click_command</Click_command>
        </button>
        <button image="play.png"/>
        <checkbutton text="复选框1" fg="black" id="chk1" bg="lightgray" x="100" y="200"
                     anchor="center" bd="1" font="Arial 10" state="normal" 
                     variable="chk_var" onvalue="1" offvalue="0" 
                     indicatoron="True" selectcolor="red" 
                     wraplength="100" image="play.png">
            <Click_command>chk1_Click_command</Click_command>
        </checkbutton>
    </root>
    '''
    try:
        xml_root = ET.fromstring(xml_data)
        setup_window_properties(root, xml_root)
    except ET.ParseError as e:
        print(f"XML 解析错误: {e}")
    
    create_widgets_from_xml(root, xml_root)
    
    root.mainloop()