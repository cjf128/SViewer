from widgets.MainWindow import SegmentApp
from app.config import ConfigManager

class App(object):
    def __init__(self):
        self.config_manager = ConfigManager()
        self.config = self.config_manager.load()
        
        self.main_window = SegmentApp(self.config)

    def run(self):
        self.main_window.show()

    def shutdown(self):
        config = self.main_window.get_window_config()
        self.config_manager.save(config)
