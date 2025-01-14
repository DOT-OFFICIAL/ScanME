from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from Custom.notice import Notice
import os
import sys

class About(QWidget):
    def __init__(self, setting):
        super().__init__()
        self.path = getattr(sys, '_MEIPASS', os.getcwd())
        self.win = uic.loadUi(f"{self.path}\\RES\\UI\\ABOUT.ui", self)
        self.s = setting
        self.win.setStyleSheet(self.s.about_pg)
        self.win.More.clicked.connect(self.more)
        self.load_svg()
        self.load_img()
    
    def more(self):
        file = f"{self.path}\\RES\\DOC\\notice.txt"
        os.startfile(file)
    
    def load_svg(self):
        layout = self.win.svg.layout()
        layout.addWidget(Notice(
            title="HOME SVG ICON", 
            author="Author: Solar Icons", 
            license="License: CC Attribution License", 
            img="HOME.svg", 
            web_url="https://www.svgrepo.com/svg/524649/home-1", 
            license_url="https://www.svgrepo.com/page/licensing/#CC%20Attribution", 
            settings=self.s))

        layout.addWidget(Notice(
            title="SETTINGS SVG ICON", 
            author="Author: Solar Icons", 
            license="License: CC Attribution License", 
            img="SETTINGS.svg", 
            web_url="https://www.svgrepo.com/svg/524954/settings", 
            license_url="https://www.svgrepo.com/page/licensing/#CC%20Attribution", 
            settings=self.s))

        layout.addWidget(Notice(
            title="INFO CIRCLE SVG ICON", 
            author="Author: Solar Icons", 
            license="License: CC Attribution License", 
            img="INFO.svg", 
            web_url="https://www.svgrepo.com/svg/524660/info-circle", 
            license_url="https://www.svgrepo.com/page/licensing/#CC%20Attribution", 
            settings=self.s))

        layout.addWidget(Notice(
            title="ALT ARROW DOWN SVG ICON", 
            author="Author: Solar Icons", 
            license="License: CC Attribution License", 
            img="ARROW.svg", 
            web_url="https://www.svgrepo.com/svg/524248/alt-arrow-down", 
            license_url="https://www.svgrepo.com/page/licensing/#CC%20Attribution", 
            settings=self.s))

        layout.addWidget(Notice(
            title="Link Minimalistic 2 SVG Vector", 
            author="Author: Solar Icons", 
            license="License: CC Attribution License", 
            img="LINK.svg", 
            web_url="https://www.svgrepo.com/svg/524683/link-minimalistic-2", 
            license_url="https://www.svgrepo.com/page/licensing/#CC%20Attribution", 
            settings=self.s))
        
        layout.addWidget(Notice(
            title="Document Text SVG Vector", 
            author="Author: Solar Icons", 
            license="License: CC Attribution License", 
            img="DOC.svg", 
            web_url="https://www.svgrepo.com/svg/524028/document-text", 
            license_url="https://www.svgrepo.com/page/licensing/#CC%20Attribution", 
            settings=self.s))

        layout.addWidget(Notice(
            title="More Horizontal SVG Vector", 
            author="krystonschwarze", 
            license="License: CC Attribution License", 
            img="MORE.svg", 
            web_url="https://www.svgrepo.com/svg/511076/more-horizontal", 
            license_url="https://www.svgrepo.com/page/licensing/#CC%20Attribution", 
            settings=self.s))
        
        


        
    
    def load_img(self):
        layout = self.win.img.layout()
        layout.addWidget(Notice(
            title="Printer Windows 11 Style", 
            author="Printer icon by Icons8", 
            license="Universal Multimedia License Agreement", 
            img="icons8-printer-96 1.png", 
            web_url="https://icons8.com/icon/vccK0o8zIU3K/printer", 
            license_url="https://intercom.help/icons8-7fb7577e8170/en/articles/5534926-universal-multimedia-license-agreement-for-icons8", 
            settings=self.s))