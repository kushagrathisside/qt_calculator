"""Calculator Standard mode module.

Returns:
    StandardMode (class): Standard calculator mode class
"""


from collections.abc import Callable


from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon, QFont
from PyQt6.QtWidgets import (QLabel, QGridLayout, QMenuBar,
                             QPushButton, QVBoxLayout, QWidget)


from actions_handler import ActionsHandler

class StandardMode:
    """Calculator Standard mode class
    
    Attributes:
        btn_actions: ActionsHandler class instance
        window (QWidget): App's main window
        layout (QVBoxLayout): Scientific mode window layout
        grid (QGridLayout): Buttons grid layout
        log_line (QLabel): Log QLabel
        output_line (QLabel): Output QLabel
    """
    
    def __init__(self) -> None:
        """Class Initialization
        """
        
        self.btn_actions = ActionsHandler()
        
    def set_window(self, window: QWidget) -> None:
        """Set up the window

        Args:
            window (QWidget): Window
        """
        self.window = window
        
        self.window.setWindowIcon(QIcon("/icons/calculator.png"))
        self.window.setWindowTitle("Калькулятор")
        self.window.setFixedSize(330, 480)
        
        self.layout = self._get_layout()
        self.window.setLayout(self.layout)
        
        self.window.curr_mode = "Standard"
        
    def _get_layout(self) -> QVBoxLayout:
        """Standard mode window layout

        Returns:
            vbox (QVBoxLayout): Vertical Box Layout
        """
        
        vbox = QVBoxLayout(self.window)
        
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
        
        menu_bar = self._menu_bar()
        
        self.grid = self._grid_layout()
        
        vbox.addWidget(menu_bar)
        vbox.addWidget(self.log_line)
        vbox.addWidget(self.output_line)
        vbox.addLayout(self.grid)
        vbox.setContentsMargins(10, 10, 10, 10)
        
        return vbox
    
    def _menu_bar(self) -> QMenuBar:
        """Create menu bar

        Returns:
            menu_bar (QMenuBar): Menu Bar
        """
        
        menu_bar = QMenuBar(self.window)
        menu_bar.setBaseSize(self.output_line.width(), 15)
        
        scientific = QAction("Scientific", self.window)
        scientific.triggered.connect(self._switch_to_sci)
        
        menu_bar.addAction(scientific)
                
        return menu_bar
    
    def _switch_to_sci(self) -> None:
        """Handle switching from standard to scientific mode
        """
        
        layout = self.window.layout()
        self.btn_actions.reset_calculator(self.output_line, self.log_line)
        self.btn_actions.delete_widgets(self.layout)
        del layout
        self.window.m_scientific.set_window(self.window)
    
    # Grid Methods
    def _grid_layout(self) -> QGridLayout:
        """Buttons Grid Layout

        Returns:
            QGridLayout: Grid Layout
        """
        
        grid = QGridLayout(self.window)
        
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
    def _sign_btns_init(self) -> tuple:
        """Create all buttons except numbers.

        Returns:
            tuple[QPushButton]: Buttons
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
            self.btn_actions.toggle_negativity(self.output_line, self.log_line))
        
        dot_btn = self._func_btns_init(".", lambda: 
            self.btn_actions.turn_to_float(self.output_line, self.log_line))
        
        fraction_btn = self._func_btns_init(f"1/{italic_x}", lambda: 
            self.btn_actions.to_fraction(self.output_line, self.log_line))
        
        pow_two_btn = self._func_btns_init(f"{italic_x}{ss_two}", lambda: 
            self.btn_actions.pow_of_two(self.output_line, self.log_line))
        
        sqrt_btn = self._func_btns_init(f"\u221A{italic_x}", lambda: 
            self.btn_actions.square_root(self.output_line, self.log_line))   
             
        prcnt_btn = self._func_btns_init("%", lambda: 
            self.btn_actions.turn_to_percentage(self.output_line, self.log_line))
        
        #Clear buttons
        clear_btn = self._func_btns_init("C", lambda: 
            self.btn_actions.clear_text(self.output_line, self.log_line))
        
        ce_btn = self._func_btns_init("CE", lambda: 
            self.btn_actions.clear_output(self.output_line))
        
        erase_btn = self._func_btns_init("\u232B", lambda: 
            self.btn_actions.erase(self.output_line, self.log_line))
        
        return add_btn, sub_btn, mult_btn, div_btn, equal_btn,\
            pos_neg_btn, prcnt_btn, clear_btn, ce_btn,dot_btn,\
                erase_btn, fraction_btn, pow_two_btn, sqrt_btn

    def _op_btns_init(self, operation: str) -> QPushButton:
        """Connect arithmetic operations to their respective methods.

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
    
    def _func_btns_init(self, label: str, func: Callable[[], None]) -> QPushButton:
        """Connect functional buttons to the specified method.

        Args:
            label (str): Button Label
            func (Callable): Button Function

        Returns:
            QPushButton: Button
        """
        
        func_btn = QPushButton(label)
        func_btn.setMinimumSize(75, 50)
        func_btn.clicked.connect(func)
        
        return func_btn
    
    #Number Buttons Initializer
    def _numbers_btns_init(self, number: int) -> QPushButton:
        """Create and connect numbers to the numbers handler method.

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
    