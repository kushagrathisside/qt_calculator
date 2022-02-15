#Standard Modules
import sys


#Third-Party Modules
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtWidgets import (QApplication, QGridLayout, QLabel, 
                             QMenuBar, QPushButton, QVBoxLayout, 
                             QWidget)


from actions_handler import ActionsHandler


class MainWindow(QWidget):
    """Calculator's Main Window

    Args:
        QWidget ([type]): QWidget Parent Class
    """
    
    def __init__(self) -> None:
        """Class Initialization
        """
        
        super().__init__()
                
        self.btn_actions = ActionsHandler()
        
        self._window_settings()
        
        layout = self._main_layout()
        
        self.setLayout(layout)
        
    def _window_settings(self) -> None:
        """Window Settings
        """
        
        self.setWindowIcon(QIcon("icons/calculator.png"))
        self.setWindowTitle("Калькулятор Morrison")
        self.setFixedSize(330, 480)
    
    # Window Layout
    def _main_layout(self) -> QVBoxLayout:
        """Calculator's Window Layout

        Returns:
            QVBoxLayout: Vertical Layout
        """
        
        vbox = QVBoxLayout()
        
        self.log_line = QLabel(self.btn_actions.log)
        self.log_line.setFixedSize(300, 22)
        self.log_line.setAlignment(Qt.AlignmentFlag.AlignRight 
                                   | Qt.AlignmentFlag.AlignBottom)
        self.log_line.setFont(QFont("Times", 18))
        
        self.output_line = QLabel(self.btn_actions.text)
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
            pos_neg_btn, prcnt_btn, clear_btn, ce_btn,dot_btn,\
                erase_btn, fraction_btn, pow_two_btn, sqrt_btn = self._sign_btns_init()
        
        #Adding Buttons to a Grid
        buttons = [prcnt_btn, ce_btn, clear_btn, erase_btn,
                   fraction_btn, pow_two_btn, sqrt_btn, add_btn,
                   one_btn, two_btn, three_btn, sub_btn,
                   four_btn, five_btn, six_btn, mult_btn,
                   seven_btn, eight_btn, nine_btn, div_btn,
                   pos_neg_btn, zero_btn, dot_btn, equal_btn]
        
        count = 0
        for row in range(0, 6):
            for col in range(0, 4):
                grid.addWidget(buttons[row + col + count], row, col)
            count += 3
        
        return grid

    #Buttons Initializers
    def _sign_btns_init(self) -> QPushButton:
        """Creating buttons for signs

        Returns:
            QPushButton: Buttons
        """
        
        italic_x = "\N{MATHEMATICAL ITALIC SMALL X}"
        ss_two = "\N{SUPERSCRIPT TWO}"
        
        #Arithmetic operations
        add_btn = self._op_btns_init("+")
        sub_btn = self._op_btns_init("-")
        mult_btn = self._op_btns_init("\u00D7")
        div_btn = self._op_btns_init("\u00F7")  
        equal_btn = self._op_btns_init("=")
        
        #Additional operations
        pos_neg_btn = self._func_btns_init("\u00B1", lambda: 
            self.btn_actions._toggle_negativity(self.output_line, self.log_line))
        
        dot_btn = self._func_btns_init(".", lambda: 
            self.btn_actions._turn_to_float(self.output_line, self.log_line))
        
        fraction_btn = self._func_btns_init(f"1/{italic_x}", lambda: 
            self.btn_actions._to_fraction(self.output_line, self.log_line))
        
        pow_two_btn = self._func_btns_init(f"{italic_x}{ss_two}", lambda: 
            self.btn_actions._pow_of_two(self.output_line, self.log_line))
        
        sqrt_btn = self._func_btns_init(f"\u221A{italic_x}", lambda: 
            self.btn_actions._square_root(self.output_line, self.log_line))   
             
        prcnt_btn = self._func_btns_init("%", lambda: 
            self.btn_actions._turn_to_percentage(self.output_line, self.log_line))
        
        #Clear buttons
        clear_btn = self._func_btns_init("C", lambda: 
            self.btn_actions._clear_text(self.output_line, self.log_line))
        
        ce_btn = self._func_btns_init("CE", lambda: 
            self.btn_actions._clear_output(self.output_line))
        
        erase_btn = self._func_btns_init("\u232B", lambda: 
            self.btn_actions._erase(self.output_line, self.log_line))
        
        return add_btn, sub_btn, mult_btn, div_btn, equal_btn,\
            pos_neg_btn, prcnt_btn, clear_btn, ce_btn,dot_btn,\
                erase_btn, fraction_btn, pow_two_btn, sqrt_btn

    def _op_btns_init(self, operation: str) -> QPushButton:
        """Handles operation buttons

        Args:
            operation (str): Operation sign

        Returns:
            QPushButton: Operation button
        """

        op_btn = QPushButton(operation)
        op_btn.setMinimumSize(75, 50)
        if operation == "\u00D7":
            op_btn.clicked.connect(lambda: 
                self.btn_actions._operations_handler("*", 
                                                    self.output_line, 
                                                    self.log_line))
        elif operation == "\u00F7":
            op_btn.clicked.connect(lambda: 
                self.btn_actions._operations_handler("/", 
                                                    self.output_line, 
                                                    self.log_line))
        else:
            op_btn.clicked.connect(lambda: 
                self.btn_actions._operations_handler(op_btn.text(), 
                                                    self.output_line, 
                                                    self.log_line))
        
        return op_btn
    
    def _func_btns_init(self, label: str, func) -> QPushButton:
        """Handles initialization of additional buttons

        Args:
            label (str): Button Label
            func ([type]): Button Function

        Returns:
            QPushButton: Button
        """
        
        func_btn = QPushButton(label)
        func_btn.setMinimumSize(75, 50)
        func_btn.clicked.connect(func)
        
        return func_btn
    
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
        num_btn.clicked.connect(lambda: 
            self.btn_actions._add_numbers(num_btn.text(), 
                                         self.output_line, self.log_line))
        
        return num_btn
        

#Run Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    main_window = MainWindow()
    main_window.show()  
    sys.exit(app.exec())