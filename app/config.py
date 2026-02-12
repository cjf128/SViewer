from dataclasses import dataclass
from PySide6.QtCore import QSettings

@dataclass
class AppConfig:
    width: int = 900
    height: int = 600

class ConfigManager:
    def __init__(self):
        # self._settings = QSettings("MyCompany", "MyApp")
        self._settings = QSettings("config.ini", QSettings.IniFormat)


    def load(self) -> AppConfig:
        return AppConfig(
            width=int(self._settings.value("window/width", 900)),
            height=int(self._settings.value("window/height", 600)),
        )

    def save(self, config: AppConfig):
        self._settings.setValue("window/width", config.width)
        self._settings.setValue("window/height", config.height)

