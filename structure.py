from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys



app = QApplication(sys.argv)
dialog = QDialog()
dialog.show()
sys.exit(app.exec_())