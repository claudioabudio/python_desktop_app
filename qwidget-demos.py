from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class QWidgetDemos(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QWidgets Demo")
        layout = QVBoxLayout()
        label = QLabel("Hello World !")
        line_edit = QLineEdit()
        line_edit.setText("Hello Pluralsight")
        line_edit.selectAll()
        line_edit.setEchoMode(QLineEdit.Password)
        line_edit.setReadOnly(True)
        close_button = QPushButton("Close")

        layout.addWidget(label)
        layout.addWidget(line_edit)
        layout.addWidget(close_button)

        self.setLayout(layout)

        close_button.clicked.connect(self.close)
        line_edit.textChanged.connect(label.setText)
        #self.setFocus()

app = QApplication(sys.argv)
dialog = QWidgetDemos()  
dialog.show()
sys.exit(app.exec_())