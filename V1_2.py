from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.sum = 0
        self.n = 0
        self.move(200,200)
        self.setFixedSize(300,250)
        self.start()
    
    def start(self):
        self.lb = QLabel("Hello world",self)
        self.lb.setStyleSheet("color: black; font-size: 20px")
        self.lb.setFixedSize(220, 30)
        self.lb.move(40,40)

        self.le = QLineEdit(self)
        self.le.setFixedSize(220, 30)
        self.le.move(40,80)


        self.btn = QPushButton("Count", self)
        self.btn.setFixedSize(220, 30)
        self.btn.move(40, 130)
        self.btn.clicked.connect(self.next)

        self.l_sum = QLabel(self)
        self.l_sum.setStyleSheet("color: black")
        self.l_sum.setFixedSize(220, 30)
        self.l_sum.move(40,180)
        

    def next(self):
        self.l_sum.setText(str(len(self.le.text())))
        


app = QApplication([])
win = Window()

win.show()
app.exec_()