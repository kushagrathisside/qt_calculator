from math import sqrt


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
        
        op_flags = ["=", "1/x", "%", "pow", "sqrt"]
        
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
            #Addition
            if operation == "+":
                if self._first_value != 0:
                    self._check_operations(operation, out_line)
                else:
                    self._check_float(out_line)
                
                self._op_set_values(operation, out_line, log_line)
        
            #Subtraction
            if operation == "-":
                if self._first_value != 0:
                    self._check_operations(operation, out_line)
                else:
                    self._check_float(out_line)
                
                self._op_set_values(operation, out_line, log_line)
            
            #Multiplication
            if operation == "*":
                if self._first_value != 0:
                    self._check_operations(operation, out_line)
                else:
                    self._check_float(out_line)
                
                self._op_set_values(operation, out_line, log_line)
            
            #Division
            if operation == "/":
                if self._first_value != 0:
                    self._check_operations(operation, out_line)
                else:
                    self._check_float(out_line)
                
                self._op_set_values(operation, out_line, log_line)
            
            #Equation
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
            self.log += "\u00D7"
        elif operation == "/":
            self.log += "\u00F7"
        else:
            self.log += operation
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
                res = round(float(self.text) ** 2)  
            else:
                res = round(int(self.text) ** 2)
            
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
                self.text = str(round(sqrt(float(self.text)), 2))
            else:
                self.text = str(round(sqrt(int(self.text)), 2))
                
            self.log = self.text
            self._check_dot()
            self._prev_operation = "sqrt"
            
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
