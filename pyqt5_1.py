import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon, QFont
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator | by J.SH.Z")
        self.setWindowIcon(QIcon("C:\\Users\\Shakhboz Juraev\\Pictures\\calculator.png"))
        self.setFixedSize(400,550)

        btn1=QPushButton("1")
        btn2=QPushButton("2")
        btn3=QPushButton("3")
        btn4=QPushButton("4")
        btn5=QPushButton("5")
        btn6=QPushButton("6")
        btn7=QPushButton("7")
        btn8=QPushButton("8")
        btn9=QPushButton("9")
        btn0=QPushButton("0")
        btn11=QPushButton("+")
        btn12=QPushButton("-")
        btn13=QPushButton("*")
        btn14=QPushButton("/")
        btn15=QPushButton("=")
        btn16=QPushButton(".")
        btn17=QPushButton("D")
        btn18=QPushButton("C")
        btn19=QPushButton("ON/OFF")
        
        h_r1 = QHBoxLayout()
        h_r1.addWidget(btn7)
        h_r1.addWidget(btn8)
        h_r1.addWidget(btn9)

        h_r2 = QHBoxLayout()
        h_r2.addWidget(btn4)
        h_r2.addWidget(btn5)
        h_r2.addWidget(btn6)

        h_r3 = QHBoxLayout()
        h_r3.addWidget(btn1)
        h_r3.addWidget(btn2)
        h_r3.addWidget(btn3)

        v_r = QVBoxLayout()
        v_r.addWidget(h_r1)
        v_r.addWidget(h_r2)
        v_r.addWidget(h_r3)
        

        self.setLayout(v_r)
app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())