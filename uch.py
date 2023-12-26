import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QLineEdit
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QListWidget

class AddWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.start()
    
    def start(self):
        self.v_edit_lay = QVBoxLayout()
        self.h_edit_btn_lay = QHBoxLayout()
        self.v_main_lay = QVBoxLayout()

        self.eng_edit = QLineEdit()
        self.eng_edit.setPlaceholderText("Eng...")

        self.uz_edit = QLineEdit()
        self.uz_edit.setPlaceholderText("Uz...")

        self.send_btn = QPushButton("Send")
        self.send_btn.clicked.connect(self.send)

        self.lbl = QLabel("")
        
        self.menu_btn = QPushButton("Menu")
        self.menu_btn.clicked.connect(self.menu)

        self.v_edit_lay.addWidget(self.eng_edit)
        self.v_edit_lay.addWidget(self.uz_edit)

        self.h_edit_btn_lay.addLayout(self.v_edit_lay)
        self.h_edit_btn_lay.addWidget(self.send_btn)

        self.v_main_lay.addLayout(self.h_edit_btn_lay)
        self.v_main_lay.addWidget(self.lbl)
        self.v_main_lay.addWidget(self.menu_btn)

        self.setLayout(self.v_main_lay)

    def send(self):
        f = open("dict.txt", "a")
        f.write(self.eng_edit.text()+": "+self.uz_edit.text()+"\n")
        f.close()
        self.eng_edit.clear()
        self.uz_edit.clear()

    def menu(self):
        pass

class Search_Window(QWidget):
    def __init__(self):
        super().__init__()

class List_Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("List")
        self.start()
    
    def start(self):
        self.v_main_lay = QVBoxLayout()
        self.h_lbl_lay = QHBoxLayout()
        self.h_lst_wdg_lay = QHBoxLayout()

        self.eng_lbl = QLabel('English')
        self.uz_lbl = QLabel("Uzbek")

        self.eng_lst_wdg = QListWidget()
        self.uz_lst_wdg = QListWidget()

        self.menu_btn = QPushButton("MENU")
        self.menu_btn.clicked.connect(self.menu)

        self.h_lbl_lay.addWidget(self.eng_lbl)
        self.h_lbl_lay.addWidget(self.uz_lbl)

        self.h_lst_wdg_lay.addWidget(self.eng_lst_wdg)
        self.h_lst_wdg_lay.addWidget(self.uz_lst_wdg)

        self.v_main_lay.addLayout(self.h_lbl_lay)
        self.v_main_lay.addLayout(self.h_lst_wdg_lay)
        self.v_main_lay.addWidget(self.menu_btn)

        self.setLayout(self.v_main_lay)

    def menu(self):
        pass
        

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Asosiy oyna")
        self.setFixedSize(300, 350)
        self.start()
    
    def start(self):
        self.h_main_lay = QHBoxLayout()
        self.v_btn_lay = QVBoxLayout()

        self.add_btn = QPushButton("ADD")
        self.add_btn.clicked.connect(self.add)

        self.search_btn = QPushButton("SEARCH")
        self.search_btn.clicked.connect(self.search)

        self.list_btn = QPushButton("LIST")
        self.list_btn.clicked.connect(self.list)

        self.exit_btn = QPushButton("EXIT")
        self.exit_btn.clicked.connect(exit)

        self.lst_btns = [self.add_btn, self.search_btn, self.list_btn, self.exit_btn]
        for i in self.lst_btns:
            i.setFixedSize(100,80)

        self.v_btn_lay.addWidget(self.add_btn)
        self.v_btn_lay.addWidget(self.search_btn)
        self.v_btn_lay.addWidget(self.list_btn)
        self.v_btn_lay.addWidget(self.exit_btn)

        self.h_main_lay.addStretch()
        self.h_main_lay.addLayout(self.v_btn_lay)
        self.h_main_lay.addStretch()

        self.setLayout(self.h_main_lay)

    def add(self):
        self.add_oyna = AddWindow()
        self.add_oyna.show()

    def search(self):
        self.search_oyna = Search_Window()
        self.search_oyna.show()

    def list(self):
        self.lst_oyna = List_Window()
        self.lst_oyna.show()

app = QApplication([])
win = Window()
win.show()
app.exec_()


