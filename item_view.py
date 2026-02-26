
from PySide6.QtCore import QEvent
from PySide6.QtGui import QEnterEvent
from PySide6.QtWidgets import (QWidget, QPushButton, 
                               QHBoxLayout, QLabel)

class ItemView(QWidget):
    def __init__(self, pdf_path:str):
        super().__init__()
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(15,5,15,5)

        self.label = QLabel(pdf_path)
        layout.addWidget(self.label)
        layout.addStretch()

        self.edit_button = QPushButton("🛠️")
        self.edit_button.setVisible(False)
        self.edit_button.setFixedSize(24,24)
        layout.addWidget(self.edit_button)

    def enterEvent(self, event: QEnterEvent):
        self.edit_button.setVisible(True)
        super().enterEvent(event)

    def leaveEvent(self, event: QEvent):
        self.edit_button.setVisible(False)
        super().leaveEvent(event)