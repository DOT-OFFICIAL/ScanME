from PyQt5 import QtWidgets, uic, QtCore, QtGui
import sys, os
from PyQt5.QtWidgets import QFrame
from SETTINGS import Settings
from Custom.TAB import TAB
from home import Home
from about import About
from param import PARAMETR
from hPyT import title_bar


sys.path.append(os.path.join(os.path.dirname(__file__), "Script"))


class App(QtWidgets.QMainWindow):
    def __init__(self, hide="back"):
        super().__init__()
        self.path = getattr(sys, '_MEIPASS', os.getcwd())
        self.win = uic.loadUi(f"{self.path}\\RES\\UI\\main.ui", self)
        self.win.resize(1138, 804)

        self.full = False
        self.s = Settings()
        self.win.TITLE.setText("ScanME")
        self.win.setWindowTitle("ScanME")
        self.win.setWindowIcon(QtGui.QIcon(f'{self.path}\\RES\\ICON\\icon.ico'))
        if hide == "back":
            self.win.BACK.hide()
        
        else:
           self.win.LOGO.hide() 
        self.tabs = []
        self.home_pg = Home(setting=self.s)
        self.info_pg = About(setting=self.s)
        self.param_pg = PARAMETR(setting=self.s)
                 
        self.layout = self.win.APP.layout()
        self.layout.addWidget(self.home_pg)
        self.layout.addWidget(self.info_pg)
        self.layout.addWidget(self.param_pg)
        self.info_pg.hide()
        self.param_pg.hide()

       
        self.win.CLOSE.clicked.connect(self.CLOSE_APP)
        self.win.HIDE.clicked.connect(self.MIN_APP)
        self.win.MAX.clicked.connect(self.MAX_APP)
        
        
        self.win.clickPosition = None
        self.load_tabs()
        
    

    def load_tabs(self):
        imgs_top = ["HOME.svg", "INFO.svg"]
        imgs_but = ["SETTINGS.svg"]
        self.top_frame = self.findChild(QFrame, "TOP").layout()
        self.but_frame = self.findChild(QFrame, "BOTTOM").layout()

        for img in imgs_top:
            if img == "HOME.svg":
                tab = TAB(self.s, f"{self.path}\\RES\\ICON\\{img}", True, self)
            else:
                tab = TAB(self.s, f"{self.path}\\RES\\ICON\\{img}", False, self)
            self.tabs.append(tab)
            self.top_frame.addWidget(tab)
        
        for img in imgs_but:
            tab = TAB(self.s, f"{self.path}\\RES\\ICON\\{img}", False, self)
            self.tabs.append(tab)
            self.but_frame.addWidget(tab)



    def mousePressEvent(self, event):
        self.win.clickPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        try:
            if self.full == False:
                if event.buttons() == QtCore.Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.win.clickPosition)
                    self.win.clickPosition = event.globalPos()
                    event.accept()
        except Exception as e:
            pass

    def show_info(self):
        self.home_pg.hide()
        self.param_pg.hide()
        self.info_pg.show()
        self.win.resize(1138, 804)
        
    
    def show_home(self):
        self.info_pg.hide()
        self.param_pg.hide()
        self.home_pg.show()
        self.win.resize(1138, 804)
    
    def show_param(self):
        self.home_pg.hide()
        self.info_pg.hide()
        self.param_pg.show()
        self.win.resize(1138, 804)
    
        
    
    def CLOSE_APP(self):
        self.win.close()
    
    def MIN_APP(self):
        self.win.showMinimized()
    
    def MAX_APP(self):
        if not self.full:
            self.last_geometry = self.win.geometry()
            self.win.showFullScreen()
            self.full = True
        else:
            self.win.showNormal()
            self.win.setGeometry(self.last_geometry)
            self.full = False

    def non_active_all(self):
        for tab in self.tabs:
            tab.non_active()


def Run_Program():
    app = App()
    title_bar.hide(app)
    app.show()


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        Run_Program()
        sys.exit(app.exec_())
    
    except Exception as e:
        print(e)