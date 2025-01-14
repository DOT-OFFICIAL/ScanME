from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap
from win11toast import toast
from PyQt5 import uic
from Scan import Scanner
from Custom.QCB import QCB
import os
import sys

class Home(QWidget):
    def __init__(self, setting):
        super().__init__()
        self.path = getattr(sys, '_MEIPASS', os.getcwd())
        self.win = uic.loadUi(f"{self.path}\\RES\\UI\\HOME.ui", self)
        self.win.SCAN.clicked.connect(self.scan)
        self.win.PREVIEW.clicked.connect(self.prew)
        self.s = setting
        self.Scan = Scanner(self.s)
        self.win.setStyleSheet(self.s.home_pg_style)
        self.qtbs = []
        self.lists = [self.s.devices, self.s.color_list, self.s.dpi_list, self.s.or_list, self.s.doc_list]
        self.num = len(self.lists)
        layout = self.win.Custom.layout()
        for i in range(self.num):
            hide = None
            if i >= 1:
                hide = True
            
            qcb = QCB(title=f"{i}", settings=self.s, data_list=self.lists[i], hide=hide)
            layout.addWidget(qcb)
            self.qtbs.append(qcb)
    
    def scan(self):
        printer = self.qtbs[0].return_value()
        color = self.qtbs[1].return_value()
        if color == "Цветное": color = "color"
        else: color = "bw"
        dpi = int(str(self.qtbs[2].return_value()).replace(" dpi",""))
        align = self.qtbs[3].return_value()
        if align == "Вертикальное": align = "vertical"
        else: align = "horizontal"
        doc_type = self.qtbs[4].return_value()
        spin = int(self.win.spinBox.value())
        name = self.win.NAME.text()
        try:
            self.Scan.scan(printer_name=printer, scan_type=color, dpi=dpi, save_format=doc_type, rotation=spin, orientation=align, name=name)

        except:
            title = f"Устройство: {printer} недоступно"
            text = '''
            Убедитесь что провод питания подключен к сети, убедитесь что устройство подключено. Попробуйте выбрать другое устройство или обратитесь к производителю
            '''
            toast(title, text, duration='short')
    
    def prew(self):
        printer = self.qtbs[0].return_value()
        try:
            self.Scan.prew(printer)
            img_path = f"{self.path}\\prew\\scan_output.png"
            pixmap = QPixmap(img_path)
            self.win.ICON.setPixmap(pixmap)
        except:
            title = f"Устройство: {printer} недоступно"
            text = '''
            Убедитесь что провод питания подключен к сети, убедитесь что устройство подключено. Попробуйте выбрать другое устройство или обратитесь к производителю
            '''
            toast(title, text, duration='short')
        

        
        