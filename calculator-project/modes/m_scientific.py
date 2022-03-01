from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import (QLabel, QGridLayout, QMenuBar,
                             QPushButton, QVBoxLayout, QWidget)


from actions_handler import ActionsHandler

class ScientificMode:
    
    def __init__(self) -> None:
        """Class Initialization
        """
        
        self.btn_actions = ActionsHandler()
        
    def set_window(self, window: QWidget) -> None:
        """Set up the window

        Args:
            window (QWidget): Window
        """
        
        window.setWindowIcon(QIcon("/icons/calculator.png"))
        window.setWindowTitle("Калькулятор Morrison")
        window.setFixedSize(410, 480)
        
        layout = self._get_layout()
        window.setLayout(layout)
        
        window.curr_mode = "Scientific"
        
    def _get_layout(self) -> QVBoxLayout:
        """Calculator's Window Layout

        Returns:
            QVBoxLayout: Vertical Layout
        """
        
        vbox = QVBoxLayout()
        
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
        
        grid = self._grid_layout()
        
        vbox.addWidget(menu_bar)
        vbox.addWidget(self.log_line)
        vbox.addWidget(self.output_line)
        vbox.addLayout(grid)
        vbox.setContentsMargins(10, 10, 10, 10)
        
        return vbox
    
    def _menu_bar(self) -> QMenuBar:
        """Creates menu bar

        Returns:
            QMenuBar: Menu Bar
        """
        
        menu_bar = QMenuBar()
        menu_bar.setBaseSize(self.output_line.width(), 15)
        
        modes_menu = menu_bar.addMenu("&Modes")
        modes_menu.addAction("Standard")
        modes_menu.addAction("Scientific")
                
        return menu_bar
    
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
        
        # Arithmetic Operations Buttons
        add_btn, sub_btn, mult_btn, div_btn, equal_btn,\
            e_btn, pi_btn = self._arithmetic_btns_init()
            
        # Insertion Buttons
        pos_neg_btn, lb_btn, rb_btn, dot_btn = self._insertion_btns_init()
        
        # Float Buttons
        fraction_btn = self._float_btns_init()
        
        # Advanced Operations Buttons
        factorial_btn, mod_btn, exp_btn, abs_btn,\
            log_btn, nat_log_btn, log_y_btn = self._adv_btns_init()
               
        # Power and Root Buttons
        two_to_x_btn, ten_to_x_btn, e_to_x_btn, pow_two_btn,\
            pow_three_btn, pow_y_btn, sqrt_btn, cubedrt_btn,\
                yroot_btn = self._pow_root_btns_init()
        
        # Additional Buttons
        next_page_btn, clear_btn, \
            erase_btn = self._additional_btns_init()
        
        #Adding Buttons to a Grid
        first_page = [next_page_btn, pi_btn, e_btn, clear_btn, erase_btn,
                      pow_two_btn, fraction_btn, abs_btn, exp_btn, mod_btn,
                      sqrt_btn, lb_btn, rb_btn, factorial_btn, div_btn,
                      pow_y_btn, one_btn, two_btn, three_btn, mult_btn,
                      ten_to_x_btn, four_btn, five_btn, six_btn, sub_btn,
                      log_btn, seven_btn, eight_btn, nine_btn, add_btn,
                      nat_log_btn, pos_neg_btn, zero_btn, dot_btn, equal_btn]
        
        count = 0
        for row in range(0, 7):
            for col in range(0, 5):
                grid.addWidget(first_page[row + col + count], row, col)
            count += 4
        
        return grid

    #Buttons Initializers
    def _arithmetic_btns_init(self) -> tuple:
        """Creating buttons for signs

        Returns:
            QPushButton: Buttons
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

    def _insertion_btns_init(self) -> tuple:
        
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

    def _float_btns_init(self) -> tuple:
        
        it_x = "\U0001D465"
        
        # Float operations
        fraction_btn = self._connect_functions(f"1/{it_x}", lambda: 
            self.btn_actions.to_fraction(self.output_line, self.log_line))
        
        return fraction_btn

    # Advanced operations
    def _adv_btns_init(self) -> tuple:
        
        
        it_x = "\U0001D465"
        sub_y = "\u1D67"
        
        factorial_btn = self._connect_functions("\U0001D48F!", lambda:
            self.btn_actions.factorial(self.output_line, self.log_line))
        
        mod_btn = self._op_btns_init("mod")
        
        exp_btn = self._connect_functions("exp", lambda:
            self.btn_actions.exponent(self.output_line, self.log_line))
        
        abs_btn = self._connect_functions(f"|{it_x}|", lambda:
            self.btn_actions.absolute(self.output_line, self.log_line))
        
        #Logarithms
        log_btn = self._connect_functions("log", lambda:
            self.btn_actions.logarithm(self.output_line, self.log_line))
        
        nat_log_btn = self._connect_functions("ln", lambda:
            self.btn_actions.nat_log(self.output_line, self.log_line))
        
        log_y_btn = self._op_btns_init(f"log{sub_y}{it_x}")
        
        return factorial_btn, mod_btn, exp_btn, abs_btn,\
               log_btn, nat_log_btn, log_y_btn
    
    # Powers and Roots
    def _pow_root_btns_init(self) -> tuple:
        
        it_x = "\U0001D465"
        it_y = "\U0001D466"
        
        ss_x = "\u02E3"
        ss_y = "\u02B8"
        ss_two = "\u00B2"
        ss_three = "\u00B3"
        
        sq_root = "\u221A"
        cube_root = "\u221B"
        
        two_to_x_btn = self._connect_functions(f"2{ss_x}", lambda:
            self.btn_actions.two_to_x(self.output_line, self.log_line))
        
        ten_to_x_btn = self._connect_functions(f"10{ss_x}", lambda:
            self.btn_actions.ten_to_x(self.output_line, self.log_line))
        
        e_to_x_btn = self._connect_functions(f"e{ss_x}", lambda:
            self.btn_actions.e_to_x(self.output_line, self.log_line))
        
        pow_two_btn = self._connect_functions(f"{it_x}{ss_two}", lambda: 
            self.btn_actions.pow_of_two(self.output_line, self.log_line))
        
        pow_three_btn = self._connect_functions(f"{it_x}{ss_three}", lambda:
            self.btn_actions.pow_of_three(self.output_line, self.log_line))
        
        pow_y_btn = self._op_btns_init(f"{it_x}{ss_y}")
        
        sqrt_btn = self._connect_functions(f"{sq_root}{it_x}", lambda: 
            self.btn_actions.square_root(self.output_line, self.log_line))   
        
        cubedrt_btn = self._connect_functions(f"{cube_root}{it_x}", lambda:
            self.btn_actions.cubed_root(self.output_line, self.log_line))
        
        yroot_btn = self._op_btns_init(f"{it_y}{sq_root}{it_x}")
        
        return two_to_x_btn, ten_to_x_btn, e_to_x_btn, pow_two_btn,\
               pow_three_btn, pow_y_btn, sqrt_btn, cubedrt_btn,\
               yroot_btn
               
    def _additional_btns_init(self) -> tuple:
        
        next_page = "\u21AA"
        
        # Functional buttons
        next_page_btn = self._connect_functions(f"{next_page}",
            self._show_next_page)
        
        clear_btn = self._connect_functions("C", lambda: 
            self.btn_actions.clear_text(self.output_line, self.log_line))
        
        erase_btn = self._connect_functions("\u232B", lambda: 
            self.btn_actions.erase(self.output_line, self.log_line))
        
        return next_page_btn, clear_btn, erase_btn

    def _op_btns_init(self, operation: str) -> QPushButton:
        """Handles operation buttons

        Args:
            operation (str): Operation sign

        Returns:
            QPushButton: Operation button
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
    
    def _connect_functions(self, label: str, func) -> QPushButton:
        """Handles button to function connection

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
    
    def _show_next_page(self) -> None:
        
        print("")
    