import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 400)

        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.result_display = QLineEdit()
        self.result_display.setReadOnly(True)
        self.layout.addWidget(self.result_display)

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
        ]

        self.buttons = {}

        for button_text, row, col in buttons:
            button = QPushButton(button_text)
            button.clicked.connect(self.on_button_click)
            self.layout.addWidget(button, row, col)
            self.buttons[button_text] = button

        self.central_widget.setLayout(self.layout)

        self.current_input = ""

    def on_button_click(self):
        sender = self.sender()
        button_text = sender.text()

        if button_text == "=":
            try:
                result = eval(self.current_input)
                self.result_display.setText(str(result))
            except Exception as e:
                self.result_display.setText("Error")
        else:
            self.current_input += button_text
            self.result_display.setText(self.current_input)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
