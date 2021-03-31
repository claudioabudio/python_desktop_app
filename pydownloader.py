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
        browse = QPushButton("Browse")

        self.url.setPlaceholderText("URL")
        self.save_location.setPlaceholderText("File save location")
        self.progress.setValue(0)
        self.progress.setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.url)
        layout.addWidget(self.save_location)
        layout.addWidget(browse)
        layout.addWidget(self.progress)
        layout.addWidget(download)

        self.setFocus();
        self.setWindowTitle("Pydownloader")
        self.setLayout(layout)
        
        download.clicked.connect(self.download)
        browse.clicked.connect(self.browse_file)


    def download(self):
        url = self.url.text()
        save_location = self.save_location.text()
        try:
            urllib.request.urlretrieve(url, save_location, self.report)
        except Exception as e:
            QMessageBox.warning(self, "warning", "download failed: " + str(e) )
            return 

        QMessageBox.information(self, "information", "download completed !")
        self.progress.setValue(0)
        self.url.setText("")
        self.save_location.setText("")


    def report(self, blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize
        if totalsize > 0:
            percent = readsofar * 100 / totalsize
            self.progress.setValue(int(percent))
        
    def browse_file(self):
        #note: save_file is saved as a Tuple
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        save_file = QFileDialog.getSaveFileName(self, caption="Save file as", directory=".", filter="All files (*.*)", options=options)
        print(save_file)
        self.save_location.setText(QDir.toNativeSeparators(save_file[0]))

app = QApplication(sys.argv)
dialog = Downloader()  
dialog.show()
sys.exit(app.exec_())