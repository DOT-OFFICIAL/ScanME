from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon
from PyQt5 import uic
import os, sys

#364c4a

class Notice(QWidget):
    def __init__(self, img, title, author, license, web_url, license_url, settings):
        super().__init__()
        self.path = getattr(sys, '_MEIPASS', os.getcwd())
        self.win = uic.loadUi(f"{self.path}\\RES\\UI\\notice.ui", self)
        self.s = settings
        self.win.BG.setStyleSheet(self.s.notice_style)
        self.win.TITLE.setText(title)
        self.win.AUTHOR.setText(author)
        self.win.LICENSE.setText(license)
        self.win.IMG.setIcon(QIcon(f"{self.path}\\RES\\ICON\\{img}"))
        self.win.WEB.clicked.connect(lambda: self.open_url(web_url))
        self.win.READ.clicked.connect(lambda: self.open_url(license_url))
    
    def open_url(self, url):
        os.startfile(url)
