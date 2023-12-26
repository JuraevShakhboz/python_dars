from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QMainWindow
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize, Qt

app = QApplication([])
oyna = QWidget()

# oyna.move(200, 150)
# oyna.setFixedSize(400, 50)
oyna.setGeometry(200,150,400,250)
oyna.setWindowTitle("Foundation-23")
# oyna.setWindowIcon(QIcon("C:\\Users\\99893\\Desktop\\python_new\\pyqt5\\web.png"))
# oyna.setStyleSheet("background-color: #000000")

lbl = QLabel("POLIz vs Sabzavot",oyna)
lbl.move(50, 50)
# lbl.setText(input(">> "))
# lbl.setFont(QFont('Times', 20))
# lbl.setFixedSize(100, 100)
lbl.setStyleSheet("background-color: yellow; font-size: 20px")
print(lbl.text())

edit = QLineEdit(oyna)
edit.move(50, 100)
edit.setStyleSheet("background-color: purple; color:white")

def info():
    lbl.setText(edit.text())
    lbl.adjustSize()
    # edit.setText("")
    edit.clear()

btn1 = QPushButton("Submit", oyna)
btn1.setCentralWidget()
btn1.clicked.connect(info)
btn1.setStyleSheet("background-color: lightGreen; color:red; font-size:30px")

oyna.show()
app.exec_()