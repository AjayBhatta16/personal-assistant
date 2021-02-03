# Qt5 imports
from PyQt5.QtCore import pyqtSlot, Qt 
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QMainWindow, QWidget, QLineEdit, QApplication, QLabel
from PyQt5.QtWidgets import QPushButton, QGridLayout

# App service imports
from voice import getCommand
from apps import execute

class Container(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(350,350)
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self.style = QPalette()
        self.InitUI()

    def InitUI(self):
        # initialize layouts
        mainLayout = QGridLayout()
        topSubLayout = QGridLayout()
        searchBarSubLayout = QGridLayout()
        # main message box
        self.mainMessageBox = QLabel("Hi. I'm Joyner, your personal assistant. How can I help you?")
        self.mainMessageBox.setFixedWidth(300)
        self.mainMessageBox.setWordWrap(True)
        mainLayout.addWidget(self.mainMessageBox, 0, 0)
        # query box
        self.textbox = QLineEdit(self)
        self.textbox.setFixedSize(250, 40)
        self.textbox.setPlaceholderText("Ask me a question...")
        topSubLayout.addWidget(self.textbox, 0, 0)
        # voice command button
        self.voiceCommandButton = QPushButton("🎤")
        self.voiceCommandButton.setFixedSize(40, 40)
        self.voiceCommandButton.clicked.connect(self.receiveVoice)
        topSubLayout.addWidget(self.voiceCommandButton, 0, 1)
        # search button
        self.searchButton = QPushButton("Search")
        self.searchButton.setFixedSize(100, 30)
        self.searchButton.clicked.connect(self.sendQuery)
        searchBarSubLayout.addWidget(self.searchButton, 0, 0)
        # add sub-layouts to main layout
        mainLayout.addLayout(topSubLayout, 1, 0)
        mainLayout.addLayout(searchBarSubLayout, 2, 0)
        # add main layout to window
        self._centralWidget.setLayout(mainLayout)

    @pyqtSlot()
    def receiveVoice(self):
        self.textbox.displayText = getCommand()
    def sendQuery(self):
        self.mainMessageBox.setText(execute(self.textbox.text()))

def launch():
    app = QApplication([])
    view = Container()
    view.show()
    app.exec_()
