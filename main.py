import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from app.app import App
from path import BASE_PATH 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(str(BASE_PATH / "icons" / "my_icon.ico")))
    app.setStyle('Fusion')
    application = App()
    application.run()
    app.aboutToQuit.connect(application.shutdown)
    sys.exit(app.exec())
