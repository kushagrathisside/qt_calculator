"""Handle majority of the app's functionality.
"""


import math


from PyQt6 import sip
from PyQt6.QtWidgets import QLabel, QLayout

class ActionsHandler:
    """Handle Button Actions and Mathematical Operations
    """
    
    def __init__(self) -> None:
        """Handle class initialization
        """
        
        # Public Variables
        self.text = ""
        self.log = ""
        
        # Protected
        self._prev_operation = ""
        
        self._is_float = False
        self._clear_log = False
        
        self._first_value = 0
    
    # Decorators
    def prev_op_handler(prev_op: str="") -> None:
        """Set previous operation attribute and display the answer.

        Args:
            prev_op (str, optional): Operation flag. Defaults to "".
        """
        
        def decorator(func) -> None:
            
            def wrapper(self, out_line: QLabel, log_line: QLabel) -> None:
                
                func(self, out_line, log_line)
                self._prev_operation = prev_op
                self.log = self.text
                
                self._check_dot()    
                self._set_text(out_line, log_line)
                
            return wrapper
        
        return decorator
    
    # Adding Numbers to the String
    def _add_numbers(self, number: str, out_line: QLabel, 
                     log_line: QLabel) -> None:
        """Handle Number Buttons Actions
        
        Args:
            number (str): Number button text
        """
        
        op_flags = ["=", "1/x", "%", "pow", "root",
                    "fac", "2x", "10x", "ex", "log", 
                    "three", "exp"]
        
        if len(self.text) <= 12:  #float size
            if self._prev_operation in op_flags or self._clear_log: #setting up flags
                self.text = ""
                self.log = ""
                self._is_float = False
                self._clear_log = False
                self._prev_operation = ""
                
                self.text += number
                self.log += number        
            else: #direct add
                self.text += number
                self.log += number     
        
        if self.text[0] == "0":  #string can take 0 but float won't accept it
            if not self._is_float:     
                self.text = self.text[1:]   #remove 0 and copy the rest
                self.log = self.log[1:]
        
        self._set_text(out_line, log_line)
    
    # Arithmetic operations    
    def _operations_handler(self, operation: str, out_line: QLabel,
                            log_line: QLabel) -> None:
        """Handle arithmetic operations

        Args:
            operation (str): Operation button text
        """
        
        if self.text:
            # Addition
            if operation == "+": 
                self._check_first_value(operation, out_line, log_line)
        
            # Subtraction
            if operation == "-":
                self._check_first_value(operation, out_line, log_line)
            
            # Multiplication
            if operation == "*":
                self._check_first_value(operation, out_line, log_line)
            
            # Division
            if operation == "/":
                self._check_first_value(operation, out_line, log_line)
            
            if operation == "mod":
                self._check_first_value(operation, out_line, log_line)
            
            # Root
            if operation == "yroot":
                self._check_first_value(operation, out_line, log_line)
            
            # Power
            if operation == "ypow":
                self._check_first_value(operation, out_line, log_line)
            
            # Logarithm
            if operation == "ylog":
                self._check_first_value(operation, out_line, log_line)
            
            # Equation
            if operation == "=":
                #Check for Equation sign
                if self._first_value != 0:
                    self._process_log(operation, log_line)
                    self._check_prev_op(operation, out_line)

    def _check_operations(self, operation: str, out_line: QLabel) -> None:
        """Handle float check of first_value and perform type sensitive
        arithmetic operations.

        Args:
            operation (str): Arithmetic operation sign
        """
        
        if operation == "+":
            if self._is_float:
                self._first_value += float(out_line.text())
            else:
                self._first_value += int(out_line.text())
    
        elif operation == "-":
            if self._is_float:
                self._first_value -= float(out_line.text())
            else:
                self._first_value -= int(out_line.text())
    
        elif operation == "*":
            if self._is_float:
                self._first_value *= float(out_line.text())
            else:
                self._first_value *= int(out_line.text())
        
        elif operation == "/":
            if self._is_float:
                self._first_value /= float(out_line.text())
            else:
                self._first_value /= int(out_line.text())
        
        elif operation == "mod":
            if self._is_float:
                self._first_value %= float(self.text)
            else:
                self._first_value %= int(self.text)
        
        elif operation == "ylog":
            self._check_float()
                
        elif operation == "ypow":
            self._check_float()
                
        elif operation == "yroot":
            self._check_float()
    
    def _check_result(self, out_line: QLabel) -> int:
        """Handle result float check and perform type sensitivie
        arithmetic operations

        Args:
            out_line (QLabel): Output QLabel

        Returns:
            int | float: Result
        """
        
        res = 0
        
        
        if self._prev_operation == "+":
            if self._is_float:
                res = self._first_value + float(out_line.text())
            else:
                res = self._first_value + int(out_line.text())
            return res
        
        if self._prev_operation == "-":
            if self._is_float:
                res = self._first_value - float(out_line.text())
            else:
                res = self._first_value - int(out_line.text())
            return res
        
        if self._prev_operation == "*":
            if self._is_float:
                res = self._first_value * float(out_line.text())
            else:
                res = self._first_value * int(out_line.text())
            return res
        
        if self._prev_operation == "/":
            if self._is_float:
                res = self._first_value / float(out_line.text())
            else:
                res = self._first_value / int(out_line.text())
            return res

        if self._prev_operation == "mod":
            if self._is_float:
                res = self._first_value % float(out_line.text())
            else:
                res = self._first_value % int(out_line.text())
            return res
        
        if self._prev_operation == "yroot":
            if self._is_float:
                res = self._first_value ** (1 / float(self.text))
            else:
                res = self._first_value ** (1 / int(self.text))
            return res
        
        if self._prev_operation == "ylog":
            if self._is_float:
                res = round(math.log(self._first_value, float(self.text)), 2)
            else:
                res = round(math.log(self._first_value, int(self.text)), 2)
            return res
        
        if self._prev_operation == "ypow":
            if self._is_float:
                res = round(pow(self._first_value, float(self.text)), 2)
            else:
                res = round(pow(self._first_value, int(self.text)), 2)
            return res
      
    def _check_float(self) -> None:
        """Check output QLabel for float value

        Args:
            out_line (QLabel): Output QLabel
        """
        
        if self._is_float:
            self._first_value = float(self.text)
        else:
            self._first_value = int(self.text)

    def _process_calculations(self, operation: str, out_line: QLabel,
                       log_line: QLabel) -> None:
        """Process calculations for proper output in the log and 
        output QLabel.

        Args:
            operation (str): Operation sign
            out_line (QLabel): Output QLabel
            log_line (QLabel): Log QLabel
        """
        
        self._prev_operation = operation
        self.text = ""
        self._is_float = False
            
        self.log = str(self._first_value)
        if operation == "*":
            self.log += " \u00D7 "
        elif operation == "/":
            self.log += " \u00F7 "
        elif operation == "ypow":
            self.log += " ^ "
        elif operation == "ylog":
            self.log += " log base "
        elif operation == "yroot":
            self.log += "\u221A"
        else:
            self.log += f" {operation} "
        
        log_line.setText(self.log)
        out_line.setText(str(self._first_value))

    # Str-to-Float Methods
    def turn_to_float(self, out_line: QLabel, log_line: QLabel) -> None:
        """Handle number to float conversion
        """
        
        if self._prev_operation == "=":
            self._prev_operation = "."
            self._initial_float(out_line, log_line)
        
        if not self._is_float:
            if self.text:
                self.text += "."
                self.log += "."
                
                self._set_text(out_line, log_line)
                
                self._is_float = True
            else:
                self._initial_float(out_line, log_line)

    # To Percentage Method    
    def turn_to_percentage(self, out_line: QLabel, log_line: QLabel) -> None:
        """Handle number to percentage conversion
        """
        
        if self.text: #if text is not NULL
            if self._is_float: #in case of float(float type-casting needed)
                percentage = round(float(self.text) / 100, 2)
            else: #in case of int(int type-casting needed)
                percentage = round(int(self.text) / 100, 2)
            
            self._is_float = True  
            self._prev_operation = "%"
            
            self._display_answer(out_line, log_line, percentage)
    
    # Toggle number positivity
    def toggle_negativity(self, out_line: QLabel, log_line: QLabel) -> None:
        """Handle number negativity

        Args:
            out_line (QLabel): Output QLabel
            log_line (QLabel): Log QLabel
        """
        
        if self.text:
            if self._is_float:
                neg_number = -(float(self.text))
            else:
                neg_number = -(int(self.text))
            
            self._display_answer(out_line, log_line, neg_number)
    
    # Fraction
    @prev_op_handler(prev_op="1/x")
    def to_fraction(self, out_line: QLabel, log_line: QLabel) -> None:
        """Handle number to fraction conversion

        Args:
            out_line (QLabel): Output QLabel
            log_line (QLabel): Log QLabel
        """
        if self.text: #if text not equals to NULL
            if self._is_float: #for typecasting
                res = 1 / float(self.text)       
            else:
                res = 1 / int(self.text)
            
            if len(str(res)) > 10 and len(set(str(res))) > 4: #showing if same digits are repeatedly used 
                self._sci_notation(res)
            elif len(set(str(res))) <= 4: #rounding off
                self.text = str(round(res, 3))
            else:
                self.text = str(res) 
    
    # Scientific Mode Methods
    # Power of Two
    def alt_ops_handler(self, btn_text: str,
                        out_line: QLabel, log_line: QLabel) -> None:
        """Connect buttons with respective operations corresponding
           to their text

        Args:
            btn_text (str): Button label
            out_line (QLabel): Output QLabel
            log_line (QLabel): Log QLabel
        """
        
        it_x = "\U0001D465"
        it_y = "\U0001D466"
        
        ss_x = "\u02E3"
        ss_y = "\u02B8"
        ss_two = "\u00B2"
        ss_three = "\u00B3"
        
        sq_root = "\u221A"
        cube_root = "\u221B"
        
        alt_ops = [f"{it_x}{ss_two}", f"{sq_root}{it_x}", f"{it_x}{ss_y}",
                   f"10{ss_x}", "log", "ln", f"{it_x}{ss_three}", 
                   f"{cube_root}{it_x}", f"{it_y}{sq_root}{it_x}",
                   f"2{ss_x}", f"log{it_y}{it_x}", f"e{ss_x}"]
        
        if btn_text == alt_ops[0]:       #power of two
            self.pow_of_two(out_line, log_line)
        if btn_text == alt_ops[1]:       #square root of a number
            self.square_root(out_line, log_line)
        if btn_text == alt_ops[2]:       #op handler
            self._operations_handler("ypow", out_line, log_line)
        if btn_text == alt_ops[3]:       #10 to power x
            self.ten_to_x(out_line, log_line)
        if btn_text == alt_ops[4]:       #log value
            self.logarithm(out_line, log_line)
        if btn_text == alt_ops[5]:
            self.nat_log(out_line, log_line)
        if btn_text == alt_ops[6]:       #power of 3
            self.pow_of_three(out_line, log_line)
        if btn_text == alt_ops[7]:      #cube root
            self.cubed_root(out_line, log_line)
        if btn_text == alt_ops[8]:
            self._operations_handler("yroot", out_line, log_line)
        if btn_text == alt_ops[9]:      #2 raised to power x
            self.two_to_x(out_line, log_line)
        if btn_text == alt_ops[10]:
            self._operations_handler("ylog", out_line, log_line)
        if btn_text == alt_ops[11]:     #e raised to power x
            self.e_to_x(out_line, log_line)
    
    @prev_op_handler(prev_op="pow")
    def pow_of_two(self, out_line: QLabel, log_line: QLabel) -> None:
        """Handle output of a number to the power of two

        Args:
            out_line (QLabel): Output QLabel
            log_line (QLabel): Log QLabel
        """
        
        if self.text:
            if self._is_float:
                res = round(float(self.text) ** 2, 2)  
            else:
                res = round(int(self.text) ** 2, 2)
            
            self._sci_notation(res)
        
    # Square Root of a Number
    @prev_op_handler(prev_op="root")
    def square_root(self, out_line: QLabel, log_line: QLabel) -> None:
        """Handle output of a number's square root

        Args:
            out_line (QLabel): Output QLabel
            log_line (QLabel): Log QLabel
        """
        
        if self.text:
            if self._is_float:     #using sqrt, math library and rounding off to 2
                self.text = str(round(math.sqrt(float(self.text)), 2))  
            else:
                self.text = str(round(math.sqrt(int(self.text)), 2))
    
    # Bracket Insertion    
    def insert_bracket(self, bracket: str, log_line: QLabel) -> None:
        """Insert respective bracket into the log line

        Args:
            bracket (str): Bracket symbol
            log_line (QLabel): Log QLabel
        """
        
        if bracket == "(":
            self.log += "("
        else:
            self.log += ")"
        
        log_line.setText(self.log) 

    # Factorial Button Method
    def factorial(self, out_line: QLabel, log_line: QLabel) -> None:
        """Handle factorial button action and output of calculation

        Args:
            out_line (QLabel): Outputl QLabel
            log_line (QLabel): Log QLabel
        """
        
        if self.text:
            if not self._is_float:
                res = self._factorial(int(self.text))
            
                self._sci_notation(res)
                self._check_dot()
                
                self._set_text(out_line, log_line)
            else:
                self.log = "Only integers!"
                
                log_line.setText(self.log)
                
            self._prev_operation = "fac"
    
    # Factorial Calculation
    def _factorial(self, number: int) -> int:
        """Return factorial of a number

        Args:
            number (int): Number

        Returns:
            int: Answer
        """
        
        if number == 0:
            return 1
        else:
            return number * self._factorial(number - 1)
    
    # Absolute Button method    
    def absolute(self, out_line: QLabel, log_line: QLabel) -> None:
        """Convert number to its absolute value

        Args:
            out_line (QLabel): Output QLabel
            log_line (QLabel): Log QLabel
        """
        
        if self.text:
            if self._is_float:
                self.text = str(abs(float(self.text)))
            else:
                self.text = str(abs(int(self.text)))
            
            self.log = self.text
            
            self._set_text(out_line, log_line)
    
    # Logarithm Button method
    @prev_op_handler(prev_op="log")
    def logarithm(self, out_line: QLabel, log_line: QLabel) -> None:
        """Output a logarithm of a number with base 10

        Args:
            out_line (QLabel): Output QLabel
            log_line (QLabel): Log QLabel
        """
        
        if self.text:
            if self._is_float:
                res = round(math.log(float(self.text), 10), 2)
            else:
                res = round(math.log(int(self.text), 10), 2)
            
            self._sci_notation(res)
    
    # Natural Logarithm Button method
    @prev_op_handler(prev_op="ln")
    def nat_log(self, out_line: QLabel, log_line: QLabel) -> None:
        """Output a natural logarithm of a number

        Args:
            out_line (QLabel): Output QLabel
            log_line (QLabel): Log QLabel
        """
        
        if self.text:
            if self._is_float:
                res = round(math.log(float(self.text)), 2)
            else:
                res = round(math.log(int(self.text)), 2)
            
            self._sci_notation(res)
    
    # Two to the Power of X Button method
    @prev_op_handler(prev_op="2x")
    def two_to_x(self, out_line: QLabel, log_line: QLabel) -> None:
        """Output 2 to the power of a number

        Args:
            out_line (QLabel): Output QLabel
            log_line (QLabel): Log QLabel
        """
        
        if self.text:
            if self._is_float:
                res = 2 ** float(self.text)
            else:
                res = 2 ** int(self.text)
            
            self._sci_notation(res)
    
    # Ten to the Power of X Button method
    @prev_op_handler(prev_op="10x")
    def ten_to_x(self, out_line: QLabel, log_line: QLabel) -> None:
        """Output 10 to the power of a number

        Args:
            out_line (QLabel): Output QLabel
            log_line (QLabel): Log QLabel
        """
        
        if self.text:
            if self._is_float:
                res = 10 ** float(self.text)
            else:
                res = 10 ** int(self.text)
            
            self._sci_notation(res)
    
    # e to the Power of X Button method   
    @prev_op_handler(prev_op="ex") 
    def e_to_x(self, out_line: QLabel, log_line: QLabel) -> None:
        """Output e to the power of a number

        Args:
            out_line (QLabel): Output QLabel
            log_line (QLabel): Log QLabel
        """
        
        if self.text:
            if self._is_float:
                res = math.e ** float(self.text)
            else:
                res = math.e ** int(self.text)
            
            self._sci_notation(res)
    
    # Power of Three Button method   
    @prev_op_handler(prev_op="three") 
    def pow_of_three(self, out_line: QLabel, log_line: QLabel) -> None:
        """Output a number to the power of three

        Args:
            out_line (QLabel): Output QLabel
            log_line (QLabel): Log QLabel
        """
        
        if self.text:
            if self._is_float:
                res = round(float(self.text) ** 3, 2)
            else:
                res = round(int(self.text) ** 3, 2)
            
            self._sci_notation(res)
    
    # Cubet root Button method
    @prev_op_handler(prev_op="root")   
    def cubed_root(self, out_line: QLabel, log_line: QLabel) -> None:
        """Output a cubic root of a number

        Args:
            out_line (QLabel): _description_
            log_line (QLabel): _description_
        """
        
        if self.text:
            if self._is_float:
                if float(self.text) < 0:
                    self.text = abs(float(self.text))
                    self.text = str(round(self.text ** 1/3, 2))
                else:
                    self.text = str(round(float(self.text) ** 1/3, 2))
            else:
                if int(self.text) < 0:
                    self.text = abs(int(self.text))
                    self.text = str(round(int(self.text) ** 1/3, 2))
                else:
                    self.text = str(round(int(self.text) ** 1/3, 2)) 
    
    # Exponent Button method        
    @prev_op_handler(prev_op="exp") 
    def exponent(self, out_line: QLabel, log_line: QLabel) -> None:
        """Handle exponent of a number

        Args:
            out_line (QLabel): Output QLabel
            log_line (QLabel): Log QLabel
        """
        
        if self.text:
            if self._is_float:
                res = math.exp(float(self.text))
            else:
                res = math.exp(int(self.text))
            
            self._sci_notation(res)
    
    # pi Button method        
    def print_pi(self, out_line: QLabel, log_line: QLabel) -> None:
        """Output the pi number

        Args:
            out_line (QLabel): Output QLabel
            log_line (QLabel): Log QLabel
        """
        
        pi = round(math.pi, 5)
        
        self._display_constants(pi, out_line, log_line)
    
    # e Button method
    def print_e(self, out_line: QLabel, log_line: QLabel) -> None:
        """Print the e constant

        Args:
            out_line (QLabel): Output QLabel
            log_line (QLabel): Log QLabel
        """
        
        e = round(math.e, 5)
        
        self._display_constants(e, out_line, log_line)
    
    # Checker helper methods
    def _check_dot(self):
        """Check if there is dot in the Output QLabel
        """

        if "." in self.text:
            self._is_float = True
    
    def _check_prev_op(self, operation: str, out_line: QLabel) -> None:
        """Check if previous operation was equal sign.

        Args:
            operation (str): Operation flag
            out_line (QLabel): Output QLabel
        """
        
        if self._prev_operation != "=":
            res = self._check_result(out_line)
                        
            self._sci_notation(res)
                        
            self._prev_operation = operation
            self._check_dot()
                        
            out_line.setText(self.text)
            self._first_value = 0

    def _check_first_value(self, operation: str, 
                           out_line: QLabel, log_line: QLabel) -> None:
        """Check the current value of the first_value attribute.

        Args:
            operation (str): Operation flag
            out_line (QLabel): Output QLabel
            log_line (QLabel): Log QLabel
        """
        
        if self._first_value != 0:
            self._check_operations(operation, out_line)
        else:
            self._check_float(out_line)
                
        self._process_calculations(operation, out_line, log_line)
    
    # Processer helper methods        
    def _sci_notation(self, res):
        """Format output line to the scientific notation

        Args:
            res ([type]): Number
        """
        
        if len(str(res)) > 10:
            self.text = "{:e}".format(res)
        elif "." in str(res):
            self.text = str(round(res, 2))
        else:
            self.text = str(res)
    
    def _initial_float(self, out_line: QLabel, log_line: QLabel) -> None:
        """Set initial float value when Output QLabel is empty.

        Args:
            out_line (QLabel): Output QLabel
            log_line (QLabel): Log QLabel
        """
        
        self.text = "0."
        self.log = "0."
                
        self._set_text(out_line, log_line)
                
        self._is_float = True
    
    def _process_log(self, operation: str, log_line: QLabel) -> None:
        """Process log QLabel for proper output when equal sign button is pressed.

        Args:
            operation (str): Operation flag
            log_line (QLabel): Log QLabel
        """
        
        if self.log[-1] == "=":
            log_line.setText(self.log)
        elif self.log[-1] != self._prev_operation:
            self.log += operation
            log_line.setText(self.log)
        else:
            self.log += str(self._first_value)
            self.log += operation
            log_line.setText(self.log)
    
    # Display helper methods
    def _display_constants(self, const: float, 
                            out_line: QLabel, log_line: QLabel) -> None:
            """Handle display of constants in the calculator.

            Args:
                const (float): Constant
                out_line (QLabel): Output QLabel
                log_line (QLabel): Log QLabel
            """
            
            op_flags = ["=", "1/x", "%", "pow", "root",
                        "fac", "2x", "10x", "ex", "exp", 
                        "log", "three"]
            
            if self._prev_operation in op_flags or self._clear_log\
                or str(math.e) in self.log or str(math.pi) in self.log:
                self.text = str(const)
                self.log = str(const)
                
                self._is_float = True
                self._clear_log = False            
            else:
                self.text = str(const)
                self.log += str(const)
                
                self._is_float = True
            
            self._set_text(out_line, log_line)
    
    def _display_answer(self, out_line: QLabel, log_line: QLabel, value) -> None:
        """Display calculation answer on Output QLabel and Log QLabel

        Args:
            out_line (QLabel): Output QLabel
            log_line (QLabel): Log Qlabel
            value (int | float): Calculation value
        """
        
        self.text = str(value)
        self.log = self.text
            
        self._set_text(out_line, log_line)

    def _set_text(self, out_line: QLabel, log_line: QLabel) -> None:
        """Set self.text and self.log attributes as Output and Log
        QLabel text.

        Args:
            out_line (QLabel): Output QLabel
            log_line (QLabel): Log QLabel
        """
        
        out_line.setText(self.text)
        log_line.setText(self.log)
    
    #Clearing Output QLabel and Log QLabel       
    def clear_text(self, out_line: QLabel, log_line: QLabel) -> None:
        """Clear both Output and Log QLabels.
        
        Args:
            out_line (Qlabel): Output QLabel
            log_line (Qlabel): Log QLabel
        """
        
        self.text = ""
        self.log = ""
        self._first_value = 0
        self._is_float = False
        
        out_line.setText(self.text)
        log_line.setText(self.log)
        
    def clear_output(self, out_line: QLabel) -> None:
        """Clear Output QLabel
        
        Args:
            out_line (QLabel): Output QLabel
        """
        
        self.text = ""
        self._is_float = False
        
        if self._prev_operation == ""\
            or self._prev_operation == "=":
            self._clear_log = True
        else:
            self._clear_log = False
        
        out_line.setText(self.text)
        
    def erase(self, out_line: QLabel, log_line: QLabel) -> None:
        """Erase one symbol at a time

        Args:
            out_line (QLabel): Output QLabel
            log_line (QLabel): Log QLabel
        """
        
        self.text = self.text[:-1]
        self.log = self.log[:-1]
        
        out_line.setText(self.text)
        log_line.setText(self.log)
        
    def reset_calculator(self, out_line: QLabel, 
                         log_line: QLabel) -> None:
        """Reset calculator public variables
        """
        
        self._prev_operation = ""
        self._is_float = False
        self._clear_log = False
        self._first_value = 0
        self.log = ""
        self.text = ""
        
        out_line.setText(self.text)
        log_line.setText(self.log)
    
    # Deleting widgets from the layout   
    def delete_widgets(self, layout: QLayout) -> None:
        """Delete widgets within layout and layout itself

        Args:
            layout (QLayout): App's current layout
        """
        
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.delete_widgets(item.layout())
            sip.delete(layout)
