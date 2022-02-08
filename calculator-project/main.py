#Standard Modules
import sys


#Third-Party Modules
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtWidgets import (QApplication, QGridLayout, QLabel, 
                             QMenuBar, QPushButton, QVBoxLayout, 
                             QWidget)

# "\u221A\u1D465" <- square root
# "\u1D465\N{SUPERSCRIPT TWO}" <- power of two
# "\u232B" <- Erase
# "1/\u1D465" <- 1/x

class MainWindow(QWidget):
    """Calculator's Main Window

    Args:
        QWidget ([type]): QWidget Parent Class
    """
    
    def __init__(self) -> None:
        """Class Initialization
        """
        
        super().__init__()
        
        self.prev_operation = ""
        self.first_value = 0
        self.is_float = False
        self.clear_log = False
        
        self._window_settings()
        
        layout = self._main_layout()
        
        self.setLayout(layout)
        
    def _window_settings(self) -> None:
        """Window Settings
        """
        
        self.setWindowIcon(QIcon("icons/calculator.png"))
        self.setWindowTitle("Калькулятор Morrison")
        self.setFixedSize(330, 400)
        
    def _main_layout(self) -> QVBoxLayout:
        """Calculator's Window Layout

        Returns:
            QVBoxLayout: Vertical Layout
        """
        
        vbox = QVBoxLayout()
        self.text = ""
        self.log = ""
        
        self.log_line = QLabel(self.log)
        self.log_line.setFixedSize(300, 22)
        self.log_line.setAlignment(Qt.AlignmentFlag.AlignRight 
                                   | Qt.AlignmentFlag.AlignBottom)
        self.log_line.setFont(QFont("Times", 18))
        
        self.output_line = QLabel(self.text)
        self.output_line.setFixedSize(300, 40)
        self.output_line.setAlignment(Qt.AlignmentFlag.AlignRight 
                                      | Qt.AlignmentFlag.AlignBottom)
        self.output_line.setFont(QFont("Times", 30))
        
        grid = self._grid_layout()
        
        vbox.addWidget(self.log_line)
        vbox.addWidget(self.output_line)
        vbox.addLayout(grid)
        vbox.setContentsMargins(10, 10, 10, 10)
        
        return vbox
        
    def _grid_layout(self) -> QGridLayout:
        """Buttons Grid Layout

        Returns:
            QGridLayout: Grid Layout
        """
        
        grid = QGridLayout()
        
        #Number Buttons
        one_btn = self._numbers_btns_init(1)
        two_btn = self._numbers_btns_init(2)
        three_btn = self._numbers_btns_init(3)
        four_btn = self._numbers_btns_init(4)
        five_btn = self._numbers_btns_init(5)
        six_btn = self._numbers_btns_init(6)
        seven_btn = self._numbers_btns_init(7)
        eight_btn = self._numbers_btns_init(8)
        nine_btn = self._numbers_btns_init(9)
        zero_btn = self._numbers_btns_init(0)
        
        #Sign Buttons
        add_btn, sub_btn, mult_btn, div_btn, equal_btn,\
            pos_neg_btn, prcnt_btn, clear_btn, ce_btn,\
                dot_btn = self._sign_btns_init()
        
        #Adding Buttons to a Grid
        buttons = [prcnt_btn, ce_btn, clear_btn, add_btn,
                   one_btn, two_btn, three_btn, sub_btn,
                   four_btn, five_btn, six_btn, mult_btn,
                   seven_btn, eight_btn, nine_btn, div_btn,
                   pos_neg_btn, zero_btn, dot_btn, equal_btn]
        
        count = 0
        for row in range(0, 5):
            for col in range(0, 4):
                grid.addWidget(buttons[row + col + count], row, col)
            count += 3
        
        return grid

    #Button Initializers
    def _sign_btns_init(self) -> QPushButton:
        """Creating buttons for signs

        Returns:
            QPushButton: Buttons
        """
        
        add_btn = self._op_btns_init("+")
        sub_btn = self._op_btns_init("-")
        mult_btn = self._op_btns_init("\u00D7")
        div_btn = self._op_btns_init("\u00F7")  
        equal_btn = self._op_btns_init("=")
        
        pos_neg_btn = QPushButton("\u00B1")
        pos_neg_btn.setMinimumSize(75, 50)
        pos_neg_btn.clicked.connect(self._toggle_pos_neg)
        
        dot_btn = QPushButton(".")
        dot_btn.setMinimumSize(75, 50)
        dot_btn.clicked.connect(self._turn_to_float)
        
        prcnt_btn = QPushButton("%")
        prcnt_btn.setMinimumSize(75, 50)
        prcnt_btn.clicked.connect(self._turn_to_percentage)
        
        clear_btn = QPushButton("C")
        clear_btn.setMinimumSize(75, 50)
        clear_btn.clicked.connect(self._clear_text)
        
        ce_btn = QPushButton("CE")
        ce_btn.setMinimumSize(75, 50)
        ce_btn.clicked.connect(self._clear_output)
        
        return add_btn, sub_btn, mult_btn, div_btn, equal_btn,\
            pos_neg_btn, prcnt_btn, clear_btn, ce_btn,\
            dot_btn

    #Operation Buttons Initializer
    def _op_btns_init(self, operation: str) -> QPushButton:
        """Handles operation buttons

        Args:
            operation (str): Operation sign

        Returns:
            QPushButton: Operation button
        """
        
        op_btn = QPushButton(operation)
        op_btn.setMinimumSize(75, 50)
        op_btn.clicked.connect(lambda: self._operations_handler(op_btn.text()))
        
        return op_btn
    
    #Number Buttons Initializer
    def _numbers_btns_init(self, number: int) -> QPushButton:
        """Handles number buttons creation

        Args:
            number (int): Number from 0 to 9

        Returns:
            QPushButton: Button
        """
        
        num_btn = QPushButton(str(number))
        num_btn.setMinimumSize(75, 50)
        num_btn.clicked.connect(lambda: self._add_numbers(num_btn.text()))
        
        return num_btn

    #Str-to-Float functions
    def _turn_to_float(self):
        """Turns number to float
        """
        if self.prev_operation == "=":
            self.prev_operation = "."
            self._initial_float()
        
        if not self.is_float:
            if self.text:
                self.text += "."
                self.log += "."
                
                self.output_line.setText(self.text)
                self.log_line.setText(self.log)
                
                self.is_float = True
            else:
                self._initial_float()

    def _initial_float(self):
        self.text = "0."
        self.log = "0."
                
        self.output_line.setText(self.text)
        self.log_line.setText(self.log)
                
        self.is_float = True
        
    def _turn_to_percentage(self):
        """Turns number to percentage
        """
        if self.text:
            if not self.is_float:
                percentage = int(self.text) / 100
            else:
                percentage = float(self.text) / 100
            
            self.is_float = True
            self.text = str(percentage)
            self.log = str(percentage)
            
            self.output_line.setText(self.text)
            self.log_line.setText(self.log)
    
    #Toggle number positivity
    def _toggle_pos_neg(self):
        if self.text:
            if not self.is_float:
                neg_number = -(int(self.text))
            else:
                neg_number = -(float(self.text))
            
            self.text = str(neg_number)
            self.log = str(neg_number)
            
            self.output_line.setText(self.text)
            self.log_line.setText(self.log)
            
    #Number buttons functions
    def _add_numbers(self, number: str) -> None:
        """Adding numbers to the calculator screen

        Args:
            number (str): Number button text
        """
        
        if len(self.text) <= 10:
            if self.prev_operation == "=" or self.clear_log:
                self.text = ""
                self.log = ""
                self.is_float = False
                self.clear_log = False
                self.prev_operation = ""
                
                self.text += number
                self.log += number        
            else:
                self.text += number
                self.log += number     
                if self.text[0] == "0":
                    if not self.is_float:
                        self.text = self.text[1:]
                        self.log = self.log[1:]
        
        self.log_line.setText(self.log)
        self.output_line.setText(self.text)
    
    #Arithmetic operations    
    def _operations_handler(self, operation: str) -> None:
        """Handles arithmetic operations

        Args:
            operation (str): Operation button text
        """
        
        res = 0
        
        #Addition
        if operation == "+":
            if self.first_value != 0:
                if not self.is_float:
                    self.first_value += int(self.output_line.text())
                else:
                    self.first_value += float(self.output_line.text())
            else:
                self._check_float()
            
            self._op_set_values(operation)
       
        #Subtraction
        if operation == "-":
            if self.first_value != 0:
                if not self.is_float:
                    self.first_value -= int(self.output_line.text())
                else:
                    self.first_value -= float(self.output_line.text())
            else:
                self._check_float()
            
            self._op_set_values(operation)
        
        #Multiplication
        if operation == "*":
            if self.first_value != 0:
                if not self.is_float:
                    self.first_value *= int(self.output_line.text())
                else:
                    self.first_value *= float(self.output_line.text())
            else:
                self._check_float()
            
            self._op_set_values(operation)
        
        #Division
        if operation == "/":
            if self.first_value != 0:
                if not self.is_float:
                    self.first_value /= int(self.output_line.text())
                else:
                    self.first_value /= float(self.output_line.text())
            else:
                self._check_float()
            
            self._op_set_values(operation)
        
        #Equation
        if operation == "=":
            #Check for Equation sign
            if self.log[-1] == "=":
                self.log_line.setText(self.log)
            elif self.log[-1] != self.prev_operation:
                self.log += operation
                self.log_line.setText(self.log)
            else:
                self.log += str(self.first_value)
                self.log += operation
                self.log_line.setText(self.log)
            
            #Addition
            if self.prev_operation == "+":
                self.prev_operation = operation
                if not self.is_float:
                    res = self.first_value + int(self.output_line.text())
                else:
                    res = self.first_value + float(self.output_line.text())
                self.text = str(res)
                
                self.output_line.setText(self.text)
                self.first_value = 0
            
            #Subtraction
            if self.prev_operation == "-":
                self.prev_operation = operation
                if not self.is_float:
                    res = self.first_value - int(self.output_line.text())
                else:
                    res = self.first_value - float(self.output_line.text())
                self.text = str(res)

                self.output_line.setText(self.text)
                self.first_value = 0
            
            #Multiplication
            if self.prev_operation == "*":
                self.prev_operation = operation
                if not self.is_float:
                    res = self.first_value * int(self.output_line.text())
                else:
                    res = self.first_value * float(self.output_line.text())
                self.text = str(res)
                
                self.output_line.setText(self.text)
                self.first_value = 0
            
            #Division
            if self.prev_operation == "/":
                self.prev_operation = operation
                if not self.is_float:
                    res = self.first_value / int(self.output_line.text())
                else:
                    res = self.first_value / float(self.output_line.text())
                self.text = str(res)
                
                self.output_line.setText(self.text)
                self.first_value = 0

    def _check_float(self):
        if not self.is_float:
            self.first_value = int(self.output_line.text())
        else:
            self.first_value = float(self.output_line.text())

    def _op_set_values(self, operation):
        self.prev_operation = operation
        self.text = ""
        self.is_float = False
            
        self.log = str(self.first_value)
        self.log += operation
        self.log_line.setText(self.log)
        self.output_line.setText(str(self.first_value))
                
    #Clearing Output QLabel and Log QLabel       
    def _clear_text(self) -> None:
        """Clears calculator screen
        """
        
        self.text = ""
        self.log = ""
        self.first_value = 0
        self.is_float = False
        
        self.output_line.setText(self.text)
        self.log_line.setText(self.log)
        
    def _clear_output(self) -> None:
        """Clears output line
        """
        self.text = ""
        self.is_float = False
        
        if self.prev_operation == ""\
            or self.prev_operation == "=":
            self.clear_log = True
        else:
            self.clear_log = False
        
        self.output_line.setText(self.text)
        

#Run Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    main_window = MainWindow()
    main_window.show()  
    sys.exit(app.exec())