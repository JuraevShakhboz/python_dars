from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMainWindow
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize, Qt

app = QApplication([])
oyna = QWidget()

oyna.setGeometry(200,150,300,250)
lb = QLabel("Hello world", oyna)

lb.move(50,40)
lb.setFont(QFont('Times', 20))
lb.setStyleSheet("font-size: 20px")

edit = QLineEdit(oyna)
edit.move(50, 70)
edit.setStyleSheet("background-color: purple; color:white")

def info():
    pass

btn1 = QPushButton("Count", oyna)
btn1.move(100, 120)
btn1.clicked.connect(info)
btn1.setStyleSheet("background-color: lightGreen; color:red; font-size:30px")
        
oyna.show()
app.exec_()