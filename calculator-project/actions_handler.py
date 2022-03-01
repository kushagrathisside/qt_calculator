import math


from PyQt6.QtWidgets import QLabel


class ActionsHandler:
    """Handles Button Actions and Mathematical Operations
    """
    
    def __init__(self) -> None:
        """Handles class initialization
        """
        
        # Public Variables
        self.text = ""
        self.log = ""
        
        # Protected
        self._prev_operation = ""
        
        self._is_float = False
        self._clear_log = False
        
        self._first_value = 0
    
    #Adding Numbers to the String
    def _add_numbers(self, number: str, out_line: QLabel, 
                     log_line: QLabel) -> None:
        """Handles Number Buttons Actions
        
        Args:
            number (str): Number button text
        """
        
        op_flags = ["=", "1/x", "%", "pow", "root",
                    "fac", "2x", "10x", "exp", "log", 
                    "three"]
        
        if len(self.text) <= 12:
            if self._prev_operation in op_flags or self._clear_log:
                self.text = ""
                self.log = ""
                self._is_float = False
                self._clear_log = False
                self._prev_operation = ""
                
                self.text += number
                self.log += number        
            else:
                self.text += number
                self.log += number     
        
        if self.text[0] == "0":
            if not self._is_float:
                self.text = self.text[1:]
                self.log = self.log[1:]
        
        out_line.setText(self.text)
        log_line.setText(self.log)
    
    #Arithmetic operations    
    def _operations_handler(self, operation: str, out_line: QLabel,
                            log_line: QLabel) -> None:
        """Handles arithmetic operations

        Args:
            operation (str): Operation button text
        """
        
        if self.text:
            # Addition
            if operation == "+":
                if self._first_value != 0:
                    self._check_operations(operation, out_line)
                else:
                    self._check_float(out_line)
                
                self._op_set_values(operation, out_line, log_line)
        
            # Subtraction
            if operation == "-":
                if self._first_value != 0:
                    self._check_operations(operation, out_line)
                else:
                    self._check_float(out_line)
                
                self._op_set_values(operation, out_line, log_line)
            
            # Multiplication
            if operation == "*":
                if self._first_value != 0:
                    self._check_operations(operation, out_line)
                else:
                    self._check_float(out_line)
                
                self._op_set_values(operation, out_line, log_line)
            
            # Division
            if operation == "/":
                if self._first_value != 0:
                    self._check_operations(operation, out_line)
                else:
                    self._check_float(out_line)
                
                self._op_set_values(operation, out_line, log_line)
            
            if operation == "mod":
                if self._first_value != 0:
                    self._check_operations(operation, out_line)
                else:
                    self._check_float(out_line)
                
                self._op_set_values(operation, out_line, log_line)
            
            # Root
            if operation == "yroot":
                if self._first_value != 0:
                    self._check_operations(operation, out_line)
                else:
                    self._check_float(out_line)
                
                self._op_set_values(operation, out_line, log_line)
            
            # Power
            if operation == "ypow":
                if self._first_value != 0:
                    self._check_operations(operation, out_line)
                else:
                    self._check_float(out_line)
                
                self._op_set_values(operation, out_line, log_line)
            
            # Logarithm
            if operation == "ylog":
                if self._first_value != 0:
                    self._check_operations(operation, out_line)
                else:
                    self._check_float(out_line)
                
                self._op_set_values(operation, out_line, log_line)
            
            # Equation
            if operation == "=":
                #Check for Equation sign
                if self._first_value != 0:
                    if self.log[-1] == "=":
                        log_line.setText(self.log)
                    elif self.log[-1] != self._prev_operation:
                        self.log += operation
                        log_line.setText(self.log)
                    else:
                        self.log += str(self._first_value)
                        self.log += operation
                        log_line.setText(self.log)
                    
                    if self._prev_operation != "=":
                        res = self._check_result(out_line)
                        
                        self._sci_notation(res)
                        
                        self._prev_operation = operation
                        self._check_dot()
                        
                        out_line.setText(self.text)
                        self._first_value = 0

    def _check_operations(self, operation: str, out_line: QLabel) -> None:
        """Handles float check of first_value and performs type sensitive
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
            if self._is_float:
                self._first_value = float(self.text)
            else:
                self._first_value = int(self.text)
                
        elif operation == "ypow":
            if self._is_float:
                self._first_value = float(self.text)
            else:
                self._first_value = int(self.text)
                
        elif operation == "yroot":
            if self._is_float:
                self._first_value = float(self.text)
            else:
                self._first_value = int(self.text)
    
    def _check_result(self, out_line: QLabel) -> int:
        """Handles result float check and performs type sensitivie
        arithmetic operations

        Args:
            out_line (QLabel): Output Line

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
      
    def _check_float(self, out_line: QLabel) -> None:
        
        if self._is_float:
            self._first_value = float(out_line.text())
        else:
            self._first_value = int(out_line.text())

    def _op_set_values(self, operation: str, out_line: QLabel,
                       log_line: QLabel) -> None:
        """Handles multiplication and division operations

        Args:
            operation (str): Operation sign
            out_line (QLabel): Output Line
            log_line (QLabel): Log Line
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

    #Str-to-Float functions
    def turn_to_float(self, out_line: QLabel, log_line: QLabel) -> None:
        """Handles number to float conversion
        """
        
        if self._prev_operation == "=":
            self._prev_operation = "."
            self._initial_float(out_line, log_line)
        
        if not self._is_float:
            if self.text:
                self.text += "."
                self.log += "."
                
                out_line.setText(self.text)
                log_line.setText(self.log)
                
                self._is_float = True
            else:
                self._initial_float(out_line, log_line)

    def _initial_float(self, out_line: QLabel, log_line: QLabel) -> None:
        """Handles Dot Button press on empty Output Line

        Args:
            out_line (QLabel): Output Line
            log_line (QLabel): Log Line
        """
        
        self.text = "0."
        self.log = "0."
                
        out_line.setText(self.text)
        log_line.setText(self.log)
                
        self._is_float = True
        
    def turn_to_percentage(self, out_line: QLabel, log_line: QLabel) -> None:
        """Handles number to percentage conversion
        """
        
        if self.text:
            if self._is_float:
                percentage = round(float(self.text) / 100, 2)
            else:
                percentage = round(int(self.text) / 100, 2)
            
            self._is_float = True
            self._prev_operation = "%"
            
            self.text = str(percentage)
            self.log = str(percentage)
            
            out_line.setText(self.text)
            log_line.setText(self.log)
    
    #Toggle number positivity
    def toggle_negativity(self, out_line: QLabel, log_line: QLabel) -> None:
        """Handles number negativity

        Args:
            out_line (QLabel): Output Line
            log_line (QLabel): Log Line
        """
        
        if self.text:
            if self._is_float:
                neg_number = -(float(self.text))
            else:
                neg_number = -(int(self.text))
            
            self.text = str(neg_number)
            self.log = str(neg_number)
            
            out_line.setText(self.text)
            log_line.setText(self.log)
    
    #Fraction
    def to_fraction(self, out_line: QLabel, log_line: QLabel) -> None:
        """Handles number to fraction conversion

        Args:
            out_line (QLabel): [description]
            log_line (QLabel): [description]
        """
        if self.text:
            if self._is_float:
                self.text = str(round(1 / float(self.text), 2))         
            else:
                self.text = str(round(1 / int(self.text), 2))  
            
            self._prev_operation = "1/x"
            self.log = self.text
            self._check_dot()
            
            out_line.setText(self.text)
            log_line.setText(self.log)
    
    #Power of Two
    def pow_of_two(self, out_line: QLabel, log_line: QLabel) -> None:
        """Handles output of number to the power of two

        Args:
            out_line (QLabel): Output Line
            log_line (QLabel): Log Line
        """
        
        if self.text:
            if self._is_float:
                res = round(float(self.text) ** 2, 2)  
            else:
                res = round(int(self.text) ** 2, 2)
            
            self._sci_notation(res)
            
            self.log = self.text
            self._check_dot()
            self._prev_operation = "pow"
            
            out_line.setText(self.text)
            log_line.setText(self.log)
        
    #Square Root of a Number
    def square_root(self, out_line: QLabel, log_line: QLabel) -> None:
        """Handles output of number's square root

        Args:
            out_line (QLabel): Output Line
            log_line (QLabel): Log Line
        """
        
        if self.text:
            if self._is_float:
                self.text = str(round(math.sqrt(float(self.text)), 2))
            else:
                self.text = str(round(math.sqrt(int(self.text)), 2))
                
            self.log = self.text
            self._check_dot()
            self._prev_operation = "root"
            
            out_line.setText(self.text)
            log_line.setText(self.log)
    
    # Helper Methods
    def _check_dot(self):
        """Checks if there is dot in the Output Line
        """
        

        if "." in self.text:
            self._is_float = True
            
    def _sci_notation(self, res):
        """Format's output line to scientific notation

        Args:
            res ([type]): Number
        """
        
        if len(str(res)) > 10:
            self.text = "{:e}".format(res)
        elif "." in str(res):
            self.text = str(round(res, 2))
        else:
            self.text = str(res)
    
    #Clearing Output QLabel and Log QLabel       
    def clear_text(self, out_line: QLabel, log_line: QLabel) -> None:
        """Clears calculator screen
        """
        
        self.text = ""
        self.log = ""
        self._first_value = 0
        self._is_float = False
        
        out_line.setText(self.text)
        log_line.setText(self.log)
        
    def clear_output(self, out_line: QLabel) -> None:
        """Clears output line
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
        """Erases one digit at a time

        Args:
            out_line (QLabel): Output Line
            log_line (QLabel): Log Line
        """
        
        self.text = self.text[:-1]
        self.log = self.log[:-1]
        
        out_line.setText(self.text)
        log_line.setText(self.log)
        
    def insert_bracket(self, bracket: str, log_line: QLabel) -> None:
        """Inserts brackets into the log line

        Args:
            bracket (str): Bracket symbol
            log_line (QLabel): Log line
        """
        
        if bracket == "(":
            self.log += "("
        else:
            self.log += ")"
        
        log_line.setText(self.log) 
        
    def factorial(self, out_line: QLabel, log_line: QLabel) -> None:
        """Handles factorial button action

        Args:
            out_line (QLabel): Outputl Label
            log_line (QLabel): Log Label
        """
        
        if self.text:
            if not self._is_float:
                res = self._factorial(int(self.text))
            
            self._sci_notation(res)
            self._prev_operation = "fac"
            self._check_dot()
            
            out_line.setText(self.text)
            log_line.setText(self.log)
            
    def _factorial(self, number: int) -> int:
        """Returns factorial of a number

        Args:
            number (int): Number

        Returns:
            int: Answer
        """
        
        if number == 0:
            return 1
        else:
            return number * self._factorial(number - 1)
        
    def absolute(self, out_line: QLabel, log_line: QLabel) -> None:
        """Handles absolute numbers

        Args:
            out_line (QLabel): Output Label
            log_line (QLabel): Log Label
        """
        
        if self.text:
            if self._is_float:
                self.text = str(abs(float(self.text)))
            else:
                self.text = str(abs(int(self.text)))
            
            self.log = self.text
            
            out_line.setText(self.text)
            log_line.setText(self.log)
        
    def logarithm(self, out_line: QLabel, log_line: QLabel) -> None:
        """Outputs a logarithm of a number with base 10

        Args:
            out_line (QLabel): Output Label
            log_line (QLabel): Log Label
        """
        
        if self.text:
            if self._is_float:
                res = round(math.log(float(self.text), 10), 2)
            else:
                res = round(math.log(int(self.text), 10), 2)
            
            self._sci_notation(res)
            
            self.log = self.text
            self._prev_operation = "log"
            self._check_dot()
            
            out_line.setText(self.text)
            log_line.setText(self.log)
    
    def nat_log(self, out_line: QLabel, log_line: QLabel) -> None:
        """Outputs a natural logarithm of a number

        Args:
            out_line (QLabel): Output Label
            log_line (QLabel): Log Label
        """
        
        if self.text:
            if self._is_float:
                res = round(math.log(float(self.text)), 2)
            else:
                res = round(math.log(int(self.text)), 2)
            
            self._sci_notation(res)
            
            self.log = self.text
            self._prev_operation = "log"
            self._check_dot()
            
            out_line.setText(self.text)
            log_line.setText(self.log)
      
    def two_to_x(self, out_line: QLabel, log_line: QLabel) -> None:
        """Outputs 2 to the power of a number

        Args:
            out_line (QLabel): Output Label
            log_line (QLabel): Log Label
        """
        
        if self.text:
            if self._is_float:
                res = 2 ** float(self.text)
            else:
                res = 2 ** int(self.text)
            
            self._sci_notation(res)
            
            self.log = self.text
            self._prev_operation = "2x"
            self._check_dot()
            
            out_line.setText(self.text)
            log_line.setText(self.log)
        
    def ten_to_x(self, out_line: QLabel, log_line: QLabel) -> None:
        """Outputs 10 to the power of a number

        Args:
            out_line (QLabel): Output Label
            log_line (QLabel): Log Label
        """
        
        if self.text:
            if self._is_float:
                res = 10 ** float(self.text)
            else:
                res = 10 ** int(self.text)
            
            self._sci_notation(res)
            
            self.log = self.text
            self._prev_operation = "10x"
            self._check_dot()
            
            out_line.setText(self.text)
            log_line.setText(self.log)
        
    def e_to_x(self, out_line: QLabel, log_line: QLabel) -> None:
        """Outputs e to the power of a number

        Args:
            out_line (QLabel): Output Label
            log_line (QLabel): Log Label
        """
        
        if self.text:
            if self._is_float:
                res = math.e ** float(self.text)
            else:
                res = math.e ** int(self.text)
            
            self._sci_notation(res)
            
            self.log = self.text
            self._prev_operation = "ex"
            self._check_dot()
            
            out_line.setText(self.text)
            log_line.setText(self.log)
        
    def pow_of_three(self, out_line: QLabel, log_line: QLabel) -> None:
        """Outputs number to the power of three

        Args:
            out_line (QLabel): Output Label
            log_line (QLabel): Log Label
        """
        
        if self.text:
            if self._is_float:
                res = round(float(self.text) ** 3, 2)
            else:
                res = round(int(self.text) ** 3, 2)
            
            self._sci_notation(res)
            
            self.log = self.text
            self._prev_operation = "three"
            self._check_dot()
            
            out_line.setText(self.text)
            log_line.setText(self.log)
        
    def cubed_root(self, out_line: QLabel, log_line: QLabel) -> None:
        """Outputs a cubic root of a number

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
             
            self.log = self.text
            self._check_dot()
            self._prev_operation = "root"
            
            out_line.setText(self.text)
            log_line.setText(self.log)
             
    def exponent(self, out_line: QLabel, log_line: QLabel) -> None:
        """Handles exponent of a number

        Args:
            out_line (QLabel): Output Label
            log_line (QLabel): Log Label
        """
        
        if self.text:
            if self._is_float:
                res = math.exp(float(self.text))
            else:
                res = math.exp(int(self.text))
            
            self._sci_notation(res)
            
            self.log = self.text
            self._prev_operation = "exp"
            self._check_dot()
            
            out_line.setText(self.text)
            log_line.setText(self.log)
            
    def print_pi(self, out_line: QLabel, log_line: QLabel) -> None:
        
        op_flags = ["=", "1/x", "%", "pow", "root",
                    "fac", "2x", "10x", "exp", "log", 
                    "three"]
        
        pi = round(math.pi, 5)
        
        if self._prev_operation in op_flags or self._clear_log:
            self.text = str(pi)
            self.log = str(pi)
            
            self._is_float = True
            self._clear_log = False
            self._prev_operation = ""        
        else:
            self.text = str(pi)
            self.log += str(pi)
            
            self._is_float = True
        
        out_line.setText(self.text)
        log_line.setText(self.log)

    def print_e(self, out_line: QLabel, log_line: QLabel) -> None:
        
        op_flags = ["=", "1/x", "%", "pow", "root",
                    "fac", "2x", "10x", "exp", "log", 
                    "three"]
        
        e = round(math.e, 5)
        
        if self._prev_operation in op_flags or self._clear_log:
            self.text = str(e)
            self.log = str(e)
            
            self._is_float = True
            self._clear_log = False
            self._prev_operation = ""        
        else:
            self.text = str(e)
            self.log += str(e)
            
            self._is_float = True
            
        out_line.setText(self.text)
        log_line.setText(self.log)