
import tkinter as tk


class Calculator:
    """
    forms a simple calculator with 'root' as tkinter class object
    """
    i = 0   #display index
    operator_container = ('*','/')
    operator_container1 = ('+','-','*','/')
    operator_container2 = ('+','-','*','/','%','**2','!')

    def __init__(self, root):

        self.root = root
        self.display = tk.Entry(self.root, font=('Arial 22'))
        self.display.grid(row=1, columnspan=6, sticky=tk.W+tk.E)
        self.display.insert(0, '0')

        tk.Button(self.root, text='1', height=3, width=6, command=lambda:self.get_variable(1)).grid(row=2, column=0)
        tk.Button(self.root, text='2', height=3, width=6, command=lambda:self.get_variable(2)).grid(row=2, column=1)
        tk.Button(self.root, text='3', height=3, width=6, command=lambda:self.get_variable(3)).grid(row=2, column=2)

        tk.Button(self.root, text='4', height=3, width=6, command=lambda:self.get_variable(4)).grid(row=3, column=0)
        tk.Button(self.root, text='5', height=3, width=6, command=lambda:self.get_variable(5)).grid(row=3, column=1)
        tk.Button(self.root, text='6', height=3, width=6, command=lambda:self.get_variable(6)).grid(row=3, column=2)

        tk.Button(self.root, text='7', height=3, width=6, command=lambda:self.get_variable(7)).grid(row=4, column=0)
        tk.Button(self.root, text='8', height=3, width=6, command=lambda:self.get_variable(8)).grid(row=4, column=1)
        tk.Button(self.root, text='9', height=3, width=6, command=lambda:self.get_variable(9)).grid(row=4, column=2)

        tk.Button(self.root, text='AC', height=3, width=6, command=lambda:self.clear_all()).grid(row=5, column=0)
        tk.Button(self.root, text='0', height=3, width=6, command=lambda:self.get_variable(0)).grid(row=5, column=1)
        tk.Button(self.root, text='=', height=3, width=6, command=lambda:self.calculate()).grid(row=5, column=2)

        tk.Button(self.root, text='+', height=3, width=6, command=lambda:self.get_operator('+')).grid(row=2, column=3)
        tk.Button(self.root, text='-', height=3, width=6, command=lambda:self.get_operator('-')).grid(row=3, column=3)
        tk.Button(self.root, text='*', height=3, width=6, command=lambda:self.get_operator('*')).grid(row=4, column=3)
        tk.Button(self.root, text='/', height=3, width=6, command=lambda:self.get_operator('/')).grid(row=5, column=3)

        tk.Button(self.root, text='pi', height=3, width=6, command=lambda:self.get_operator('3.14159265')).grid(row=2, column=4)
        tk.Button(self.root, text='%', height=3, width=6, command=lambda:self.get_operator('%')).grid(row=3, column=4)
        tk.Button(self.root, text='(', height=3, width=6, command=lambda:self.get_operator('(')).grid(row=4, column=4)
        tk.Button(self.root, text='.', height=3, width=6, command=lambda:self.get_operator('.')).grid(row=5, column=4)

        tk.Button(self.root, text='<-', height=3, width=6, command=lambda:self.undo()).grid(row=2, column=5)
        tk.Button(self.root, text='x!', height=3, width=6, command=lambda:self.get_operator('!')).grid(row=3, column=5)
        tk.Button(self.root, text=')', height=3, width=6, command=lambda:self.get_operator(')')).grid(row=4, column=5)
        tk.Button(self.root, text='^2', height=3, width=6, command=lambda:self.get_operator('**2')).grid(row=5, column=5)

    def initial_clear(self):
        """
        clear screen for first time
        """
        expression = self.display.get()
        if expression == '0':
            self.display.delete(0, tk.END)

    def r_clear(self):
        """
        clear screen for result display
        """
        self.display.delete(0, tk.END)

    def clear_all(self):
        """
        AC button function to clear screen
        """
        self.display.delete(0, tk.END)
        self.display.insert(0, '0')

    def undo(self):
        """
        backspace button function to delete
        """
        entire_string = self.display.get()
        if len(entire_string):
            new_string = entire_string[:-1]
            self.r_clear()
            self.display.insert(0, new_string)
        else:
            self.r_clear()

    def factorial(self, num):
        """
        find factorial of a number
        """
        if num == 1:
            return 1
        else:
            return num * self.factorial(num-1)

    def get_factorial_num(self, entire_string, index):
        """
        extract number prefix to the factorial operator
        """
        n = 1
        factorial_num = ''
        #index = entire_string.index(sign)
        num = int(entire_string[index-n])
        while type(num) == int:
            if index-n != abs(index-n):
                break
            factorial_num = factorial_num + entire_string[index-n]
            n += 1
            try:
                num = int(entire_string[index-n])
            except:
                break

        return int(factorial_num[::-1])-1

    def get_variable(self, num):
        """
        get user input and display to screen
        """
        self.initial_clear()
        self.display.insert(Calculator.i, num)
        Calculator.i += 1

    def get_operator(self, op):
        """
        get operator and display to screen
        """
        self.initial_clear()
        expression = self.display.get()
        expression_length = len(expression)
        operator_length = len(op)
        #prevents consecutive dot(.) operation
        if expression_length and (expression[expression_length-1] == '.') and op == '.':
            self.undo()
            self.display.insert(Calculator.i-operator_length, op)
        #prefix 0 to (* or /) operators if used at beginning
        elif not expression_length and op in self.operator_container:
            self.display.insert(0, '0'+op)
            operator_length += 1
        #prevent consecutive arithmetic operators    
        elif expression_length and (expression[expression_length-1] in self.operator_container1) and (op in self.operator_container2):
            self.undo()
            self.display.insert(Calculator.i-operator_length, op)
        else:    
            self.display.insert(Calculator.i, op)
        Calculator.i += operator_length

    def calculate(self):
        """
        calculate and display result
        """
        expression = self.display.get()
        try:
            #raw_expression = parser.expr(expression).compile()
            for var in expression:
                if var == '!':
                    index = expression.index(var)
                    expression = expression[:index] + '*{}'.format(self.factorial(self.get_factorial_num(expression,index))) + expression[index+1:]
            result = eval(expression)
            self.r_clear()
            self.display.insert(0, result)
        except Exception:
            self.r_clear()
            self.display.insert(0, 'Math Error')


root = tk.Tk()
root.title("Calculator")
root.iconbitmap('cal.ico')
calc = Calculator(root)
root.mainloop()
