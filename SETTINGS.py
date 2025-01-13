import pywinstyles
import win32com.client
import os
from platformdirs import user_documents_dir, user_data_dir
#364c4a

class Device():
    def __init__(self, name, type, status):
        self.name = name
        self.type = type
        self.status = status

class Settings():
    def __init__(self):
        self.accent = pywinstyles.get_accent_color()
        self.accent_rgb = self.get_rgb()
        self.accent_rgba = self.accent_rgb.replace(")", ", 0.1)")
        self.accent_but_rgba = self.accent_rgb.replace(")", ", 0.15)")
        self.line_rgba = self.accent_rgb.replace(")", ", 0.5)")
        self.tab_style = self.get_TAB_style()
        self.qmenu_style = self.get_QMenu_style()
        self.qmenu_items = self.get_qmenu_items_style()
        self.qcb_style = self.get_QCB_style()
        self.home_pg_style = self.get_home_pg_style()
        self.notice_style = self.get_notice_style()
        self.devices = self.get_device()
        self.color_list = self.get_color_list()
        self.dpi_list = self.get_dpi_list()
        self.or_list = self.get_orintation_list()
        self.doc_list = self.get_doc_type()
        self.appdata_path = user_data_dir()
        self.safe_path = self.get_save_path()
        self.about_pg = self.get_about_pg_style()
        self.param_pg = self.get_param_pg_style()
        
    
    def get_rgb(self):
        rgb = tuple(int(self.accent[i:i+2], 16) for i in (1, 3, 5))
        return str(rgb)
    
    def get_TAB_style(self):
        tab_style = '''                        
            QWidget:hover {
                background-color: rgba[accent_rgba];
                border-radius: 10px;
            }

            QWidget, QLabel:hover {
                background-color: transparent;
            }

            QWidget#line {
                background-color: rgba[line_rgba];
                border: none;
                border-radius: 2px;
            }

        '''.replace("[accent_rgba]", self.accent_rgba).replace("[line_rgba]", self.line_rgba)
        return tab_style
    
    def get_QMenu_style(self):
        qmenu_style = """
            QMenu {
                background-color: #fff;
                border-radius: 15px;
                border: 1px solid rgba(0, 0, 0, 0);
                color: black;
            }
            QMenu::item {
                margin-bottom: 0px;
                border-radius: 15px;
                background-color: rgba[accent_rgba];
            }
            QMenu::separator {
                height: 7px;
                background-color: rgba(0, 0, 0, 0);
            }
        """.replace("[accent_rgba]", self.accent_rgba)
        return qmenu_style
    
    def get_qmenu_items_style(self):
        qmenu_items = '''
                Form {
                    margin-bottom: 7px;
                }

                QLabel{
                    color: rgba(30, 30, 30, 0.5);
                }

                #TITLE{	
                    font: 87 12pt "Inter 18pt Black";
                    color: rgba(30, 30, 30, 1);
                }

                #STATUS{	
                    font: 10pt "Inter";
                }
                QFrame {
                    background-color: transparent;
                }
                #BG {
                    border-radius: 15px; 
                    background-color: rgba[acent_rgba]; 
                }
                #BG:hover {
                    border: 1px solid [acent_color];
                }
            '''.replace("[acent_color]", self.accent).replace("[acent_rgba]", self.accent_rgba)
        return qmenu_items

    def get_QCB_style(self):
        qcb = '''
            #BG{
                background-color: rgba[acent_rgba];
                border-radius: 10;
            }

            QPushButton{
                background-color: none;
                border: none;
            }

            #ITEM{
                background-color: none;
                border: none;
            }
        '''.replace("[acent_rgba]", self.accent_rgba)
        return qcb

    def get_home_pg_style(self):
        style = '''*{
                border: none;
                background-color: #fff;
            }

            #APP_TITLE{
                font: 18pt "Inter";
            }

            #align_label{	
                font: 87 12pt "Inter 18pt Black";
            }

            QSpinBox, QLineEdit{
                padding: 5px 15px;
                font: 12pt "Inter";
                border: 2px solid rgba[acent_rgb];
                border-radius: 10px;
            }

            QSpinBox::up-button, QSpinBox::down-button{
                    border: transparent;
            }

            QPushButton{
                font: 87 12pt "Inter 18pt Black";
                background-color: rgba[acent_rgb];
                border:none;
                border-radius: 10px;
            }

            QPushButton:hover{
                background-color: rgba[acent_but_rgb];
            }

            #Right{
                border: 2px solid rgba[acent_rgb];
                border-radius: 10px;
            }
            
            #Right #ICON{
                border-radius: 10px;
            }'''.replace("[acent_rgb]", self.accent_rgba).replace("[acent_but_rgb]", self.accent_but_rgba)
        return style

    def get_about_pg_style(self):
        style = '''
        *{	
            background-color: rgb(255, 255, 255);	
            font: 10pt "Inter";
            border:none;
        }

        #Title, #Title_3{
            font: 18pt "Inter";
        }

        #Title_2, #sub_title, #sub_title_2{
            
            font: 87 12pt "Inter 18pt Black";
        }

        #license{
            color: rgba(30, 30, 30, 0.5);
        }

        #app{
            background-color:rgba[acent_rgb];
            border-radius: 10px;
        }

        QFrame {
                            background-color: transparent;
                        }

        QScrollArea{
            border: none;
        }

        QScrollBar:vertical{
            background-color: #fff;
            border: none;
            width: 6px;
        }

        QScrollBar::handle:vertical{
            background: #1e1e1e;
            min-height: 40px;
            border-radius: 3;
        }

        QPushButton{
                        font: 87 12pt "Inter 18pt Black";
                        background-color: rgba[acent_rgb];
                        border:none;
                        border-radius: 10px;
                    }
        
        QPushButton:hover{
            background-color: rgba[acent_but_rgb];
        }
        '''.replace("[line]", self.accent).replace("[acent_rgb]",self.accent_rgba).replace("[acent_but_rgb]", self.accent_but_rgba)
        return style
    
    def get_param_pg_style(self):
        style = '''
        *{
                border: none;
                background-color: #fff;
            }

            #TITLE{
                font: 18pt "Inter";
            }

            #align_label{	
                font: 87 12pt "Inter 18pt Black";
            }


            #folder{
                border: 2px solid rgba[acent_rgba];
                border-radius: 10px;
            }


            QSpinBox, QLineEdit{
                padding: 5px 15px;
                font: 12pt "Inter";
                border: none;
                border-radius: 10px;
            }

            QSpinBox::up-button, QSpinBox::down-button{
                    border: transparent;
            }

            QPushButton{
                font: 87 12pt "Inter 18pt Black";
                background-color: rgba[acent_rgba];
                border:none;
                border-radius: 10px;
            }

                QPushButton:hover{
                background-color: rgba[acent_but_rgb];
            }

            #MORE{
                border: transparent;
                background-color: transparent;
            }

            #Right{
                border: 2px solid rgba[acent_rgba];
                border-radius: 10px;
            }

            #Right #ICON{
                border-radius: 10px;
            }
        '''.replace("[acent_rgba]", self.accent_rgba).replace("[acent_but_rgb]", self.accent_but_rgba)
        return style

    def get_notice_style(self):
        style = '''
        *{	
            font: 9pt "Inter";
            background-color: rgba(255, 255, 255, 0);
        }

        QPushButton{
            border: none;
        }

        QLabel{
            color: rgba(30, 30, 30, 0.5);
        }

        #TITLE{
            color: #000;
            
            font: 87 12pt "Inter 18pt Black";
        }

        #BG{
            background-color: rgba[acent_rgba];
            border-radius: 10px;
        }
        '''.replace("[acent_rgba]", self.accent_rgba)
        return style

    def get_color_list(self):
        color_list = []
        color = Device(name="Цветное", type="", status="Документ будет содержать все цвета RGB")
        dark = Device(name="Черно-Белое", type="", status="Документ будет содержать черно-белые оттенки RGB")
        color_list.append(color)
        color_list.append(dark)
        return color_list
        
    def get_dpi_list(self):
        dpi_list = []
        dpi_200 = Device("200 dpi", "", "Влияет на качество и скорость сканирования")
        dpi_100 = Device("100 dpi", "", "Влияет на качество и скорость сканирования")
        dpi_300 = Device("300 dpi", "", "Влияет на качество и скорость сканирования")
        dpi_list.append(dpi_200)
        dpi_list.append(dpi_100)
        dpi_list.append(dpi_300)
        return dpi_list
    
    def get_orintation_list(self):
        or_list = []
        vert = Device("Вертикальное", "", "Документ будет сохранен в вертикальном положении")
        hor = Device("Горизонтальное", "", "Документ будет сохранен в горизонтальном положении")
        or_list.append(vert)
        or_list.append(hor)
        return or_list

    def get_doc_type(self):
        doc_list = []
        pdf = Device("PDF", "", "Скан будет сохранен как PDF")
        doc = Device("DOCX", "", "Скан будет сохранен как Документ")
        png = Device("PNG", "", "Скан будет сохранен как Изображение")
        doc_list.append(pdf)
        doc_list.append(doc)
        doc_list.append(png)
        return doc_list

    def get_device(self):
        wmi = win32com.client.GetObject("winmgmts:")
        devices = []
        printers = wmi.InstancesOf("Win32_Printer")
        for printer in printers:
            name = printer.Name
            status = "Подключено" if printer.WorkOffline is False else "Отключено"
            device = Device(name, "Принтер", status)
            devices.append(device)

        # Получаем сканеры
        scanners = wmi.InstancesOf("Win32_PnPEntity")
        for device in scanners:
            if "scanner" in (device.Description or "").lower():
                name = device.Name
                status = "Подключено" if device.Status == "OK" else "Отключено"
                device = Device(name, "Принтер", status)
                devices.append(device)

        devices.reverse()
        return devices

    def print_fields(self):
        for field, value in self.__dict__.items():
            try:
                print(f"{field}: {value.name}")
            
            except:
                print(f"{field}: {value}")

    def get_save_path(self):
        # Определение пути к папке ScanMe и файла path.txt
        scanme_path = os.path.join(self.appdata_path, "DOT", "APP", "ScanMe")
        file_path = os.path.join(scanme_path, "path.txt")
        
        try:
            # Создание вложенных директорий, если они не существуют
            os.makedirs(scanme_path, exist_ok=True)
        except Exception as e:
            print(f"Ошибка при создании директорий: {e}")

        try:
            # Попытка прочитать сохранённый путь из файла path.txt
            with open(file_path, "r", encoding="utf-8") as file:
                safe_path = file.read().strip()
        except FileNotFoundError:
            # Если файл не найден, сохраняем путь к папке "Документы"
            safe_path = user_documents_dir()
            try:
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(safe_path)
            except Exception as e:
                print(f"Ошибка при записи в файл: {e}")
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")

        return safe_path
    
    def send_new_path(self, text):
        scanme_path = os.path.join(self.appdata_path, "DOT", "APP", "ScanMe")
        file_path = os.path.join(scanme_path, "path.txt")
        with open(file_path, "w", encoding="utf-8") as file:
                    file.write(text)
        
        self.safe_path = text




if __name__ == "__main__":
    s = Settings()
    s.print_fields()