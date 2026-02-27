
from PySide6.QtWidgets import (QWidget, QAbstractItemView, QListView, QVBoxLayout, QListWidget, QListWidgetItem, QFileDialog, QPushButton)
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPixmap, QTransform
from PySide6.QtPdf import QPdfDocument
from pypdf import PdfReader, PdfWriter
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMenu
from PySide6.QtGui import QAction


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

        # 1. Tell the list to allow custom right-click menus
        self.pages.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        
        # 2. Connect the right-click event to a new function we are about to write
        self.pages.customContextMenuRequested.connect(self.show_context_menu)

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

            page_data = {
                "original_index" : 1,
                "rotation" : 0
            }
            item.setData(Qt.ItemDataRole.UserRole, page_data)

            self.pages.addItem(item)
            
    def export_rearranged_pdf(self):
        print("asd")
        savepath, _ = QFileDialog.getSaveFileName(self, "Save Rearranged PDF", "", "PDF Files (*.pdf)")

        if not savepath:
            return

        reader = PdfReader(self.pdf_path)
        writer = PdfWriter()

        for i in range(self.pages.count()):
            item = self.pages.item(i)
            page_data = item.data(Qt.ItemDataRole.UserRole)
            original_index = page_data['original_index']
            rotation = page_data['rotation']
            writer.add_page(reader.pages[original_index])
            

        with open(savepath, "wb") as output_file:
            writer.write(output_file)

        print("file saved to " + savepath)
        
    def remove_page(self, item):
        row_index = self.pages.row(item)
        self.pages.takeItem(row_index)

    def show_context_menu(self, position):
        item = self.pages.itemAt(position)

        if not item:
            return
        
        menu = QMenu(self)

        rotate_action = menu.addAction("Rotate 90°")
        menu.addSeparator()
        delete_action = menu.addAction("Delete Page ❌")

        global_position = self.pages.mapToGlobal(position)

        selected_action = menu.exec(global_position)

        if selected_action == rotate_action:
            self.rotate_page(item)
        elif selected_action == delete_action:
            self.remove_page(item)


    def rotate_page(self, item):
        data = item.data(Qt.ItemDataRole.UserRole)
        data['rotation'] = (data['rotation'] + 90) % 360
        item.setData(Qt.ItemDataRole.UserRole, data)

        current_pixmap = item.icon().pixmap(QSize(195, 260))

        transform = QTransform().rotate(90)
        new_pixmap = current_pixmap.transformed(transform)
        item.setIcon(QIcon(new_pixmap))