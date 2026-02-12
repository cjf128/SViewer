import sys

from PySide6.QtWidgets import QGroupBox, QVBoxLayout, QTabWidget, QWidget, QLabel, QSpacerItem, QSizePolicy, QComboBox, \
    QApplication

from widgets.CustomSlider import CustomSlider
from widgets.FileWidget import FileWidget


class Sidebar(QGroupBox):
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(280)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(2, 2, 2, 2)

        # 创建一个文件控件
        self.file_widget = FileWidget()
        layout.addWidget(self.file_widget)

        # 创建信息栏
        self.adjust_layout = QVBoxLayout()

        # 创建tab管理信息栏
        self.tab_widget = QTabWidget(self)
        self.tab_widget.setMinimumWidth(250)

        self.tab1 = QWidget(self)
        self.tab_widget.addTab(self.tab1, '调整')

        self.image_label = QLabel("图像选择：")
        self.image_combox = QComboBox(self)
        self.image_combox.addItem("病人原图+分割图像")
        self.image_combox.addItem("病人原图")
        self.image_combox.addItem("分割图像")
        self.image_layout = QVBoxLayout()
        self.image_layout.addWidget(self.image_label)
        self.image_layout.addWidget(self.image_combox)
        self.adjust_layout.addLayout(self.image_layout)

        # 基础信息栏
        self.ct_layer = QLabel("CT层数：")
        self.ct_layer.setFixedHeight(18)
        self.ct_layer_slider = CustomSlider(0, 1, 0)
        self.adjust_layout.addWidget(self.ct_layer)
        self.adjust_layout.addWidget(self.ct_layer_slider)

        self.alpha_label = QLabel("透明度：")
        self.alpha_label.setFixedHeight(18)
        self.alpha_slider = CustomSlider(0, 100, 1)
        self.adjust_layout.addWidget(self.alpha_label)
        self.adjust_layout.addWidget(self.alpha_slider)

        self.win_width = QLabel("窗宽：")
        self.win_width.setFixedHeight(18)
        self.win_width_slider = CustomSlider(1, 2000, 0)
        self.adjust_layout.addWidget(self.win_width)
        self.adjust_layout.addWidget(self.win_width_slider)

        self.win_level = QLabel("窗位：")
        self.win_level.setFixedHeight(18)
        self.win_level_slider = CustomSlider(-1000, 1000, 0)
        self.adjust_layout.addWidget(self.win_level)
        self.adjust_layout.addWidget(self.win_level_slider)

        self.spacer = QSpacerItem(20, 71, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.adjust_layout.addItem(self.spacer)

        self.tab1.setLayout(self.adjust_layout)

        layout.addWidget(self.tab_widget)
        self.setLayout(layout)

    def stop_work(self):
        self.setDisabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Sidebar()
    window.show()
    sys.exit(app.exec_())