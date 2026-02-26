
from PySide6.QtWidgets import (QWidget, QAbstractItemView, QListView, QVBoxLayout, QListWidget, QListWidgetItem, QFileDialog, QLabel, QLineEdit)
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtPdf import QPdfDocument
from pypdf import PdfReader, PdfWriter

class EditView(QWidget):
    def __init__(self, pdf_path):
        super().__init__()

        self.setWindowTitle("Edit PDF")
        self.resize(1200, 1050)

        self.pages = QListWidget()
    
        self.pages.setViewMode(QListView.ViewMode.ListMode)
        
        # 2. Make the list flow horizontally instead of vertically
        self.pages.setFlow(QListView.Flow.LeftToRight)
        
        # 3. Tell it to wrap to a new row when it hits the edge of the window
        self.pages.setWrapping(True)
        self.pages.setResizeMode(QListView.ResizeMode.Adjust)

        self.pages.setIconSize(QSize(225, 300))
        self.pages.setSpacing(15)
        
        # Pro-tip: Enforce a strict grid size so longer text labels don't ruin the alignment
        self.pages.setGridSize(QSize(245, 330))
        
        self.pages.setDragEnabled(True)
        self.pages.setAcceptDrops(True)
        self.pages.setDropIndicatorShown(True)
        self.pages.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)

        layout = QVBoxLayout(self)
        layout.addWidget(self.pages)

        self.document = QPdfDocument()
        self.document.load(pdf_path)

        for i in range(self.document.pageCount()):
            image = self.document.render(i, QSize(225, 300))
            pixmap = QPixmap.fromImage(image)
            icon = QIcon(pixmap)

            item = QListWidgetItem(icon, f"{i+1}")
            self.pages.addItem(item)
            
        

        


