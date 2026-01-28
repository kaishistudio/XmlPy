# XmlPy User Manual

> 📘 Complete Guide to XmlPy Framework

---

## 📖 Table of Contents

1. [Introduction](#1-introduction)
2. [Installation and Setup](#2-installation-and-setup)
3. [Quick Start](#3-quick-start)
4. [XML Syntax Guide](#4-xml-syntax-guide)
5. [Widget Reference](#5-widget-reference)
6. [Event Handling](#6-event-handling)
7. [Advanced Features](#7-advanced-features)
8. [Practical Examples](#8-practical-examples)
9. [Best Practices](#9-best-practices)
10. [Troubleshooting](#10-troubleshooting)
11. [API Reference](#11-api-reference)
12. [FAQ](#12-faq)

---

## 1. Introduction

### 1.1 What is XmlPy?

XmlPy is an XML-based Python GUI framework that allows developers to define graphical user interfaces using XML, without writing extensive Tkinter code.

### 1.2 Core Features

- ✅ **XML-Driven** - Define interfaces with XML for cleaner code
- ✅ **Rich Widgets** - Support for buttons, labels, entries, and more
- ✅ **Easy Maintenance** - Separate interface from logic for easy modifications
- ✅ **Rapid Development** - Reduce repetitive code and improve efficiency
- ✅ **Flexible Layout** - Support for absolute positioning and nested layouts
- ✅ **Event Binding** - Simple event handling mechanism

### 1.3 Use Cases

- 🎯 Desktop application development
- 📊 Data visualization tools
- 🧮 Calculators and utilities
- 🎮 Simple game interfaces
- 📝 Forms and data entry applications

---

## 2. Installation and Setup

### 2.1 System Requirements

- Python 3.6 or higher
- Tkinter (usually installed with Python)
- Operating Systems: Windows, macOS, Linux

### 2.2 Installation Steps

#### Step 1: Get the Code

```bash
git clone https://github.com/your-username/xml-py.git
cd xml-py/Code
```

#### Step 2: Verify Installation

```python
# Test import
from XmlPy import *
print("XmlPy imported successfully!")
```

### 2.3 Directory Structure

```
xml-py/
├── Code/
│   ├── XmlPy.py          # Framework core file
│   ├── README.md         # Project documentation
│   ├── USER_MANUAL_EN.md # English user manual (this file)
│   └── examples/        # Example code
│       ├── hello_world.py
│       ├── calculator.py
│       └── ...
```

---

## 3. Quick Start

### 3.1 First Program: Hello World

#### Python Code

```python
from XmlPy import *

def say_hello(widget=None):
    print("Hello, XmlPy!")

global_commands = {
    'say_hello': say_hello
}

xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<window title="Hello World" geometry="400x300" bg="#2c3e50">
    <label id="greeting" text="Hello, XmlPy!"
           x="150" y="100" fg="white" bg="#2c3e50"/>
    <button id="btn_click" text="Click Me"
            x="150" y="150" width="10" height="2"
            bg="#3498db" fg="white">
        <Click_command>say_hello</Click_command>
    </button>
</window>
"""

XmlInit_string(xml_content, global_commands)
```

#### Running the Program

After running the program, a window will appear containing a label and a button. Clicking the button will output "Hello, XmlPy!" to the console.

### 3.2 Loading XML from File

#### Create XML File (hello.xml)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<window title="Hello World" geometry="400x300" bg="#2c3e50">
    <label id="greeting" text="Hello, XmlPy!"
           x="150" y="100" fg="white" bg="#2c3e50"/>
    <button id="btn_click" text="Click Me"
            x="150" y="150" width="10" height="2"
            bg="#3498db" fg="white">
        <Click_command>say_hello</Click_command>
    </button>
</window>
```

#### Python Code

```python
from XmlPy import *

def say_hello(widget=None):
    print("Hello, XmlPy!")

global_commands = {
    'say_hello': say_hello
}

XmlInit_Path('hello.xml', global_commands)
```

---

## 4. XML Syntax Guide

### 4.1 XML Structure

#### Format 1: Window as Root Element (Recommended)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<window title="My App" geometry="800x600" bg="#2c3e50">
    <!-- Widget definitions -->
</window>
```

#### Format 2: Root Wrapping Window (Legacy Compatible)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<root>
    <window title="My App" geometry="800x600" bg="#2c3e50"/>
    <!-- Widget definitions -->
</root>
```

### 4.2 Window Properties

| Attribute | Type | Required | Description | Example |
|-----------|-------|-----------|-------------|---------|
| title | string | No | Window title | `title="My App"` |
| geometry | string | No | Window size | `geometry="800x600"` |
| bg | color | No | Background color | `bg="#2c3e50"` |
| minsize | string | No | Minimum size | `minsize="400x300"` |
| maxsize | string | No | Maximum size | `maxsize="1200x900"` |
| resizable | boolean | No | Resizable | `resizable="true,true"` |
| iconbitmap | path | No | Window icon | `iconbitmap="icon.ico"` |

### 4.3 Common Attributes

All widgets support the following attributes:

| Attribute | Description | Example |
|-----------|-------------|---------|
| id | Unique widget identifier | `id="btn1"` |
| x | X coordinate | `x="10"` |
| y | Y coordinate | `y="20"` |
| bg | Background color | `bg="#3498db"` |
| fg | Foreground color (text color) | `fg="white"` |
| font | Font settings | `font="Arial 12"` |
| width | Width | `width="10"` |
| height | Height | `height="2"` |

### 4.4 Color Formats

#### Hexadecimal Colors

```xml
<button bg="#3498db" fg="white"/>
```

#### Color Names

```xml
<button bg="blue" fg="white"/>
```

#### Common Color Reference

| Color | Hex Code | Usage |
|-------|-----------|-------|
| Red | #e74c3c | Errors, Delete |
| Blue | #3498db | Primary actions |
| Green | #27ae60 | Success, Confirm |
| Yellow | #f39c12 | Warnings |
| Purple | #9b59b6 | Special features |
| Gray | #95a5a6 | Secondary actions |
| Dark | #2c3e50 | Backgrounds |
| Darker | #34495e | Panels |
| Light | #ecf0f1 | Light backgrounds |

---

## 5. Widget Reference

### 5.1 Button

#### Basic Usage

```xml
<button id="btn1" text="Click Me"
        x="10" y="10" width="10" height="2"
        bg="#3498db" fg="white">
    <Click_command>my_function</Click_command>
</button>
```

#### Complete Attributes

| Attribute | Description | Default |
|-----------|-------------|----------|
| text | Button text | "Button" |
| width | Width | 10 |
| height | Height | 1 |
| bg | Background color | System default |
| fg | Text color | System default |
| font | Font | System default |
| relief | Border style | "raised" |
| cursor | Mouse cursor | System default |
| state | State | "normal" |

#### Events

```xml
<button id="btn1" text="Event Test">
    <Click_command>on_click</Click_command>
    <Double_Click_command>on_double_click</Double_Click_command>
    <Right_Click_command>on_right_click</Right_Click_command>
</button>
```

#### Python Code

```python
def on_click(widget=None):
    print("Single click event")

def on_double_click(widget=None):
    print("Double click event")

def on_right_click(widget=None):
    print("Right click event")

global_commands = {
    'on_click': on_click,
    'on_double_click': on_double_click,
    'on_right_click': on_right_click
}
```

### 5.2 Label

#### Basic Usage

```xml
<label id="label1" text="This is a label"
       x="10" y="50" fg="white" bg="#2c3e50"/>
```

#### Complete Attributes

| Attribute | Description | Default |
|-----------|-------------|----------|
| text | Label text | "Label" |
| width | Width | Auto |
| height | Height | Auto |
| bg | Background color | System default |
| fg | Text color | System default |
| font | Font | System default |
| justify | Alignment | "left" |
| relief | Border style | "flat" |

#### Alignment Options

```xml
<!-- Left align -->
<label justify="left" text="Left aligned"/>

<!-- Center align -->
<label justify="center" text="Center aligned"/>

<!-- Right align -->
<label justify="right" text="Right aligned"/>
```

### 5.3 Entry (Text Input)

#### Basic Usage

```xml
<entry id="entry1" width="30"
        fg="white" bg="#1a252f"
        justify="right" x="10" y="100"/>
```

#### Complete Attributes

| Attribute | Description | Default |
|-----------|-------------|----------|
| width | Width (characters) | 20 |
| fg | Text color | System default |
| bg | Background color | System default |
| font | Font | System default |
| justify | Alignment | "left" |
| show | Display character | "" (show actual) |
| state | State | "normal" |
| bd | Border width | System default |

#### Password Entry

```xml
<entry id="password" width="30"
        show="*" x="10" y="100"/>
```

#### Read-Only Entry

```xml
<entry id="readonly" width="30"
        state="readonly" x="10" y="100"/>
```

#### Python Operations

```python
# Get input content
entry = entry_id_map.get('entry1')
if entry:
    content = entry.get()
    print(f"Input content: {content}")

# Set input content
entry = entry_id_map.get('entry1')
if entry:
    entry.delete(0, tk.END)
    entry.insert(0, "Default value")

# Clear entry
entry = entry_id_map.get('entry1')
if entry:
    entry.delete(0, tk.END)
```

### 5.4 Frame (Container)

#### Basic Usage

```xml
<frame id="frame1" bg="#34495e"
        x="10" y="150" width="200" height="100">
    <!-- Child widgets -->
    <label id="inner_label" text="Label inside frame"
           x="10" y="10" fg="white"/>
</frame>
```

#### Complete Attributes

| Attribute | Description | Default |
|-----------|-------------|----------|
| bg | Background color | System default |
| width | Width | Auto |
| height | Height | Auto |
| relief | Border style | "flat" |
| bd | Border width | 0 |

#### Border Styles

```xml
<!-- Flat border -->
<frame relief="flat"/>

<!-- Raised border -->
<frame relief="raised"/>

<!-- Sunken border -->
<frame relief="sunken"/>

<!-- Groove border -->
<frame relief="groove"/>

<!-- Ridge border -->
<frame relief="ridge"/>
```

### 5.5 Canvas (Drawing Area)

#### Basic Usage

```xml
<canvas id="canvas1" bg="white"
         x="10" y="270" width="200" height="150"/>
```

#### Python Drawing

```python
# Get canvas
canvas = canvas_id_map.get('canvas1')
if canvas:
    # Draw rectangle
    canvas.create_rectangle(10, 10, 100, 100, fill="red")

    # Draw circle
    canvas.create_oval(120, 10, 180, 70, fill="blue")

    # Draw line
    canvas.create_line(10, 120, 180, 120, fill="green", width=3)

    # Draw text
    canvas.create_text(100, 140, text="Hello Canvas", fill="black")
```

### 5.6 Checkbutton (Checkbox)

#### Basic Usage

```xml
<checkbutton id="cb1" text="Enable feature"
             x="10" y="440" bg="#34495e" fg="white">
    <Click_command>toggle_check</Click_command>
</checkbutton>
```

#### Python Operations

```python
# Get checkbox state
cb = checkbutton_id_map.get('cb1')
if cb:
    var = checkbutton_vars.get('cb1')
    if var:
        is_checked = var.get()
        print(f"Checkbox state: {is_checked}")

# Set checkbox state
cb = checkbutton_id_map.get('cb1')
if cb:
    var = checkbutton_vars.get('cb1')
    if var:
        var.set(True)  # Checked
        var.set(False)  # Unchecked
```

### 5.7 Radiobutton (Radio Button)

#### Basic Usage

```xml
<radiobutton id="rb1" text="Option 1"
             x="10" y="480" bg="#34495e" fg="white">
    <Click_command>select_option1</Click_command>
</radiobutton>
<radiobutton id="rb2" text="Option 2"
             x="10" y="510" bg="#34495e" fg="white">
    <Click_command>select_option2</Click_command>
</radiobutton>
```

#### Python Operations

```python
# Get radio button state
rb = radio_id_map.get('rb1')
if rb:
    var = radio_vars.get('rb1')
    if var:
        selected_value = var.get()
        print(f"Selected value: {selected_value}")
```

### 5.8 Text (Text Area)

#### Basic Usage

```xml
<text id="text1" width="30" height="10"
      bg="white" fg="black" x="10" y="550"/>
```

#### Python Operations

```python
# Get text widget
text_widget = text_id_map.get('text1')
if text_widget:
    # Get content
    content = text_widget.get("1.0", tk.END)
    print(f"Text content: {content}")

    # Set content
    text_widget.delete("1.0", tk.END)
    text_widget.insert("1.0", "New content")

    # Append content
    text_widget.insert(tk.END, "\nAppended content")
```

### 5.9 Scale (Slider)

#### Basic Usage

```xml
<scale id="scale1" from_="0" to="100"
       orient="horizontal" x="10" y="650" width="200"/>
```

#### Complete Attributes

| Attribute | Description | Default |
|-----------|-------------|----------|
| from_ | Minimum value | 0 |
| to | Maximum value | 100 |
| orient | Orientation | "horizontal" |
| length | Length | Auto |
| resolution | Step size | 1 |

#### Python Operations

```python
# Get scale value
scale = scale_id_map.get('scale1')
if scale:
    value = scale.get()
    print(f"Scale value: {value}")

# Set scale value
scale = scale_id_map.get('scale1')
if scale:
    scale.set(50)
```

### 5.10 Listbox (List)

#### Basic Usage

```xml
<listbox id="list1" width="30" height="5"
         bg="white" fg="black" x="10" y="700"/>
```

#### Python Operations

```python
# Get listbox
listbox = listbox_id_map.get('list1')
if listbox:
    # Add items
    listbox.insert(tk.END, "Item 1")
    listbox.insert(tk.END, "Item 2")
    listbox.insert(tk.END, "Item 3")

    # Get selected item
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        value = listbox.get(index)
        print(f"Selected item: {value}")

    # Delete items
    listbox.delete(0, tk.END)  # Clear all

    # Get all items
    all_items = listbox.get(0, tk.END)
    print(f"All items: {all_items}")
```

### 5.11 Menu

#### Basic Usage

```xml
<menu id="menu1">
    <item id="item_file" text="File">
        <Click_command>file_menu</Click_command>
    </item>
    <item id="item_edit" text="Edit">
        <Click_command>edit_menu</Click_command>
    </item>
    <item id="item_help" text="Help">
        <Click_command>help_menu</Click_command>
    </item>
</menu>
```

#### Python Code

```python
def file_menu(widget=None):
    print("File menu")

def edit_menu(widget=None):
    print("Edit menu")

def help_menu(widget=None):
    print("Help menu")

global_commands = {
    'file_menu': file_menu,
    'edit_menu': edit_menu,
    'help_menu': help_menu
}
```

---

## 6. Event Handling

### 6.1 Event Types

| Event | XML Tag | Description |
|-------|----------|-------------|
| Click | `<Click_command>` | Left mouse button click |
| Double Click | `<Double_Click_command>` | Left mouse button double click |
| Right Click | `<Right_Click_command>` | Right mouse button click |
| Text Changed | `<Textchanged_Command>` | Text content changed |

### 6.2 Event Handler Functions

#### Basic Format

```python
def event_handler(widget=None):
    """
    Event handler function

    Args:
        widget: The widget that triggered the event
    """
    print("Event triggered")
```

#### Getting Widget Information

```python
def on_button_click(widget=None):
    if widget:
        print(f"Widget ID: {widget}")
        print(f"Widget type: {type(widget)}")

        # Get button text
        if hasattr(widget, 'cget'):
            text = widget.cget('text')
            print(f"Button text: {text}")
```

### 6.3 Global Command Mapping

```python
# Define event handler functions
def function1(widget=None):
    print("Function 1 called")

def function2(widget=None):
    print("Function 2 called")

# Create global command mapping
global_commands = {
    'function1': function1,
    'function2': function2,
    'on_click': lambda w: print("Anonymous function"),
    'append_digit': lambda w, digit: print(f"Digit entered: {digit}")
}
```

### 6.4 Widget ID Mapping

XmlPy provides several global dictionaries to access widgets:

```python
# Button mapping
button = button_id_map.get('btn_id')

# Label mapping
label = label_id_map.get('label_id')

# Entry mapping
entry = entry_id_map.get('entry_id')

# Text mapping
text = text_id_map.get('text_id')

# Canvas mapping
canvas = canvas_id_map.get('canvas_id')

# Listbox mapping
listbox = listbox_id_map.get('list_id')

# Scale mapping
scale = scale_id_map.get('scale_id')

# Checkbutton mapping
checkbutton = checkbutton_id_map.get('cb_id')

# Radiobutton mapping
radiobutton = radio_id_map.get('rb_id')
```

---

## 7. Advanced Features

### 7.1 Nested Layouts

```xml
<window title="Nested Layout Example" geometry="800x600">
    <frame id="main_frame" bg="#2c3e50" x="10" y="10" width="780" height="580">
        <frame id="header_frame" bg="#34495e" x="10" y="10" width="760" height="80">
            <label id="title" text="Title" x="350" y="30" fg="white"/>
        </frame>

        <frame id="content_frame" bg="#34495e" x="10" y="100" width="760" height="400">
            <button id="btn1" text="Button 1" x="10" y="10" width="10" height="2">
                <Click_command>action1</Click_command>
            </button>
            <button id="btn2" text="Button 2" x="120" y="10" width="10" height="2">
                <Click_command>action2</Click_command>
            </button>
        </frame>

        <frame id="footer_frame" bg="#34495e" x="10" y="510" width="760" height="60">
            <label id="status" text="Ready" x="350" y="20" fg="white"/>
        </frame>
    </frame>
</window>
```

### 7.2 Dynamic Widget Updates

```python
from XmlPy import *
import time

def update_label(widget=None):
    label = label_id_map.get('status_label')
    if label:
        for i in range(5):
            label.config(text=f"Processing... {i+1}/5")
            root.update()
            time.sleep(1)
        label.config(text="Completed!")

global_commands = {
    'update_label': update_label
}
```

### 7.3 Data Binding

```xml
<entry id="entry1" width="30" x="10" y="10">
    <Textchanged_Command>on_text_change</Textchanged_Command>
</entry>
<label id="preview" text="Preview: " x="10" y="50"/>
```

```python
def on_text_change(widget=None):
    entry = entry_id_map.get('entry1')
    label = label_id_map.get('preview')
    if entry and label:
        content = entry.get()
        label.config(text=f"Preview: {content}")

global_commands = {
    'on_text_change': on_text_change
}
```

### 7.4 Style Themes

#### Create Theme File (theme.xml)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<window title="Theme Example" geometry="800x600" bg="#2c3e50">
    <frame id="main_frame" bg="#34495e" x="10" y="10" width="780" height="580">
        <button id="btn1" text="Primary Button" x="10" y="10" width="12" height="2"
                bg="#3498db" fg="white">
            <Click_command>action1</Click_command>
        </button>
        <button id="btn2" text="Secondary Button" x="150" y="10" width="12" height="2"
                bg="#95a5a6" fg="white">
            <Click_command>action2</Click_command>
        </button>
        <button id="btn3" text="Success Button" x="290" y="10" width="12" height="2"
                bg="#27ae60" fg="white">
            <Click_command>action3</Click_command>
        </button>
        <button id="btn4" text="Warning Button" x="430" y="10" width="12" height="2"
                bg="#f39c12" fg="white">
            <Click_command>action4</Click_command>
        </button>
        <button id="btn5" text="Danger Button" x="570" y="10" width="12" height="2"
                bg="#e74c3c" fg="white">
            <Click_command>action5</Click_command>
        </button>
    </frame>
</window>
```

---

## 8. Practical Examples

### 8.1 Login Form

#### XML File (login.xml)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<window title="Login" geometry="400x300" bg="#2c3e50">
    <frame id="login_frame" bg="#34495e" x="50" y="50" width="300" height="200">
        <label id="username_label" text="Username:"
               x="20" y="20" fg="white" bg="#34495e"/>
        <entry id="username" width="25"
                x="100" y="20" bg="#1a252f" fg="white"/>

        <label id="password_label" text="Password:"
               x="20" y="60" fg="white" bg="#34495e"/>
        <entry id="password" width="25" show="*"
                x="100" y="60" bg="#1a252f" fg="white"/>

        <button id="btn_login" text="Login"
                x="50" y="120" width="10" height="2"
                bg="#3498db" fg="white">
            <Click_command>login</Click_command>
        </button>
        <button id="btn_cancel" text="Cancel"
                x="170" y="120" width="10" height="2"
                bg="#e74c3c" fg="white">
            <Click_command>cancel</Click_command>
        </button>
    </frame>
</window>
```

#### Python Code

```python
from XmlPy import *
import tkinter.messagebox as messagebox

def login(widget=None):
    username_entry = entry_id_map.get('username')
    password_entry = entry_id_map.get('password')

    if username_entry and password_entry:
        username = username_entry.get()
        password = password_entry.get()

        if username and password:
            messagebox.showinfo("Login", f"Welcome, {username}!")
        else:
            messagebox.showwarning("Warning", "Please enter username and password")

def cancel(widget=None):
    username_entry = entry_id_map.get('username')
    password_entry = entry_id_map.get('password')

    if username_entry:
        username_entry.delete(0, tk.END)
    if password_entry:
        password_entry.delete(0, tk.END)

global_commands = {
    'login': login,
    'cancel': cancel
}

XmlInit_Path('login.xml', global_commands)
```

### 8.2 Todo List

#### XML File (todo.xml)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<window title="Todo List" geometry="500x400" bg="#2c3e50">
    <frame id="main_frame" bg="#34495e" x="10" y="10" width="480" height="380">
        <entry id="new_task" width="40"
                x="10" y="10" bg="#1a252f" fg="white"/>
        <button id="btn_add" text="Add"
                x="350" y="10" width="8" height="2"
                bg="#27ae60" fg="white">
            <Click_command>add_task</Click_command>
        </button>

        <listbox id="task_list" width="55" height="15"
                 bg="white" fg="black" x="10" y="50"/>

        <button id="btn_complete" text="Complete"
                x="10" y="320" width="8" height="2"
                bg="#3498db" fg="white">
            <Click_command>complete_task</Click_command>
        </button>
        <button id="btn_delete" text="Delete"
                x="100" y="320" width="8" height="2"
                bg="#e74c3c" fg="white">
            <Click_command>delete_task</Click_command>
        </button>
    </frame>
</window>
```

#### Python Code

```python
from XmlPy import *
import tkinter.messagebox as messagebox

def add_task(widget=None):
    entry = entry_id_map.get('new_task')
    listbox = listbox_id_map.get('task_list')

    if entry and listbox:
        task = entry.get()
        if task:
            listbox.insert(tk.END, task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter task content")

def complete_task(widget=None):
    listbox = listbox_id_map.get('task_list')
    if listbox:
        selection = listbox.curselection()
        if selection:
            index = selection[0]
            task = listbox.get(index)
            listbox.delete(index)
            listbox.insert(index, f"✓ {task}")
        else:
            messagebox.showwarning("Warning", "Please select a task to complete")

def delete_task(widget=None):
    listbox = listbox_id_map.get('task_list')
    if listbox:
        selection = listbox.curselection()
        if selection:
            index = selection[0]
            listbox.delete(index)
        else:
            messagebox.showwarning("Warning", "Please select a task to delete")

global_commands = {
    'add_task': add_task,
    'complete_task': complete_task,
    'delete_task': delete_task
}

XmlInit_Path('todo.xml', global_commands)
```

---

## 9. Best Practices

### 9.1 Naming Conventions

#### Widget ID Naming

```xml
<!-- Good naming -->
<button id="btn_submit"/>
<entry id="username_input"/>
<label id="error_message"/>

<!-- Bad naming -->
<button id="b1"/>
<entry id="input1"/>
<label id="msg"/>
```

#### Function Naming

```python
# Good naming
def submit_form(widget=None):
    pass

def validate_input(widget=None):
    pass

# Bad naming
def func1(widget=None):
    pass

def do_it(widget=None):
    pass
```

### 9.2 Code Organization

#### Separate Logic and Interface

```python
# calculator.py - Business logic
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

# calculator_gui.py - Interface code
from calculator import Calculator
from XmlPy import *

calc = Calculator()

def on_add(widget=None):
    # Call business logic
    result = calc.add(1, 2)
    print(result)

global_commands = {
    'on_add': on_add
}

XmlInit_Path('calculator.xml', global_commands)
```

### 9.3 Error Handling

```python
def safe_operation(widget=None):
    try:
        entry = entry_id_map.get('user_input')
        if entry:
            value = float(entry.get())
            result = perform_calculation(value)
            display_result(result)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
```

### 9.4 Performance Optimization

```python
# Avoid frequent updates
def batch_update(widget=None):
    label = label_id_map.get('status')
    if label:
        # Update all content at once
        label.config(text="Processing completed")
        root.update()
```

---

## 10. Troubleshooting

### 10.1 Common Issues

#### Issue 1: Widget Not Displayed

**Cause**: Incorrect coordinates or size settings

**Solution**:
```xml
<!-- Check coordinates and size -->
<button id="btn1" text="Button"
        x="10" y="10" width="10" height="2"/>
```

#### Issue 2: Events Not Triggering

**Cause**: Command name mismatch

**Solution**:
```xml
<!-- Command name in XML -->
<button>
    <Click_command>my_function</Click_command>
</button>
```

```python
# Function name in Python must match
global_commands = {
    'my_function': my_function  # Names must match
}
```

#### Issue 3: Widget Access Failed

**Cause**: Incorrect widget ID or widget not created

**Solution**:
```python
# Check if widget exists
button = button_id_map.get('btn1')
if button:
    button.config(text="New text")
else:
    print("Widget does not exist")
```

### 10.2 Debugging Tips

#### Print Widget Information

```python
def debug_info(widget=None):
    print(f"Widget type: {type(widget)}")
    print(f"Widget properties: {widget.config()}")
```

#### Check Mapping Dictionaries

```python
# Print all buttons
print("All buttons:", button_id_map.keys())

# Print all labels
print("All labels:", label_id_map.keys())
```

---

## 11. API Reference

### 11.1 Core Functions

#### XmlInit_string()

```python
XmlInit_string(xml_data, global_commands)
```

**Parameters**:
- `xml_data` (str): XML string
- `global_commands` (dict): Global command mapping

**Example**:
```python
xml_content = """<window title="App">...</window>"""
global_commands = {'func': my_func}
XmlInit_string(xml_content, global_commands)
```

#### XmlInit_Path()

```python
XmlInit_Path(xmlpath, global_commands)
```

**Parameters**:
- `xmlpath` (str): XML file path
- `global_commands` (dict): Global command mapping

**Example**:
```python
global_commands = {'func': my_func}
XmlInit_Path('app.xml', global_commands)
```

### 11.2 Global Mappings

#### Widget Mapping Dictionaries

```python
button_id_map = {}      # Button mapping
label_id_map = {}       # Label mapping
entry_id_map = {}       # Entry mapping
text_id_map = {}        # Text mapping
canvas_id_map = {}      # Canvas mapping
listbox_id_map = {}    # Listbox mapping
scale_id_map = {}       # Scale mapping
checkbutton_id_map = {} # Checkbutton mapping
radio_id_map = {}      # Radiobutton mapping
checkbutton_vars = {}   # Checkbutton variables
radio_vars = {}        # Radiobutton variables
```

### 11.3 Tkinter Integration

#### Access Root Window

```python
from XmlPy import root

# Set window properties
root.title("New Title")
root.geometry("800x600")

# Close window
root.destroy()
```

---

## 12. FAQ

### Q1: Which Python versions does XmlPy support?

**A**: XmlPy supports Python 3.6 and higher.

### Q2: How do I create custom widgets?

**A**: You can create custom widgets by inheriting from Tkinter widgets and using the place() method for positioning in Python code.

### Q3: Does XmlPy support responsive layouts?

**A**: Currently, XmlPy mainly supports absolute positioning. Responsive layouts can be achieved by dynamically calculating coordinates.

### Q4: How do I package XmlPy applications?

**A**: You can use tools like PyInstaller, cx_Freeze, or similar to package Python applications.

### Q5: What is XmlPy's performance?

**A**: XmlPy's performance is comparable to using Tkinter directly, as it's built on top of Tkinter.

### Q6: Does it support internationalization?

**A**: Yes. You can extract interface text to configuration files and load different XML files based on language.

### Q7: How do I handle large amounts of data?

**A**: For large amounts of data, it's recommended to use pagination or virtual lists to avoid loading all data at once.

### Q8: Is there a graphical designer for XmlPy?

**A**: Currently, there is no graphical designer, but you can manually write XML, which is clear and easy to read.

---

## Appendix

### A. Color Quick Reference

| Color | Hex Code | RGB | Usage |
|-------|-----------|-----|-------|
| Red | #e74c3c | 231, 76, 60 | Errors, Delete |
| Dark Red | #c0392b | 192, 57, 43 | Dangerous operations |
| Blue | #3498db | 52, 152, 219 | Primary actions |
| Dark Blue | #2980b9 | 41, 128, 185 | Links |
| Green | #27ae60 | 39, 174, 96 | Success, Confirm |
| Dark Green | #229954 | 34, 153, 84 | Complete |
| Yellow | #f39c12 | 243, 156, 18 | Warnings |
| Dark Yellow | #d68910 | 214, 137, 16 | Attention |
| Purple | #9b59b6 | 155, 89, 182 | Special features |
| Dark Purple | #8e44ad | 142, 68, 173 | Advanced features |
| Gray | #95a5a6 | 149, 165, 166 | Secondary actions |
| Dark Gray | #7f8c8d | 127, 140, 141 | Disabled state |
| Dark | #2c3e50 | 44, 62, 80 | Background |
| Darker | #34495e | 52, 73, 94 | Panels |
| Light | #ecf0f1 | 236, 240, 241 | Light background |
| White | #ffffff | 255, 255, 255 | Text |

### B. Font Settings

```xml
<!-- Basic font -->
<font="Arial 12"/>

<!-- Bold -->
<font="Arial 12 bold"/>

<!-- Italic -->
<font="Arial 12 italic"/>

<!-- Bold italic -->
<font="Arial 12 bold italic"/>

<!-- Different fonts -->
<font="Times New Roman 12"/>
<font="Courier New 12"/>
<font="Verdana 12"/>
```

### C. Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Copy | Ctrl+C |
| Paste | Ctrl+V |
| Cut | Ctrl+X |
| Select All | Ctrl+A |
| Undo | Ctrl+Z |
| Redo | Ctrl+Y |

---

## Changelog

### v1.0.0 (2024-01-01)
- 🎉 Initial release
- ✨ Support for basic widgets
- 📝 Complete documentation

---

## Contact Us

- 📧 Email: support@xmlpy.dev
- 🐛 Bug Reports: [GitHub Issues](https://github.com/your-username/xml-py/issues)
- 💡 Feature Requests: [GitHub Discussions](https://github.com/your-username/xml-py/discussions)

---

**Thank you for using XmlPy! Happy coding!** 🎉
