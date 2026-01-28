from XmlPy import *
import math

class ScientificCalculator:
    def __init__(self):
        self.current_input = ""
        self.result = ""
        self.memory = 0
        self.angle_mode = "DEG"
        self.last_operation = None
        self.waiting_for_operand = False

    def clear(self, widget=None):
        self.current_input = ""
        self.result = ""
        self.last_operation = None
        self.waiting_for_operand = False
        self.update_display()

    def clear_entry(self, widget=None):
        self.current_input = ""
        self.update_display()

    def backspace(self, widget=None):
        self.current_input = self.current_input[:-1]
        self.update_display()

    def append_digit(self, digit, widget=None):
        if self.waiting_for_operand:
            self.current_input = ""
            self.waiting_for_operand = False
        self.current_input += str(digit)
        self.update_display()

    def append_decimal(self, widget=None):
        if "." not in self.current_input:
            self.current_input += "."
            self.update_display()

    def append_operator(self, operator, widget=None):
        if self.current_input:
            self.result = self.current_input
            self.last_operation = operator
            self.waiting_for_operand = True

    def calculate(self, widget=None):
        if self.last_operation and self.current_input and self.result:
            try:
                operand1 = float(self.result)
                operand2 = float(self.current_input)
                if self.last_operation == "+":
                    self.result = str(operand1 + operand2)
                elif self.last_operation == "-":
                    self.result = str(operand1 - operand2)
                elif self.last_operation == "*":
                    self.result = str(operand1 * operand2)
                elif self.last_operation == "/":
                    self.result = str(operand1 / operand2) if operand2 != 0 else "Error"
                elif self.last_operation == "^":
                    self.result = str(operand1 ** operand2)
                elif self.last_operation == "%":
                    self.result = str(operand1 % operand2)
                if self.result != "Error":
                    self.current_input = self.result
                else:
                    self.current_input = "Error"
                self.last_operation = None
                self.waiting_for_operand = True
                self.update_display()
            except Exception as e:
                self.current_input = "Error"
                self.update_display()

    def equals(self, widget=None):
        self.calculate()
        self.last_operation = None
        self.waiting_for_operand = True

    def to_radians(self, angle):
        if self.angle_mode == "DEG":
            return math.radians(angle)
        return angle

    def sin(self, widget=None):
        try:
            value = float(self.current_input) if self.current_input else 0
            result = math.sin(self.to_radians(value))
            self.current_input = str(result)
            self.update_display()
        except:
            self.current_input = "Error"
            self.update_display()

    def cos(self, widget=None):
        try:
            value = float(self.current_input) if self.current_input else 0
            result = math.cos(self.to_radians(value))
            self.current_input = str(result)
            self.update_display()
        except:
            self.current_input = "Error"
            self.update_display()

    def tan(self, widget=None):
        try:
            value = float(self.current_input) if self.current_input else 0
            result = math.tan(self.to_radians(value))
            self.current_input = str(result)
            self.update_display()
        except:
            self.current_input = "Error"
            self.update_display()

    def asin(self, widget=None):
        try:
            value = float(self.current_input) if self.current_input else 0
            result = math.asin(value)
            if self.angle_mode == "DEG":
                result = math.degrees(result)
            self.current_input = str(result)
            self.update_display()
        except:
            self.current_input = "Error"
            self.update_display()

    def acos(self, widget=None):
        try:
            value = float(self.current_input) if self.current_input else 0
            result = math.acos(value)
            if self.angle_mode == "DEG":
                result = math.degrees(result)
            self.current_input = str(result)
            self.update_display()
        except:
            self.current_input = "Error"
            self.update_display()

    def atan(self, widget=None):
        try:
            value = float(self.current_input) if self.current_input else 0
            result = math.atan(value)
            if self.angle_mode == "DEG":
                result = math.degrees(result)
            self.current_input = str(result)
            self.update_display()
        except:
            self.current_input = "Error"
            self.update_display()

    def log(self, widget=None):
        try:
            value = float(self.current_input) if self.current_input else 0
            result = math.log10(value)
            self.current_input = str(result)
            self.update_display()
        except:
            self.current_input = "Error"
            self.update_display()

    def ln(self, widget=None):
        try:
            value = float(self.current_input) if self.current_input else 0
            result = math.log(value)
            self.current_input = str(result)
            self.update_display()
        except:
            self.current_input = "Error"
            self.update_display()

    def sqrt(self, widget=None):
        try:
            value = float(self.current_input) if self.current_input else 0
            result = math.sqrt(value)
            self.current_input = str(result)
            self.update_display()
        except:
            self.current_input = "Error"
            self.update_display()

    def square(self, widget=None):
        try:
            value = float(self.current_input) if self.current_input else 0
            result = value ** 2
            self.current_input = str(result)
            self.update_display()
        except:
            self.current_input = "Error"
            self.update_display()

    def cube(self, widget=None):
        try:
            value = float(self.current_input) if self.current_input else 0
            result = value ** 3
            self.current_input = str(result)
            self.update_display()
        except:
            self.current_input = "Error"
            self.update_display()

    def reciprocal(self, widget=None):
        try:
            value = float(self.current_input) if self.current_input else 0
            result = 1 / value
            self.current_input = str(result)
            self.update_display()
        except:
            self.current_input = "Error"
            self.update_display()

    def negate(self, widget=None):
        if self.current_input:
            if self.current_input.startswith("-"):
                self.current_input = self.current_input[1:]
            else:
                self.current_input = "-" + self.current_input
            self.update_display()

    def factorial(self, widget=None):
        try:
            value = int(float(self.current_input)) if self.current_input else 0
            result = math.factorial(value)
            self.current_input = str(result)
            self.update_display()
        except:
            self.current_input = "Error"
            self.update_display()

    def pi(self, widget=None):
        self.current_input = str(math.pi)
        self.update_display()

    def e(self, widget=None):
        self.current_input = str(math.e)
        self.update_display()

    def toggle_angle_mode(self, widget=None):
        if self.angle_mode == "DEG":
            self.angle_mode = "RAD"
        else:
            self.angle_mode = "DEG"
        if 'angle_label' in label_id_map:
            label_id_map['angle_label'].config(text=f"角度: {self.angle_mode}")

    def memory_store(self, widget=None):
        try:
            self.memory = float(self.current_input) if self.current_input else 0
        except:
            pass

    def memory_recall(self, widget=None):
        self.current_input = str(self.memory)
        self.update_display()

    def memory_clear(self, widget=None):
        self.memory = 0

    def memory_add(self, widget=None):
        try:
            value = float(self.current_input) if self.current_input else 0
            self.memory += value
        except:
            pass

    def memory_subtract(self, widget=None):
        try:
            value = float(self.current_input) if self.current_input else 0
            self.memory -= value
        except:
            pass

    def update_display(self):
        if 'display' in entry_id_map:
            display_text = self.current_input if self.current_input else "0"
            entry_id_map['display'].delete(0, tk.END)
            entry_id_map['display'].insert(0, display_text)

calculator = ScientificCalculator()

global_commands = {
    'clear': calculator.clear,
    'clear_entry': calculator.clear_entry,
    'backspace': calculator.backspace,
    'append_0': lambda w: calculator.append_digit(0, w),
    'append_1': lambda w: calculator.append_digit(1, w),
    'append_2': lambda w: calculator.append_digit(2, w),
    'append_3': lambda w: calculator.append_digit(3, w),
    'append_4': lambda w: calculator.append_digit(4, w),
    'append_5': lambda w: calculator.append_digit(5, w),
    'append_6': lambda w: calculator.append_digit(6, w),
    'append_7': lambda w: calculator.append_digit(7, w),
    'append_8': lambda w: calculator.append_digit(8, w),
    'append_9': lambda w: calculator.append_digit(9, w),
    'append_decimal': calculator.append_decimal,
    'add': lambda w: calculator.append_operator('+', w),
    'subtract': lambda w: calculator.append_operator('-', w),
    'multiply': lambda w: calculator.append_operator('*', w),
    'divide': lambda w: calculator.append_operator('/', w),
    'power': lambda w: calculator.append_operator('^', w),
    'modulo': lambda w: calculator.append_operator('%', w),
    'equals': calculator.equals,
    'sin': calculator.sin,
    'cos': calculator.cos,
    'tan': calculator.tan,
    'asin': calculator.asin,
    'acos': calculator.acos,
    'atan': calculator.atan,
    'log': calculator.log,
    'ln': calculator.ln,
    'sqrt': calculator.sqrt,
    'square': calculator.square,
    'cube': calculator.cube,
    'reciprocal': calculator.reciprocal,
    'negate': calculator.negate,
    'factorial': calculator.factorial,
    'pi': calculator.pi,
    'e': calculator.e,
    'toggle_angle': calculator.toggle_angle_mode,
    'memory_store': calculator.memory_store,
    'memory_recall': calculator.memory_recall,
    'memory_clear': calculator.memory_clear,
    'memory_add': calculator.memory_add,
    'memory_subtract': calculator.memory_subtract
}

XmlInit_Path('scientific_calculator.xml', global_commands)
