
from PySide6.QtWidgets import (QMainWindow, QApplication, QWidget, QPushButton, 
                               QVBoxLayout, QListWidget, QFileDialog, QLabel, QLineEdit)
from PySide6.QtPdf import (QPdfDocument)
from PySide6.QtPdfWidgets import (QPdfView)

class PDFViewerWindow(QMainWindow):
    def __init__(self, pdf_path:str):
        super().__init__()
        self.setWindowTitle("viewing pdf " + pdf_path)
        self.resize(800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.document = QPdfDocument()
        self.document.load(pdf_path)

        self.view = QPdfView(self)
        self.view.setDocument(self.document)
        self.view.setPageMode(QPdfView.PageMode.MultiPage)
        self.view.setZoomMode(QPdfView.ZoomMode.FitToWidth)

        layout.addWidget(self.view)