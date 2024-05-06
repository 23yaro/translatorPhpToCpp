from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic
import os
import sys
from lab1.controllers.MainWindowController import MainWindowController


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    def create(self):

        print(os.path.join(os.path.dirname(__file__), '..\\ui\\main.ui'))
        uic.loadUi(os.path.join(os.path.dirname(__file__), '..\\ui\\main.ui'), self)
        self.controller = MainWindowController(self)
        self.startButton.clicked.connect(lambda :self.controller.start())
        self.reverseButton.clicked.connect(lambda: self.controller.start_reverse())
        #self.translateRButton.clicked.connect(lambda : self.controller.start_r_translate())
        self.syntButton.clicked.connect(lambda: self.controller.start_synt())

        self.input.setReadOnly(True)
        self.output.setReadOnly(True)
        self.reverse_output.setReadOnly(True)
        self.traslateR_output.setReadOnly(True)
        self.errors_output.setReadOnly(True)


        self.startButton.setStyleSheet('QPushButton {background-color: #87CEEB;}')
        self.reverseButton.setStyleSheet('QPushButton {background-color: #87CEEB;}')
        self.translateRButton.setStyleSheet('QPushButton {background-color: #87CEEB;}')
        self.syntButton.setStyleSheet('QPushButton {background-color: #87CEEB;}')

        self.input.setStyleSheet("background-color: #A3C1DA;")
        self.output.setStyleSheet("background-color: #A3C1DA;")
        self.reverse_output.setStyleSheet("background-color: #A3C1DA;")
        self.traslateR_output.setStyleSheet("background-color: #A3C1DA;")
        self.errors_output.setStyleSheet("background-color: #A3C1DA;")
        return self
    def show(self):
        super().show()
        return self

    def closeEvent(self, QCloseEvent):
        del self.controller
        sys.exit()