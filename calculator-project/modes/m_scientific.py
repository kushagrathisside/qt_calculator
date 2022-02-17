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
        window.setFixedSize(330, 480)
        
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
        
        it_x = "\N{MATHEMATICAL ITALIC SMALL X}"
        it_y = "\U0001D466"
        ss_y = "\N{MODIFIER LETTER SMALL Y}"
        subs_y = "\u1D67"
        ss_x = "\N{MODIFIER LETTER SMALL X}"
        ss_two = "\N{SUPERSCRIPT TWO}"
        ss_three = "\N{SUPERSCRIPT THREE}"
        next_page = "\u21AA"
        pi = "\u03C0"
        cube_root = "\u221B"
        sq_root = "\u221A"
        
        # Arithmetic operations
        add_btn = self._op_btns_init("+")
        sub_btn = self._op_btns_init("-")
        mult_btn = self._op_btns_init("\u00D7")
        div_btn = self._op_btns_init("\u00F7")  
        equal_btn = self._op_btns_init("=")
        
        # Constants
        e_btn = self._func_btns_init("e", lambda:
            self.btn_actions.print_e(self.output_line))
        
        pi_btn = self._func_btns_init(f"{pi}", lambda:
            self.btn_actions.print_pi(self.output_line))
        
        # Insertions
        pos_neg_btn = self._func_btns_init("\u00B1", lambda: 
            self.btn_actions.toggle_negativity(self.output_line, self.log_line))
        
        lb_btn = self._func_btns_init("(", lambda:
            self.btn_actions.insert_bracket(self.output_line, self.log_line))
        
        rb_btn = self._func_btns_init(")", lambda:
            self.btn_actions.insert_bracket(self.output_line, self.log_line))
        
        #Float operations
        dot_btn = self._func_btns_init(".", lambda: 
            self.btn_actions.turn_to_float(self.output_line, self.log_line))
        
        fraction_btn = self._func_btns_init(f"1/{it_x}", lambda: 
            self.btn_actions.to_fraction(self.output_line, self.log_line))
             
        prcnt_btn = self._func_btns_init("%", lambda: 
            self.btn_actions.turn_to_percentage(self.output_line, self.log_line))
        
        # Advanced operations
        factorial_btn = self._func_btns_init("\U0001D48F!", lambda:
            self.btn_actions.factorial(self.output_line, self.log_line))
        
        mod_btn = self._func_btns_init("mod", lambda:
            self.btn_actions.modulo(self.output_line, self.log_line))
        
        exp_btn = self._func_btns_init("exp", lambda:
            self.btn_actions.exponent(self.output_line, self.log_line))
        
        abs_btn = self._func_btns_init(f"|{it_x}|", lambda:
            self.btn_actions.absolute(self.output_line, self.log_line))
        
        # Powers and Roots
        two_to_x_btn = self._func_btns_init(f"2{ss_x}", lambda:
            self.btn_actions.two_to_x(self.output_line, self.log_line))
        
        ten_to_x_btn = self._func_btns_init(f"10{ss_x}", lambda:
            self.btn_actions.ten_to_x(self.output_line, self.log_line))
        
        e_to_x_btn = self._func_btns_init(f"e{ss_x}", lambda:
            self.btn_actions.e_to_x(self.output_line, self.log_line))
        
        pow_two_btn = self._func_btns_init(f"{it_x}{ss_two}", lambda: 
            self.btn_actions.pow_of_two(self.output_line, self.log_line))
        
        pow_three_btn = self._func_btns_init(f"{it_x}{ss_three}", lambda:
            self.btn_actions.pow_of_three(self.output_line, self.log_line))
        
        pow_y_btn = self._func_btns_init(f"{it_x}{ss_y}", lambda:
            self.btn_actions.pow_of_y(self.output_line, self.log_line))
        
        sqrt_btn = self._func_btns_init(f"{sq_root}{it_x}", lambda: 
            self.btn_actions.square_root(self.output_line, self.log_line))   
        
        cubedrt_btn = self._func_btns_init(f"{cube_root}{it_x}", lambda:
            self.btn_actions.cubed_root(self.output_line, self.log_line))
        
        yroot_btn = self._func_btns_init(f"{it_y}{sq_root}{it_x}", lambda:
            self.btn_actions.yroot(self.output_line, self.log_line))
        
        #Logarithms
        log_btn = self._func_btns_init("log", lambda:
            self.btn_actions.log(self.output_line, self.log_line))
        
        nat_log_btn = self._func_btns_init("ln", lambda:
            self.btn_actions.nat_log(self.output_line, self.log_line))
        
        log_y_btn = self._func_btns_init(f"log{subs_y}{it_x}", lambda:
            self.btn_actions.log_y(self.output_line, self.log_line))
        
        # Functional buttons
        next_page_btn = self._func_btns_init(f"{next_page}")
        
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
    