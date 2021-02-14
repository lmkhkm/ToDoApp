import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('ToDoApp')
        self.setGeometry(100,100,1000,800)
        self.show()



