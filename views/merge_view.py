
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QListWidget, QFileDialog, QPushButton)
from pypdf import PdfWriter

class MergeView(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Merging PDFs")
        self.resize(450, 300)

        self.pdfs_to_merge = []
        self.add_pdf_button = QPushButton("Add new PDF")
        self.merge_button = QPushButton("Merge!")

        self.pages = QListWidget(self)

        layout = QVBoxLayout(self)
        layout.addWidget(self.pages)
        layout.addWidget(self.add_pdf_button)
        layout.addWidget(self.merge_button)

        self.add_pdf_button.clicked.connect(self.add_new_pdf)
        self.merge_button.clicked.connect(self.merge_pdfs)


    def add_new_pdf(self):
        pdf_path, _ = QFileDialog.getOpenFileName(self, "Open PDF", "", "PDF Files (*.pdf)")
        self.pages.addItem(pdf_path)
        self.pdfs_to_merge.append(pdf_path)

    def merge_pdfs(self):
        savepath, _ = QFileDialog.getSaveFileName(self, "Save Rearranged PDF", "", "PDF Files (*.pdf)")

        if not savepath:
            return

        merger = PdfWriter()
        for pdf in self.pdfs_to_merge:
            merger.append(pdf)

        merger.write(savepath)
        merger.close()
        print("Merge complete")