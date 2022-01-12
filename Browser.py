import PyQt5
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        Forward_btn = QAction('Forward', self)
        Forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(Forward_btn)

        Reload_btn = QAction('Reload', self)
        Reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(Reload_btn)

        Home_btn = QAction('Home', self)
        Home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(Home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com')) 
    
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())



app = QApplication(sys.argv)
QApplication.setApplicationName('My Browser')
QApplication.setWindowIcon(QIcon('//home//abhishek//abhishek//game developement//image//blue-giant.png'))
window = MainWindow()
app.exec_()