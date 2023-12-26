from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QMessageBox, QCheckBox, QComboBox, QRadioButton

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(900, 200, 350, 250)
        self.start()
    
    def start(self):
        self.lb = QLabel("Hello world",self)
        self.lb.move(50, 50)
        self.lb.setStyleSheet("color:balck")

        self.r1 = QRadioButton("Real",self)
        self.r1.move(70, 70)

        self.r2 = QRadioButton("MU", self)
        self.r2.move(70, 90)

        self.r3 = QRadioButton("MC", self)
        self.r3.move(70, 110)

        self.r4 = QRadioButton("Arsenal", self)
        self.r4.move(70, 130)

        self.check_btn = QPushButton("check", self)
        self.check_btn.move(70, 150)
        self.check_btn.clicked.connect(self.check)

        self.natija = QLabel("", self)    
        self.natija.move(110, 180)
    
    def check(self):
        if self.r4.isChecked():
            self.natija.setText("CORRECT")
            self.natija.adjustSize()
            self.natija.setStyleSheet('color:Green')
        else:
            self.natija.setText("INCORRECT")
            self.natija.adjustSize()
            self.natija.setStyleSheet('color:Red')

app = QApplication([])
oyna = Window()
oyna.show()
app.exec_()