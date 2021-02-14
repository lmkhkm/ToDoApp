import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('ToDoApp')
        self.setGeometry(1000,1000,1000,800)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())