import sys
import platform
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow

my_system =  platform.uname()

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    w = QWidget()
    w.setFixedSize(400,200)
    w.setWindowTitle("System info by Krish")
    w.label_1 = QLabel(f"System OS Type : {my_system.system}", w)
    w.label_1.setFont(QFont('Times', 10, QFont.Bold))
    w.label_1.move(20,20)
    w.label_1.setFixedHeight(30)
    w.label_2 = QLabel(f"Host Name: {my_system.node}", w)
    w.label_2.setFont(QFont('Times', 10, QFont.Bold))
    w.label_2.move(20,20)
    w.label_2.setFixedHeight(70)
    w.label_3 = QLabel(f"OS Version: {my_system.version}", w)
    w.label_3.setFont(QFont('Times', 10, QFont.Bold))
    w.label_3.move(20,20)
    w.label_3.setFixedHeight(110)
    w.label_4 = QLabel(f"Machine: {my_system.machine}", w)
    w.label_4.setFont(QFont('Times', 10, QFont.Bold))
    w.label_4.move(20,20)
    w.label_4.setFixedHeight(150)
    w.label_5 = QLabel(f"Processor: {my_system.processor}", w)
    w.label_5.setFont(QFont('Times', 10, QFont.Bold))
    w.label_5.move(20,20)
    w.label_5.setFixedHeight(190)
    w.label_6 = QLabel("Krishnendu Bhowmick", w)
    w.label_6.move(290,180)
    w.label_6.setFont(QFont('Times', 7))
    w.show()
    sys.exit(app.exec_())
