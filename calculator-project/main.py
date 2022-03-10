"""Main module that creates an instance of the calculator.
"""


# Standard Modules
import sys


# Third-Party Modules
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtWidgets import (QApplication, QWidget)


# Local Modules
from modes import StandardMode
from modes import ScientificMode


class MainWindow(QWidget):
    """Calculator's Main Window

    Args:
        QWidget (QWidget): QWidget Parent Class
        
    Attributes:
        m_standard (StandardMode): Standard Calculator Mode
        m_scientific (ScientificMode): Scientific Calculator Mode
    """
    
    def __init__(self) -> None:
        """Class Initialization
        """
        
        super().__init__()
        
        # Calculator Modes
        self.m_standard = StandardMode()
        self.m_scientific = ScientificMode()
        
        # Public Variables
        self.curr_mode = "Standard"
        
        # Startup Mode
        if self.curr_mode == "Standard":
            self.m_standard.set_window(self)
        elif self.curr_mode == "Scientific":
            self.m_scientific.set_window(self)
        

# Run Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    main_window = MainWindow()
    main_window.show()  
    sys.exit(app.exec())