import sys
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, 
                               QVBoxLayout, QListWidget, QFileDialog)



def main():

    def open_file_dialog():
        file_name, _ = QFileDialog.getOpenFileName(window, "Open PDF", "", "PDF Files (*.pdf)")
        
        pdf_list.addItem(file_name)


    app = QApplication(sys.argv)
    window = QWidget()

    window.setWindowTitle("PDF Tool Prototype")
    window.resize(600, 450)

    layout = QVBoxLayout(window)

    pdf_list = QListWidget()
    load_button = QPushButton("Select PDF File")

    layout.addWidget(pdf_list)
    layout.addWidget(load_button)

    load_button.clicked.connect(open_file_dialog)   

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()