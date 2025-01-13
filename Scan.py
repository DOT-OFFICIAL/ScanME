import win32com.client
from PIL import Image, ImageOps
import os
from win11toast import toast
from reportlab.pdfgen import canvas
from docx import Document

class Scanner:
    def __init__(self, settings):
        self.wia = win32com.client.Dispatch("WIA.CommonDialog")
        self.s = settings  # Параметр с настройками

    def list_devices(self):
        devices = win32com.client.Dispatch("WIA.DeviceManager").DeviceInfos
        return [device.Properties["Name"].Value for device in devices]

    def scan(self, printer_name, scan_type="color", dpi=300, orientation="horizontal", save_format="png", rotation=0, name="scan"):
        try:
            # Получение устройства
            devices = win32com.client.Dispatch("WIA.DeviceManager").DeviceInfos
            device = None
            for d in devices:
                if printer_name in d.Properties["Name"].Value:
                    device = d.Connect()
                    break

            if not device:
                raise Exception(f"Сканер '{printer_name}' не найден. Доступные устройства: {', '.join(self.list_devices())}")

            # Настройка сканирования
            scan_item = device.Items[0]

            # Установка разрешения
            try:
                scan_item.Properties["Horizontal Resolution"].Value = dpi
                scan_item.Properties["Vertical Resolution"].Value = dpi
            except Exception as e:
                print(f"Предупреждение: невозможно установить разрешение. Используется значение по умолчанию. ({e})")

            # Сканирование
            format_id = "{B96B3CAB-0728-11D3-9D7B-0000F81EF32E}"  # Формат BMP
            image = self.wia.ShowTransfer(scan_item, format_id)

            # Сохранение временного изображения
            temp_image = "temp_scan.bmp"
            with open(temp_image, "wb") as f:
                f.write(image.FileData.BinaryData)

            # Обработка изображения
            img = Image.open(temp_image)

            # Поворот изображения
            
            
            if orientation == "horizontal":
                img = img.rotate(-90, expand=True)

            
            if rotation:
                img = img.rotate(rotation, expand=True)

            # Исправление ориентации
            img = ImageOps.exif_transpose(img)

            # Применение цветокоррекции
            if scan_type.lower() == "grayscale" or scan_type.lower() == "bw":
                img = img.convert("L")  # Преобразование в градации серого

            # Проверка и создание директории для сохранения
            save_dir = os.path.dirname(self.s.safe_path)
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            # Сохранение в указанном формате
            output_filename = f"{self.s.safe_path}\\{name}.{save_format}"
            if save_format.lower() == "png":
                img.save(output_filename, "PNG")
            elif save_format.lower() == "pdf":
                # Определение ориентации
                img_width, img_height = img.size
                if img_width > img_height:
                    page_size = (img_width, img_height)
                else:
                    page_size = (img_height, img_width)

                # Создание PDF с учетом ориентации и отключением полей
                c = canvas.Canvas(output_filename, pagesize=page_size)
                c.drawImage(temp_image, 0, 0, width=img_width, height=img_height)
                c.save()
            elif save_format.lower() == "docx":
                # Создание DOCX с изображением
                doc = Document()

                # Удаление полей для страницы
                sections = doc.sections
                for section in sections:
                    section.top_margin = 0
                    section.bottom_margin = 0
                    section.left_margin = 0
                    section.right_margin = 0

                # Добавление изображения
                img.save(temp_image, "PNG")
                doc.add_picture(temp_image, width=doc.sections[0].page_width, height=doc.sections[0].page_height)
                doc.save(output_filename)

            else:
                raise ValueError("Формат сохранения должен быть 'png', 'pdf' или 'docx'.")

            os.remove(temp_image)

        except Exception as e:
            print(f"Ошибка: {e}")

    def prew(self, printer_name):
        try:
            devices = win32com.client.Dispatch("WIA.DeviceManager").DeviceInfos
            device = None
            for d in devices:
                if printer_name in d.Properties["Name"].Value:
                    device = d.Connect()
                    break

            scan_item = device.Items[0]
            try:
                scan_item.Properties["Horizontal Resolution"].Value = 100
                scan_item.Properties["Vertical Resolution"].Value = 100
            except Exception:
                pass

            format_id = "{B96B3CAB-0728-11D3-9D7B-0000F81EF32E}"
            image = self.wia.ShowTransfer(scan_item, format_id)

            temp_image = "temp_scan.bmp"
            with open(temp_image, "wb") as f:
                f.write(image.FileData.BinaryData)

            img = Image.open(temp_image)
            img = ImageOps.exif_transpose(img)

            preview_path = os.path.join("prew", "scan_output.png")
            os.makedirs(os.path.dirname(preview_path), exist_ok=True)
            img.save(preview_path, "PNG")

            os.remove(temp_image)

        except Exception as e:
            print(f"Ошибка предпросмотра: {e}")


# Пример использования
if __name__ == "__main__":
    from SETTINGS import Settings
    settings = Settings()
    scanner = Scanner(settings)

    devices = scanner.list_devices()
    print(f"Доступные устройства: {', '.join(devices)}")

    try:
        scanner.scan(printer_name="EPSON L3100 Series", scan_type="color", dpi=300, orientation="horizontal", save_format="docx", rotation=0)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

    
