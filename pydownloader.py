from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import urllib.request

class Downloader(QDialog):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
    
        self.url = QLineEdit()
        self.save_location = QLineEdit()
        self.progress = QProgressBar()
        download = QPushButton("Download")

        self.url.setPlaceholderText("URL")
        self.save_location.setPlaceholderText("File save location")
        self.progress.setValue(0)
        self.progress.setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.url)
        layout.addWidget(self.save_location)
        layout.addWidget(self.progress)
        layout.addWidget(download)

        self.setFocus();
        self.setWindowTitle("Pydownloader")
        self.setLayout(layout)
        
        download.clicked.connect(self.download)
        # line_edit.textChanged.connect(label.setText)


    def download(self):
        url = self.url.text()
        save_location = self.save_location.text()
        urllib.request.urlretrieve(url, save_location, self.report)
        

    def report(self, blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize
        if totalsize > 0:
            percent = readsofar * 100 / totalsize
            self.progress.setValue(int(percent))
        

app = QApplication(sys.argv)
dialog = Downloader()  
dialog.show()
sys.exit(app.exec_())