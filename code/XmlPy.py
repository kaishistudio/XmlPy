import tkinter as tk
from tkinter import ttk
import xml.etree.ElementTree as ET

canvas_id_map = {}
button_id_map = {}
menu_id_map = {}
button_images = {}
checkbutton_id_map = {}
checkbutton_vars = {}
checkbutton_images = {}
radio_id_map = {}
radio_vars = {}
global_commands = {}
label_id_map = {}
entry_id_map = {}
text_id_map = {}
scale_id_map = {}
listbox_id_map = {}
rightmenu_name=["Select all","Cut","Copy","Paste","Delete"]
spinbox_id_map = {}
frame_id_map = {}
labelframe_id_map = {}
ttk_button_id_map = {}
ttk_label_id_map = {}
ttk_entry_id_map = {}
ttk_combobox_id_map = {}
ttk_treeview_id_map = {}
ttk_progressbar_id_map = {}
ttk_notebook_id_map = {}
notebook_tab_id_map = {}
ttk_separator_id_map = {}
ttk_scale_id_map = {}
ttk_checkbutton_id_map = {}
ttk_radiobutton_id_map = {}

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
            if command_name and command_name in global_commands:
                command = lambda btn=button, cmd=command_name: global_commands[cmd](btn)
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
        elif child.tag == 'Text':
            bg = child.attrib.get('bg')
            bd = child.attrib.get('bd')
            cursor = child.attrib.get('cursor')
            font = child.attrib.get('font')
            fg = child.attrib.get('fg')
            height = child.attrib.get('height')
            relief = child.attrib.get('relief')
            state = child.attrib.get('state')
            width = child.attrib.get('width')
            x = child.attrib.get('x')
            y = child.attrib.get('y')
            wrap = child.attrib.get('wrap')
            text = child.attrib.get('text', '')
            text_id = child.attrib.get('id')
            exportselection = child.attrib.get('exportselection')
            highlightbackground = child.attrib.get('highlightbackground')
            highlightcolor = child.attrib.get('highlightcolor')
            highlightthickness = child.attrib.get('highlightthickness')
            insertbackground = child.attrib.get('insertbackground')
            insertborderwidth = child.attrib.get('insertborderwidth')
            insertofftime = child.attrib.get('insertofftime')
            insertontime = child.attrib.get('insertontime')
            insertwidth = child.attrib.get('insertwidth')
            padx = child.attrib.get('padx')
            pady = child.attrib.get('pady')
            selectbackground = child.attrib.get('selectbackground')
            selectborderwidth = child.attrib.get('selectborderwidth')
            spacing1 = child.attrib.get('spacing1')
            spacing2 = child.attrib.get('spacing2')
            spacing3 = child.attrib.get('spacing3')
            tabs = child.attrib.get('tabs')
            xscrollcommand = child.attrib.get('xscrollcommand')
            yscrollcommand = child.attrib.get('yscrollcommand')

            if bd:
                bd = int(bd)
            if height:
                height = int(height)
            if width:
                width = int(width)
            if x:
                x = int(x)
            if y:
                y = int(y)
            if highlightthickness:
                highlightthickness = int(highlightthickness)
            if insertborderwidth:
                insertborderwidth = int(insertborderwidth)
            if insertofftime:
                insertofftime = int(insertofftime)
            if insertontime:
                insertontime = int(insertontime)
            if insertwidth:
                insertwidth = int(insertwidth)
            if padx:
                padx = int(padx)
            if pady:
                pady = int(pady)
            if selectborderwidth:
                selectborderwidth = int(selectborderwidth)
            if spacing1:
                spacing1 = int(spacing1)
            if spacing2:
                spacing2 = int(spacing2)
            if spacing3:
                spacing3 = int(spacing3)

            text_args = {}
            if bg:
                text_args['bg'] = bg
            if bd:
                text_args['bd'] = bd
            if cursor:
                text_args['cursor'] = cursor
            if font:
                text_args['font'] = font
            if fg:
                text_args['fg'] = fg
            if height:
                text_args['height'] = height
            if relief:
                text_args['relief'] = relief.lower()
            if state:
                text_args['state'] = state.lower()
            if width:
                text_args['width'] = width
            if wrap:
                text_args['wrap'] = wrap.lower()
            else:
                text_args['wrap'] = 'word'
            if exportselection:
                text_args['exportselection'] = int(exportselection)
            if highlightbackground:
                text_args['highlightbackground'] = highlightbackground
            if highlightcolor:
                text_args['highlightcolor'] = highlightcolor
            if highlightthickness:
                text_args['highlightthickness'] = highlightthickness
            if insertbackground:
                text_args['insertbackground'] = insertbackground
            if insertborderwidth:
                text_args['insertborderwidth'] = insertborderwidth
            if insertofftime:
                text_args['insertofftime'] = insertofftime
            if insertontime:
                text_args['insertontime'] = insertontime
            if insertwidth:
                text_args['insertwidth'] = insertwidth
            if padx:
                text_args['padx'] = padx
            if pady:
                text_args['pady'] = pady
            if selectbackground:
                text_args['selectbackground'] = selectbackground
            if selectborderwidth:
                text_args['selectborderwidth'] = selectborderwidth
            if spacing1:
                text_args['spacing1'] = spacing1
            if spacing2:
                text_args['spacing2'] = spacing2
            if spacing3:
                text_args['spacing3'] = spacing3
            if tabs:
                text_args['tabs'] = tabs
            if xscrollcommand:
                text_args['xscrollcommand'] = xscrollcommand
            if yscrollcommand:
                text_args['yscrollcommand'] = yscrollcommand

            text_widget = tk.Text(root_widget, **text_args)
            if text:
                text_widget.insert('1.0', text)

            textchanged_command = None
            for sub_child in child:
                if sub_child.tag == 'Textchanged_Command':
                    textchanged_command = sub_child.text
            if textchanged_command and textchanged_command in global_commands:
                def on_text_modified(event=None, cmd=textchanged_command, widget=text_widget):
                    if widget.edit_modified():
                        global_commands[cmd](widget)
                        widget.edit_modified(False)
                text_widget.bind('<<Modified>>', on_text_modified)

            menu = tk.Menu(text_widget, tearoff=0)
            menu.add_command(label=rightmenu_name[0], command=lambda w=text_widget: w.tag_add(tk.SEL, "1.0", tk.END))
            menu.add_command(label=rightmenu_name[1], command=lambda w=text_widget: w.event_generate("<<Cut>>"))
            menu.add_command(label=rightmenu_name[2], command=lambda w=text_widget: w.event_generate("<<Copy>>"))
            menu.add_command(label=rightmenu_name[3], command=lambda w=text_widget: w.event_generate("<<Paste>>"))
            menu.add_command(label=rightmenu_name[4], command=lambda w=text_widget: w.delete(tk.SEL_FIRST, tk.SEL_LAST) if w.tag_ranges(tk.SEL) else None)

            def show_context_menu(event, widget_menu=menu):
                widget_menu.tk_popup(event.x_root, event.y_root)

            text_widget.bind("<Button-3>", lambda e, m=menu: show_context_menu(e, m))

            if x is not None and y is not None:
                place_args = {'x': x, 'y': y}
                text_widget.place(**place_args)
            else:
                pack_args = {}
                if padx:
                    pack_args['padx'] = int(padx)
                if pady:
                    pack_args['pady'] = int(pady)
                if ipadx:
                    pack_args['ipadx'] = int(ipadx)
                if ipady:
                    pack_args['ipady'] = int(ipady)
                text_widget.pack(**pack_args)

            if text_id:
                text_id_map[text_id] = text_widget
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
            command_name = None
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
            if justify:
                checkbutton_args['justify'] = justify
            if state:
                checkbutton_args['state'] = state
            if image:
                im=tk.PhotoImage(file=image)
                checkbutton_images[button_id]=im
                checkbutton_args['image'] = im
            if variable:
                if variable not in checkbutton_vars:
                    checkbutton_vars[variable] = tk.IntVar()
                checkbutton_args['variable'] = checkbutton_vars[variable]
            if onvalue:
                checkbutton_args['onvalue'] = onvalue
            if offvalue:
                checkbutton_args['offvalue'] = offvalue
            if indicatoron is not None:
                checkbutton_args['indicatoron'] = indicatoron
            if wraplength:
                checkbutton_args['wraplength'] = wraplength
            checkbutton = tk.Checkbutton(root_widget, **checkbutton_args)
            if command_name and command_name in global_commands:
                command = lambda btn=checkbutton, cmd=command_name: global_commands[cmd](btn)
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
                if variable:
                    checkbutton_id_map[button_id].var = checkbutton_vars[variable]
        elif child.tag == 'scale':
            from_ = int(child.attrib.get('from', 0))
            to = int(child.attrib.get('to', 100))
            orient = child.attrib.get('orient', 'horizontal')
            length = int(child.attrib.get('length', 100))
            resolution = float(child.attrib.get('resolution', 1))
            x = child.attrib.get('x')
            y = child.attrib.get('y')
            scale_id = child.attrib.get('id')
            state = child.attrib.get('state')
            activebackground = child.attrib.get('activebackground')
            bigincrement = child.attrib.get('bigincrement')
            borderwidth = child.attrib.get('borderwidth')
            digits = child.attrib.get('digits')
            font = child.attrib.get('font')
            highlightcolor = child.attrib.get('highlightcolor')
            label = child.attrib.get('label')
            repeatdelay = child.attrib.get('repeatdelay')
            repeatinterval = child.attrib.get('repeatinterval')
            showvalue = child.attrib.get('showvalue')
            sliderlength = child.attrib.get('sliderlength')
            takefocus = child.attrib.get('takefocus')
            tickinterval = child.attrib.get('tickinterval')
            troughcolor = child.attrib.get('troughcolor')
            variable = child.attrib.get('variable')
            width = child.attrib.get('width')
        
            scale_args = {
                'from_': from_,
                'to': to,
                'orient': orient,
                'length': length,
                'resolution': resolution
            }
        
            if state:
                scale_args['state'] = state
            if activebackground:
                scale_args['activebackground'] = activebackground
            if bigincrement:
                scale_args['bigincrement'] = float(bigincrement)
            if borderwidth:
                scale_args['borderwidth'] = int(borderwidth)
            if digits:
                scale_args['digits'] = int(digits)
            if font:
                scale_args['font'] = font
            if highlightcolor:
                scale_args['highlightcolor'] = highlightcolor
            if label:
                scale_args['label'] = label
            if repeatdelay:
                scale_args['repeatdelay'] = int(repeatdelay)
            if repeatinterval:
                scale_args['repeatinterval'] = int(repeatinterval)
            if showvalue:
                scale_args['showvalue'] = showvalue.lower() == 'true'
            if sliderlength:
                scale_args['sliderlength'] = int(sliderlength)
            if takefocus:
                scale_args['takefocus'] = takefocus.lower() == 'true'
            if tickinterval:
                scale_args['tickinterval'] = float(tickinterval)
            if troughcolor:
                scale_args['troughcolor'] = troughcolor
            if variable:
                scale_args['variable'] = variable
            if width:
                scale_args['width'] = int(width)
        
            command_name = None
            for sub_child in child:
                if sub_child.tag == 'Valuechanged_Command':
                    command_name = sub_child.text
            
            scale = tk.Scale(root_widget, **scale_args)
            if command_name and command_name in global_commands:
                scale.config(command=lambda *args,btn=scale, cmd=command_name: global_commands[cmd](btn))
            
            
            if x is not None and y is not None:
                x = int(x)
                y = int(y)
                scale.place(x=x, y=y)
            else:
                scale.pack()
            if scale_id:
                scale_id_map[scale_id] = scale
        elif child.tag == 'label':
            text = child.attrib.get('text', 'Label')
            bg = child.attrib.get('bg')
            fg = child.attrib.get('fg')
            width = child.attrib.get('width')
            height = child.attrib.get('height')
            label_id = child.attrib.get('id')
            x = child.attrib.get('x')
            y = child.attrib.get('y')
            anchor = child.attrib.get('anchor')
            bd = child.attrib.get('bd')
            font = child.attrib.get('font')
            image = child.attrib.get('image')
            justify = child.attrib.get('justify')
            padx = child.attrib.get('padx')
            pady = child.attrib.get('pady')
            ipadx = child.attrib.get('ipadx')
            ipady = child.attrib.get('ipady')
            relief = child.attrib.get('relief')
            state = child.attrib.get('state')
            textvariable = child.attrib.get('textvariable')
            underline = child.attrib.get('underline')
            wraplength = child.attrib.get('wraplength')
            compound = child.attrib.get('compound')
            
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
            if underline:
                underline = int(underline)
            if wraplength:
                wraplength = int(wraplength)
            
            label_args = {'text': text}
            if bg:
                label_args['bg'] = bg
            if fg:
                label_args['fg'] = fg
            if width:
                label_args['width'] = width
            if height:
                label_args['height'] = height
            if anchor:
                label_args['anchor'] = anchor
            if bd:
                label_args['bd'] = bd
            if font:
                label_args['font'] = font
            if justify:
                label_args['justify'] = justify
            if relief:
                label_args['relief'] = relief.lower()
            if state:
                label_args['state'] = state.lower()
            if underline is not None:
                label_args['underline'] = underline
            if wraplength:
                label_args['wraplength'] = wraplength
            if compound:
                label_args['compound'] = compound
            if image:
                im = tk.PhotoImage(file=image)
                button_images[label_id] = im
                label_args['image'] = im
            
            label = tk.Label(root_widget, **label_args)
            
            if x is not None and y is not None:
                place_args = {'x': x, 'y': y}
                if ipadx:
                    place_args['x'] -= ipadx
                if ipady:
                    place_args['y'] -= ipady
                label.place(**place_args)
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
                label.pack(**pack_args)
            
            if label_id:
                label_id_map[label_id] = label
        elif child.tag == 'entry':
            bg = child.attrib.get('bg')
            bd = child.attrib.get('bd')
            cursor = child.attrib.get('cursor')
            font = child.attrib.get('font')
            exportselection = child.attrib.get('exportselection')
            fg = child.attrib.get('fg')
            highlightcolor = child.attrib.get('highlightcolor')
            justify = child.attrib.get('justify')
            relief = child.attrib.get('relief')
            selectbackground = child.attrib.get('selectbackground')
            selectborderwidth = child.attrib.get('selectborderwidth')
            selectforeground = child.attrib.get('selectforeground')
            show = child.attrib.get('show')
            state = child.attrib.get('state')
            textvariable = child.attrib.get('textvariable')
            width = child.attrib.get('width')
            xscrollcommand = child.attrib.get('xscrollcommand')
            x = child.attrib.get('x')
            y = child.attrib.get('y')
            if bd:
                bd = int(bd)
            if width:
                width = int(width)
            if x:
                x = int(x)
            if y:
                y = int(y)
            if exportselection:
                exportselection = int(exportselection)
            if selectborderwidth:
                selectborderwidth = int(selectborderwidth)
            textchanged_command_name = None
            for sub_child in child:
                if sub_child.tag == 'Textchanged_Command':
                    textchanged_command_name = sub_child.text
            entry_args = {}
            if bg:
                entry_args['bg'] = bg
            if bd:
                entry_args['bd'] = bd
            if cursor:
                entry_args['cursor'] = cursor
            if font:
                entry_args['font'] = font
            if exportselection is not None:
                entry_args['exportselection'] = exportselection
            if fg:
                entry_args['fg'] = fg
            if highlightcolor:
                entry_args['highlightcolor'] = highlightcolor
            if justify:
                entry_args['justify'] = justify.lower()  
            if relief:
                entry_args['relief'] = relief.upper() 
            if selectbackground:
                entry_args['selectbackground'] = selectbackground
            if selectborderwidth:
                entry_args['selectborderwidth'] = selectborderwidth
            if selectforeground:
                entry_args['selectforeground'] = selectforeground
            if show:
                entry_args['show'] = show
            if state:
                entry_args['state'] = state.lower() 
            if textvariable:
                if textvariable not in globals():
                    globals()[textvariable] = tk.StringVar()
                entry_args['textvariable'] = globals()[textvariable]
            if width:
                entry_args['width'] = width
            if xscrollcommand:
                entry_args['xscrollcommand'] = xscrollcommand
            entry = tk.Entry(root_widget, **entry_args)
            if textvariable and textchanged_command_name and textchanged_command_name in global_commands:
                command = lambda *args,btn=entry, cmd=textchanged_command_name: global_commands[cmd](btn)
                entry_args['textvariable'].trace_add('write', command)
            on_modified = None
            for sub_child in child:
                if sub_child.tag == 'OnModified':
                    on_modified = sub_child.text
            
            if on_modified and on_modified in global_commands:
                def on_entry_modified(event, cmd=on_modified, widget=entry):
                    widget.event_generate('<<Modified>>')
                    if widget.getvar('entry_modified'):
                        global_commands[cmd](widget)
                        widget.setvar('entry_modified', False)
                
                entry.bind('<<Modified>>', on_entry_modified)
                entry.setvar('entry_modified', False)
            
            if x is not None and y is not None:
                place_args = {'x': x, 'y': y}
                entry.place(**place_args)
            else:
                pack_args = {}
                entry.pack(**pack_args)
            
            entry_id = child.attrib.get('id') 
            
            if entry_id:
                entry_id_map[entry_id] = entry
        elif child.tag == 'listbox':
                bg = child.attrib.get('bg')
                bd = child.attrib.get('bd')
                cursor = child.attrib.get('cursor')
                font = child.attrib.get('font')
                fg = child.attrib.get('fg')
                height = child.attrib.get('height')
                highlightcolor = child.attrib.get('highlightcolor')
                highlightthickness = child.attrib.get('highlightthickness')
                relief = child.attrib.get('relief')
                selectbackground = child.attrib.get('selectbackground')
                selectmode = child.attrib.get('selectmode')
                width = child.attrib.get('width')
                xscrollcommand = child.attrib.get('xscrollcommand')
                yscrollcommand = child.attrib.get('yscrollcommand')
                x = child.attrib.get('x')
                y = child.attrib.get('y')
                listbox_id = child.attrib.get('id')

                # 类型转换
                if bd:
                    bd = int(bd)
                if height:
                    height = int(height)
                if highlightthickness:
                    highlightthickness = int(highlightthickness)
                if width:
                    width = int(width)
                if x:
                    x = int(x)
                if y:
                    y = int(y)

                listbox_args = {}
                if bg:
                    listbox_args['bg'] = bg
                if bd:
                    listbox_args['bd'] = bd
                if cursor:
                    listbox_args['cursor'] = cursor
                if font:
                    listbox_args['font'] = font
                if fg:
                    listbox_args['fg'] = fg
                if height:
                    listbox_args['height'] = height
                if highlightcolor:
                    listbox_args['highlightcolor'] = highlightcolor
                if highlightthickness:
                    listbox_args['highlightthickness'] = highlightthickness
                if relief:
                    listbox_args['relief'] = relief.lower()
                if selectbackground:
                    listbox_args['selectbackground'] = selectbackground
                if selectmode:
                    listbox_args['selectmode'] = selectmode.lower()
                if width:
                    listbox_args['width'] = width
                if xscrollcommand:
                    listbox_args['xscrollcommand'] = xscrollcommand
                if yscrollcommand:
                    listbox_args['yscrollcommand'] = yscrollcommand

                listbox = tk.Listbox(root_widget, **listbox_args)
                
                bind_events(listbox, child)
                
                select_changed_command = None
                for sub_child in child:
                    if sub_child.tag == 'listitem' or sub_child.tag == 'item':
                        listbox.insert(tk.END, sub_child.text)
                    elif sub_child.tag == 'Selectchanged_Command':
                        select_changed_command = sub_child.text
                
                if select_changed_command and select_changed_command in global_commands:
                    listbox.bind('<<ListboxSelect>>', lambda e, cmd=select_changed_command: global_commands[cmd](listbox))

                # 布局处理
                if x is not None and y is not None:
                    place_args = {'x': x, 'y': y}
                    listbox.place(**place_args)
                else:
                    listbox.pack()

                # 存储 listbox 实例
                if listbox_id:
                    listbox_id_map[listbox_id] = listbox
        elif child.tag == 'menu':
            menu_id_map = {}
            menu_id = child.attrib.get('id')
            tearoff = child.attrib.get('tearoff', 'False')
            tearoff = int(tearoff.lower() == 'true')
            # 获取 menu 点击事件命令
            menu_command = child.attrib.get('command')
            # 创建 Menubutton 作为菜单入口
            menubutton = tk.Menubutton(root_widget, text=child.attrib.get('label', 'Menu'))
            menu = tk.Menu(menubutton, tearoff=tearoff)
            menubutton.config(menu=menu)
            # 绑定点击事件
            if menu_command and menu_command in global_commands:
                menubutton.config(command=lambda cmd=menu_command: global_commands[cmd]())
            if menu_id:
                menu_id_map[menu_id] = menubutton

            for sub_child in child:
                if sub_child.tag == 'menuitem':
                    item_args = {}
                    accelerator = sub_child.attrib.get('accelerator')
                    command = sub_child.attrib.get('command')
                    label = sub_child.attrib.get('label')
                    menu_ref = sub_child.attrib.get('menu')
                    selectcolor = sub_child.attrib.get('selectcolor')
                    state = sub_child.attrib.get('state')
                    onvalue = sub_child.attrib.get('onvalue')
                    offvalue = sub_child.attrib.get('offvalue')
                    underline = sub_child.attrib.get('underline')
                    value = sub_child.attrib.get('value')
                    variable = sub_child.attrib.get('variable')

                    if label:
                        item_args['label'] = label
                    if accelerator:
                        item_args['accelerator'] = accelerator
                    if command and command in global_commands:
                        item_args['command'] = lambda cmd=command: global_commands[cmd]()
                    if menu_ref and menu_ref in menu_id_map:
                        item_args['menu'] = menu_id_map[menu_ref]
                    if state:
                        item_args['state'] = state
                    if underline is not None:
                        item_args['underline'] = int(underline)
                    if variable:
                        if variable not in globals():
                            if onvalue is not None or offvalue is not None:
                                globals()[variable] = tk.IntVar()
                            else:
                                globals()[variable] = tk.StringVar()
                        item_args['variable'] = globals()[variable]
                        if onvalue is not None:
                            item_args['onvalue'] = onvalue
                        if offvalue is not None:
                            item_args['offvalue'] = offvalue

                    # 移除无效选项
                    item_args.pop('selectcolor', None)
                    item_args.pop('value', None)

                    if menu_ref:
                        menu.add_cascade(**item_args)
                    elif variable:
                        if onvalue is not None and offvalue is not None:
                            menu.add_checkbutton(**item_args)
                        else:
                            menu.add_radiobutton(**item_args)
                    else:
                        menu.add_command(**item_args)

            # 布局 Menubutton
            x = child.attrib.get('x')
            y = child.attrib.get('y')
            if x is not None and y is not None:
                place_args = {'x': int(x), 'y': int(y)}
                menubutton.place(**place_args)
            else:
                menubutton.pack(side=tk.LEFT)

            # 如果是主窗口，添加菜单栏布局逻辑
            if isinstance(root_widget, tk.Tk):
                # 此处可以添加菜单栏的额外布局逻辑
                pass
        elif child.tag == 'spinbox':
            activebackground = child.attrib.get('activebackground')
            bg = child.attrib.get('bg')
            bd = child.attrib.get('bd')
            command = child.attrib.get('command')
            cursor = child.attrib.get('cursor')
            disabledbackground = child.attrib.get('disabledbackground')
            disabledforeground = child.attrib.get('disabledforeground')
            fg = child.attrib.get('fg')
            font = child.attrib.get('font')
            format_ = child.attrib.get('format')
            from_ = child.attrib.get('from_')
            justify = child.attrib.get('justify', 'LEFT')
            relief = child.attrib.get('relief', 'SUNKEN')
            repeatdelay = child.attrib.get('repeatdelay')
            repeatinterval = child.attrib.get('repeatinterval')
            state = child.attrib.get('state', 'NORMAL')
            textvariable = child.attrib.get('textvariable')
            to = child.attrib.get('to')
            validate = child.attrib.get('validate', 'none')
            validatecommand = child.attrib.get('validatecommand')
            values = child.attrib.get('values')
            vcmd = child.attrib.get('vcmd')
            width = child.attrib.get('width', '20')
            wrap = child.attrib.get('wrap')
            xscrollcommand = child.attrib.get('xscrollcommand')
            x = child.attrib.get('x')
            y = child.attrib.get('y')
            spinbox_id = child.attrib.get('id')

            spinbox_args = {}
            if activebackground:
                spinbox_args['activebackground'] = activebackground
            if bg:
                spinbox_args['bg'] = bg
            if bd:
                spinbox_args['bd'] = int(bd)
            if cursor:
                spinbox_args['cursor'] = cursor
            if disabledbackground:
                spinbox_args['disabledbackground'] = disabledbackground
            if disabledforeground:
                spinbox_args['disabledforeground'] = disabledforeground
            if fg:
                spinbox_args['fg'] = fg
            if font:
                spinbox_args['font'] = font
            if format_:
                spinbox_args['format'] = format_
            if from_:
                spinbox_args['from_'] = int(from_)
            if justify:
                spinbox_args['justify'] = justify.lower()
            if relief:
                spinbox_args['relief'] = relief.lower()
            if repeatdelay:
                spinbox_args['repeatdelay'] = int(repeatdelay)
            if repeatinterval:
                spinbox_args['repeatinterval'] = int(repeatinterval)
            if state:
                # 将状态值转换为小写
                spinbox_args['state'] = state.lower()
            if textvariable:
                if textvariable not in globals():
                    globals()[textvariable] = tk.StringVar()
                spinbox_args['textvariable'] = globals()[textvariable]
            if to:
                spinbox_args['to'] = int(to)
            if validate:
                spinbox_args['validate'] = validate
            if validatecommand:
                spinbox_args['validatecommand'] = validatecommand
            if values:
                spinbox_args['values'] = tuple(map(str.strip, values.split(',')))
            if vcmd:
                spinbox_args['vcmd'] = vcmd
            if width:
                spinbox_args['width'] = int(width)
            if wrap:
                spinbox_args['wrap'] = wrap.lower() == 'true'
            if xscrollcommand:
                spinbox_args['xscrollcommand'] = xscrollcommand

            spinbox = tk.Spinbox(root_widget, **spinbox_args)

            # 获取 Valuechanged_Command 值
            valuechanged_command = child.find('Valuechanged_Command')
            if valuechanged_command is not None and valuechanged_command.text in global_commands:
                spinbox.config(command=lambda *args, cmd=valuechanged_command.text: global_commands[cmd](spinbox))
            if command and command in global_commands:
                spinbox.config(command=lambda cmd=command: global_commands[cmd]())

            if x is not None and y is not None:
                place_args = {'x': int(x), 'y': int(y)}
                spinbox.place(**place_args)
            else:
                pack_args = {}
                spinbox.pack(**pack_args)

            if spinbox_id:
                spinbox_id_map[spinbox_id] = spinbox
        elif child.tag == 'Canvas':
            bd = child.attrib.get('bd')
            bg = child.attrib.get('bg')
            confine = child.attrib.get('confine')
            cursor = child.attrib.get('cursor')
            height = child.attrib.get('height')
            highlightcolor = child.attrib.get('highlightcolor')
            relief = child.attrib.get('relief')
            scrollregion = child.attrib.get('scrollregion')
            width = child.attrib.get('width')
            xscrollincrement = child.attrib.get('xscrollincrement')
            xscrollcommand = child.attrib.get('xscrollcommand')
            yscrollincrement = child.attrib.get('yscrollincrement')
            yscrollcommand = child.attrib.get('yscrollcommand')
            
            if bd:
                bd = int(bd)
            if height:
                height = int(height)
            if width:
                width = int(width)
            if xscrollincrement:
                xscrollincrement = int(xscrollincrement)
            if yscrollincrement:
                yscrollincrement = int(yscrollincrement)
            
            canvas_args = {}
            if bd:
                canvas_args['bd'] = bd
            if bg:
                canvas_args['bg'] = bg
            if confine:
                canvas_args['confine'] = confine.lower() == 'true'
            if cursor:
                canvas_args['cursor'] = cursor
            if height:
                canvas_args['height'] = height
            if highlightcolor:
                canvas_args['highlightcolor'] = highlightcolor
            if relief:
                canvas_args['relief'] = relief.lower()
            if scrollregion:
                canvas_args['scrollregion'] = scrollregion
            if width:
                canvas_args['width'] = width
            if xscrollincrement:
                canvas_args['xscrollincrement'] = xscrollincrement
            if xscrollcommand:
                canvas_args['xscrollcommand'] = xscrollcommand
            if yscrollincrement:
                canvas_args['yscrollincrement'] = yscrollincrement
            if yscrollcommand:
                canvas_args['yscrollcommand'] = yscrollcommand
            
            canvas = tk.Canvas(root_widget, **canvas_args)
            
            x = child.attrib.get('x')
            y = child.attrib.get('y')
            if x is not None and y is not None:
                x = int(x)
                y = int(y)
                place_args = {'x': x, 'y': y}
                canvas.place(**place_args)
            else:
                pack_args = {}
                canvas.pack(**pack_args)
            
            canvas_id = child.attrib.get('id')
            if canvas_id:
                # Bug fix: 移除重新定义 canvas_id_map 的代码，使用全局的 canvas_id_map
                global canvas_id_map
                canvas_id_map[canvas_id] = canvas
        elif child.tag == 'Radiobutton':
            text = child.attrib.get('text', 'Radiobutton')
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
            highlightbackground = child.attrib.get('highlightbackground')
            image = child.attrib.get('image')
            justify = child.attrib.get('justify')
            padx = child.attrib.get('padx')
            pady = child.attrib.get('pady')
            ipadx = child.attrib.get('ipadx')
            ipady = child.attrib.get('ipady')
            state = child.attrib.get('state')
            variable = child.attrib.get('variable')
            value = child.attrib.get('value')
            cursor = child.attrib.get('cursor')
            relief = child.attrib.get('relief')
            selectcolor = child.attrib.get('selectcolor')
            selectimage = child.attrib.get('selectimage')
            underline = child.attrib.get('underline')
            wraplength = child.attrib.get('wraplength')
            bitmap = child.attrib.get('bitmap')
            textvariable = child.attrib.get('textvariable')
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
            if underline:
                underline = int(underline)
            if wraplength:
                wraplength = int(wraplength)
            command_name = None
            for sub_child in child:
                if sub_child.tag == 'Click_command':
                    command_name = sub_child.text
            radio_args = {
                'text': text
            }
            if bg:
                radio_args['bg'] = bg
            if fg:
                radio_args['fg'] = fg
            if width:
                radio_args['width'] = width
            if height:
                radio_args['height'] = height
            if anchor:
                radio_args['anchor'] = anchor
            if activebackground:
                radio_args['activebackground'] = activebackground
            if activeforeground:
                radio_args['activeforeground'] = activeforeground
            if bd:
                radio_args['bd'] = bd
            if font:
                radio_args['font'] = font
            if highlightcolor:
                radio_args['highlightcolor'] = highlightcolor
            if highlightbackground:
                radio_args['highlightbackground'] = highlightbackground
            if justify:
                radio_args['justify'] = justify
            if state:
                radio_args['state'] = state
            if image:
                im=tk.PhotoImage(file=image)
                button_images[button_id]=im
                radio_args['image'] = im
            if cursor:
                radio_args['cursor'] = cursor
            if relief:
                radio_args['relief'] = relief
            if selectcolor:
                radio_args['selectcolor'] = selectcolor
            if selectimage:
                im=tk.PhotoImage(file=selectimage)
                button_images[button_id]=im
                radio_args['selectimage'] = im
            if underline is not None:
                radio_args['underline'] = underline
            if wraplength:
                radio_args['wraplength'] = wraplength
            if bitmap:
                radio_args['bitmap'] = bitmap
            if textvariable:
                radio_args['textvariable'] = textvariable
            if variable:
                if variable not in radio_vars:
                    radio_vars[variable] = tk.StringVar()
                radio_args['variable'] = radio_vars[variable]
            if value:
                radio_args['value'] = value
            radio = tk.Radiobutton(root_widget, **radio_args)
            if command_name and command_name in global_commands:
                command = lambda btn=radio, cmd=command_name: global_commands[cmd](btn)
                radio.config(command=command)
            if x is not None and y is not None:
                place_args = {'x': x, 'y': y}
                if ipadx:
                    place_args['x'] -= ipadx
                if ipady:
                    place_args['y'] -= ipady
                radio.place(**place_args)
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
                radio.pack(**pack_args)
            if button_id:
                radio_id_map[button_id] = radio
                if variable:
                    radio_id_map[button_id].var = radio_vars[variable]

        elif child.tag == 'frame':
            bg = child.attrib.get('bg')
            bd = child.attrib.get('bd')
            cursor = child.attrib.get('cursor')
            height = child.attrib.get('height')
            relief = child.attrib.get('relief')
            width = child.attrib.get('width')
            x = child.attrib.get('x')
            y = child.attrib.get('y')
            frame_id = child.attrib.get('id')
            padx = child.attrib.get('padx')
            pady = child.attrib.get('pady')
            ipadx = child.attrib.get('ipadx')
            ipady = child.attrib.get('ipady')
            
            if bd:
                bd = int(bd)
            if height:
                height = int(height)
            if width:
                width = int(width)
            if x:
                x = int(x)
            if y:
                y = int(y)
            if padx:
                padx = int(padx)
            if pady:
                pady = int(pady)
            if ipadx:
                ipadx = int(ipadx)
            if ipady:
                ipady = int(ipady)
            
            frame_args = {}
            if bg:
                frame_args['bg'] = bg
            if bd:
                frame_args['bd'] = bd
            if cursor:
                frame_args['cursor'] = cursor
            if height:
                frame_args['height'] = height
            if relief:
                frame_args['relief'] = relief.lower()
            if width:
                frame_args['width'] = width
            
            frame = tk.Frame(root_widget, **frame_args)
            
            bind_events(frame, child)
            
            if x is not None and y is not None:
                place_args = {'x': x, 'y': y}
                if ipadx:
                    place_args['x'] -= ipadx
                if ipady:
                    place_args['y'] -= ipady
                frame.place(**place_args)
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
                frame.pack(**pack_args)
            
            if frame_id:
                frame_id_map[frame_id] = frame
            
            create_widgets_from_xml(frame, child)

        elif child.tag == 'labelframe':
            bg = child.attrib.get('bg')
            bd = child.attrib.get('bd')
            cursor = child.attrib.get('cursor')
            height = child.attrib.get('height')
            relief = child.attrib.get('relief')
            width = child.attrib.get('width')
            x = child.attrib.get('x')
            y = child.attrib.get('y')
            frame_id = child.attrib.get('id')
            text = child.attrib.get('text', 'LabelFrame')
            padx = child.attrib.get('padx')
            pady = child.attrib.get('pady')
            ipadx = child.attrib.get('ipadx')
            ipady = child.attrib.get('ipady')
            font = child.attrib.get('font')
            fg = child.attrib.get('fg')
            labelanchor = child.attrib.get('labelanchor')
            
            if bd:
                bd = int(bd)
            if height:
                height = int(height)
            if width:
                width = int(width)
            if x:
                x = int(x)
            if y:
                y = int(y)
            if padx:
                padx = int(padx)
            if pady:
                pady = int(pady)
            if ipadx:
                ipadx = int(ipadx)
            if ipady:
                ipady = int(ipady)
            
            frame_args = {'text': text}
            if bg:
                frame_args['bg'] = bg
            if bd:
                frame_args['bd'] = bd
            if cursor:
                frame_args['cursor'] = cursor
            if height:
                frame_args['height'] = height
            if relief:
                frame_args['relief'] = relief.lower()
            if width:
                frame_args['width'] = width
            if font:
                frame_args['font'] = font
            if fg:
                frame_args['fg'] = fg
            if labelanchor:
                frame_args['labelanchor'] = labelanchor
            
            labelframe = tk.LabelFrame(root_widget, **frame_args)
            
            bind_events(labelframe, child)
            
            if x is not None and y is not None:
                place_args = {'x': x, 'y': y}
                if ipadx:
                    place_args['x'] -= ipadx
                if ipady:
                    place_args['y'] -= ipady
                labelframe.place(**place_args)
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
                labelframe.pack(**pack_args)
            
            if frame_id:
                labelframe_id_map[frame_id] = labelframe
            
            create_widgets_from_xml(labelframe, child)

        elif child.tag == 'ttk_button':
            text = child.attrib.get('text', 'Button')
            command = None
            width = child.attrib.get('width')
            button_id = child.attrib.get('id')
            x = child.attrib.get('x')
            y = child.attrib.get('y')
            style = child.attrib.get('style')
            state = child.attrib.get('state')
            image = child.attrib.get('image')
            compound = child.attrib.get('compound')
            padx = child.attrib.get('padx')
            pady = child.attrib.get('pady')
            ipadx = child.attrib.get('ipadx')
            ipady = child.attrib.get('ipady')
            
            if width:
                width = int(width)
            if x:
                x = int(x)
            if y:
                y = int(y)
            if padx:
                padx = int(padx)
            if pady:
                pady = int(pady)
            if ipadx:
                ipadx = int(ipadx)
            if ipady:
                ipady = int(ipady)
            
            button_args = {'text': text}
            if width:
                button_args['width'] = width
            if style:
                button_args['style'] = style
            if state:
                button_args['state'] = state
            if compound:
                button_args['compound'] = compound
            
            button = ttk.Button(root_widget, **button_args)
            
            if image:
                im = tk.PhotoImage(file=image)
                button_images[button_id] = im
                button.config(image=im)
            
            command_name = None
            for sub_child in child:
                if sub_child.tag == 'Click_command':
                    command_name = sub_child.text
            
            if command_name and command_name in global_commands:
                command = lambda btn=button, cmd=command_name: global_commands[cmd](btn)
                button.config(command=command)
            
            bind_events(button, child)
            
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
                ttk_button_id_map[button_id] = button

        elif child.tag == 'ttk_label':
            text = child.attrib.get('text', 'Label')
            width = child.attrib.get('width')
            label_id = child.attrib.get('id')
            x = child.attrib.get('x')
            y = child.attrib.get('y')
            anchor = child.attrib.get('anchor')
            font = child.attrib.get('font')
            image = child.attrib.get('image')
            compound = child.attrib.get('compound')
            padx = child.attrib.get('padx')
            pady = child.attrib.get('pady')
            ipadx = child.attrib.get('ipadx')
            ipady = child.attrib.get('ipady')
            style = child.attrib.get('style')
            
            if width:
                width = int(width)
            if x:
                x = int(x)
            if y:
                y = int(y)
            if padx:
                padx = int(padx)
            if pady:
                pady = int(pady)
            if ipadx:
                ipadx = int(ipadx)
            if ipady:
                ipady = int(ipady)
            
            label_args = {'text': text}
            if width:
                label_args['width'] = width
            if anchor:
                label_args['anchor'] = anchor
            if font:
                label_args['font'] = font
            if compound:
                label_args['compound'] = compound
            if style:
                label_args['style'] = style
            
            label = ttk.Label(root_widget, **label_args)
            
            if image:
                im = tk.PhotoImage(file=image)
                button_images[label_id] = im
                label.config(image=im)
            
            bind_events(label, child)
            
            if x is not None and y is not None:
                place_args = {'x': x, 'y': y}
                if ipadx:
                    place_args['x'] -= ipadx
                if ipady:
                    place_args['y'] -= ipady
                label.place(**place_args)
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
                label.pack(**pack_args)
            
            if label_id:
                ttk_label_id_map[label_id] = label

        elif child.tag == 'ttk_entry':
            width = child.attrib.get('width', 20)
            entry_id = child.attrib.get('id')
            x = child.attrib.get('x')
            y = child.attrib.get('y')
            font = child.attrib.get('font')
            show = child.attrib.get('show')
            state = child.attrib.get('state')
            style = child.attrib.get('style')
            padx = child.attrib.get('padx')
            pady = child.attrib.get('pady')
            ipadx = child.attrib.get('ipadx')
            ipady = child.attrib.get('ipady')
            textvariable = child.attrib.get('textvariable')
            
            if width:
                width = int(width)
            if x:
                x = int(x)
            if y:
                y = int(y)
            if padx:
                padx = int(padx)
            if pady:
                pady = int(pady)
            if ipadx:
                ipadx = int(ipadx)
            if ipady:
                ipady = int(ipady)
            
            entry_args = {'width': width}
            if font:
                entry_args['font'] = font
            if show:
                entry_args['show'] = show
            if state:
                entry_args['state'] = state
            if style:
                entry_args['style'] = style
            
            if textvariable:
                if textvariable not in globals():
                    globals()[textvariable] = tk.StringVar()
                entry_args['textvariable'] = globals()[textvariable]
            
            entry = ttk.Entry(root_widget, **entry_args)
            
            bind_events(entry, child)
            
            command_name = None
            for sub_child in child:
                if sub_child.tag == 'Textchanged_Command':
                    command_name = sub_child.text
            
            if command_name and command_name in global_commands:
                def on_entry_modified(event=None, cmd=command_name, widget=entry):
                    global_commands[cmd](widget)
                entry.bind('<KeyRelease>', on_entry_modified)
            
            if x is not None and y is not None:
                place_args = {'x': x, 'y': y}
                if ipadx:
                    place_args['x'] -= ipadx
                if ipady:
                    place_args['y'] -= ipady
                entry.place(**place_args)
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
                entry.pack(**pack_args)
            
            if entry_id:
                ttk_entry_id_map[entry_id] = entry

        elif child.tag == 'ttk_combobox':
            width = child.attrib.get('width', 20)
            combobox_id = child.attrib.get('id')
            x = child.attrib.get('x')
            y = child.attrib.get('y')
            font = child.attrib.get('font')
            state = child.attrib.get('state')
            style = child.attrib.get('style')
            values = child.attrib.get('values', '')
            padx = child.attrib.get('padx')
            pady = child.attrib.get('pady')
            ipadx = child.attrib.get('ipadx')
            ipady = child.attrib.get('ipady')
            textvariable = child.attrib.get('textvariable')
            
            if width:
                width = int(width)
            if x:
                x = int(x)
            if y:
                y = int(y)
            if padx:
                padx = int(padx)
            if pady:
                pady = int(pady)
            if ipadx:
                ipadx = int(ipadx)
            if ipady:
                ipady = int(ipady)
            
            entry_args = {'width': width}
            if font:
                entry_args['font'] = font
            if state:
                entry_args['state'] = state
            if style:
                entry_args['style'] = style
            if values:
                entry_args['values'] = values.split(',')
            
            if textvariable:
                if textvariable not in globals():
                    globals()[textvariable] = tk.StringVar()
                entry_args['textvariable'] = globals()[textvariable]
            
            combobox = ttk.Combobox(root_widget, **entry_args)
            
            bind_events(combobox, child)
            
            command_name = None
            for sub_child in child:
                if sub_child.tag == 'SelectionChanged_Command':
                    command_name = sub_child.text
            
            if command_name and command_name in global_commands:
                def on_combobox_changed(event=None, cmd=command_name, widget=combobox):
                    global_commands[cmd](widget)
                combobox.bind('<<ComboboxSelected>>', on_combobox_changed)
            
            if x is not None and y is not None:
                place_args = {'x': x, 'y': y}
                if ipadx:
                    place_args['x'] -= ipadx
                if ipady:
                    place_args['y'] -= ipady
                combobox.place(**place_args)
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
                combobox.pack(**pack_args)
            
            if combobox_id:
                ttk_combobox_id_map[combobox_id] = combobox

        elif child.tag == 'ttk_treeview':
            tree_id = child.attrib.get('id')
            x = child.attrib.get('x')
            y = child.attrib.get('y')
            height = child.attrib.get('height', 10)
            width = child.attrib.get('width')
            show = child.attrib.get('show')
            selectmode = child.attrib.get('selectmode', 'browse')
            style = child.attrib.get('style')
            columns = child.attrib.get('columns', '')
            padx = child.attrib.get('padx')
            pady = child.attrib.get('pady')
            ipadx = child.attrib.get('ipadx')
            ipady = child.attrib.get('ipady')
            
            if height:
                height = int(height)
            if width:
                width = int(width)
            if x:
                x = int(x)
            if y:
                y = int(y)
            if padx:
                padx = int(padx)
            if pady:
                pady = int(pady)
            if ipadx:
                ipadx = int(ipadx)
            if ipady:
                ipady = int(ipady)
            
            tree_args = {}
            if height:
                tree_args['height'] = height
            if width:
                tree_args['width'] = width
            if show:
                tree_args['show'] = show
            if selectmode:
                tree_args['selectmode'] = selectmode
            if style:
                tree_args['style'] = style
            if columns:
                tree_args['columns'] = columns.split(',')
            
            tree = ttk.Treeview(root_widget, **tree_args)
            
            bind_events(tree, child)
            
            command_name = None
            for sub_child in child:
                if sub_child.tag == 'SelectionChanged_Command':
                    command_name = sub_child.text
                elif sub_child.tag == 'column':
                    col_id = sub_child.attrib.get('id')
                    col_text = sub_child.attrib.get('text', '')
                    col_width = sub_child.attrib.get('width')
                    col_anchor = sub_child.attrib.get('anchor')
                    if col_id:
                        if col_text:
                            tree.heading(col_id, text=col_text)
                        if col_width:
                            tree.column(col_id, width=int(col_width))
                        if col_anchor:
                            tree.column(col_id, anchor=col_anchor)
            
            if command_name and command_name in global_commands:
                def on_tree_select(event=None, cmd=command_name, widget=tree):
                    global_commands[cmd](widget)
                tree.bind('<<TreeviewSelect>>', on_tree_select)
            
            if x is not None and y is not None:
                place_args = {'x': x, 'y': y}
                if ipadx:
                    place_args['x'] -= ipadx
                if ipady:
                    place_args['y'] -= ipady
                tree.place(**place_args)
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
                tree.pack(**pack_args)
            
            if tree_id:
                ttk_treeview_id_map[tree_id] = tree

        elif child.tag == 'ttk_progressbar':
            progressbar_id = child.attrib.get('id')
            x = child.attrib.get('x')
            y = child.attrib.get('y')
            length = child.attrib.get('length', 200)
            mode = child.attrib.get('mode', 'determinate')
            maximum = child.attrib.get('maximum', 100)
            value = child.attrib.get('value', 0)
            style = child.attrib.get('style')
            orient = child.attrib.get('orient', 'horizontal')
            padx = child.attrib.get('padx')
            pady = child.attrib.get('pady')
            ipadx = child.attrib.get('ipadx')
            ipady = child.attrib.get('ipady')
            
            if length:
                length = int(length)
            if maximum:
                maximum = float(maximum)
            if value:
                value = float(value)
            if x:
                x = int(x)
            if y:
                y = int(y)
            if padx:
                padx = int(padx)
            if pady:
                pady = int(pady)
            if ipadx:
                ipadx = int(ipadx)
            if ipady:
                ipady = int(ipady)
            
            progressbar_args = {}
            if length:
                progressbar_args['length'] = length
            if mode:
                progressbar_args['mode'] = mode
            if maximum:
                progressbar_args['maximum'] = maximum
            if value:
                progressbar_args['value'] = value
            if style:
                progressbar_args['style'] = style
            if orient:
                progressbar_args['orient'] = orient
            
            progressbar = ttk.Progressbar(root_widget, **progressbar_args)
            
            bind_events(progressbar, child)
            
            if x is not None and y is not None:
                place_args = {'x': x, 'y': y}
                if ipadx:
                    place_args['x'] -= ipadx
                if ipady:
                    place_args['y'] -= ipady
                progressbar.place(**place_args)
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
                progressbar.pack(**pack_args)
            
            if progressbar_id:
                ttk_progressbar_id_map[progressbar_id] = progressbar

        elif child.tag == 'ttk_notebook':
            notebook_id = child.attrib.get('id')
            x = child.attrib.get('x')
            y = child.attrib.get('y')
            width = child.attrib.get('width')
            height = child.attrib.get('height')
            style = child.attrib.get('style')
            padx = child.attrib.get('padx')
            pady = child.attrib.get('pady')
            ipadx = child.attrib.get('ipadx')
            ipady = child.attrib.get('ipady')
            
            if width:
                width = int(width)
            if height:
                height = int(height)
            if x:
                x = int(x)
            if y:
                y = int(y)
            if padx:
                padx = int(padx)
            if pady:
                pady = int(pady)
            if ipadx:
                ipadx = int(ipadx)
            if ipady:
                ipady = int(ipady)
            
            notebook_args = {}
            if width:
                notebook_args['width'] = width
            if height:
                notebook_args['height'] = height
            if style:
                notebook_args['style'] = style
            
            notebook = ttk.Notebook(root_widget, **notebook_args)
            
            bind_events(notebook, child)
            
            for sub_child in child:
                if sub_child.tag == 'tab':
                    tab_text = sub_child.attrib.get('text', 'Tab')
                    tab_id = sub_child.attrib.get('id')
                    tab_frame = tk.Frame(notebook)
                    notebook.add(tab_frame, text=tab_text)
                    if tab_id:
                        notebook_tab_id_map[tab_id] = tab_frame
                    create_widgets_from_xml(tab_frame, sub_child)
            
            if x is not None and y is not None:
                place_args = {'x': x, 'y': y}
                if ipadx:
                    place_args['x'] -= ipadx
                if ipady:
                    place_args['y'] -= ipady
                notebook.place(**place_args)
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
                notebook.pack(**pack_args)
            
            if notebook_id:
                ttk_notebook_id_map[notebook_id] = notebook

        elif child.tag == 'ttk_separator':
            separator_id = child.attrib.get('id')
            x = child.attrib.get('x')
            y = child.attrib.get('y')
            orient = child.attrib.get('orient', 'horizontal')
            style = child.attrib.get('style')
            padx = child.attrib.get('padx')
            pady = child.attrib.get('pady')
            ipadx = child.attrib.get('ipadx')
            ipady = child.attrib.get('ipady')
            
            if x:
                x = int(x)
            if y:
                y = int(y)
            if padx:
                padx = int(padx)
            if pady:
                pady = int(pady)
            if ipadx:
                ipadx = int(ipadx)
            if ipady:
                ipady = int(ipady)
            
            separator_args = {}
            if orient:
                separator_args['orient'] = orient
            if style:
                separator_args['style'] = style
            
            separator = ttk.Separator(root_widget, **separator_args)
            
            bind_events(separator, child)
            
            if x is not None and y is not None:
                place_args = {'x': x, 'y': y}
                if ipadx:
                    place_args['x'] -= ipadx
                if ipady:
                    place_args['y'] -= ipady
                separator.place(**place_args)
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
                separator.pack(**pack_args)
            
            if separator_id:
                ttk_separator_id_map[separator_id] = separator

        elif child.tag == 'ttk_scale':
            from_ = int(child.attrib.get('from', 0))
            to = int(child.attrib.get('to', 100))
            orient = child.attrib.get('orient', 'horizontal')
            length = int(child.attrib.get('length', 100))
            x = child.attrib.get('x')
            y = child.attrib.get('y')
            scale_id = child.attrib.get('id')
            state = child.attrib.get('state')
            style = child.attrib.get('style')
            command = child.attrib.get('command')
            variable = child.attrib.get('variable')
            padx = child.attrib.get('padx')
            pady = child.attrib.get('pady')
            ipadx = child.attrib.get('ipadx')
            ipady = child.attrib.get('ipady')
            
            scale_args = {
                'from_': from_,
                'to': to,
                'orient': orient,
                'length': length
            }
            
            if state:
                scale_args['state'] = state
            if style:
                scale_args['style'] = style
            if variable:
                if variable not in globals():
                    globals()[variable] = tk.DoubleVar()
                scale_args['variable'] = globals()[variable]
            
            scale = ttk.Scale(root_widget, **scale_args)
            
            bind_events(scale, child)
            
            command_name = None
            for sub_child in child:
                if sub_child.tag == 'Valuechanged_Command':
                    command_name = sub_child.text
            
            if command_name and command_name in global_commands:
                scale.config(command=lambda *args, btn=scale, cmd=command_name: global_commands[cmd](btn))
            
            if x is not None and y is not None:
                x = int(x)
                y = int(y)
                place_args = {'x': x, 'y': y}
                if ipadx:
                    place_args['x'] -= ipadx
                if ipady:
                    place_args['y'] -= ipady
                scale.place(**place_args)
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
                scale.pack(**pack_args)
            
            if scale_id:
                ttk_scale_id_map[scale_id] = scale

        elif child.tag == 'ttk_checkbutton':
            text = child.attrib.get('text', 'Checkbutton')
            command = None
            width = child.attrib.get('width')
            button_id = child.attrib.get('id')
            x = child.attrib.get('x')
            y = child.attrib.get('y')
            style = child.attrib.get('style')
            state = child.attrib.get('state')
            variable = child.attrib.get('variable')
            onvalue = child.attrib.get('onvalue', 1)
            offvalue = child.attrib.get('offvalue', 0)
            padx = child.attrib.get('padx')
            pady = child.attrib.get('pady')
            ipadx = child.attrib.get('ipadx')
            ipady = child.attrib.get('ipady')
            
            if width:
                width = int(width)
            if x:
                x = int(x)
            if y:
                y = int(y)
            if padx:
                padx = int(padx)
            if pady:
                pady = int(pady)
            if ipadx:
                ipadx = int(ipadx)
            if ipady:
                ipady = int(ipady)
            if onvalue:
                onvalue = int(onvalue)
            if offvalue:
                offvalue = int(offvalue)
            
            checkbutton_args = {'text': text}
            if width:
                checkbutton_args['width'] = width
            if style:
                checkbutton_args['style'] = style
            if state:
                checkbutton_args['state'] = state
            
            if variable:
                if variable not in globals():
                    globals()[variable] = tk.IntVar()
                checkbutton_args['variable'] = globals()[variable]
            else:
                if 'temp_var' not in globals():
                    globals()['temp_var'] = tk.IntVar()
                checkbutton_args['variable'] = globals()['temp_var']
            
            checkbutton_args['onvalue'] = onvalue
            checkbutton_args['offvalue'] = offvalue
            
            checkbutton = ttk.Checkbutton(root_widget, **checkbutton_args)
            
            bind_events(checkbutton, child)
            
            command_name = None
            for sub_child in child:
                if sub_child.tag == 'Click_command':
                    command_name = sub_child.text
            
            if command_name and command_name in global_commands:
                command = lambda btn=checkbutton, cmd=command_name: global_commands[cmd](btn)
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
                ttk_checkbutton_id_map[button_id] = checkbutton

        elif child.tag == 'ttk_radiobutton':
            text = child.attrib.get('text', 'Radiobutton')
            command = None
            width = child.attrib.get('width')
            button_id = child.attrib.get('id')
            x = child.attrib.get('x')
            y = child.attrib.get('y')
            style = child.attrib.get('style')
            state = child.attrib.get('state')
            variable = child.attrib.get('variable')
            value = child.attrib.get('value')
            padx = child.attrib.get('padx')
            pady = child.attrib.get('pady')
            ipadx = child.attrib.get('ipadx')
            ipady = child.attrib.get('ipady')
            
            if width:
                width = int(width)
            if x:
                x = int(x)
            if y:
                y = int(y)
            if padx:
                padx = int(padx)
            if pady:
                pady = int(pady)
            if ipadx:
                ipadx = int(ipadx)
            if ipady:
                ipady = int(ipady)
            
            radio_args = {'text': text}
            if width:
                radio_args['width'] = width
            if style:
                radio_args['style'] = style
            if state:
                radio_args['state'] = state
            
            if variable:
                if variable not in globals():
                    globals()[variable] = tk.StringVar()
                radio_args['variable'] = globals()[variable]
            else:
                if 'temp_radio_var' not in globals():
                    globals()['temp_radio_var'] = tk.StringVar()
                radio_args['variable'] = globals()['temp_radio_var']
            
            if value:
                radio_args['value'] = value
            
            radio = ttk.Radiobutton(root_widget, **radio_args)
            
            bind_events(radio, child)
            
            command_name = None
            for sub_child in child:
                if sub_child.tag == 'Click_command':
                    command_name = sub_child.text
            
            if command_name and command_name in global_commands:
                command = lambda btn=radio, cmd=command_name: global_commands[cmd](btn)
                radio.config(command=command)
            
            if x is not None and y is not None:
                place_args = {'x': x, 'y': y}
                if ipadx:
                    place_args['x'] -= ipadx
                if ipady:
                    place_args['y'] -= ipady
                radio.place(**place_args)
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
                radio.pack(**pack_args)
            
            if button_id:
                ttk_radiobutton_id_map[button_id] = radio

def bind_events(widget, child):
    for sub_child in child:
        event_name = sub_child.tag
        command_name = sub_child.text
        if command_name and command_name in global_commands:
            event_map = {
                'Enter_command': '<Enter>',
                'Leave_command': '<Leave>',
                'FocusIn_command': '<FocusIn>',
                'FocusOut_command': '<FocusOut>',
                'KeyPress_command': '<KeyPress>',
                'KeyRelease_command': '<KeyRelease>',
                'ButtonPress_command': '<ButtonPress>',
                'ButtonRelease_command': '<ButtonRelease>',
                'Motion_command': '<Motion>',
                'Configure_command': '<Configure>',
                'Map_command': '<Map>',
                'Unmap_command': '<Unmap>',
                'Expose_command': '<Expose>',
                'Destroy_command': '<Destroy>'
            }
            if event_name in event_map:
                widget.bind(event_map[event_name], lambda e, cmd=command_name: global_commands[cmd](widget, e))

def setup_window_properties(root, window_node):
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

def XmlInit_Path(xmlpath,globals):
    global global_commands
    global root
    global_commands = globals
    try:
        with open(xmlpath, 'r', encoding='utf-8') as file:
            xml_data = file.read()
    except FileNotFoundError:
        print(f"XML path error")
        return
    try:
        xml_root = ET.fromstring(xml_data)
        
        if xml_root.tag == 'window':
            window_node = xml_root
            root = tk.Tk()
            setup_window_properties(root, window_node)
            create_widgets_from_xml(root, xml_root)
        elif xml_root.tag == 'root':
            window_node = xml_root.find('window')
            if window_node is not None:
                root = tk.Tk()
                setup_window_properties(root, window_node)
            else:
                root = tk.Tk()
            create_widgets_from_xml(root, xml_root)
        else:
            root = tk.Tk()
            create_widgets_from_xml(root, xml_root)
    except ET.ParseError as e:
        print(f"XML parsing error: {e}")
        root = tk.Tk()
    root.mainloop()

def XmlInit_string(xml_data,globals):
    global global_commands
    global root
    global_commands = globals
    try:
        xml_root = ET.fromstring(xml_data)
        
        if xml_root.tag == 'window':
            window_node = xml_root
            root = tk.Tk()
            setup_window_properties(root, window_node)
            create_widgets_from_xml(root, xml_root)
        elif xml_root.tag == 'root':
            window_node = xml_root.find('window')
            if window_node is not None:
                root = tk.Tk()
                setup_window_properties(root, window_node)
            else:
                root = tk.Tk()
            create_widgets_from_xml(root, xml_root)
        else:
            root = tk.Tk()
            create_widgets_from_xml(root, xml_root)
    except ET.ParseError as e:
        print(f"XML parsing error: {e}")
        root = tk.Tk()

    root.mainloop()
