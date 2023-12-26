import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtWidgets import QMessageBox, QRadioButton
from PyQt5.QtGui import QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QRadioButton")
        self.setGeometry(200, 150, 800, 500)
        self.start()
        self.show()

    def font(self, obj, x, y):
        obj.setFont(QFont("Times", 20))
        obj.move(x, y)

    def start(self):
        savol = QLabel("Compiler dasturlash tillarini tanlang:", self)
        self.font(savol, 50, 50)
        self.javob1 = QRadioButton("C dasturlash tili", self)
        self.font(self.javob1, 100, 100)
        self.javob2 = QRadioButton("Python dasturlash tili", self)
        self.font(self.javob2, 100, 140)
        self.javob3 = QRadioButton("Rust dasturlash tili", self)
        self.font(self.javob3, 100, 180)
        self.javob4 = QRadioButton("C# dasturlash tili", self)
        self.font(self.javob4, 100, 220)

        enter = QPushButton("Enter", self)
        self.font(enter, 50, 300)
        enter.clicked.connect(self.test)
    
    def test(self):
        win = QMessageBox(self)
        if self.javob1.isChecked():
            win.setText("Siz to'g'ri javob berdingiz")
        elif not(self.javob1.isChecked()) and not(self.javob2.isChecked()) and not(self.javob3.isChecked()) and not(self.javob4.isChecked()):
            win.setText("Siz javoblardan hech birini tanlamadingiz")
        else:
            win.setText("Siz noto'g'ri javob berdingiz")
        win.show()

app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())