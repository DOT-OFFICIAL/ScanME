from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5 import uic
import os
import sys

class PARAMETR(QWidget):
    def __init__(self, setting):
        super().__init__()
        self.path = getattr(sys, '_MEIPASS', os.getcwd())
        self.win = uic.loadUi(f"{self.path}\\RES\\UI\\PARAMETR.ui", self)
        self.s = setting
        self.win.setStyleSheet(self.s.param_pg)
        self.win.PATH.setText(self.s.safe_path)
        self.win.MORE.clicked.connect(self.get_path)
        self.win.CODE.clicked.connect(lambda: self.open_url("https://github.com/DOT-OFFICIAL/ScanME"))
        self.win.DONUT.clicked.connect(lambda: self.open_url("https://yoomoney.ru/to/4100118161558859"))
        self.win.TIPS.clicked.connect(lambda: self.open_url("https://tips.yandex.ru/guest/payment/3177409"))
    
    def get_path(self):
        folder_path = QFileDialog.getExistingDirectory(None, "Выберите папку")
        if folder_path:
            self.win.PATH.setText(folder_path)
            self.s.send_new_path(folder_path)
    
    def open_url(self, url):
        os.startfile(url)
