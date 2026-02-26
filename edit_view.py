
from PySide6.QtWidgets import (QWidget, QPushButton, QListView, QVBoxLayout, QListWidget, QListWidgetItem, QFileDialog, QLabel, QLineEdit)
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtPdf import QPdfDocument

class EditView(QWidget):
    def __init__(self, pdf_path):
        super().__init__()

        self.setWindowTitle("Edit PDF")
        self.resize(1200, 1050)

        self.pages = QListWidget()
        self.pages.setViewMode(QListView.ViewMode.IconMode)
        self.pages.setResizeMode(QListView.ResizeMode.Adjust)
        self.pages.setIconSize(QSize(150, 200))
        self.pages.setSpacing(10)

        layout = QVBoxLayout(self)
        layout.addWidget(self.pages)

        self.document = QPdfDocument()
        self.document.load(pdf_path)

        for i in range(self.document.pageCount()):
            image = self.document.render(i, QSize(150, 200))
            pixmap = QPixmap.fromImage(image)
            icon = QIcon(pixmap)

            item = QListWidgetItem(icon, f"Page {i+1}")
            self.pages.addItem(item)
            

        


