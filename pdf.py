import sys
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, 
                               QVBoxLayout, QListWidget, QFileDialog, QLabel, QLineEdit)

from pdf_viewer import PDFViewerWindow

class MainScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PDF Tool Prototype")
        self.resize(600, 450)

        self.pdf_list = QListWidget()
        self.load_button = QPushButton("Select PDF File")
        self.label = QLabel()
        self.label.setText("asd")
        self.edit = QLineEdit()
        self.edit.editingFinished.connect(self.textchange)

        layout = QVBoxLayout(self)
        layout.addWidget(self.pdf_list)
        layout.addWidget(self.load_button)
        layout.addWidget(self.label)
        layout.addWidget(self.edit)

        self.load_button.clicked.connect(self.open_file_dialog)
    
    def open_file_dialog(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open PDF", "", "PDF Files (*.pdf)")
        
        self.pdf_list.addItem(file_name)

        view_window = PDFViewerWindow(file_name)
        view_window.show()
        print("file showing")

    def textchange(self):
        print("text was changed")
    
def main():

    app = QApplication(sys.argv)

    window = MainScreen()

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()