
from PySide6.QtWidgets import (QWidget, QPushButton, QVBoxLayout, QListWidget, QListWidgetItem, QFileDialog, QLabel, QLineEdit)
from views.pdf_viewer import PDFViewerWindow
from views.item_view import ItemView
from views.edit_view import EditView
from PySide6.QtCore import Qt
from views.merge_view import MergeView

class MainScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.open_pdfs = []

        self.setWindowTitle("PDFast")
        self.resize(600, 450)

        self.pdf_list = QListWidget()
        self.load_button = QPushButton("Select PDF File")
        self.merge_button = QPushButton("Merge PDFs")

        layout = QVBoxLayout(self)
        layout.addWidget(self.pdf_list)
        layout.addWidget(self.merge_button)
        layout.addWidget(self.load_button)

        self.load_button.clicked.connect(self.open_file_dialog)
        self.pdf_list.itemDoubleClicked.connect(self.open_pdf_viewer)
        self.merge_button.clicked.connect(self.open_pdf_merger)
    
    def open_file_dialog(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open PDF", "", "PDF Files (*.pdf)")
        list_item = QListWidgetItem()
        list_item.setData(Qt.ItemDataRole.UserRole, file_name)
        self.pdf_list.addItem(list_item)
        custom_item = ItemView(file_name)
        list_item.setSizeHint(custom_item.sizeHint())
        self.pdf_list.setItemWidget(list_item, custom_item)

        custom_item.edit_button.clicked.connect(lambda checked=False, fn=file_name: self.open_pdf_editor(fn)) # hell nah argument passing

    def open_pdf_editor(self, pdf_name):
        edit_window = EditView(pdf_name)
        self.open_pdfs.append(edit_window)
        edit_window.show()

    def open_pdf_viewer(self, item):
        pdf_name = item.data(Qt.ItemDataRole.UserRole)
        view_window = PDFViewerWindow(pdf_name)
        self.open_pdfs.append(view_window)
        view_window.show()

    def open_pdf_merger(self):
        view_window = MergeView()
        self.open_pdfs.append(view_window)
        view_window.show()