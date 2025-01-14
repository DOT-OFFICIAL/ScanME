from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtSvg import QSvgRenderer
import os, sys

#364c4a

class TAB(QWidget):
    def __init__(self, settings, path, act, app):
        super().__init__()
        self.s = settings  # акцентный цвет
        self.img = path      # путь к SVG изображению
        self.path = getattr(sys, '_MEIPASS', os.getcwd())
        self.app = app
        self.win = uic.loadUi(f"{self.path}\\RES\\UI\\nav-tab.ui", self)
        if act == False:
            self.win.line.hide()
            self.win.frame.layout().setContentsMargins(0, 0, 0, 0)
        self.load_img()
        self.win.setStyleSheet(self.s.tab_style)
    
    def non_active(self):
        self.win.line.hide()
        self.win.frame.layout().setContentsMargins(0, 0, 0, 0)
    
    def active_tab(self):
        self.win.line.show()
        self.win.frame.layout().setContentsMargins(0, 0, 6, 0)
    
    def mousePressEvent(self, event):
        self.app.non_active_all()
        self.active_tab()
        img = self.img.split("\\")[-1]
        if img == "HOME.svg":
            self.app.show_home()

        elif img == "DOC.svg":
            pass

        elif img == "INFO.svg":
            self.app.show_info()

        elif img == "SETTINGS.svg":
            self.app.show_param()
        super().enterEvent(event)


    def load_img(self):
        # Чтение SVG файла
        with open(self.img, 'r') as file:
            svg_data = file.read()

        # Заменяем все атрибуты fill на новый цвет (акцентный цвет)
        #svg_data = svg_data.replace('#1E1E1E', f'{self.accent}')  # Замените на ваш цвет

        # Создаем временный файл для измененного SVG
        temp_svg_path = os.path.join(self.path, "temp_svg.svg")
        with open(temp_svg_path, 'w') as temp_file:
            temp_file.write(svg_data)

        # Рендерим измененный SVG
        svg_renderer = QSvgRenderer(temp_svg_path)

        # Получаем размер изображения
        size = svg_renderer.defaultSize()

        # Создаем QPixmap для отрисовки изображения
        pixmap = QPixmap(size)
        pixmap.fill(Qt.transparent)  # Устанавливаем прозрачный фон

        # Рисуем SVG на QPixmap
        painter = QPainter(pixmap)
        svg_renderer.render(painter)
        painter.end()

        # Устанавливаем изображение в QLabel
        self.win.icon.setPixmap(pixmap)

        # Удаляем временный SVG файл
        os.remove(temp_svg_path)

