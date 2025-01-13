from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5 import uic
import os
import sys

class QCBI(QWidget):
    clicked = pyqtSignal()  # Создаем кастомный сигнал

    def __init__(self,setting, title, status, path="printer.ui", items=None, hide=None):
        super().__init__()
        self.path = getattr(sys, '_MEIPASS', os.getcwd())
        self.win = uic.loadUi(f"{self.path}\\RES\\UI\\{path}", self)
        self.win.TITLE.setText(title)
        self.win.STATUS.setText(status)
        self.s = setting

        # Настройка стилей, если items == True
        if items == True:
            self.win.BG.layout().setContentsMargins(15, 15, 15, 12)
            self.win.setStyleSheet(self.s.qmenu_items)
        
        if hide == True:
            self.win.ICON.hide()
        

        # Подключение события клика
        self.win.BG.mousePressEvent = self.emit_click

    def emit_click(self, event):
        """Вызывает сигнал clicked при клике."""
        if event.button() == Qt.LeftButton:  # Проверка, что клик левой кнопкой
            self.clicked.emit()
