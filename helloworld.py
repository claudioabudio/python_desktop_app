from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class HelloWorld(QDialog):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        label = QLabel("Hello World !")
        line_edit = QLineEdit()
        button = QPushButton("Close")

        layout.addWidget(label, 0, 0)
        layout.addWidget(line_edit, 0, 1)
        layout.addWidget(button, 1, 1)

        self.setLayout(layout)

        button.clicked.connect(self.close)
        line_edit.textChanged.connect(label.setText)

app = QApplication(sys.argv)
dialog = HelloWorld()  
dialog.show()
sys.exit(app.exec_())