"""Calculator Scientific Mode module

Returns:
    ScientificMode (class): Scientific calculator mode class
"""


from collections.abc import Callable


from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon, QFont
from PyQt6.QtWidgets import (QLabel, QGridLayout, QMenuBar,
                             QPushButton, QVBoxLayout, QWidget)


from actions_handler import ActionsHandler

class ScientificMode:
    """Calculator Scientific mode class
    
    Attributes:
        btn_actions (ActionsHandler): Instance of ActionsHandler class
        curr_page (int): Current operations page
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
        
        self.curr_page = 0
        
    def set_window(self, window: QWidget) -> None:
        """Set up the window

        Args:
            window (QWidget): App window
        """
        
        self.window = window
        
        self.window.setWindowIcon(QIcon("/icons/calculator.png"))
        self.window.setWindowTitle("Калькулятор")
        self.window.setFixedSize(410, 480)
        
        self.layout = self._get_layout()
        self.window.setLayout(self.layout)
        
        self.window.curr_mode = "Scientific"
        
    def _get_layout(self) -> QVBoxLayout:
        """Scientific mode window layout

        Returns:
            vbox (QVBoxLayout): Vertical Box Layout
        """
        
        vbox = QVBoxLayout(self.window)
        
        self.log_line = QLabel(self.btn_actions.log)
        self.log_line.setFixedSize(380, 22)
        self.log_line.setAlignment(Qt.AlignmentFlag.AlignRight 
                                   | Qt.AlignmentFlag.AlignBottom)
        self.log_line.setFont(QFont("Times", 18))
        
        self.output_line = QLabel(self.btn_actions.text)
        self.output_line.setFixedSize(380, 40)
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
        
        self.standard = QAction("Standard", self.window)
        self.standard.triggered.connect(self._switch_to_std)
                
        menu_bar.addAction(self.standard)
        
        return menu_bar
    
    # Scientific-to-Standard switch handling methods
    def _switch_to_std(self) -> None:
        """Handle switching from scientific to standard mode
        """
            
        layout = self.window.layout()
        self.btn_actions.reset_calculator(self.output_line, self.log_line)
        self.btn_actions.delete_widgets(self.layout)
        del layout
        self.window.m_standard.set_window(self.window)
    
    def _grid_layout(self) -> QGridLayout:
        """Buttons Grid Layout

        Returns:
            grid (QGridLayout): Grid Layout
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
        
        # Arithmetic Operations Buttons
        add_btn, sub_btn, mult_btn, div_btn, equal_btn,\
            e_btn, pi_btn = self._arithmetic_btns_init()
            
        # Insertion Buttons
        pos_neg_btn, lb_btn, rb_btn, dot_btn = self._insertion_btns_init()
        
        # Float Buttons
        fraction_btn = self._float_btns_init()
        
        # Advanced Operations Buttons
        factorial_btn, mod_btn, exp_btn, abs_btn = self._adv_btns_init()
        
        # Additional Buttons
        next_page_btn, clear_btn, \
            erase_btn = self._additional_btns_init()
        
        # Alternating Buttons
        self.alt_btn_one, self.alt_btn_two, self.alt_btn_three, self.alt_btn_four,\
            self.alt_btn_five, self.alt_btn_six = self._alt_btns_init()
        
        #Adding Buttons to a Grid
        main_grid = [next_page_btn, pi_btn, e_btn, clear_btn, erase_btn,
                     self.alt_btn_one, fraction_btn, abs_btn, exp_btn, mod_btn,
                     self.alt_btn_two, lb_btn, rb_btn, factorial_btn, div_btn,
                     self.alt_btn_three, one_btn, two_btn, three_btn, mult_btn,
                     self.alt_btn_four, four_btn, five_btn, six_btn, sub_btn,
                     self.alt_btn_five, seven_btn, eight_btn, nine_btn, add_btn,
                     self.alt_btn_six, pos_neg_btn, zero_btn, dot_btn, equal_btn]

        count = 0
        
        for row in range(0, 7):
            for col in range(0, 5):
                grid.addWidget(main_grid[row + col + count], row, col)
            count += 4
        
        return grid

    #Buttons Initializers
    def _arithmetic_btns_init(self) -> tuple:
        """Create basic arithmetic operations buttons.

        Returns:
            tuple: Buttons
        """

        pi = "\u03C0"
        
        # Arithmetic operations
        add_btn = self._op_btns_init("+")
        sub_btn = self._op_btns_init("-")
        mult_btn = self._op_btns_init("\u00D7")
        div_btn = self._op_btns_init("\u00F7")  
        equal_btn = self._op_btns_init("=")
        
        # Constants
        e_btn = self._connect_functions("e", lambda:
            self.btn_actions.print_e(self.output_line, self.log_line))     
        pi_btn = self._connect_functions(f"{pi}", lambda:
            self.btn_actions.print_pi(self.output_line, self.log_line))
        
        
        return add_btn, sub_btn, mult_btn, div_btn, equal_btn, e_btn, pi_btn

    def _insertion_btns_init(self) -> tuple[QPushButton, QPushButton,
                                            QPushButton, QPushButton]:
        """Create buttons for insertion symbols.
        
        Examples:
            ., -, (, ): Insertion symbols

        Returns:
            tuple[QPushButton, QPushButton, QPushButton, QPushButton]: Buttons
        """
        
        # Insertions
        pos_neg_btn = self._connect_functions("\u00B1", lambda: 
            self.btn_actions.toggle_negativity(self.output_line, self.log_line))
        lb_btn = self._connect_functions("(", lambda:
            self.btn_actions.insert_bracket("(", self.log_line))
        rb_btn = self._connect_functions(")", lambda:
            self.btn_actions.insert_bracket(")", self.log_line))
        dot_btn = self._connect_functions(".", lambda: 
            self.btn_actions.turn_to_float(self.output_line, self.log_line))
        
        return pos_neg_btn, lb_btn, rb_btn, dot_btn

    def _float_btns_init(self) -> QPushButton:
        """Create number fractioning button

        Returns:
            fraction_btn (QPushButton): Button
        """
        
        it_x = "\U0001D465"
        
        # Float operations
        fraction_btn = self._connect_functions(f"1/{it_x}", lambda: 
            self.btn_actions.to_fraction(self.output_line, self.log_line))
        
        return fraction_btn

    # Advanced operations
    def _adv_btns_init(self) -> tuple[QPushButton, QPushButton, QPushButton,
                                      QPushButton]:
        """Create advanced arithmetic operations buttons

        Examples:
            Factorial, modulo, exponent, absolute value

        Returns:
            tuple[QPushButton, QPushButton, QPushButton, QPushButton]: Buttons
        """
        
        it_x = "\U0001D465"
        
        factorial_btn = self._connect_functions("\U0001D48F!", lambda:
            self.btn_actions.factorial(self.output_line, self.log_line))
        
        mod_btn = self._op_btns_init("mod")
        
        exp_btn = self._connect_functions("exp", lambda:
            self.btn_actions.exponent(self.output_line, self.log_line))
        
        abs_btn = self._connect_functions(f"|{it_x}|", lambda:
            self.btn_actions.absolute(self.output_line, self.log_line))
        
        return factorial_btn, mod_btn, exp_btn, abs_btn
    
    # Powers and Roots
    def _alt_btns_init(self) -> tuple[QPushButton, QPushButton, QPushButton,
                                      QPushButton, QPushButton, QPushButton]:
        """Create buttons with alternating labels

        Returns:
            tuple[QPushButton, QPushButton, QPushButton, QPushButton, QPushButton, QPushButton]: Buttons
        """
        
        it_x = "\U0001D465"
        it_y = "\U0001D466"
        
        ss_x = "\u02E3"
        ss_y = "\u02B8"
        ss_two = "\u00B2"
        ss_three = "\u00B3"
        
        sq_root = "\u221A"
        cube_root = "\u221B"
        
        self.alt_ops = [f"{it_x}{ss_two}", f"{sq_root}{it_x}", f"{it_x}{ss_y}",
                      f"10{ss_x}", "log", "ln", f"{it_x}{ss_three}", 
                      f"{cube_root}{it_x}", f"{it_y}{sq_root}{it_x}",
                      f"2{ss_x}", f"log{it_y}{it_x}", f"e{ss_x}"]
        
        alt_btn_one = self._alt_btns_connect(self.alt_ops[0])
        alt_btn_two = self._alt_btns_connect(self.alt_ops[1])
        alt_btn_three = self._alt_btns_connect(self.alt_ops[2])
        alt_btn_four = self._alt_btns_connect(self.alt_ops[3])
        alt_btn_five = self._alt_btns_connect(self.alt_ops[4])
        alt_btn_six = self._alt_btns_connect(self.alt_ops[5])
        
        return alt_btn_one, alt_btn_two, alt_btn_three,\
               alt_btn_four, alt_btn_five, alt_btn_six
    
    def _alt_btns_connect(self, operation: str) -> QPushButton:
        """Connect buttons with alternating labels to a handler

        Args:
            operation (str): Button label

        Returns:
            alt_btn (QPushButton): Button
        """
        
        alt_btn = QPushButton(operation)
        alt_btn.setMinimumSize(75, 50)
        alt_btn.clicked.connect(lambda:
            self.btn_actions.alt_ops_handler(alt_btn.text(), self.output_line, 
                                             self.log_line))
        
        return alt_btn
    
    # Functional Buttons Initializer          
    def _additional_btns_init(self) -> tuple[QPushButton, QPushButton, 
                                             QPushButton]:
        """Create additional buttons

        Returns:
            tuple[QPushButton, QPushButton, QPushButton]: Buttons
        """
        
        next_page = "\u21AA"
        
        # Functional buttons
        next_page_btn = self._connect_functions(f"{next_page}",
            self._change_btn_text)
        
        clear_btn = self._connect_functions("C", lambda: 
            self.btn_actions.clear_text(self.output_line, self.log_line))
        
        erase_btn = self._connect_functions("\u232B", lambda: 
            self.btn_actions.erase(self.output_line, self.log_line))
        
        return next_page_btn, clear_btn, erase_btn

    # Operation Buttons Initializer
    def _op_btns_init(self, operation: str) -> QPushButton:
        """Connect operations buttons to the respective methods

        Args:
            operation (str): Operation sign

        Returns:
            QPushButton: Button
        """

        it_x = "\U0001D465"
        it_y = "\U0001D466"

        ss_y = "\u02B8"
        sub_y = "\u1D67"
        
        sq_root = "\u221A"
        
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
        elif operation == f"{it_y}{sq_root}{it_x}":
            op_btn.clicked.connect(lambda: 
                self.btn_actions._operations_handler("yroot", 
                                                    self.output_line, 
                                                    self.log_line))
        elif operation == f"log{sub_y}{it_x}":
            op_btn.clicked.connect(lambda: 
                self.btn_actions._operations_handler("ylog", 
                                                    self.output_line, 
                                                    self.log_line))
        elif operation == f"{it_x}{ss_y}":
            op_btn.clicked.connect(lambda: 
                self.btn_actions._operations_handler("ypow", 
                                                    self.output_line, 
                                                    self.log_line))
        else:
            op_btn.clicked.connect(lambda: 
                self.btn_actions._operations_handler(op_btn.text(), 
                                                    self.output_line, 
                                                    self.log_line))
        
        return op_btn
    
    #Number Buttons Initializer
    def _numbers_btns_init(self, number: int) -> QPushButton:
        """Connect numbers to the respective methods in current btn_actions instance.

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
    
    # Buttons' Methods Connector
    def _connect_functions(self, label: str, 
                           func: Callable[[], None]) -> QPushButton:
        """Connect buttons to the specified method

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
    
    # Next Page Method
    def _change_btn_text(self) -> None:
        """Change button labels.
        """
        
        alt_ops = self.alt_ops
        
        if self.curr_page == 0:
            offset = 6
            self.curr_page = 1
        else:
            offset = 0
            self.curr_page = 0
        
        alt_btns = [self.alt_btn_one, self.alt_btn_two, self.alt_btn_three,
                    self.alt_btn_four, self.alt_btn_five, self.alt_btn_six]
        
        for i in range(0, 6):
            alt_btns[i].setText(alt_ops[i + offset])
        
        
            
        
    