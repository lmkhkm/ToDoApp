import sys
from PyQt5.QtWidgets import QApplication, QWidget
import mainWindow as mw

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = mw.MainWindow()
    sys.exit(app.exec_())