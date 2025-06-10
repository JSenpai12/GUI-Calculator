import sys 
from PySide6.QtWidgets import (
    QApplication,  QMainWindow
)
from PySide6.QtCore import QTimer
from calDesign import Ui_Calculator

class Calculator(QMainWindow, Ui_Calculator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.result = None
    
        buttons = [self.pushButton_9, self.pushButton_16, self.pushButton_7,
                   self.pushButton_11, self.pushButton_14, self.pushButton_8,
                   self.pushButton, self.pushButton_2, self.pushButton_15, 
                   self.pushButton_12, self.pushButton_13, self.pushButton_10,
                   self.pushButton_4, self.pushButton_3]
        
        for btn in buttons:
            btn.clicked.connect(self.cal_display)

        self.pushButton_5.clicked.connect(self.clear_display)
        self.pushButton_6.clicked.connect(self.calculation)
        
    def cal_display(self):
        button = self.sender()
        if button:
            if self.label.text() == self.result:
                self.clear_display()
            current = self.label.text()
            self.label.setText(current + button.text())

    def calculation(self):
        try:
            by_product = int(eval(self.label.text()))
            self.result = str(by_product)
            self.label.setText(str(self.result))

        except Exception:
            self.label.setText("Error")
            QTimer.singleShot(1000, self.clear_display)
    
    def clear_display(self):
        self.label.setText("")


if __name__ == '__main__':
    app = QApplication([])
    window = Calculator()
    window.show()
    sys.exit(app.exec())