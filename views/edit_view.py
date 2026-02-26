
from PySide6.QtWidgets import (QWidget, QAbstractItemView, QListView, QVBoxLayout, QListWidget, QListWidgetItem, QFileDialog, QPushButton)
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtPdf import QPdfDocument
from pypdf import PdfReader, PdfWriter
from PySide6.QtCore import Qt

class EditView(QWidget):
    def __init__(self, pdf_path):
        super().__init__()

        self.pdf_path = pdf_path

        self.setWindowTitle("Edit PDF")
        self.resize(1200, 1050)

        self.pages = QListWidget()
    
        self.pages.setViewMode(QListView.ViewMode.ListMode)
        self.pages.setFlow(QListView.Flow.LeftToRight)
        self.pages.setWrapping(True)
        self.pages.setResizeMode(QListView.ResizeMode.Adjust)
        self.pages.setIconSize(QSize(195, 260))
        self.pages.setSpacing(15)        
        self.pages.setGridSize(QSize(245, 300))

        self.pages.setDragEnabled(True)
        self.pages.setAcceptDrops(True)
        self.pages.setDropIndicatorShown(True)
        self.pages.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)

        self.pages.setStyleSheet("""
            QListWidget::item {
                border-radius: 8px; /* Smooth corners for the item bounds */
                padding: 5px;
            }
            QListWidget::item:hover {
                background-color: rgba(0, 0, 0, 30); /* A subtle dark transparent tint */
            }
            QListWidget::item:selected {
                background-color: rgba(0, 120, 215, 60); /* A soft blue tint when clicked */
                border: 2px solid #0078d7;               /* Windows-style blue border */
            }
        """)

        self.pages.itemDoubleClicked.connect(self.remove_page)

        self.saveButton = QPushButton("Save new PDF")
        self.saveButton.clicked.connect(self.export_rearranged_pdf)

        layout = QVBoxLayout(self)
        layout.addWidget(self.pages)
        layout.addWidget(self.saveButton)

        self.document = QPdfDocument()
        self.document.load(pdf_path)

        for i in range(self.document.pageCount()):
            image = self.document.render(i, QSize(195, 260))
            pixmap = QPixmap.fromImage(image)
            icon = QIcon(pixmap)

            item = QListWidgetItem(icon, f"{i+1}")

            item.setData(Qt.ItemDataRole.UserRole, i)

            self.pages.addItem(item)
            
    def export_rearranged_pdf(self):
        print("asd")
        savepath, _ = QFileDialog.getSaveFileName(self, "Save Rearranged PDF", "", "PDF Files (*.pdf)")

        reader = PdfReader(self.pdf_path)
        writer = PdfWriter()

        for i in range(self.pages.count()):
            item = self.pages.item(i)
            original_index = item.data(Qt.ItemDataRole.UserRole)
            writer.add_page(reader.pages[original_index])

        with open(savepath, "wb") as output_file:
            writer.write(output_file)

        print("file saved to " + savepath)
        
    def remove_page(self, item):
        row_index = self.pages.row(item)
        self.pages.takeItem(row_index)
