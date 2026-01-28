# XmlPy 用户手册

> 📘 完整的XmlPy框架使用指南

---

## 📖 目录

1. [简介](#1-简介)
2. [安装与配置](#2-安装与配置)
3. [快速入门](#3-快速入门)
4. [XML语法详解](#4-xml语法详解)
5. [控件详解](#5-控件详解)
6. [事件处理](#6-事件处理)
7. [高级功能](#7-高级功能)
8. [实战案例](#8-实战案例)
9. [最佳实践](#9-最佳实践)
10. [故障排除](#10-故障排除)
11. [API参考](#11-api参考)
12. [常见问题](#12-常见问题)

---

## 1. 简介

### 1.1 什么是XmlPy？

XmlPy是一个基于XML的Python GUI框架，它允许开发者使用XML来定义图形用户界面，而不需要编写大量的Tkinter代码。

### 1.2 核心特性

- ✅ **XML驱动** - 使用XML定义界面，代码更清晰
- ✅ **控件丰富** - 支持按钮、标签、输入框等多种控件
- ✅ **易于维护** - 界面与逻辑分离，便于修改
- ✅ **快速开发** - 减少重复代码，提高开发效率
- ✅ **灵活布局** - 支持绝对定位和嵌套布局
- ✅ **事件绑定** - 简单的事件处理机制

### 1.3 适用场景

- 🎯 桌面应用程序开发
- 📊 数据可视化工具
- 🧮 计算器和小工具
- 🎮 简单的游戏界面
- 📝 表单和数据录入应用

---

## 2. 安装与配置

### 2.1 系统要求

- Python 3.6 或更高版本
- Tkinter（通常随Python一起安装）
- 操作系统：Windows、macOS、Linux

### 2.2 安装步骤

#### 步骤1：获取代码

```bash
git clone https://github.com/your-username/xml-py.git
cd xml-py/Code
```

#### 步骤2：验证安装

```python
# 测试导入
from XmlPy import *
print("XmlPy导入成功！")
```

### 2.3 目录结构

```
xml-py/
├── Code/
│   ├── XmlPy.py          # 框架核心文件
│   ├── README.md         # 项目说明
│   ├── USER_MANUAL.md    # 用户手册（本文件）
│   └── examples/        # 示例代码
│       ├── hello_world.py
│       ├── calculator.py
│       └── ...
```

---

## 3. 快速入门

### 3.1 第一个程序：Hello World

#### Python代码

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
    <button id="btn_click" text="点击我" 
            x="150" y="150" width="10" height="2" 
            bg="#3498db" fg="white">
        <Click_command>say_hello</Click_command>
    </button>
</window>
"""

XmlInit_string(xml_content, global_commands)
```

#### 运行结果

运行程序后，将显示一个窗口，包含一个标签和一个按钮。点击按钮会在控制台输出"Hello, XmlPy!"。

### 3.2 从文件加载XML

#### 创建XML文件（hello.xml）

```xml
<?xml version="1.0" encoding="UTF-8"?>
<window title="Hello World" geometry="400x300" bg="#2c3e50">
    <label id="greeting" text="Hello, XmlPy!" 
           x="150" y="100" fg="white" bg="#2c3e50"/>
    <button id="btn_click" text="点击我" 
            x="150" y="150" width="10" height="2" 
            bg="#3498db" fg="white">
        <Click_command>say_hello</Click_command>
    </button>
</window>
```

#### Python代码

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

## 4. XML语法详解

### 4.1 XML结构

#### 格式1：Window作为根元素（推荐）

```xml
<?xml version="1.0" encoding="UTF-8"?>
<window title="我的应用" geometry="800x600" bg="#2c3e50">
    <!-- 控件定义 -->
</window>
```

#### 格式2：Root包裹Window（兼容旧版本）

```xml
<?xml version="1.0" encoding="UTF-8"?>
<root>
    <window title="我的应用" geometry="800x600" bg="#2c3e50"/>
    <!-- 控件定义 -->
</root>
```

### 4.2 Window属性

| 属性 | 类型 | 必需 | 说明 | 示例 |
|------|------|------|------|------|
| title | 字符串 | 否 | 窗口标题 | `title="我的应用"` |
| geometry | 字符串 | 否 | 窗口大小 | `geometry="800x600"` |
| bg | 颜色 | 否 | 背景颜色 | `bg="#2c3e50"` |
| minsize | 字符串 | 否 | 最小尺寸 | `minsize="400x300"` |
| maxsize | 字符串 | 否 | 最大尺寸 | `maxsize="1200x900"` |
| resizable | 布尔 | 否 | 是否可调整大小 | `resizable="true,true"` |
| iconbitmap | 路径 | 否 | 窗口图标 | `iconbitmap="icon.ico"` |

### 4.3 通用属性

所有控件都支持以下属性：

| 属性 | 说明 | 示例 |
|------|------|------|
| id | 控件唯一标识符 | `id="btn1"` |
| x | X坐标 | `x="10"` |
| y | Y坐标 | `y="20"` |
| bg | 背景颜色 | `bg="#3498db"` |
| fg | 前景颜色（文字颜色） | `fg="white"` |
| font | 字体设置 | `font="Arial 12"` |
| width | 宽度 | `width="10"` |
| height | 高度 | `height="2"` |

### 4.4 颜色格式

#### 十六进制颜色

```xml
<button bg="#3498db" fg="white"/>
```

#### 颜色名称

```xml
<button bg="blue" fg="white"/>
```

#### 常用颜色参考

| 颜色 | 十六进制 | 用途 |
|------|---------|------|
| 红色 | #e74c3c | 错误、删除 |
| 蓝色 | #3498db | 主要操作 |
| 绿色 | #27ae60 | 成功、确认 |
| 黄色 | #f39c12 | 警告 |
| 紫色 | #9b59b6 | 特殊功能 |
| 灰色 | #95a5a6 | 次要操作 |
| 深色 | #2c3e50 | 背景 |
| 浅色 | #ecf0f1 | 浅色背景 |

---

## 5. 控件详解

### 5.1 Button（按钮）

#### 基本用法

```xml
<button id="btn1" text="点击我" 
        x="10" y="10" width="10" height="2" 
        bg="#3498db" fg="white">
    <Click_command>my_function</Click_command>
</button>
```

#### 完整属性

| 属性 | 说明 | 默认值 |
|------|------|--------|
| text | 按钮文字 | "Button" |
| width | 宽度 | 10 |
| height | 高度 | 1 |
| bg | 背景颜色 | 系统默认 |
| fg | 文字颜色 | 系统默认 |
| font | 字体 | 系统默认 |
| relief | 边框样式 | "raised" |
| cursor | 鼠标样式 | 系统默认 |
| state | 状态 | "normal" |

#### 事件

```xml
<button id="btn1" text="事件测试">
    <Click_command>on_click</Click_command>
    <Double_Click_command>on_double_click</Double_Click_command>
    <Right_Click_command>on_right_click</Right_Click_command>
</button>
```

#### Python代码

```python
def on_click(widget=None):
    print("单击事件")

def on_double_click(widget=None):
    print("双击事件")

def on_right_click(widget=None):
    print("右键点击事件")

global_commands = {
    'on_click': on_click,
    'on_double_click': on_double_click,
    'on_right_click': on_right_click
}
```

### 5.2 Label（标签）

#### 基本用法

```xml
<label id="label1" text="这是一个标签" 
       x="10" y="50" fg="white" bg="#2c3e50"/>
```

#### 完整属性

| 属性 | 说明 | 默认值 |
|------|------|--------|
| text | 标签文字 | "Label" |
| width | 宽度 | 自动 |
| height | 高度 | 自动 |
| bg | 背景颜色 | 系统默认 |
| fg | 文字颜色 | 系统默认 |
| font | 字体 | 系统默认 |
| justify | 对齐方式 | "left" |
| relief | 边框样式 | "flat" |

#### 对齐方式

```xml
<!-- 左对齐 -->
<label justify="left" text="左对齐"/>

<!-- 居中对齐 -->
<label justify="center" text="居中对齐"/>

<!-- 右对齐 -->
<label justify="right" text="右对齐"/>
```

### 5.3 Entry（输入框）

#### 基本用法

```xml
<entry id="entry1" width="30" 
        fg="white" bg="#1a252f" 
        justify="right" x="10" y="100"/>
```

#### 完整属性

| 属性 | 说明 | 默认值 |
|------|------|--------|
| width | 宽度（字符数） | 20 |
| fg | 文字颜色 | 系统默认 |
| bg | 背景颜色 | 系统默认 |
| font | 字体 | 系统默认 |
| justify | 对齐方式 | "left" |
| show | 显示字符 | ""（显示实际字符） |
| state | 状态 | "normal" |
| bd | 边框宽度 | 系统默认 |

#### 密码输入框

```xml
<entry id="password" width="30" 
        show="*" x="10" y="100"/>
```

#### 只读输入框

```xml
<entry id="readonly" width="30" 
        state="readonly" x="10" y="100"/>
```

#### Python操作

```python
# 获取输入内容
entry = entry_id_map.get('entry1')
if entry:
    content = entry.get()
    print(f"输入内容: {content}")

# 设置输入内容
entry = entry_id_map.get('entry1')
if entry:
    entry.delete(0, tk.END)
    entry.insert(0, "默认值")

# 清空输入框
entry = entry_id_map.get('entry1')
if entry:
    entry.delete(0, tk.END)
```

### 5.4 Frame（框架）

#### 基本用法

```xml
<frame id="frame1" bg="#34495e" 
        x="10" y="150" width="200" height="100">
    <!-- 子控件 -->
    <label id="inner_label" text="框架内的标签" 
           x="10" y="10" fg="white"/>
</frame>
```

#### 完整属性

| 属性 | 说明 | 默认值 |
|------|------|--------|
| bg | 背景颜色 | 系统默认 |
| width | 宽度 | 自动 |
| height | 高度 | 自动 |
| relief | 边框样式 | "flat" |
| bd | 边框宽度 | 0 |

#### 边框样式

```xml
<!-- 平面边框 -->
<frame relief="flat"/>

<!-- 凸起边框 -->
<frame relief="raised"/>

<!-- 凹陷边框 -->
<frame relief="sunken"/>

<!-- 槽状边框 -->
<frame relief="groove"/>

<!-- 脊状边框 -->
<frame relief="ridge"/>
```

### 5.5 Canvas（画布）

#### 基本用法

```xml
<canvas id="canvas1" bg="white" 
         x="10" y="270" width="200" height="150"/>
```

#### Python绘图

```python
# 获取画布
canvas = canvas_id_map.get('canvas1')
if canvas:
    # 绘制矩形
    canvas.create_rectangle(10, 10, 100, 100, fill="red")
    
    # 绘制圆形
    canvas.create_oval(120, 10, 180, 70, fill="blue")
    
    # 绘制线条
    canvas.create_line(10, 120, 180, 120, fill="green", width=3)
    
    # 绘制文字
    canvas.create_text(100, 140, text="Hello Canvas", fill="black")
```

### 5.6 Checkbutton（复选框）

#### 基本用法

```xml
<checkbutton id="cb1" text="启用功能" 
             x="10" y="440" bg="#34495e" fg="white">
    <Click_command>toggle_check</Click_command>
</checkbutton>
```

#### Python操作

```python
# 获取复选框状态
cb = checkbutton_id_map.get('cb1')
if cb:
    var = checkbutton_vars.get('cb1')
    if var:
        is_checked = var.get()
        print(f"复选框状态: {is_checked}")

# 设置复选框状态
cb = checkbutton_id_map.get('cb1')
if cb:
    var = checkbutton_vars.get('cb1')
    if var:
        var.set(True)  # 选中
        var.set(False)  # 取消选中
```

### 5.7 Radiobutton（单选按钮）

#### 基本用法

```xml
<radiobutton id="rb1" text="选项1" 
             x="10" y="480" bg="#34495e" fg="white">
    <Click_command>select_option1</Click_command>
</radiobutton>
<radiobutton id="rb2" text="选项2" 
             x="10" y="510" bg="#34495e" fg="white">
    <Click_command>select_option2</Click_command>
</radiobutton>
```

#### Python操作

```python
# 获取单选按钮状态
rb = radio_id_map.get('rb1')
if rb:
    var = radio_vars.get('rb1')
    if var:
        selected_value = var.get()
        print(f"选中值: {selected_value}")
```

### 5.8 Text（文本区域）

#### 基本用法

```xml
<text id="text1" width="30" height="10" 
      bg="white" fg="black" x="10" y="550"/>
```

#### Python操作

```python
# 获取文本区域
text_widget = text_id_map.get('text1')
if text_widget:
    # 获取内容
    content = text_widget.get("1.0", tk.END)
    print(f"文本内容: {content}")
    
    # 设置内容
    text_widget.delete("1.0", tk.END)
    text_widget.insert("1.0", "新内容")
    
    # 追加内容
    text_widget.insert(tk.END, "\n追加的内容")
```

### 5.9 Scale（滑块）

#### 基本用法

```xml
<scale id="scale1" from_="0" to="100" 
       orient="horizontal" x="10" y="650" width="200"/>
```

#### 完整属性

| 属性 | 说明 | 默认值 |
|------|------|--------|
| from_ | 最小值 | 0 |
| to | 最大值 | 100 |
| orient | 方向 | "horizontal" |
| length | 长度 | 自动 |
| resolution | 步长 | 1 |

#### Python操作

```python
# 获取滑块值
scale = scale_id_map.get('scale1')
if scale:
    value = scale.get()
    print(f"滑块值: {value}")

# 设置滑块值
scale = scale_id_map.get('scale1')
if scale:
    scale.set(50)
```

### 5.10 Listbox（列表框）

#### 基本用法

```xml
<listbox id="list1" width="30" height="5" 
         bg="white" fg="black" x="10" y="700"/>
```

#### Python操作

```python
# 获取列表框
listbox = listbox_id_map.get('list1')
if listbox:
    # 添加项目
    listbox.insert(tk.END, "项目1")
    listbox.insert(tk.END, "项目2")
    listbox.insert(tk.END, "项目3")
    
    # 获取选中项
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        value = listbox.get(index)
        print(f"选中项: {value}")
    
    # 删除项目
    listbox.delete(0, tk.END)  # 清空所有
    
    # 获取所有项目
    all_items = listbox.get(0, tk.END)
    print(f"所有项目: {all_items}")
```

### 5.11 Menu（菜单）

#### 基本用法

```xml
<menu id="menu1">
    <item id="item_file" text="文件">
        <Click_command>file_menu</Click_command>
    </item>
    <item id="item_edit" text="编辑">
        <Click_command>edit_menu</Click_command>
    </item>
    <item id="item_help" text="帮助">
        <Click_command>help_menu</Click_command>
    </item>
</menu>
```

#### Python代码

```python
def file_menu(widget=None):
    print("文件菜单")

def edit_menu(widget=None):
    print("编辑菜单")

def help_menu(widget=None):
    print("帮助菜单")

global_commands = {
    'file_menu': file_menu,
    'edit_menu': edit_menu,
    'help_menu': help_menu
}
```

---

## 6. 事件处理

### 6.1 事件类型

| 事件 | XML标签 | 说明 |
|------|---------|------|
| 单击 | `<Click_command>` | 鼠标左键单击 |
| 双击 | `<Double_Click_command>` | 鼠标左键双击 |
| 右键 | `<Right_Click_command>` | 鼠标右键单击 |
| 文本改变 | `<Textchanged_Command>` | 文本内容改变 |

### 6.2 事件处理函数

#### 基本格式

```python
def event_handler(widget=None):
    """
    事件处理函数
    
    Args:
        widget: 触发事件的控件对象
    """
    print("事件被触发")
```

#### 获取控件信息

```python
def on_button_click(widget=None):
    if widget:
        print(f"控件ID: {widget}")
        print(f"控件类型: {type(widget)}")
        
        # 获取按钮文字
        if hasattr(widget, 'cget'):
            text = widget.cget('text')
            print(f"按钮文字: {text}")
```

### 6.3 全局命令映射

```python
# 定义事件处理函数
def function1(widget=None):
    print("功能1被调用")

def function2(widget=None):
    print("功能2被调用")

# 创建全局命令映射
global_commands = {
    'function1': function1,
    'function2': function2,
    'on_click': lambda w: print("匿名函数"),
    'append_digit': lambda w, digit: print(f"输入数字: {digit}")
}
```

### 6.4 控件ID映射

XmlPy提供了多个全局字典来访问控件：

```python
# 按钮映射
button = button_id_map.get('btn_id')

# 标签映射
label = label_id_map.get('label_id')

# 输入框映射
entry = entry_id_map.get('entry_id')

# 文本区域映射
text = text_id_map.get('text_id')

# 画布映射
canvas = canvas_id_map.get('canvas_id')

# 列表框映射
listbox = listbox_id_map.get('list_id')

# 滑块映射
scale = scale_id_map.get('scale_id')

# 复选框映射
checkbutton = checkbutton_id_map.get('cb_id')

# 单选按钮映射
radiobutton = radio_id_map.get('rb_id')
```

---

## 7. 高级功能

### 7.1 嵌套布局

```xml
<window title="嵌套布局示例" geometry="800x600">
    <frame id="main_frame" bg="#2c3e50" x="10" y="10" width="780" height="580">
        <frame id="header_frame" bg="#34495e" x="10" y="10" width="760" height="80">
            <label id="title" text="标题" x="350" y="30" fg="white"/>
        </frame>
        
        <frame id="content_frame" bg="#34495e" x="10" y="100" width="760" height="400">
            <button id="btn1" text="按钮1" x="10" y="10" width="10" height="2">
                <Click_command>action1</Click_command>
            </button>
            <button id="btn2" text="按钮2" x="120" y="10" width="10" height="2">
                <Click_command>action2</Click_command>
            </button>
        </frame>
        
        <frame id="footer_frame" bg="#34495e" x="10" y="510" width="760" height="60">
            <label id="status" text="就绪" x="350" y="20" fg="white"/>
        </frame>
    </frame>
</window>
```

### 7.2 动态更新控件

```python
from XmlPy import *
import time

def update_label(widget=None):
    label = label_id_map.get('status_label')
    if label:
        for i in range(5):
            label.config(text=f"处理中... {i+1}/5")
            root.update()
            time.sleep(1)
        label.config(text="完成！")

global_commands = {
    'update_label': update_label
}
```

### 7.3 数据绑定

```xml
<entry id="entry1" width="30" x="10" y="10">
    <Textchanged_Command>on_text_change</Textchanged_Command>
</entry>
<label id="preview" text="预览: " x="10" y="50"/>
```

```python
def on_text_change(widget=None):
    entry = entry_id_map.get('entry1')
    label = label_id_map.get('preview')
    if entry and label:
        content = entry.get()
        label.config(text=f"预览: {content}")

global_commands = {
    'on_text_change': on_text_change
}
```

### 7.4 样式主题

#### 创建主题文件（theme.xml）

```xml
<?xml version="1.0" encoding="UTF-8"?>
<window title="主题示例" geometry="800x600" bg="#2c3e50">
    <frame id="main_frame" bg="#34495e" x="10" y="10" width="780" height="580">
        <button id="btn1" text="主要按钮" x="10" y="10" width="12" height="2"
                bg="#3498db" fg="white">
            <Click_command>action1</Click_command>
        </button>
        <button id="btn2" text="次要按钮" x="150" y="10" width="12" height="2"
                bg="#95a5a6" fg="white">
            <Click_command>action2</Click_command>
        </button>
        <button id="btn3" text="成功按钮" x="290" y="10" width="12" height="2"
                bg="#27ae60" fg="white">
            <Click_command>action3</Click_command>
        </button>
        <button id="btn4" text="警告按钮" x="430" y="10" width="12" height="2"
                bg="#f39c12" fg="white">
            <Click_command>action4</Click_command>
        </button>
        <button id="btn5" text="危险按钮" x="570" y="10" width="12" height="2"
                bg="#e74c3c" fg="white">
            <Click_command>action5</Click_command>
        </button>
    </frame>
</window>
```

---

## 8. 实战案例

### 8.1 登录表单

#### XML文件（login.xml）

```xml
<?xml version="1.0" encoding="UTF-8"?>
<window title="登录" geometry="400x300" bg="#2c3e50">
    <frame id="login_frame" bg="#34495e" x="50" y="50" width="300" height="200">
        <label id="username_label" text="用户名:" 
               x="20" y="20" fg="white" bg="#34495e"/>
        <entry id="username" width="25" 
                x="100" y="20" bg="#1a252f" fg="white"/>
        
        <label id="password_label" text="密码:" 
               x="20" y="60" fg="white" bg="#34495e"/>
        <entry id="password" width="25" show="*"
                x="100" y="60" bg="#1a252f" fg="white"/>
        
        <button id="btn_login" text="登录" 
                x="50" y="120" width="10" height="2" 
                bg="#3498db" fg="white">
            <Click_command>login</Click_command>
        </button>
        <button id="btn_cancel" text="取消" 
                x="170" y="120" width="10" height="2" 
                bg="#e74c3c" fg="white">
            <Click_command>cancel</Click_command>
        </button>
    </frame>
</window>
```

#### Python代码

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
            messagebox.showinfo("登录", f"欢迎, {username}!")
        else:
            messagebox.showwarning("警告", "请输入用户名和密码")

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

### 8.2 待办事项列表

#### XML文件（todo.xml）

```xml
<?xml version="1.0" encoding="UTF-8"?>
<window title="待办事项" geometry="500x400" bg="#2c3e50">
    <frame id="main_frame" bg="#34495e" x="10" y="10" width="480" height="380">
        <entry id="new_task" width="40" 
                x="10" y="10" bg="#1a252f" fg="white"/>
        <button id="btn_add" text="添加" 
                x="350" y="10" width="8" height="2" 
                bg="#27ae60" fg="white">
            <Click_command>add_task</Click_command>
        </button>
        
        <listbox id="task_list" width="55" height="15" 
                 bg="white" fg="black" x="10" y="50"/>
        
        <button id="btn_complete" text="完成" 
                x="10" y="320" width="8" height="2" 
                bg="#3498db" fg="white">
            <Click_command>complete_task</Click_command>
        </button>
        <button id="btn_delete" text="删除" 
                x="100" y="320" width="8" height="2" 
                bg="#e74c3c" fg="white">
            <Click_command>delete_task</Click_command>
        </button>
    </frame>
</window>
```

#### Python代码

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
            messagebox.showwarning("警告", "请输入任务内容")

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
            messagebox.showwarning("警告", "请选择要完成的任务")

def delete_task(widget=None):
    listbox = listbox_id_map.get('task_list')
    if listbox:
        selection = listbox.curselection()
        if selection:
            index = selection[0]
            listbox.delete(index)
        else:
            messagebox.showwarning("警告", "请选择要删除的任务")

global_commands = {
    'add_task': add_task,
    'complete_task': complete_task,
    'delete_task': delete_task
}

XmlInit_Path('todo.xml', global_commands)
```

---

## 9. 最佳实践

### 9.1 命名规范

#### 控件ID命名

```xml
<!-- 好的命名 -->
<button id="btn_submit"/>
<entry id="username_input"/>
<label id="error_message"/>

<!-- 不好的命名 -->
<button id="b1"/>
<entry id="input1"/>
<label id="msg"/>
```

#### 函数命名

```python
# 好的命名
def submit_form(widget=None):
    pass

def validate_input(widget=None):
    pass

# 不好的命名
def func1(widget=None):
    pass

def do_it(widget=None):
    pass
```

### 9.2 代码组织

#### 分离逻辑和界面

```python
# calculator.py - 业务逻辑
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

# calculator_gui.py - 界面代码
from calculator import Calculator
from XmlPy import *

calc = Calculator()

def on_add(widget=None):
    # 调用业务逻辑
    result = calc.add(1, 2)
    print(result)

global_commands = {
    'on_add': on_add
}

XmlInit_Path('calculator.xml', global_commands)
```

### 9.3 错误处理

```python
def safe_operation(widget=None):
    try:
        entry = entry_id_map.get('user_input')
        if entry:
            value = float(entry.get())
            result = perform_calculation(value)
            display_result(result)
    except ValueError:
        messagebox.showerror("错误", "请输入有效的数字")
    except Exception as e:
        messagebox.showerror("错误", f"发生错误: {str(e)}")
```

### 9.4 性能优化

```python
# 避免频繁更新
def batch_update(widget=None):
    label = label_id_map.get('status')
    if label:
        # 一次性更新所有内容
        label.config(text="处理完成")
        root.update()
```

---

## 10. 故障排除

### 10.1 常见问题

#### 问题1：控件不显示

**原因**：坐标或尺寸设置不当

**解决**：
```xml
<!-- 检查坐标和尺寸 -->
<button id="btn1" text="按钮" 
        x="10" y="10" width="10" height="2"/>
```

#### 问题2：事件不触发

**原因**：命令名称不匹配

**解决**：
```xml
<!-- XML中的命令名 -->
<button>
    <Click_command>my_function</Click_command>
</button>
```

```python
# Python中的函数名必须一致
global_commands = {
    'my_function': my_function  # 名称必须匹配
}
```

#### 问题3：控件访问失败

**原因**：控件ID错误或控件未创建

**解决**：
```python
# 检查控件是否存在
button = button_id_map.get('btn1')
if button:
    button.config(text="新文字")
else:
    print("控件不存在")
```

### 10.2 调试技巧

#### 打印控件信息

```python
def debug_info(widget=None):
    print(f"控件类型: {type(widget)}")
    print(f"控件属性: {widget.config()}")
```

#### 检查映射字典

```python
# 打印所有按钮
print("所有按钮:", button_id_map.keys())

# 打印所有标签
print("所有标签:", label_id_map.keys())
```

---

## 11. API参考

### 11.1 核心函数

#### XmlInit_string()

```python
XmlInit_string(xml_data, global_commands)
```

**参数**：
- `xml_data` (str): XML字符串
- `global_commands` (dict): 全局命令映射

**示例**：
```python
xml_content = """<window title="App">...</window>"""
global_commands = {'func': my_func}
XmlInit_string(xml_content, global_commands)
```

#### XmlInit_Path()

```python
XmlInit_Path(xmlpath, global_commands)
```

**参数**：
- `xmlpath` (str): XML文件路径
- `global_commands` (dict): 全局命令映射

**示例**：
```python
global_commands = {'func': my_func}
XmlInit_Path('app.xml', global_commands)
```

### 11.2 全局映射

#### 控件映射字典

```python
button_id_map = {}      # 按钮映射
label_id_map = {}       # 标签映射
entry_id_map = {}       # 输入框映射
text_id_map = {}        # 文本区域映射
canvas_id_map = {}      # 画布映射
listbox_id_map = {}    # 列表框映射
scale_id_map = {}       # 滑块映射
checkbutton_id_map = {} # 复选框映射
radio_id_map = {}      # 单选按钮映射
checkbutton_vars = {}   # 复选框变量
radio_vars = {}        # 单选按钮变量
```

### 11.3 Tkinter集成

#### 访问root窗口

```python
from XmlPy import root

# 设置窗口属性
root.title("新标题")
root.geometry("800x600")

# 关闭窗口
root.destroy()
```

---

## 12. 常见问题

### Q1: XmlPy支持哪些Python版本？

**A**: XmlPy支持Python 3.6及更高版本。

### Q2: 如何创建自定义控件？

**A**: 可以通过继承Tkinter控件并在Python代码中创建，然后使用place()方法定位。

### Q3: XmlPy支持响应式布局吗？

**A**: 目前主要支持绝对定位。响应式布局可以通过动态计算坐标实现。

### Q4: 如何打包XmlPy应用？

**A**: 可以使用PyInstaller、cx_Freeze等工具打包Python应用。

### Q5: XmlPy的性能如何？

**A**: XmlPy的性能与直接使用Tkinter相当，因为底层就是Tkinter。

### Q6: 支持国际化吗？

**A**: 支持。可以将界面文字提取到配置文件中，根据语言加载不同的XML文件。

### Q7: 如何处理大量数据？

**A**: 对于大量数据，建议使用分页或虚拟列表，避免一次性加载所有数据。

### Q8: XmlPy有图形化设计器吗？

**A**: 目前没有图形化设计器，但可以手动编写XML，结构清晰易读。

---

## 附录

### A. 颜色速查表

| 颜色 | 十六进制 | RGB | 用途 |
|------|---------|-----|------|
| 红色 | #e74c3c | 231, 76, 60 | 错误、删除 |
| 深红 | #c0392b | 192, 57, 43 | 危险操作 |
| 蓝色 | #3498db | 52, 152, 219 | 主要操作 |
| 深蓝 | #2980b9 | 41, 128, 185 | 链接 |
| 绿色 | #27ae60 | 39, 174, 96 | 成功、确认 |
| 深绿 | #229954 | 34, 153, 84 | 完成 |
| 黄色 | #f39c12 | 243, 156, 18 | 警告 |
| 深黄 | #d68910 | 214, 137, 16 | 注意 |
| 紫色 | #9b59b6 | 155, 89, 182 | 特殊功能 |
| 深紫 | #8e44ad | 142, 68, 173 | 高级功能 |
| 灰色 | #95a5a6 | 149, 165, 166 | 次要操作 |
| 深灰 | #7f8c8d | 127, 140, 141 | 禁用状态 |
| 深色 | #2c3e50 | 44, 62, 80 | 背景 |
| 深色2 | #34495e | 52, 73, 94 | 面板 |
| 浅色 | #ecf0f1 | 236, 240, 241 | 浅色背景 |
| 白色 | #ffffff | 255, 255, 255 | 文字 |

### B. 字体设置

```xml
<!-- 基本字体 -->
<font="Arial 12"/>

<!-- 粗体 -->
<font="Arial 12 bold"/>

<!-- 斜体 -->
<font="Arial 12 italic"/>

<!-- 粗斜体 -->
<font="Arial 12 bold italic"/>

<!-- 不同字体 -->
<font="Times New Roman 12"/>
<font="Courier New 12"/>
<font="Verdana 12"/>
```

### C. 快捷键参考

| 操作 | 快捷键 |
|------|--------|
| 复制 | Ctrl+C |
| 粘贴 | Ctrl+V |
| 剪切 | Ctrl+X |
| 全选 | Ctrl+A |
| 撤销 | Ctrl+Z |
| 重做 | Ctrl+Y |

---

## 更新日志

### v1.0.0 (2024-01-01)
- 🎉 初始版本发布
- ✨ 支持基本控件
- 📝 完整文档

---

## 联系我们

- 📧 Email: support@xmlpy.dev
- 🐛 问题反馈: [GitHub Issues](https://github.com/your-username/xml-py/issues)
- 💡 功能建议: [GitHub Discussions](https://github.com/your-username/xml-py/discussions)

---

**感谢使用XmlPy！祝您开发愉快！** 🎉
