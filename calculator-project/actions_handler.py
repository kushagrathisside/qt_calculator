from math import sqrt


from PyQt6.QtWidgets import QLabel


class ActionsHandler:
    
    def __init__(self) -> None:
        
        #Public Variables
        self.text = ""
        self.log = ""
        
        #Private
        self._prev_operation = ""
        
        self._is_float = False
        self._clear_log = False
        
        self._first_value = 0
    
    #Adding Numbers to the String
    def _add_numbers(self, number: str, out_line: QLabel, 
                     log_line: QLabel) -> None:
        """Adding numbers to the calculator screen

        Args:
            number (str): Number button text
        """
        
        if len(self.text) <= 10:
            if self._prev_operation == "=" or self._clear_log:
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
                    res = self._check_result(operation, out_line)

                    self._prev_operation = operation
                    self.text = str(round(res, 1))
                    
                    out_line.setText(self.text)
                    self._first_value = 0

    def _check_operations(self, operation: str, out_line: QLabel) -> None:
        """Handles float check of first_value

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
    
    def _check_result(self, operation: str, out_line: QLabel):
        
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
    def _turn_to_float(self, out_line: QLabel, log_line: QLabel) -> None:
        """Turns number to float
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
        
        self.text = "0."
        self.log = "0."
                
        out_line.setText(self.text)
        log_line.setText(self.log)
                
        self._is_float = True
        
    def _turn_to_percentage(self, out_line: QLabel, log_line: QLabel) -> None:
        """Turns number to percentage
        """
        if self.text:
            if self._is_float:
                percentage = float(self.text) / 100
            else:
                percentage = int(self.text) / 100
            
            self._is_float = True
            self.text = str(percentage)
            self.log = str(percentage)
            
            out_line.setText(self.text)
            log_line.setText(self.log)
    
    #Toggle number positivity
    def _toggle_negativity(self, out_line: QLabel, log_line: QLabel) -> None:
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
    def _to_fraction(self, out_line: QLabel, log_line: QLabel) -> None:
        
        if self._is_float:
            self.text = str(1 / float(self.text))
            self.log = str(1 / float(self.log))
        else:
            self.text = str(1 / int(self.text))
            self.log = str(1 / int(self.log))
        
        self._is_float = True
        
        out_line.setText(self.text)
        log_line.setText(self.log)
    
    #Power of Two
    def _pow_of_two(self, out_line: QLabel, log_line: QLabel) -> None:
        
        if self._is_float:
            self.text = str(float(self.text) ** 2)
            self.log = str(float(self.log) ** 2)
        else:
            self.text = str(int(self.text) ** 2)
            self.log = str(int(self.log) ** 2)
        
        out_line.setText(self.text)
        log_line.setText(self.log)
        
    #Square Root of a Number
    def _square_root(self, out_line: QLabel, log_line: QLabel) -> None:
        
        if self._is_float:
            self.text = str(sqrt(float(self.text)))
            self.log = str(sqrt(float(self.log)))
        else:
            self.text = str(sqrt(int(self.text)))
            self.log = str(sqrt(int(self.log)))
        
        out_line.setText(self.text)
        log_line.setText(self.log)
     
    #Clearing Output QLabel and Log QLabel       
    def _clear_text(self, out_line: QLabel, log_line: QLabel) -> None:
        """Clears calculator screen
        """
        
        self.text = ""
        self.log = ""
        self._first_value = 0
        self._is_float = False
        
        out_line.setText(self.text)
        log_line.setText(self.log)
        
    def _clear_output(self, out_line: QLabel) -> None:
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
        
    def _erase(self, out_line: QLabel, log_line: QLabel) -> None:
        
        self.text = self.text[:-1]
        self.log = self.log[:-1]
        
        out_line.setText(self.text)
        log_line.setText(self.text)
