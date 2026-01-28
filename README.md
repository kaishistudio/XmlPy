# 🚀 XmlPy - XML-Driven GUI Framework for Python

![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

> 🎨 Create beautiful GUI applications with XML - No more tedious widget coding!

## 📖 Table of Contents

- [✨ Features](#-features)
- [🎯 Why XmlPy?](#-why-xmlpy)
- [📦 Installation](#-installation)
- [🚀 Quick Start](#-quick-start)
- [📚 Documentation](#-documentation)
- [🎨 Supported Widgets](#-supported-widgets)
- [💡 Examples](#-examples)
- [🔧 Advanced Features](#-advanced-features)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

## ✨ Features

- 🎯 **XML-Driven UI Design** - Define your entire interface in clean XML
- 🧩 **Widget Support** - Buttons, Labels, Entries, Frames, and more!
- 🎨 **Easy Styling** - Customize colors, fonts, and sizes effortlessly
- 🔗 **Event Handling** - Bind commands and events with simple XML tags
- 📱 **Responsive Layout** - Absolute positioning with pixel-perfect control
- 🔄 **Two XML Formats** - Choose between `<root>` or `<window>` as root element
- 🎭 **Theme Support** - Create beautiful, consistent interfaces
- ⚡ **Lightweight** - Minimal dependencies, maximum performance
- 🛠️ **Easy Integration** - Works seamlessly with existing Python code

## 🎯 Why XmlPy?

| Traditional Tkinter | XmlPy |
|-------------------|-------|
| 😰 Hundreds of lines of widget code | 😌 Clean XML structure |
| 🐛 Hard to maintain and modify | 🎨 Easy to update UI |
| 📝 Mixed logic and presentation | 🧩 Separation of concerns |
| 🎨 Difficult styling | 💅 Simple attribute-based styling |
| ⏱️ Time-consuming development | ⚡ Rapid prototyping |

## 📦 Installation

### Prerequisites
- Python 3.6 or higher
- Tkinter (usually included with Python)

### Setup

1. **Clone or download the repository:**
   ```bash
   git clone https://github.com/your-username/xml-py.git
   cd xml-py/Code
   ```

2. **No installation required!** Just import and use:
   ```python
   from XmlPy import *
   ```

## 🚀 Quick Start

### Basic Example - Hello World

```python
from XmlPy import *

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

def say_hello(widget=None):
    print("Hello from XmlPy! 🎉")

global_commands = {
    'say_hello': say_hello
}

XmlInit_string(xml_content, global_commands)
```

### Load from XML File

```python
from XmlPy import *

def on_click(widget=None):
    print("Button clicked! 🎯")

global_commands = {
    'on_click': on_click
}

# Load from external XML file
XmlInit_Path('my_app.xml', global_commands)
```

## 📚 Documentation

### XML Structure

#### Format 1: Window as Root Element (Recommended) 🌟
```xml
<?xml version="1.0" encoding="UTF-8"?>
<window title="My App" geometry="800x600" bg="#2c3e50">
    <!-- Widgets go here -->
</window>
```

#### Format 2: Root with Window (Legacy) 📜
```xml
<?xml version="1.0" encoding="UTF-8"?>
<root>
    <window title="My App" geometry="800x600" bg="#2c3e50"/>
    <!-- Widgets go here -->
</root>
```

### Window Properties

| Attribute | Description | Example |
|-----------|-------------|---------|
| `title` | Window title | `title="My App"` |
| `geometry` | Window size | `geometry="800x600"` |
| `bg` | Background color | `bg="#2c3e50"` |
| `minsize` | Minimum size | `minsize="400x300"` |
| `maxsize` | Maximum size | `maxsize="1200x900"` |
| `resizable` | Resizable? | `resizable="true,true"` |
| `iconbitmap` | Window icon | `iconbitmap="icon.ico"` |

## 🎨 Supported Widgets

### 🔘 Button
```xml
<button id="btn1" text="Click Me" 
        x="10" y="10" width="10" height="2" 
        bg="#3498db" fg="white">
    <Click_command>my_function</Click_command>
</button>
```

### 📝 Label
```xml
<label id="label1" text="Hello World" 
       x="10" y="50" fg="white" bg="#2c3e50"/>
```

### ⌨️ Entry (Text Input)
```xml
<entry id="entry1" width="30" 
        fg="white" bg="#1a252f" 
        justify="right" x="10" y="100"/>
```

### 🖼️ Frame (Container)
```xml
<frame id="frame1" bg="#34495e" 
        x="10" y="150" width="200" height="100">
    <!-- Child widgets -->
</frame>
```

### 📊 Canvas
```xml
<canvas id="canvas1" bg="white" 
         x="10" y="270" width="200" height="150"/>
```

### ☑️ Checkbutton
```xml
<checkbutton id="cb1" text="Check me" 
             x="10" y="440" bg="#34495e" fg="white">
    <Click_command>toggle_check</Click_command>
</checkbutton>
```

### 📻 Radiobutton
```xml
<radiobutton id="rb1" text="Option 1" 
             x="10" y="480" bg="#34495e" fg="white">
    <Click_command>select_option</Click_command>
</radiobutton>
```

### 📜 Text Area
```xml
<text id="text1" width="30" height="10" 
      bg="white" fg="black" x="10" y="520"/>
```

### 📏 Scale (Slider)
```xml
<scale id="scale1" from_="0" to="100" 
       orient="horizontal" x="10" y="620" width="200"/>
```

### 📋 Listbox
```xml
<listbox id="list1" width="30" height="5" 
         bg="white" fg="black" x="10" y="680"/>
```

### 🎨 Menu
```xml
<menu id="menu1">
    <item id="item1" text="File">
        <Click_command>file_menu</Click_command>
    </item>
    <item id="item2" text="Edit">
        <Click_command>edit_menu</Click_command>
    </item>
</menu>
```

## 💡 Examples

### 🧮 Scientific Calculator

A fully functional scientific calculator with XML-driven UI:

```python
from XmlPy import *

class Calculator:
    def __init__(self):
        self.current_input = ""
        self.result = ""
    
    def append_digit(self, digit, widget=None):
        self.current_input += str(digit)
        self.update_display()
    
    def calculate(self, widget=None):
        try:
            self.result = str(eval(self.current_input))
            self.current_input = self.result
            self.update_display()
        except:
            self.current_input = "Error"
            self.update_display()
    
    def update_display(self):
        entry = entry_id_map.get('display')
        if entry:
            entry.delete(0, tk.END)
            entry.insert(0, self.current_input)

calculator = Calculator()

global_commands = {
    'append_0': lambda w: calculator.append_digit(0),
    'append_1': lambda w: calculator.append_digit(1),
    'calculate': calculator.calculate,
    # ... more commands
}

XmlInit_Path('calculator.xml', global_commands)
```

### 🎨 Color Palette Example

```xml
<window title="Color Demo" geometry="600x400" bg="#2c3e50">
    <button id="btn_red" text="Red" x="50" y="50" 
            width="8" height="2" bg="#e74c3c" fg="white">
        <Click_command>show_red</Click_command>
    </button>
    <button id="btn_blue" text="Blue" x="200" y="50" 
            width="8" height="2" bg="#3498db" fg="white">
        <Click_command>show_blue</Click_command>
    </button>
    <button id="btn_green" text="Green" x="350" y="50" 
            width="8" height="2" bg="#27ae60" fg="white">
        <Click_command>show_green</Click_command>
    </button>
</window>
```

## 🔧 Advanced Features

### 🎭 Custom Styling

```xml
<button id="styled_btn" text="Styled Button"
        x="10" y="10" width="15" height="3"
        bg="#9b59b6" fg="white"
        font="Arial 12 bold"
        relief="raised"
        cursor="hand2">
    <Click_command>on_click</Click_command>
</button>
```

### 📐 Layout Management

```xml
<frame id="main_frame" bg="#34495e" 
        x="10" y="10" width="780" height="580">
    
    <frame id="header_frame" bg="#2c3e50" 
            x="10" y="10" width="760" height="80">
        <label id="title" text="My Application" 
               x="300" y="30" fg="white" bg="#2c3e50"/>
    </frame>
    
    <frame id="content_frame" bg="#34495e" 
            x="10" y="100" width="760" height="400">
        <!-- Main content -->
    </frame>
    
    <frame id="footer_frame" bg="#2c3e50" 
            x="10" y="510" width="760" height="60">
        <!-- Footer content -->
    </frame>
</frame>
```

### 🔗 Event Handling

```xml
<button id="btn_events" text="Events Demo"
        x="10" y="10" width="15" height="2">
    <Click_command>on_click</Click_command>
    <Double_Click_command>on_double_click</Double_Click_command>
    <Right_Click_command>on_right_click</Right_Click_command>
</button>
```

```python
def on_click(widget=None):
    print("Single click! 👆")

def on_double_click(widget=None):
    print("Double click! 👆👆")

def on_right_click(widget=None):
    print("Right click! 👈")
```

### 🎯 Widget ID Mapping

Access widgets programmatically:

```python
# Access button
button = button_id_map.get('btn1')
if button:
    button.config(text="New Text")

# Access entry
entry = entry_id_map.get('entry1')
if entry:
    content = entry.get()

# Access label
label = label_id_map.get('label1')
if label:
    label.config(text="Updated Label")
```

## 🎨 Color Palette Reference

| Color | Hex Code | Usage |
|-------|----------|-------|
| 🔴 Red | `#e74c3c` | Errors, Delete |
| 🔵 Blue | `#3498db` | Primary actions |
| 🟢 Green | `#27ae60` | Success, Confirm |
| 🟡 Yellow | `#f39c12` | Warnings |
| 🟣 Purple | `#9b59b6` | Special features |
| ⚪ Gray | `#95a5a6` | Secondary actions |
| ⚫ Dark | `#2c3e50` | Backgrounds |
| ⬛ Darker | `#34495e` | Panels |
| ⬜ Light | `#ecf0f1` | Light backgrounds |
| 🟤 Orange | `#e67e22` | Accent |

## 🛠️ Tips & Best Practices

### ✅ DO's
- ✨ Use descriptive IDs for widgets
- 📁 Organize your XML files in a logical structure
- 🎨 Use consistent color schemes
- 📝 Comment your XML for clarity
- 🔧 Keep logic separate from UI
- 🎯 Test your layouts incrementally

### ❌ DON'Ts
- ❌ Don't use hardcoded positions for everything
- 🚫 Don't mix too many colors
- ⚠️ Don't forget to handle errors
- 🙅 Don't use very long widget IDs
- 📵 Don't create overly complex nested structures

## 🤝 Contributing

Contributions are welcome! 🎉

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with ❤️ using Python and Tkinter
- Inspired by the need for simpler GUI development
- Thanks to all contributors and users! 🌟

## 📞 Support

- 📧 Email: support@xmlpy.dev
- 💬 Discord: [Join our community](https://discord.gg/xmlpy)
- 🐛 Issues: [Report bugs](https://github.com/your-username/xml-py/issues)
- 💡 Ideas: [Suggest features](https://github.com/your-username/xml-py/issues)

---

<div align="center">

**Made with ❤️ by the XmlPy Team**

[⭐ Star us on GitHub](https://github.com/your-username/xml-py) | 
[🐦 Follow us on Twitter](https://twitter.com/xmlpy) | 
[📖 Read our Blog](https://blog.xmlpy.dev)

</div>
