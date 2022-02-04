import sys


from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QGridLayout, QLineEdit, 
                             QVBoxLayout, QPushButton, QWidget)
from PyQt6.QtGui import QFont


class MainWindow(QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        
        self._window_settings()
        
        layout = self._main_layout()
        
        self.setLayout(layout)
        
    def _window_settings(self) -> None:
        self.setWindowTitle("Калькулятор Morrison")
        self.setMinimumSize(310, 340)
        
    def _main_layout(self) -> QVBoxLayout:
        vbox = QVBoxLayout()
        self.text = ""
        
        self.output_line = QLineEdit(self.text)
        self.output_line.setMinimumSize(310, 80)
        self.output_line.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        self.output_line.setFont(QFont("Times", 14))
        self.output_line.setReadOnly(True)
        
        grid = self._grid_layout()
        
        vbox.addWidget(self.output_line)
        vbox.addLayout(grid)
        vbox.setContentsMargins(10, 10, 10, 10)
        
        return vbox
        
    def _grid_layout(self) -> QGridLayout:
        
        grid = QGridLayout()
        
        #Number Buttons
        one_btn = self.numbers_buttons(1)
        two_btn = self.numbers_buttons(2)
        three_btn = self.numbers_buttons(3)
        four_btn = self.numbers_buttons(4)
        five_btn = self.numbers_buttons(5)
        six_btn = self.numbers_buttons(6)
        seven_btn = self.numbers_buttons(7)
        eight_btn = self.numbers_buttons(8)
        nine_btn = self.numbers_buttons(9)
        zero_btn = self.numbers_buttons(0)
        
        #Sign Buttons
        add_btn = QPushButton("+")
        add_btn.setMinimumSize(72, 50)
        sub_btn = QPushButton("-")
        sub_btn.setMinimumSize(72, 50)
        mult_btn = QPushButton("*")
        mult_btn.setMinimumSize(72, 50)
        div_btn = QPushButton("/")
        div_btn.setMinimumSize(72, 50)
        equal_btn = QPushButton("=")
        equal_btn.setMinimumSize(72, 50)
        clear_btn = QPushButton("C")
        clear_btn.setMinimumSize(72, 50)
        
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
    
    def numbers_buttons(self, number: int) -> QPushButton:
        
        num_btn = QPushButton(str(number))
        num_btn.setMinimumSize(72, 50)
        num_btn.clicked.connect(lambda: self.add_numbers(num_btn.text()))
        
        return num_btn
    
    def add_numbers(self, number: str) -> None:
        
        self.text += number
        self.output_line.setText(self.text)
        
        

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()

if __name__ == "__main__":
    sys.exit(app.exec())