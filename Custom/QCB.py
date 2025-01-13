from PyQt5.QtWidgets import QWidget, QMenu, QWidgetAction
from PyQt5 import uic
from functools import partial
import os
import sys
from .QCBI import QCBI

class QCB(QWidget):
    def __init__(self, title, data_list, settings, hide = None):
        super().__init__()
        self.path = getattr(sys, '_MEIPASS', os.getcwd())
        self.title = title
        self.s = settings
        self.hiden = hide
        self.win = uic.loadUi(f"{self.path}\\RES\\UI\\QCB.ui", self)
        self.win.setStyleSheet(self.s.qcb_style)
        self.layout = self.win.ITEM.layout()
        self.printers = data_list
        self.num = len(self.printers)

        # Инициализация меню и добавление начальных виджетов
        self.load_menu()
        self.add_initial_widgets()
        self.win.MORE.clicked.connect(self.show_menu)

    def add_initial_widgets(self):
        """Добавляет начальные виджеты в layout."""
        for i in range(1):  # Добавьте больше элементов, если нужно
            self.layout.addWidget(QCBI(title=f"{self.printers[i].name}", status=f"{self.printers[i].status}", setting=self.s, hide=self.hiden))
            self.title = self.printers[i].name

    def clear_layout(self):
        """Удаляет все виджеты из self.layout."""
        self.menu.hide()
        while self.layout.count():
            item = self.layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def load_menu(self):
        """Создает меню с пользовательскими виджетами."""
        self.menu = QMenu(self)
        for i in range(self.num):
            self.menu.addSeparator()

            # Создаем пользовательский виджет
            custom_widget = QCBI(title=f"{self.printers[i].name}", status=f"{self.printers[i].status}", items=True, setting=self.s, hide=self.hiden)
            custom_widget.clicked.connect(partial(self.update_layout, i))  # Используем partial вместо лямбды

            widget_action = QWidgetAction(self.menu)
            widget_action.setDefaultWidget(custom_widget)
            self.menu.addAction(widget_action)

        # Настройки меню
        self.menu.setFixedWidth(self.win.width())
        self.menu.setStyleSheet(self.s.qmenu_style)

    def update_layout(self, index):
        """Обновляет макет с выбранным элементом."""
        try:
            self.clear_layout()
            if self.layout is not None:
                self.layout.addWidget(QCBI(title=f"{self.printers[index].name}", status=f"{self.printers[index].status}", setting=self.s, hide=self.hiden))
                self.title = self.printers[index].name
        
        except Exception as e:
            pass

    def show_menu(self):
        """Отображает меню."""
        pos = self.win.mapToGlobal(self.rect().bottomLeft())
        self.menu.move(pos)
        self.menu.show()
    
    def return_value(self):
        return self.title
