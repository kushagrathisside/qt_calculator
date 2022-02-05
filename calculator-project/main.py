#Standard Modules
import sys


#Third-Party Modules
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QGridLayout, QLineEdit, 
                             QVBoxLayout, QPushButton, QWidget)
from PyQt6.QtGui import QFont, QIcon


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
        
        self._window_settings()
        
        layout = self._main_layout()
        
        self.setLayout(layout)
        
    def _window_settings(self) -> None:
        """Window Settings
        """
        
        self.setWindowIcon(QIcon("icons/calculator.png"))
        self.setWindowTitle("Калькулятор Morrison")
        self.setFixedSize(320, 340)
        
    def _main_layout(self) -> QVBoxLayout:
        """Calculator's Window Layout

        Returns:
            QVBoxLayout: Vertical Layout
        """
        
        vbox = QVBoxLayout()
        self.text = ""
        
        self.output_line = QLineEdit(self.text)
        self.output_line.setFixedSize(300, 80)
        self.output_line.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        self.output_line.setFont(QFont("Times", 14))
        self.output_line.setReadOnly(True)
        
        grid = self._grid_layout()
        
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
        add_btn, sub_btn, mult_btn, \
            div_btn, equal_btn, clear_btn = self._sign_btns_init()
        
        #Adding Buttons to a Grid
        buttons = [one_btn, two_btn, three_btn, add_btn,
                   four_btn, five_btn, six_btn, sub_btn,
                   seven_btn, eight_btn, nine_btn, mult_btn,
                   clear_btn, zero_btn, equal_btn, div_btn]
        
        count = 0
        for row in range(0, 4):
            for col in range(0, 4):
                grid.addWidget(buttons[row + col + count], row, col)
            count += 3
        
        return grid

    def _sign_btns_init(self) -> QPushButton:
        """Creating buttons for signs

        Returns:
            QPushButton: Buttons
        """
        
        add_btn = self._op_btns_init("+")
        sub_btn = self._op_btns_init("-")
        mult_btn = self._op_btns_init("*")
        div_btn = self._op_btns_init("/")  
        equal_btn = self._op_btns_init("=")
        
        clear_btn = QPushButton("C")
        clear_btn.setMinimumSize(75, 50)
        clear_btn.clicked.connect(self._clear_text)
        
        return add_btn, sub_btn, mult_btn, div_btn, equal_btn, clear_btn

    def _op_btns_init(self, operation: str) -> QPushButton:
        """Handles operation buttons

        Args:
            operation (str): Operation sign

        Returns:
            QPushButton: Operation button
        """
        
        op_btn = QPushButton(operation)
        op_btn.setMinimumSize(75, 50)
        op_btn.clicked.connect(lambda: self._operation(op_btn.text()))
        
        return op_btn
    
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
    
    def _add_numbers(self, number: str) -> None:
        """Adding numbers to the calculator screen

        Args:
            number (str): Number button text
        """
        
        if self.prev_operation == "=":
            self.text = ""
            self.prev_operation = ""
            self.text += number
        else:
            self.text += number     
            if self.text[0] == "0":
                self.text = self.text[1:]
        
        self.output_line.setText(self.text)
        
    def _operation(self, operation: str) -> None:
        """Handles arithmetic operations

        Args:
            operation (str): Operation button text
        """
        
        res = 0
        
        #Addition
        if operation == "+":
            if self.first_value != 0:
                self.first_value += int(self.output_line.text())
            else:
                self.first_value = int(self.output_line.text())
            
            self.prev_operation = operation
            self.text = ""
       
        #Subtraction
        if operation == "-":
            if self.first_value != 0:
                self.first_value -= int(self.output_line.text())
            else:
                self.first_value = int(self.output_line.text())
            
            self.prev_operation = operation
            self.text = ""
        
        #Multiplication
        if operation == "*":
            if self.first_value != 0:
                self.first_value *= int(self.output_line.text())
            else:
                self.first_value = int(self.output_line.text())
            
            self.prev_operation = operation
            self.text = ""
        
        #Division
        if operation == "/":
            if self.first_value != 0:
                self.first_value /= int(self.output_line.text())
            else:
                self.first_value = int(self.output_line.text())
            
            self.prev_operation = operation
            self.text = ""
        
        #Equation
        if operation == "=":
            
            #Addition
            if self.prev_operation == "+":
                self.prev_operation = operation
                res = self.first_value + int(self.output_line.text())
                self.text = str(res)
                
                self.output_line.setText(self.text)
                self.first_value = 0
            
            #Subtraction
            if self.prev_operation == "-":
                self.prev_operation = operation
                res = self.first_value - int(self.output_line.text())
                self.text = str(res)

                self.output_line.setText(self.text)
                self.first_value = 0
            
            #Multiplication
            if self.prev_operation == "*":
                self.prev_operation = operation
                res = self.first_value * int(self.output_line.text())
                self.text = str(res)
                
                self.output_line.setText(self.text)
                self.first_value = 0
            
            #Division
            if self.prev_operation == "/":
                self.prev_operation = operation
                res = self.first_value / int(self.output_line.text())
                self.text = str(res)
                
                self.output_line.setText(self.text)
                self.first_value = 0
            
    def _clear_text(self) -> None:
        """Clears calculator screen
        """
        
        self.text = ""
        self.first_value = 0
        self.output_line.setText(self.text)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    main_window = MainWindow()
    main_window.show()  
    sys.exit(app.exec())