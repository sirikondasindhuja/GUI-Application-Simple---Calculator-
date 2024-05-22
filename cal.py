import tkinter as tk
from tkinter import messagebox
import math
import sys

class Calculator:
    def __init__(self):
        self.expression = ""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

    def sqrt(self, a):
        if a < 0:
            return "Error: Negative square root"
        return math.sqrt(a)

    def exponentiate(self, a, b):
        return a ** b

    def evaluate(self, expression):
        try:
            result = eval(expression, {"__builtins__": None}, {
                "add": self.add, "subtract": self.subtract,
                "multiply": self.multiply, "divide": self.divide,
                "sqrt": self.sqrt, "pow": self.exponentiate
            })
            return result
        except Exception as e:
            return f"Error: {str(e)}"

# Command-Line Interface (CLI)
def cli_calculator(calc):
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Square root")
        print("6. Exponentiation")
        print("7. Exit")
        
        choice = input("Enter choice (1/2/3/4/5/6/7): ")

        if choice == '7':
            print("Exiting the calculator.")
            break

        if choice in ['1', '2', '3', '4', '6']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"Result: {calc.add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {calc.subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {calc.multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {calc.divide(num1, num2)}")
            elif choice == '6':
                print(f"Result: {calc.exponentiate(num1, num2)}")
        
        elif choice == '5':
            num = float(input("Enter number: "))
            print(f"Result: {calc.sqrt(num)}")
        
        else:
            print("Invalid input")

# Graphical User Interface (GUI) using Tkinter
class CalculatorApp:
    def __init__(self, root, calc):
        self.root = root
        self.calc = calc
        self.root.title("Simple Calculator")

        self.expression = ""
        self.input_text = tk.StringVar()

        self.input_frame = tk.Frame(self.root, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        self.input_frame.pack(side=tk.TOP)

        self.input_field = tk.Entry(self.input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(ipady=10)

        self.btns_frame = tk.Frame(self.root, width=400, height=450, bg="grey")
        self.btns_frame.pack()

        self.create_buttons()

    def create_buttons(self):
        button_texts = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+'),
            ('sqrt', 'exp', 'C')
        ]

        for i, row in enumerate(button_texts):
            for j, text in enumerate(row):
                if text == '=':
                    btn = tk.Button(self.btns_frame, text=text, width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=self.evaluate)
                elif text == 'C':
                    btn = tk.Button(self.btns_frame, text=text, width=10, height=3, bd=0, bg="#f00", cursor="hand2", command=self.clear)
                elif text == 'sqrt':
                    btn = tk.Button(self.btns_frame, text=text, width=10, height=3, bd=0, bg="#ccc", cursor="hand2", command=self.sqrt)
                elif text == 'exp':
                    btn = tk.Button(self.btns_frame, text=text, width=10, height=3, bd=0, bg="#ccc", cursor="hand2", command=self.exponentiate)
                else:
                    btn = tk.Button(self.btns_frame, text=text, width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda t=text: self.add_to_expression(t))
                btn.grid(row=i, column=j, padx=1, pady=1)

    def add_to_expression(self, char):
        self.expression += str(char)
        self.input_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_text.set("")

    def evaluate(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
            self.expression = ""
            self.input_text.set("")

    def sqrt(self):
        try:
            result = str(self.calc.sqrt(float(self.expression)))
            self.input_text.set(result)
            self.expression = result
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
            self.expression = ""
            self.input_text.set("")

    def exponentiate(self):
        self.add_to_expression('**')

def main():
    calc = Calculator()

    if len(sys.argv) > 1 and sys.argv[1] == '--cli':
        cli_calculator(calc)
    else:
        root = tk.Tk()
        app = CalculatorApp(root, calc)
        root.mainloop()

if __name__ == "__main__":
    main()
