import sys
from PySide6.QtWidgets import QApplication
from views.main_screen import MainScreen

def main():

    app = QApplication(sys.argv)

    window = MainScreen()

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()